# Windows Server Endpoint Setup

Use the shared [Windows Endpoint Telemetry](../windows-endpoint-telemetry.md)
setup first, then apply the Windows Server-specific configuration.

## Universal Forwarder inputs

Copy [inputs.conf](inputs.conf) to:

```text
C:\Program Files\SplunkUniversalForwarder\etc\apps\SplunkUniversalForwarder\local\inputs.conf
```

In addition to Windows, PowerShell, Defender, and Sysmon events, this file
collects IIS logs from:

```text
C:\inetpub\logs\LogFiles
```

The IIS input is recursive and uses:

```text
index = web
sourcetype = iis
```

## Optional IIS web server

IIS is optional for the endpoint baseline. Enable it when the lab needs web
traffic for detection and investigation exercises. The IIS logs are then
forwarded by the Universal Forwarder using the monitor input above.

The repository web content is under [IIS](IIS/).

## Optional OpenSSH Server

The existing [SSH reference](SSH.txt) contains the OpenSSH setup commands.
The basic flow is:

```powershell
Get-Service sshd
Start-Service sshd
Set-Service sshd -StartupType Automatic
New-NetFirewallRule `
    -Name sshd `
    -DisplayName "OpenSSH Server" `
    -Direction Inbound `
    -Protocol TCP `
    -Action Allow `
    -LocalPort 22
```

Test the service from another host:

```powershell
Test-NetConnection <server-ip> -Port 22
```

SSH is optional and can be enabled when the project needs SSH authentication
or network activity for detection testing.
