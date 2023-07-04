---
title: Driver Download
keywords: Driver Download
description: Driver Download
---

## Revision History

| Version | Date       | Author | Description                                    |
| ------- | ---------- | ------ | ---------------------------------------------- |
| 1.0     | 2021-09-02 | Kayden | Initial compilation& User Guide on Quick-Start |
| 1.1     | 2021-09-10 | David  | Added the notices on environment building      |

## Build QuecPython Development Environment

### Acquire the Real EVB

For detailed operation, you can refer to the EC600X EVB.

In this document, we just take EC600S_QuecPython_EVB_V1.1 as an example. As for the differences compared with V1.2 or V1.3, you can check the above link on EC600X EVB. 

<img src="media/readme_2.png" style="zoom: 50%;" />



After acquiring the EVB, plug in the USB interface on the EVB  and carry out power supply, while on the other side, connect it to the USB interface of the PC. The multi-functional EVB supports power on/off as same as another cellphone does. As a result, we can power on once the power supply is conducted. 

### How to Boot 



| EVB                        | Boot operation                                               |
| -------------------------- | ------------------------------------------------------------ |
| EC600S_QuecPython_EVB_V1.0 | Plug in to boot                                              |
| EC600S_QuecPython_EVB_V1.1 | Long press the POWKY on the EVB for 2 seconds, the module will boot |
| EC600X_QuecPython_EVB_V1.2 | If make short circuit of the PWR_On Jumper on EVB, there is no need to long press PWK; otherwise, it should be done. |
| EC600X_QuecPython_EVB_V1.3 | After power supply,  flip the power supply selection switch to select the power supply mode, then long press the PWK to boot; or make short circuit of the PWR_On Jumper on EVB, there is no need to long press PWK. |

### Download and Install Driver

As the name implies,  " device driver ", with its full name of " device driver program ", is a special program that used to communicate between PC and device. To some extent, it is similar with the HW interface. The operation system can control the running of HW device via this interface only; and if the driver program of certain device is failed to install, it won't run normally.

Open the [Link of downloading driver](https://python.quectel.com/download), then select the driver that matched with your own PC as the figure shows. If you drag the arrow to the right, a button for downloading will appear, just click it. 

Notices on driver installation

1. **The driver is divided into two categories mainly:**

   **No. 1** Based on the platform: ASR platform (EC600SCNAA、EC600SCNLA、EC600SCNLB、EC600N、EC100Y）and RDA platform（EC600U).

   Many may ask what the platform of EC600X is. Generally, the ” **X** “ in EC600X is an unknown, which can indicate EC600S or EC600U instead of the actual platform. 

   **No. 2** Based on the PC system: Whether in Windows 7 or Windows 10, please download corresponding driver separately.

2. **While in terms of EC600SCNLA and EC600SSCNLB, it is a must to download the latest driver with at least V1.0.8 and later.** 

3. **In RDA platform, after downloading USB driver zip, it contains drivers of both Windows 7 and Windows 10.**


<img src="media/readme_3_en.png" style="zoom: 67%;" />

Please do as following sequence: open " **My Computer** "--" **Management** "--" **Device manager** "

<!-- Before installing driver: 

<img src="media/readme_4.png"  /> -->

After installing driver

![](media/readme_5_en.png)

Open unzipped package, then double click to run " **setup.exe** "; after that, keep on clicking the " **Next Step** " till the installation is done. If the port marked with " **exclamation** " in " d**evice manager** " is invisible, which means the installation is a success and normal communication can be executed. **As the above figure implies, there still exists an" exclamation ", please just ignore for it is useless.** 

![](media/readme_6.png)

![](media/readme_7_en.png)

![](media/readme_8.png)



### Note on Flashing FW

1. **Different modules are varied in FW, as a result, it does not support cross-flashing. If there is a mistake, please correct it and flash the corresponding FW, otherwise, it won’t work. Take EC600S as an example, it is divided into EC600SCNAA, EC600SCNLA, EC600SCNLB and so on, which do not support cross-flashing among these modules.** 

2. **About FW, owing to the FW zip package downloaded from official website contains FW package and change log, only unzip the FW package further can you get the flashed FW package. It is evaluated to modify the suffix of FW package as .bin. (It is in schedule. If the later update is accomplished, please select the zip file with .bin suffixed when flashing.)**

3. **Before downloading FW, it is suggested to confirm the FW version priorly so as to avoid degrade or download the wrong one. After downloading, all contents in user area will be empty.**

4. **When downloading FW, there is no need to select serial interface since the tool will select it automatically and download.**

5. **Never plug in two or more EVBs at the same time so as to avoid the unidentified situation, even worse, result in the error in downloading.**

6. **The QPYcom supports flashing Python FW instead of the FW of C or AT Standard.** 

7. **When downloading FW, please do not exit tool or plug out the serial interface, which may result in the inaccessibility of module.**

### How to Use QPYcom.exe

In official website, it provides a tool in Windows for user to debug code. 

Download link： https://python.quectel.com/download

About QPYcom, please refer to the "docs in folder  which is under the directory as same as that of tool".

### Working Principle

Hereby, we should learn about how the whole process works.

![](media/readme_9.png)

![image-20211009095453632](media/readme_10_en.png)

One QuecPython syntactic interpreter is embedded in module, which used to interpret QuecPython syntax. After that, return executed result. 

Illustration 

print('Hello world! QuecPython')

The print (), a function, is used to output some info from the inner device. Thus, the user can learn about the device on PC. 

The print () can also be used to print string and variate. 

In QuecPython, the string is indicated by a pair of single quotation marks, such as ‘Hello world! QuecPython’. 

### In Real Scenario

****![](media/readme_11_en.png)

After opening up QPYcom, we can see three ports in “select interface” are module-related, among which: 

The "Quectel USB AT Port" is used to send AT command.

As for "Quectel USB DIAG Port" , it is used to check the debugging info of module. 	

It is hardly for user to deploy above two ports. As a result, we should pay attention to " ***Quectel USB MI05 COM port*** " particularly. we can debug the code via this port only. 

Click dropdown with selecting " ***Quectel USB MI05 COM port*** " following, after that, click " **Enable serial interface** ".

Input **print('Hello world! QuecPython')** in interaction surface and click " **Enter** ".

What we can see is shown as following 

```python
>>> print('Hello World! QuecPython')

Hello World! QuecPython

>>> 
```

![image-20210910111634969](media/readme_12.png)

The returned value of module is visible and "Hello world! QuecPython" is outputted successfully. 

### Other API Interfaces

For other functions, please refer to the official website: https://python.quectel.com/wiki/#/en-us/api/QuecPythonClasslib?id=pin

 It is also available to download relevant tools, routines, drivers and documents in official website: https://python.quectel.com/download

You can also follow our Wechat official account to get more latest info. 
