# Windows 10 Endpoint Setup

Use the shared [Windows Endpoint Telemetry](../windows-endpoint-telemetry.md)
setup for the Windows 10 endpoint.

## Universal Forwarder inputs

Copy [inputs.conf](inputs.conf) to:

```text
C:\Program Files\SplunkUniversalForwarder\etc\apps\SplunkUniversalForwarder\local\inputs.conf
```

The Windows 10 configuration collects:

- Application event log
- Security event log
- System event log
- PowerShell operational events
- Windows Defender operational events
- Sysmon operational events

Restart the Universal Forwarder after placing the file:

```powershell
Restart-Service SplunkForwarder
```

Verify that events arrive in the Splunk `windows` index:

```spl
index=windows
```

Useful sourcetypes include:

```spl
index=windows sourcetype=powershell
index=windows sourcetype=sysmon
index=windows sourcetype=defender
```
