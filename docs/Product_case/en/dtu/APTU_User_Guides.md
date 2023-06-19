## About document

**Revision history**

| **Version** | **Date** | **Author** | **Description** |
| --- | --- | --- | --- |
| 1.0 | 2020-07-27 | Chavis.Chen | Initial Version |

## Abstract

In this document, it aims at the concept and application of APTU (Application Packet Transparent Unit) in QuecPython. 

## About APTU


### Concept

APTU is the acronym of Application Packet Transparent Unit. 

The APTU, via data transparency, is widely applied in scenarios such as household applications and industry that needs network. It will work by importing the configured file into file system when producing.  

### Script file

3 scripts are involved in the APTU.

- OTA.py: Execute the upgrade of user file, meanwhile it can also be upgraded. 
- aptu.py: Execute the main logic of transparency service 
- aptu_config.json: Configure file such as UART,network, server, device info and OTA. 


### Function

- **Configure parameters of all functions via configuration file** 

All function-related parameters have been configured in *aptu_config.json*.

- **Event report when starting**

After starting up, it will report **once only** when data transparency is ready or error happens. 

- **Data transparency**

In APTU, the serial interface is used as the data transmission chain. As for the uart data from device, it will be transmitted to server via TCP. 

However, in terms of the data from TCP server, it will be transmitted to device via serial port directly. 

- **Script upgrade** 

After starting up and getting access to network, it will detect whether it is a need to upgrade script automatically.

- **Auto reattachment**

The module will reattach to server automatically once disconnected. 

When the device is informed that the data transmission is done, the service can be carried out correspondingly. 


## Application notes

### Configure file

**About contents** 

The user can modify parameters of the configuration file according to actual need. 

You can take contents on “**Code List 1**” as a reference. Moreover, the #  should be added into the **json file** for better understanding. 

In “Code List 1”, it shows the contents of *aptu_config.json*.

{

```json
{
    "UART":{ # Uart-related configuration
        "No":2, # Uart number
        "baudRate":9600, # Baud rate
        "startBitsLen":1, # Start bit
        "dataBitsLen":8, # Data bit
        "parity":"None", # Parity check: "None", "Odd", "Even"  
        "stopBitsLen":1, # Stop bit
        "flowCtrl":"disable", # HW flow control："enable", disable" 
        "significantBit":"least" # LSB
    },
    
    "Network":{ # Network-related configuration
        "timeWaitForOK":30 # Wait for th overtime of auto dial up, the unit is S
    },
    
    "Server":{ # Server-related configuration 
        "ipType":"IPv4", # IP type:"IPv4" & "IPv6"  
        "protocol":"TCP", # Connected transmission layer type: "TCP" & "UDP"  
        "domain":"www.baidu.com", # Domain name
        "port":80, # Port 
        "keepAlive":{ # Configure heart beat
            "useThisItem":"off", # Close the heart beat ："on","off" 
            "parameters":{ # Configure heart beat parameter
                "keepIdle":60, # Heart beat interval, the unit is s
                "keepInterval":5, # Time interval for resending heart beat package in every heart beat. 
                "keepCount":3 # Resending count of heart beat in every heart beat. 
            }
        }
    },
    
    "DeviceInfo":{ # Device info registered in the quectel cloud platform
        "moduleType":"EC600S-CX", # Module type, it is suggested to name it with the format of "module type-program name"
        "UID":"305", # String type, the unique identifier. 
        "PK":"2bb2a48bd30b6a525a30bc64d8b3d8e0" # Private key
    },
    
    "OTA":{ # OTA upgrade configuration
        "autoUpgrade":true # Boolean type. Auto upgrade: true. Non-auto upgrade: 
    }
}

```

}

**【Note】**

- For the key **on the left** of the colon, **the capital letter and small letter should be discriminated**.
- For the value **on the right** of the colon, apart form the interior field of *deviceinfo*, **there is no need to discriminate capital or small letter.**  
- Since it does not support the TCP heart beat option in QuecPython, the value of *Server.keepAlive.useThisItem* can be set as off. 
- As for the value of Boolean, it will be true and false. 

### Configure the default of file 

When configuring file, it is compulsory to select the *"No" &"baudrate"* in "**UART**" as well as *"domain" and "port"* in "**Server**" separately.

As for other non-compulsory items, they can be deleted. However, corresponding default will be done in codes, which is shown as Tablet 1. 

Tablet 1:  Configure the file default 

![aptu_01](media\aptu_01.png)

As above tablet implies: 

- As long as the font of any field is black, the contents under this field can be removed from configurration file and the default value can be used. 
- When the field with black character is visible in configured file, the red character of the subordinate in the neighbor should be compulsory.
- The field with red character of the first raw should be vivid in the configuration file.
- The"*KeepAlive*" field is not involved in the "*Server*" object, it means closing the heart beat function. 
- The OTA can only be started when both "*Deviceinfo*" and "*OTA*" objects appear synchronously.

### Import script file 

Import these three files into the module via QPYcom. 

After it is a success, three files are vividly shown on the red blanket of the next figure which located on the right bar of file transmission page on QPYcom. 

After selecting the *aptu.py*, click the "start" button on figure 1, the script function can be tested. 

![aptu_02](media\aptu_02.png)       

​                                                            Figure 1: Method to import script file 

### Call aptu module on service

Add codes shown on list 2 to service script for sake of starting.

Code list 2: Start APTU function

```python
from usr import aptu
aptu_obj = aptu.aptu_cls()
aptu_obj.start()
```

The object initialization function of *aptu_cls* contains two default parameters. The prototype is shown as "Code list 3". 

Code list 3: Object initialization function of *aptu_cls*.

```python
@classmethod
def __init__(cls, projectName = "APTU", projectVersion = "V1.0.0"):
    try:
        cls.PROJECT_NAME = projectName
        cls.PROJECT_VERSION = projectVersion
        cls.config = cls.__read_config()
        cls.__uart_init()
        cls.__data_call_check()
        cls.__ota_check()
    except Exception as e:
        cls.__exception_handler(e.args[0])
        raise

```



What we can learn from above figure vividly is that the default parameters are program name and version number separately. Please fill in according to actual need. And the default value is "APTU" and "V1.0.0"  individually. 


## Report event 

Although the APTU can match with data transparency mode completely, whether the function is normal after starting, there is a need to notify. 

As it implies above, it will report once only when data transparency is ready or error happens


### The format of reported event 

The format of reported event  is via *Json* text. the example is shown as "Code list 4". 

Code list 4: json format of reported event

{

```json
{
    "result": {
        "code": 0,
        "desc": "OK"
    },
    "data": {
        "SN": "D1Q21E2130204660P",
        "IMEI": "861681053233719"
    }
}

```

}

Two sub objects "result" and "data" are enrolled into the json object of above text. 

- As for "result"object, it also contains two fields-- “code” and "desc", which are used to report whether the APTU is ready for data transparency. 

- In terms of "data" object, "SN" and "IMEI" are enrolled. The "data" object will be contained only when the value of "code" in "result" is 0. 

  The data type illiustration of above field are listed on Tablet 2.

Tablet 2: data type illustration

| **Field** | **Data type** |
| --- | --- |
| code | Integer |
| desc | String |
| SN | String |
| IMEI | String |

### Result interpretation 

The "result" object refers to the result notification of event. 

The result interpretation is displayed as Tablet 3

Tablet 3: Event result interpretation

| **code** | **desc** | **mark** |
| --- | --- | --- |
| 1 | OTA plain comes | The latest version is to be upgraded, when the module reports this announcement, it will reboot automatically and upgrade to the latest version. |
| 0 | OK | Valid to transmit data |
| -1 | config error | sssssssssssss Error to configure file |
| -2 | net error | Network error |
| -3 | socket create error | Fail to create socket |
| -4 | socket option set error | Fail to set socket option |
| -5 | socket connect error | Fail to access to server |
| -6 | DNS error | Failure in DNS |
| -7 | UART error | Uart error |
| -8 | sys error | System error |
