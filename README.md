# Darkly



## Setup Instructions

This project is designed to run on amd64 architecture hardware. The provided ISO file is compatible only with this architecture. The project setup involves using VirtualBox to create and configure a virtual machine (VM). Once the VM is configured and running, you can access the application via your web browser.

### Prerequisites

- **Hardware:** Ensure you are using amd64 architecture hardware.
- **Software:** Download and install [VirtualBox](https://www.virtualbox.org/).

### Step 1: Verify Hardware Architecture

Before starting, ensure that your system is using amd64 architecture hardware. This is crucial as the ISO file provided for the project is specifically built for this architecture.

### Step 2: Download VirtualBox

1. Go to the [VirtualBox download page](https://www.virtualbox.org/wiki/Downloads).
2. Download and install VirtualBox appropriate for your operating system.

### Step 3: Boot a VM Using the ISO File

1. Open VirtualBox.
2. Click on `New` to create a new virtual machine.
3. Follow the prompts to name your VM and select the operating system type and version.
4. In the Virtual Hard Disk step, choose `Use an existing virtual hard disk file` and select the downloaded ISO file from the project's page.
5. Complete the VM creation process.

### Step 4: Configure Network Settings

1. Once the VM is booted, stop the VM by clicking on `Close > Power off`.
2. Go to `Settings` for the VM.
3. Navigate to the `Network` section.
4. Ensure the `Attached to` field is set to `NAT`.
5. Expand the `Advanced` tab and click on `Port Forwarding`.

### Step 5: Set Up Port Forwarding

1. In the `Port Forwarding` window, create a new rule with the following settings:
    - **Protocol:** TCP
    - **Host IP:** 127.0.0.1
    - **Host Port:** 8080
    - **Guest IP:** Leave blank (it will automatically use the VM's IP address)
    - **Guest Port:** 80
2. Click `OK` to save the settings.

### Step 6: Restart the VM

1. Start the VM again.
2. The VM’s application is now forwarded to the host port 8080.

### Step 7: Access the Application

1. Open your web browser.
2. Navigate to `http://127.0.0.1:8080/`.
3. You should now see the application running.

