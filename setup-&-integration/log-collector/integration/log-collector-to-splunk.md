# Log Collector to Splunk Integration

## Install Splunk Universal Forwarder

Download the required package from the [Splunk Universal Forwarder download page](https://www.splunk.com/en_us/download/universal-forwarder.html), then install it on the collector:

```bash
sudo dpkg -i splunkforwarder*.deb
sudo /opt/splunkforwarder/bin/splunk enable boot-start
sudo systemctl start SplunkForwarder
```

## Connect the forwarder to Splunk

```bash
sudo /opt/splunkforwarder/bin/splunk add forward-server 10.20.30.10:9997
sudo /opt/splunkforwarder/bin/splunk list forward-server
```

Enable TCP port `9997` in Splunk under **Settings > Forwarding and Receiving > Configure Receiving**.

Create a `firewall` index with a 5000 MB maximum total data size.

## Monitor the firewall log

```bash
sudo /opt/splunkforwarder/bin/splunk add monitor \
/var/log/192.168.0.5/192.168.0.5.log \
-index firewall \
-sourcetype fortigate

sudo systemctl restart SplunkForwarder
```

## Validate ingestion (on splunk web ui)

Run this search in Splunk:

```spl
index=firewall sourcetype=fortigate
```

Confirm that HTTP, SSH, DNS, and traffic events are present.

## Validate buffering and recovery

1. Stop Splunk.
2. Generate HTTP traffic, SSH traffic, and an Nmap scan.
3. Confirm that events continue arriving at the collector.
4. Start Splunk again.
5. Confirm that the queued events are forwarded and appear in Splunk.
