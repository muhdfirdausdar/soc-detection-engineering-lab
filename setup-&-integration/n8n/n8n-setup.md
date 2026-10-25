# n8n Setup

## Docker Compose

The n8n container is defined in [docker-compose.yml](docker-compose.yml).
The configuration uses the lab address `10.20.30.10` and exposes n8n on port
`5678`. Replace the address when using a different VM or network.

Start n8n from this directory:

```powershell
docker compose up -d
```

Check the container status:

```powershell
docker compose ps
```

View startup logs:

```powershell
docker compose logs -f n8n
```

The n8n data directory is mounted to the host at `./data`. This keeps the
container data available across container restarts.

## Container verification

```powershell
docker compose exec n8n n8n --version
```

The n8n web interface for this lab is available at:

```text
http://10.20.30.10:5678
```

Web UI initialization and workflow construction are documented separately.
