import subprocess
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
SCRIPT_LIST = SCRIPT_DIR / "concurrent-scripts.txt"
output_lock = threading.Lock()
process_lock = threading.Lock()
running_processes = {}


def load_script_paths():
    script_names = []
    for line in SCRIPT_LIST.read_text(encoding="utf-8").splitlines():
        script_name = line.strip()
        if script_name and not script_name.startswith("#"):
            script_names.append(script_name)

    if not script_names:
        raise ValueError(f"No scripts listed in {SCRIPT_LIST.name}")

    script_paths = []
    for script_name in script_names:
        script_path = (SCRIPT_DIR / script_name).resolve()
        if script_path.parent != SCRIPT_DIR:
            raise ValueError(f"Only filenames in {SCRIPT_DIR.name} are allowed: {script_name}")
        if script_path.suffix.lower() != ".py":
            raise ValueError(f"Not a Python script: {script_name}")
        if not script_path.is_file():
            raise FileNotFoundError(f"Script not found: {script_name}")
        script_paths.append(script_path)

    return script_paths


def run_script(script_path):
    script_name = script_path.name
    process = subprocess.Popen(
        [sys.executable, "-u", str(script_path)],
        cwd=SCRIPT_DIR,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
    )

    with process_lock:
        running_processes[script_name] = process

    try:
        for line in process.stdout:
            with output_lock:
                print(f"[{script_name}] {line.rstrip()}", flush=True)
        return_code = process.wait()
        with output_lock:
            print(f"[{script_name}] exited with code {return_code}", flush=True)
    finally:
        with process_lock:
            running_processes.pop(script_name, None)


def stop_running_processes():
    with process_lock:
        processes = list(running_processes.values())

    for process in processes:
        if process.poll() is None:
            process.terminate()


def main():
    script_paths = load_script_paths()
    print(f"Starting {len(script_paths)} script(s). Press Ctrl+C to stop.", flush=True)

    executor = ThreadPoolExecutor(max_workers=len(script_paths))
    futures = [executor.submit(run_script, script_path) for script_path in script_paths]

    try:
        for future in futures:
            future.result()
    except KeyboardInterrupt:
        print("Stopping scripts...", flush=True)
        stop_running_processes()
        executor.shutdown(wait=True, cancel_futures=True)
        return 130
    else:
        executor.shutdown(wait=True)

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileNotFoundError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        raise SystemExit(1)