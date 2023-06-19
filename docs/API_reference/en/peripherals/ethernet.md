# ethernet - Ethernet Driver
`ethernet` module contains features related to Ethernet control and network configuration, and provides unified management for different types of Ethernet NIC.

**Example:**

This section introduces the initialization process of NIC in the terminal mode, gateway mode and static IP address configuration respectively based on different application scenarios.


> 1. The following example is only for NIC application configuration on the module. Ethernet NICs can be normally used after the corresponding operation is performed on the peer device.
> 2. Some NICs are not applicable to the following examples. Please use NICs according to the corresponding instructions for different NIC drivers.


Terminal mode:

```python
# In the terminal mode, the module connects to the external network through the Ethernet interface. For example, the W5500 network interface is connected to the router and obtains IP information through dynamic host configuration protocol (DHCP), so that the module can connect to the external network through this network interface.

import ethernet

# Loads the corresponding NIC driver and initializes the relevant configuration of NIC. Replaces the driver with the actual corresponding NIC driver.
nic = ethernet.diver(...)
print(nic.ipconfig())

# Obtains the static IP address.
nic.dhcp()
print(nic.ipconfig())

# Now starts other network services and accesses the network through Ethernet.
...

```

Gateway mode:

```python
# In the gateway mode, the module connects to the externel network with LTE network. For example, the w5500 network interface is connected to a computer and the computer configures a static IP address on the same network segment as the W5500 Ethernet interface. The gateway address is the same as that of the W5500 NIC address so that the computer can connect to the network throught a LTE NIC.
import ethernet
import dataCall

# Loads the corresponding NIC driver and initializes the relevant configuration of NIC. Replaces the driver with the actual corresponding NIC driver.
nic = ethernet.diver(...)
print(nic.ipconfig())

# Obtains current LTE network data call IP information.
lte=dataCall.getInfo(1, 0)
print(lte)
if lte[2][0] == 1:
  # Sets LTE network as the default NIC.
  nic.set_default_NIC(lte[2][2]) 

#Starts NIC.
nic.set_up()

# Now other devices can connect to the module through the network cable for LTE network access.
...

```

Static IP Address Configuration

```python
# In the static IP address configuration, customizes network information based on the current environment.
import ethernet

# Loads the corresponding NIC driver and initializes the relevant configuration of NIC. Replaces the driver with the actual corresponding NIC driver.
nic = ethernet.diver(...)
print(nic.ipconfig())

# Configures the static IP address to 192.168.0.2, subnet mask to 255.255.255.0 and gateway address to 192.168.0.1.
nic.set_addr('192.168.1.100','255.255.255.0','192.168.1.1')
print(nic.ipconfig())

# Starts NIC.
nic.set_up()

# 1. In the terminal mode, starts other network services and accesses the network through Ethernet.
# 2. In the gateway mode, configures the default NIC and the peer static IP address according to the gateway user guide in the above example and then you can use this module to provide network services.
...

```

## Classes
- [class W5500 – W5500 Driver](./ethernet.W5500.md)
- [class DM9051 – DM9051 Driver](./ethernet.DM9051.md)
- [class CH395 – CH395 Driver](./ethernet.CH395.md)
- [class YT8512H – YT8512H Driver](./ethernet.YT8512H.md)
