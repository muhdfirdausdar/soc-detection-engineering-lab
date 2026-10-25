# Sample FortiGate Network Configuration commands

## System status

```text
get sys status
get system interface physical
```

## Interfaces

```text
config system interface
    edit "port1"
        set mode dhcp
        set allowaccess ping
        set role wan
        set alias "WAN"
    next
    edit "port2"
        set ip 10.0.0.1/24
        set allowaccess https ssh ping
        set role lan
        set alias "SOC-LAN"
    next
end
```

## DNS

```text
config system dns
    set primary 8.8.8.8
    set secondary 1.1.1.1
end
```

## NTP

```text
config system ntp
    set ntpsync enable
    set type custom
    config ntpserver
        edit 1
            set server "time.google.com"
        next
    end
end
```

## Verification

```text
get system interface physical
diagnose sys ntp status
execute ping 8.8.8.8
execute ping time.google.com
```

# Disable system performance statistics logging on a FortiGate firewall. No need to send/ingest on SIEM

```text
config system global
    set sys-perf-log-interval 0
end
```