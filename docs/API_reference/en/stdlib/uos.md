# uos - Basic System Services

`uos` module contains file system access and mounting building, and realizes subsets of the corresponding CPython module. See CPython file [os](https://docs.python.org/3.5/library/os.html#module-os) for more detailed information.

## Deleting the File

### `uos.remove`

```python
uos.remove(path)
```

Deletes the file.

**Parameter**

* `path` - String type. The file name.

## Changing the Current Directory

### `uos.chdir`

```python
uos.chdir(path)
```

Changes the current directory.

**Parameter**

* `path` - String type. The directory name.

## Getting the Current Path

### `uos.getcwd`

```python
uos.getcwd()
```

Gets the current path.

**Return Value**

The return value is in string type, which indicates the current path.

## Listing the Specified Directory File

### `uos.listdir`

```python
uos.listdir( [dir] )
```

If the parameter is not provided, the current directory file will be listed. Otherwise the specified directory file will be listed.

**Parameter**

* `dir` - String type. An optional parameter indicates the directory name. Default directory: ‘/’ .

**Return Value**

The return value is in tuple type, which indicates listing all existing objects under the path (directories and files).

**Example**

```python
>>> uos.listdir()
[‘file1’, ‘read.txt’, ‘demo.py’]
```

## Creating A Directory

### `uos.mkdir`

```
uos.mkdir(path)
```

Creates a directory.

**Parameter**

* `path` indicates the name of the directory to be created. It is in the relative path of the directory.

**Example**

```python
>>> uos.mkdir('testdir')
>>> uos.listdir()
[‘file1’, ‘read.txt’, ‘demo.py’, 'testdir']
```

## Renaming the File

### `uos.rename`

```python
uos.rename(old_path, new_path)
```

Renames the file.

**Parameter**

* `old_path` - String type. The old file or directory name.
* `new_path` - String type. The new file or directory name.

**Example**

```python
>>> uos.rename('testdir', 'testdir1')
```

## Deleting the Specified Directory

### `uos.rmdir`

```python
uos.rmdir(path)
```

Deletes the specified directory.

**Parameter**

* `path` - String type. The directory name. It is in the relative path of the directory.

**Example**

```python
>>> uos.rmdir('testdir')
>>> uos.listdir()
[‘file1’, ‘read.txt’, ‘demo.py’]
```

## Listing the Parameters of the Current Directory

### `uos.ilistdir`

```python
uos.ilistdir( [dir] )
```

This function returns an iterator that generates the 3-tuple corresponding to the listed entry.

**Parameter**

* `dir` - String type. An optional parameter indicating the directory name. If the parameter is not provided, the current directory will be listed by default. Otherwise the directory specified by dir will be listed.

**Return Value**

This function returns an iterator that generates the 3-tuple corresponding to the listed entry.

The tuple has the  form of  `(name, type, inode[, size])`:

* `name` - String type.  The name of the entry. If dir is a byte object, the name is in byte type;
* `type` - Integer type. The type of the entry. 0x4000 indicates the directory, 0x8000 indicates the regular file;
* `inode` is an integer corresponding to the index node of the file, and may be 0 for file systems that don’t have such a notion;
* Some modules may return a 4-tuple that includes the entry's size. For file entries, size is an integer representing the size of the file. If it is unknown, the value will be -1. Its meaning is currently undefined for the directory entry.

## Getting the Status of the File or Directory

### `uos.stat`

```python
uos.stat(path)
```

Gets the status of the file or directory.

**Parameter**

* `path` - String type. The name of the file or directory.

**Return Value**

The return value is a tuple with the form of:

`(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)`

* `mode` – inode protection mode
* `ino` – inode node number
* `dev`  – inode device
* `nlink`  – inode number of links
* `uid ` – User ID of the owner
* `gid`  – Group ID of the owner
* `size`  – Size of the file. Unit: byte
* `atime`  – Last access time
* `mtime`  – The last modification time
* `ctime`  – "ctime" reported by the operating system. On some systems it is the latest time of meta-data changing, on others it is the creation time. See the document of the module for details.

## Getting the Status of the File System

### `uos.statvfs`

```python
uos.statvfs(path)
```

Gets the status of the file system.

**Parameter**

* `path` - String type. The name of the file or directory.

**Return Value**

Returns a tuple with the file system information:

`(f_bsize, f_frsize, f_blocks, f_bfree, f_bavail, f_files, f_ffree, f_favail, f_flag, f_namemax)`

* `f_bsize` – Block size of the file system. Unit: byte.
* `f_frsize` – Fragment size. Unit: byte.
* `f_blocks` – Number of data blocks in the file system.
* `f_bfree` – Number of available blocks.
* `f_bavai` – Number of available blocks for non-administrator.
* `f_files`  – Number of file inodes.
* `f_ffree` – Number of available file inodes.
* `f_favail` – Number of available file inodes for administrator.
* `f_flag` – Mounting flags.
* `f_namemax` – The maximum length of the file. Unit: byte.

**Example**

```python
>>> import uos
>>> res = uos.statvfs("main.py")
>>> print(res)
(4096, 4096, 256, 249, 249, 0, 0, 0, 0, 255)
```

## Getting the Information of the Underlying System or Its Operating System

### `uos.uname`

```python
uos.uname()
```

Gets the information of the underlying system or its operating system.

**Return Value**

The form of the return value of this interface differs from that of the official Micropython interface. This interface returns a tuple with the form of:

`(sysname, nodename, release, version, machine)`

* `sysname` – String type. The name of the underlying system.
* `nodename` – String type. Network name (it can be the same as sysname).
* `release` – String type. The version of the underlying system.
* `version` – String type. MicroPython version and build date.
* `machine` – String type. Identifier of the underlying hardware (such as the main board and CPU).
* `qpyver` – String type. Short QuecPython version number.

**Example**

```python
>>> import uos
>>> uos.uname()
('sysname=EC600S-CNLB', 'nodename=EC600S', 'release=1.12.0', 'version=v1.12 on 2020-06-23', 'machine=EC600S with QUECTEL', 'qpyver=V0001')
>>> uos.uname()[0].split('=')[1] # The value of sysname can be obtained in this way
'EC600S-CNLB'
```

### `uos.uname2`

```python
uos.uname2()
```

Gets the information of the underlying system or its operating system.

**Return Value**

The form of the return value of this interface is the same as that of the official Micropython interface. Please note the difference from the return value of uos.uname(). The return value with the form of:

`(sysname, nodename, release, version, machine, qpyver)`

* `sysname` – String type. The name of the underlying system.
* `nodename` – String type. Network name (it can be the same as sysname).
* `release` – String type. The version of the underlying system.
* `version` – String type. MicroPython version and build date.
* `machine` – String type. Identifier of the underlying hardware (such as the mainboard and CPU).
* `qpyver` – String type. QuecPython short version number.

**Example**

```python
>>> import uos
>>> uos.uname2()
(sysname='EC600S-CNLB', nodename='EC600S', release='1.12.0', version='v1.12 on 2020-06-23', machine='EC600S with QUECTEL', qpyver='V0001')
>>> uos.uname2().sysname  # The value of sysname can be obtained directly in this way
'EC600S-CNLB'
>>> uos.uname2().machine
'EC600S with QUECTEL'
```

## Returning A Bytes Object with *n* Random Bytes

### `uos.urandom`

```python
uos.urandom(n)
```

Returns a bytes object with *n* random bytes. If the module is equipped with a hardware random number generator, the object will be generated by the hardware random number generator.

**Parameter**

* `n` - Integer type. Number of random bytes.

**Return Value**

A bytes object with *n* random bytes.

**Example**

```python
>>> import uos
>>> uos.urandom(5)
b'\xb3\xc9Y\x1b\xe9'
```

## Registering the Storage Device - SPI - SD Card

> Only EC600N and EC800N series modules support this feature currently.

### `uos.VfsFat`

```python
uos.VfsFat(spi_port, spimode, spiclk, spics)
```

Initializes the SD card through SPI prototype and SD card communication.

**Parameter**

* `spi_port` - Integer type. Channel selection [0,1].
* `spimode` - Integer type. SPI work mode (mode 0 is the most commonly used):<br />
|Parameter|Work Mode|
| ---- | ---- |
|   0   |CPOL=0, CPHA=0|
|   1   | CPOL=0, CPHA=1|
|   2  |CPOL=1, CPHA=0|
|   3  |CPOL=1, CPHA=1|
> Clock polarity CPOL: The pin level of the clock signal SCLK when SPI is idle. (0: low level when idle; 1: high level when idle).

* `spiclk` - Integer type.

|Parameter|Clock Frequency|
| ---- | ---- |
|   0   |812.5 KHz|
|   1   |1.625 MHz|
|   2  |3.25 MHz|
|   3  |6.5 MHz|
|   4  |13 MHz|

* `spics` - Integer type. Assigns the CS pin as any GPIO. Hardware CS can connect this specified pin or the default SPI CS pin.

> 1-n: Assigns Pin.GPIO1 - Pin.GPIOn as the CS pin.

**Return Value**

If the execution is successful, VfsFat object will be returned. If the execution is failed, it will be stuck.

**Example**

```python
>>> cdev = uos.VfsFat(1, 0, 4, 1)
```

## Registering the Storage Device - SDIO - SD Card

> Only EC600U and EC200U series modules support this feature currently.

### `uos.VfsSd`

```python
uos.VfsSd(str)
```

Initializes the SD card through SDIO prototype.

* `str`– String type. Inputs "sd_fs".

**Return Value**

If the execution is successful, vfs object will be returned. If the execution is failed, the error will be reported.

**Pin Description**

| Module | Pin                                                          |
| ------ | ------------------------------------------------------------ |
| EC600U | CMD: Pin 48<br />DATA0: Pin 39<br />DATA1: Pin 40<br />DATA2: Pin 49<br />DATA3: Pin 50<br />CLK: Pin 132 |
| EC200U | CMD: Pin 33<br />DATA0: Pin 31<br />DATA1: Pin 30<br />DATA2: Pin 29<br />DATA3: Pin 28<br />CLK: Pin 32 |

**Example**

```python
>>> from uos import VfsSd
>>> udev = VfsSd("sd_fs")
```

## Setting the Pin for SD Card Detection

### `uos.set_det`

```python
uos.set_det(vfs_obj.GPIOn,mode)
```

Assigns the pin and mode for detecting the insertion and removal of the SD card.

**Parameter**

* `vfs_obj.GPIOn` - Integer type. GPIO pin number for detecting the insertion and removal of the SD card. Please refer to the definition of [Pin](../QuecPython类库/machine.Pin.md) module.
* `mode` - Integer type.<br />0: After the SD card is inserted, the detection port is in low level. After the SD card is removed, the detection port is in high level. <br />1: After the SD card is inserted, the detection port is in high level. After the SD card is removed, the detection port is in low level.

**Return Value**

`0` - Successful execution; `-1` - Failed execution.

**Example**

```python
>>> from uos import VfsSd
>>> udev = VfsSd("sd_fs")
>>> uos.mount(udev, '/sd')
>>> udev.set_det(udev.GPIO10,0)#Uses GPIO10 as the pin to detect the SD card. After the SD card is inserted, the detection port is in low level. After the SD card is removed, the detection port is in high level (actual usage depends on the hardware)
```

## Setting the Callback Function of Inserting And Removing the SD Card

### `uos.set_callback`

```python
uos.set_callback(fun)
```

Sets the user callback function when the card is inserted or removed.

**Parameter**

* `fun` - Function type. When the card is inserted or removed,  `[ind_type]` will be called.
* `ind_type` - Event type. 0: Removing the card; 1: Inserting the card.

**Return Value**

`0` - Successful execution; `-1` - Failed execution.

**SD Card (SDIO port) Example**

> Only EC600U and EC200U series modules support this feature currently.

**Example**

```python
from uos import VfsSd
import ql_fs
udev = VfsSd("sd_fs")
uos.mount(udev, '/sd')
udev.set_det(udev.GPIO10,0)
#Reads and writes the file
f = open('/sd/test.txt','w+')
f.write('1234567890abcdefghijkl')
f.close()
uos.listdir('/sd')
f = open('/sd/test.txt','r')
f.read()
f.close()
#The callback function of inserting and removing the card
def call_back(para):
    if(para == 1):
        print("insert")
        print(uos.listdir('/usr'))  
        print(ql_fs.file_copy('/usr/1.txt','/sd/test.txt'))#Copies test.txt from the SD card to 1.txt in usr
        print(uos.listdir('/usr'))
    elif(para == 0):
        print("plug out")   
  
udev.set_callback(call_back)
```

## Registering the Storage Device littleFS - SPI NOR FLASH

> Only EG915U and EC600N series modules support this feature currently.

### `uos.VfsLfs1`

```python
uos.VfsLfs1(readsize,progsize,lookahead,pname,spi_port,spi_clk)
```

Communicates with the external NOR FLASH through SPI. The storage device is mounted as the littleFS file system through SPI.

**Parameter**

* `readsize` - Integer type. Reserved. It is not used yet.
* `progsize` - Integer type. Reserved. It is not used yet.
* `lookahead` - Integer type. Reserved. It is not used yet.
* `pname` - String type. The partition name is fixed to "ext_fs". It will be expanded later.
* `spi_port` - Integer type. See SPI chapter for supported ports.
* `spi_clk` - Integer type. <br />
|Parameter|Clock Frequency|
| ---- | ---- |
|   0   |6.25 MHz|
|   1   |12.5 MHz|
|   2  |25 MHz|
|   3  |50 MHz|
|   4  |3.125 MHz|
|   5  |1.5625 MHz|
|  6  |781.25 KHz|
**Return Value**

VfsLfs1 object - Successful execution; OSError 19 - Failed execution.

**Example**

```python
>>>ldev = uos.VfsLfs1(32, 32, 32, "ext_fs",1,0)
>>>uos.mount(ldev,'/ext')
>>>f = open('/ext/test.txt','w+')
>>>f.write('hello world!!!')
>>>f.close()
  
>>>uos.listdir('ext')
  
>>>f = open('/ext/test.txt','r')
>>>f.read()
>>>f.close()
  
```

## Mounting the File System

### `uos.mount`

```python
uos.mount(vfs_obj, path)
```

Mounts the file system in substantial form (such as littleFS or FATFS ) to the virtual file system(VFS).

**Parameter**

* `vfs_obj` - vfs object. The object of the file system.
* `path` - String type. The root directory of the file system.

**Example**

```python
>>> cdev = uos.VfsFat(1, 0, 4, 1)
>>> uos.mount(cdev, '/sd')
```

**SD Card (SPI port) Example**

> Only EC600N, EC800N, EC600U and EC200U series module support this feature currently.

```python
>>> cdev = uos.VfsFat(1, 0, 4, 1)
>>> uos.mount(cdev, '/sd')
>>> f = open('/sd/test.txt','w+')
>>> f.write('0123456')
>>> f.close()
>>> uos.listdir('/sd')
>>> f = open('/sd/test.txt','r')
>>> f.read()
>>> f.close()
```
