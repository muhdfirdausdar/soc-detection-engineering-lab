# FortiGate VM Setup

## Download FortiOS

1. Create or sign in to a FortiCloud account.
2. Open the FortiOS download platform.
3. Download the required FortiGate VM image.
4. Older VMs cant be download, I found FortiOS 7.0.0 images, use the following link:

   [FortiOS 7.0.0 VM image](https://drive.google.com/drive/folders/12Hu9_M4Ymrm6YLJvfMSSJLCG-a67tZGr)

## Import the VM

1. Extract the downloaded VM files if required.
2. Import the OVF file into VMware.
3. Before starting the VM, create or add VMware network adapters for later port config on Fortigate terminal.
5. Start the VM and continue with the FortiGate initial setup.

## Related configuration

After the VM starts, apply the network configuration in
[fortigate-network-config.md](fortigate-network-config.md).
