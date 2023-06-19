## About document

**Revision history**

| Version | Date       | Author  | Description     |
| ------- | ---------- | ------- | --------------- |
| 1.0     | 2021-09-29 | Chic.YE | Initial version |



## FOTA_binary_upgrade  FW upgrade

In this document, it mainly introduces how to upgrade FW based on EC600S-CNLA module. Furthermore, you will learn about FOTA of EC600S-CNLA after reading this paper. 



## Operation Procedure

1. Export upgrade file 

Copy the *system.img* from the new and old zips separately, the rename them as *system_old.img* and *system_new.img* individually. Please check the next figure: 

![FOTA_ASR_01](media\FOTA_ASR_01.png)

 

2. Configure file. 

```python
[Image_List]

Number_of_Images = 1

1_Image_Enable = 1

1_Image_Image_ID = 0x30

1_Image_Path = system.bin

1_Image_Flash_Entry_Address = 0x00024000

1_Image_ID_Name = 1
```

 

3. Make **.bin** file

Duplicate the *system_old .img* and *system_new.img* into the root directory of FOTA tool, then execute commands as described below: *adiff.exe -l fp system_old.img system_new.img FotaFile.bin*.

![FOTA_ASR_02](media\FOTA_ASR_02.png) 

Result after executing

![FOTA_ASR_04](media\FOTA_ASR_04.png)

 The *FoteFile.bin* file will be generated for the module to download and upgrade.

4. Locate the upgraded file into http server. 

The address used to download in this test is  [http://120.197.216.227:6000/FotaFile.bin](http://120.197.216.227:6000/FotaFile.bin)



## SW design 

```Python
import fota
import utime

DEF_URL1 = 'http://120.197.216.227:6000/FotaFile.bin'

def result(args):
    print('download status:', args[0], 'download process:', args[1])

def run():
    fota_obj = fota()  # Build Fota object
    print("Enter upgrade status......")
    res = fota_obj.httpDownload(url1=DEF_URL1, callback=result)
    if res != 0:
        return
    utime.sleep(2)

run()
```



## Download and verify

#### SW code

Download the ***.py*** file and run on module

![FOTA_ASR_03](media\FOTA_ASR_03.png)



After downloading, run the script manually. 

About 5 minutes later, the upgrade will be complete, then you can check: 

Transmit in interaction surface

```python
>>> modem.getDevFwVersion()

'EC600SCNLAR01A01M16_OCPU_PY_BETA0414'
```

As the above figure implies, the verification is a success. 