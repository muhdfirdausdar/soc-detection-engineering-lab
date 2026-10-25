# FortiGate to Log Collector Integration

## Configure rsyslog TCP reception

Edit `/etc/rsyslog.conf` and enable the TCP input module:

```text
module(load="imtcp")
input(type="imtcp" port="514")
```

Create `/etc/rsyslog.d/10-fortigate.conf`:

```text
template(name="FortiGateFormat" type="string"
         string="%rawmsg%\n")

if $fromhost-ip == '192.168.0.5' then {
    action(
        type="omfile"
        file="/var/log/192.168.0.5/192.168.0.5.log"
        template="FortiGateFormat"
    )
    stop
}
```

Validate and restart rsyslog:

```bash
sudo rsyslogd -N1
sudo systemctl restart rsyslog
sudo ss -tlnp | grep 514
```

## Configure FortiGate forwarding (do on Fortigate terminal)

```text
config log syslogd setting
    set status enable
    set server "192.168.0.6"
    set mode reliable
    set port 514
    set format default
end
```

## Validate log reception

```bash
sudo tail -f /var/log/192.168.0.5/192.168.0.5.log
```

The expected format is one FortiGate event per line:

```text
<189>date=...
<189>date=...
```

After changing the rsyslog TCP listener or routing configuration, re-enable the
FortiGate syslog setting or restart the FortiGate so the TCP session is rebuilt.
