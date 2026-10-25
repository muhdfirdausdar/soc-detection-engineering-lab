# Log Collector Setup

## 1. Install rsyslog

```bash
sudo apt update
sudo apt install rsyslog -y
sudo systemctl enable --now rsyslog
sudo systemctl status rsyslog
```

## 2. Prepare dedicated log storage

The collector uses a separate 2 GB disk for firewall logs. Confirm the disk
name before partitioning because device names can differ between VMs.

```bash
lsblk
sudo fdisk /dev/sdb
```

In `fdisk`:

```text
n
p
1
Enter
Enter
w
```

Create an ext4 filesystem and mount it at the firewall log path:

```bash
sudo mkfs.ext4 /dev/sdb1
sudo mkdir -p /var/log/192.168.0.5
sudo mount /dev/sdb1 /var/log/192.168.0.5
```

Make the mount persistent:

```bash
sudo blkid /dev/sdb1
sudo nano /etc/fstab
```

Add the filesystem UUID returned by `blkid`:

```text
UUID=<filesystem-uuid> /var/log/192.168.0.5 ext4 defaults 0 2
```

Verify the mount:

```bash
sudo mount -a
df -h /var/log/192.168.0.5
```

## 3. Create the firewall log file

```bash
sudo mkdir -p /var/log/192.168.0.5
sudo touch /var/log/192.168.0.5/192.168.0.5.log
sudo chown root:adm /var/log/192.168.0.5
sudo chmod 755 /var/log/192.168.0.5
sudo chown root:adm /var/log/192.168.0.5/192.168.0.5.log
sudo chmod 640 /var/log/192.168.0.5/192.168.0.5.log
```

## 4. Configure log rotation

Create `/etc/logrotate.d/firewalls`:

```text
/var/log/192.168.0.5/192.168.0.5.log
{
    daily
    maxsize 100M
    rotate 14
    compress
    delaycompress
    missingok
    notifempty
    create 0640 root adm
    dateext
    dateformat -%Y%m%d-%H%M%S

    postrotate
        systemctl kill -s HUP rsyslog
    endscript
}
```

Validate and test rotation:

```bash
sudo logrotate -d /etc/logrotate.d/firewalls
sudo logrotate -f /etc/logrotate.d/firewalls
ls -lh /var/log/192.168.0.5
sudo tail -f /var/log/192.168.0.5/192.168.0.5.log
systemctl status logrotate.timer
```
