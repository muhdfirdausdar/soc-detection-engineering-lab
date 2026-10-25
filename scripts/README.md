# Test Traffic Scripts

These scripts generate controlled activity against lab endpoints so their logs
can be collected, searched, and used to validate detections.

Current example:

- `IIS-Web-Traffic.py`: sends repeated HTTP requests to the IIS web server,
  including normal pages, administrative paths, missing pages, and common probe
  paths, to generate IIS access logs.

Future scripts can target other endpoint services, such as SSH, to generate
authentication and connection events for testing.

Run these scripts only against endpoints in the lab environment.
