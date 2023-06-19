## About document

**Revision history**

| Version | Date       | Author  | Description     |
| ------- | ---------- | ------- | --------------- |
| 1.0     | 2021-11-25 | Chic.Ye | Initial version |

## RDA FW Upgrade

In this document, it mainly introduces how to upgrade FW via FOTA based on EC600U. 

Applicable modules: EC600U_CNLB、CNLC and EUAB

## Operation procedure on EC600U_CNLB, CNLC and EUAB

1. Extract upgrade file 

Duplicate the **.pac** file from the "old" and "new" FW packages, then rename them as **aa.pac** and **bb.pac** separately. 

![FOTA_RDA_01](media\FOTA_RDA_01.png)

 

2. Make **.bin** file

Duplicate **aa.pac** and **bb.pac** into the root directory of FOTA, after that, execute AT commands as described below. 

`dtools.exe fotacreate2 --pac aa.pac,bb.pac,setting\fota8910.xml output.pack -d v`

![FOTA_RDA_02](media\FOTA_RDA_02.png) 

3. Please check the result as described below. 

![FOTA_RDA_04](media\FOTA_RDA_04.png)

Generate **FotaFile.bin** file for downloading and upgrading module.

4. Place the upgrade file into http server

In this test, the address for downloading is shown as 

[http://120.197.216.227:6000/FotaFile.bin](http://120.197.216.227:6000/FotaFile.bin)



## SW design

```Python
import fota
import utime

DEF_URL1 = 'http://120.197.216.227:6000/FotaFile.bin'

def result(args):
    print('download status:', args[0], 'download process:', args[1])

def run():
    fota_obj = fota()  # Create FOTA object
    print("Enter Upgrade Status......")
    res = fota_obj.httpDownload(url1=DEF_URL1, callback=result)
    if res != 0:
        return
    utime.sleep(2)

run()
```



## Download and verify 

#### SW code 

Download **.py** file and run on module 

![FOTA_RDA_03](media\FOTA_RDA_03.png)



After that, run the script manually. 

The upgrade will be accomplished about 5 minutes later, as a result, you can query more details. 

Input in interaction surface

```python
>>> uos.uname2()
(sysname='EC600U-EUAB', nodename='EC600U', release='1.13.0', version='v1.12 on Tue_Oct_19_2021_5:26:44_PM', machine='EC600U with QUECTEL', qpyver='V0002')
```

By verifying, the upgrade is a success. 