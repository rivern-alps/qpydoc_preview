# fota - Firmware Upgrade

`fota`  provides the feature of firmware upgrade.

**Examples:**

```python
# OTA Upgrade. The module will restart automatically after the upgrade package is downloaded.

import fota
import utime
import log

# Sets the log output level
log.basicConfig(level=log.INFO)
fota_log = log.getLogger("Fota")

def result(args):
    print('download status:',args[0],'download process:',args[1])
    
def run():
    fota_obj = fota()  # Creates a FOTA object
    fota_log.info("httpDownload...")
    # Methods of DFOTA upgrades
    res = fota_obj.httpDownload(url1="http://www.example.com/fota.bin",callback=result)    
    # Methods of mini FOTA
    #res = fota_obj.httpDownload(url1="http://www.example.com/fota1.bin",url2="http://www.example.com/fota2.bin")
    if res != 0:
        fota_log.error("httpDownload error")
        return
    fota_log.info("wait httpDownload update...")
    utime.sleep(2)

if __name__ == '__main__':
    fota_log.info("run start...")
    run()    
```

```python
# OTA Upgrade. The module won't restart automatically after the upgrade package is downloaded.

import fota
from misc import Power

fota_obj = fota(reset_disable=1)

def result(args):
    print('download status:',args[0],'download process:',args[1])
    
fota_obj.httpDownload(url1="http://www.example.com/dfota.bin",callback=result) # Expects that the module won't restart after the upgrade package is downloaded. 
Power.powerRestart() # Restarts the module manually for the upgrade 
```

```python
# Local upgrade

import fota
import utime
import log
from misc import Power
import uos

'''
The following two global variables are necessary. You can modify the values of these two global variables based on your project requirements.
'''
PROJECT_NAME = "QuecPython_Fota_example"
PROJECT_VERSION = "1.0.0"

# Sets the log output level
log.basicConfig(level=log.INFO)
fota_log = log.getLogger("Fota")

# For this example, the file of upgrade package is required like FOTA packages of .bin files and it shall be stored in the file system.

def run():
    fota_obj = fota()  # Creates a FOTA object
    file_size = uos.stat("/usr/FotaFile.bin")[6]  # Gets the total number of bytes of the file
    print(file_size)
    with open("/usr/FotaFile.bin", "rb")as f:   # Opens .bin files (The upgrade package needs to be made.) in the rb mode
        while 1:
            c = f.read(1024)   # read
            if not c:
                break
            fota_obj.write(c, file_size)  # Writes data of .bin files and total bytes of the file
	
    fota_log.info("fota image flush...")
    res = fota_obj.flush()  # Refresh
    if res != 0:
        fota_log.error("flush error")
        return
    fota_log.info("fota image verify...")
    res = fota_obj.verify()  # Verify
    if res != 0:
        fota_log.error("verify error")
        return
    fota_log.info("power_reset...")
    utime.sleep(2)
    Power.powerRestart()   # Restarts the module


if __name__ == '__main__':
    fota_log.info("run start...")
    run()
```



## Initialization

### FOTA

```python
fota(reset_disable=)
```

Creates a FOTA object.

**Parameter:**

- `reset_disable` - Optional parameter. Whether to disable the feature that the module restarts automatically after the upgrade package is downloaded. 1–Disable; Omitted/0–Enable

**Return Value:**

- A FOTA object.

**Note:**

EC600N/EC800N/EG912N/EC600M/EC800M/EG810M series module does not support to disable the feature that the module restarts automatically after the upgrade package is downloaded.    

**Example:**

```python
import fota
fota_obj = fota() # The module will restart automatically after the upgrade package is downloaded. 
# fota_obj = fota(reset_disable=1) # The module won't restart automatically after the upgrade package is downloaded.
```

## OTA Upgrade

This interface can realize the whole process of upgrade package download and firmware upgrade.

### fota_obj.httpDownload

```python
fota_obj.httpDownload(url1=, url2=, callback=)
```

Download, write and verify the upgrade package and restart the module to complete the upgrade.

**Parameter:**

- `url1` - String type. Optional parameter. URL of the upgrade package. This URL can be in HTTP or FTP format. Note: Only EC200A series module supports the URL in FTP format.  
- `url2` - String type. Optional parameter. URL of the upgrade package of the second stage in mini FOTA upgrades. Note: This parameter needs to be passed only in mini FOTA upgrades and it is prohibited to be passed in DFOTA upgrades. Mini FOTA upgrade is a special firmware upgrade method for small storage modules and it is divided into two stages. DFOTA upgrades only have one stage. Only EC600N/EC800N/EG912N/EC600M/EC800M/EG810M series module supports mini FOTA upgrades.
- `callback` - Function type. Optional parameter. This callback function displays the download progress and status. Note: In mini FOTA upgrades, the callback function is not supported. Parameter descriptions of callback function are as follows. 

| Parameter | Type | Description                                                  |
| --------- | ---- | ------------------------------------------------------------ |
| args[0]   | int  | Download status. 0/1/2 – Successful download; Other values – Failed download. |
| args[1]   | int  | Download progress. (Note: For EC600N/EC800N/EG912N series module, it indicates percentage when the download status is successful and indicates error codes when the download status is failed. ) |

**Return Value:**

- `0` - Successful execution

  `-1` - Failed execution

  Note: For EC600N/EC800N/EG912N/EC600M/EC800M/EG810M/BC25 series module, return values only indicate successful or failed execution of this interface. The upgrade status and results are returned in callback. For other series modules, 0 indicates successful download and verification. -1 indicates failed download and verification.

**Example:**

```python
def result(args):
    print('download status:',args[0],'download process:',args[1])
    
# DFOTA upgrades over HTTP
fota_obj.httpDownload(url1="http://www.example.com/fota.bin",callback=result)
# DFOTA upgrades over FTP
fota_obj.httpDownload(url1="ftp://user:password@ip:port/fota.bin",callback=result) # You need to enter the FTP server information you actually use for "user", "password", "ip" and "port".  
#m Mini FOTA
fota_obj.httpDownload(url1="http://www.example.com/fota1.bin",url2="http://www.example.com/fota2.bin")
```

### fota_obj.apn_set

```python
fota_obj.apn_set(fota_apn=,ip_type=,fota_user=,fota_password=)
```

Sets APN information used in FOTA download.

**Parameter:**

- `fota_apn` - String type. Optional parameter. APN.
- `ip_type` - Integer type. Optional parameter. IP type: 0-IPv4; 1-IPv6.
- `fota_user` - String type. Optional parameter. Username.
- `fota_password` - String type. Optional parameter. Password.

**Return Value:**

- `0` - Successful execution

  `-1` - Failed execution

**Example:**

```python
fota_obj.apn_set(fota_apn="CMNET",ip_type=0,fota_user="abc",fota_password="123")
```

**Note:**

Only BG95 series module supports this interface.

### fota_obj.download_cancel

```python
fota_obj.download_cancel()
```

Cancels the FOTA upgrade package download in progress.

**Return Value:**

- `0` - Successful execution

  `-1` - Failed execution

**Example:**

```python
import fota
import _thread
import utime

def th_func():
    utime.sleep(40) # The time depends on the size of the upgrade package. Make sure to cancel the FOTA upgrade package download before the download is complete. 
    fota_obj.download_cancel()

def result(args):
    print('download status:',args[0],'download process:',args[1])

fota_obj = fota()
_thread.start_new_thread(th_func, ())
fota_obj.httpDownload(url1="http://www.example.com/fota.bin",callback=result)
```

**Note:**

Only BG95 series module supports this interface.

## Local Upgrade

You can call the following interfaces to write upgrade package data to flash, verify upgrade package content and restart the module to complete the upgrade.

### fota_obj.write

```python
fota_obj.write(bytesData, file_size)
```

Writes data stream of the upgrade package. 

**Parameter:**

- `bytesData` - Bytes type. The content data of the upgrade package.
- `file_size` - Integer type. Total size of upgrade package files. Unit: byte.

**Return Value:**

- `0` - Successful execution

  `-1` - Failed execution

### fota_obj.flush

```python
fota_obj.flush()
```

Refreshes data in the RAM to flash. Because the size of the upgrade package files is not necessarily an integer multiple of the RAM size in the code, `fota_obj.flush` needs to be called to write data in the RAM to flash after the last call of `fota_obj.write`.

**Return Value:**

- `0` - Successful execution

  `-1` - Failed execution

### fota_obj.verify

```python
fota_obj.verify()
```

Verifies the upgrade package.

**Return Value:**

- `0` - Successful execution

  `-1` - Failed execution

**Note:**

EC600NCNLC/EC600NCNLF/EG912N/EC600U/EC200U/EG915U/EG912U/EC800G/EC600E/EC800E series module supports the features related to local upgrade.

