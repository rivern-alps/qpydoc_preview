# fota - 固件升级相关功能

`fota`模块用于固件升级。

**示例**：

```python
#远程升级

import fota
import utime
import log

# 设置日志输出级别
log.basicConfig(level=log.INFO)
fota_log = log.getLogger("Fota")

def result(args):
    print('download status:',args[0],'download process:',args[1])
    
def run():
    fota_obj = fota()  # 创建Fota对象
    fota_log.info("httpDownload...")
    #差分升级方式
    res = fota_obj.httpDownload(url1="http://www.example.com/fota.bin",callback=result)    
    #mini fota方式
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
#本地升级

import fota
import utime
import log
from misc import Power
import uos

# 设置日志输出级别
log.basicConfig(level=log.INFO)
fota_log = log.getLogger("Fota")

# 此示例需要升级包文件(差分包等.bin文件),且存放到文件系统中

def run():
    fota_obj = fota()  # 创建Fota对象
    file_size = uos.stat("/usr/FotaFile.bin")[6]  # 获取文件总字节数
    print(file_size)
    with open("/usr/FotaFile.bin", "rb")as f:   # rb模式打开.bin文件(需要制作升级包文件)
        while 1:
            c = f.read(1024)   # read
            if not c:
                break
            fota_obj.write(c, file_size)  # 写入.bin文件数据与文件总字节数
	
    fota_log.info("fota image flush...")
    res = fota_obj.flush()  # 刷新
    if res != 0:
        fota_log.error("flush error")
        return
    fota_log.info("fota image verify...")
    res = fota_obj.verify()  # 校验
    if res != 0:
        fota_log.error("verify error")
        return
    fota_log.info("power_reset...")
    utime.sleep(2)
    Power.powerRestart()   # 重启模块


if __name__ == '__main__':
    fota_log.info("run start...")
    run()
```



## 初始化相关功能

### `fota`

```python
fota(reset_disable=)
```

创建fota对象。

**参数描述：**

- `reset_disable`-可选参数，是否关闭下载完升级包后自动重启功能。传入1关闭自动重启功能，不传入该参数或传入0则保留自动重启功能。

**返回值描述：**

- fota对象。



> EC600N/EC800N/EG912N/EC600M/EC800M/EG810M型号不支持关闭下载完升级包后自动重启功能。



**示例**：

```python
import fota
fota_obj = fota() #下载完自动重启
# fota_obj = fota(reset_disable=1) #下载完不自动重启
```

## 远程升级相关功能

一个接口实现升级包下载和升级整个过程。

### `fota_obj.httpDownload`

```python
fota_obj.httpDownload(url1=, url2=, callback=)
```

升级包下载、写入、校验及重启升级。

**参数描述：**

- `url1`-可选参数，升级包的url，该url类型可以是HTTP或FTP，类型为str。注：仅EC200A型号支持FTP url。
- `url2`-可选参数，mini fota第二阶段升级包的url，类型为str。注：仅mini fota方式需要传入该参数，差分升级方式该参数禁止传入。mini fota方式为小存储平台特殊的固件升级方式，分为2个阶段。而差分升级方式只有一个阶段，仅EC600N/EC800N/EG912N/EC600M/EC800M/EG810M型号支持mini fota方式。
- `callback`-可选参数，回调函数，显示下载进度和状态，类型为function。注：mini fota方式不支持回调函数。回调函数参数含义如下。

| callback参数 | 参数类型 | 参数说明                                                     |
| ------------ | -------- | ------------------------------------------------------------ |
| args[0]      | int      | 表示下载状态，下载成功返回整型值：0或1或2，下载失败返回整型值：非0、1、2，表示错误码。 |
| args[1]      | int      | 表示下载进度(注：EC600N/EC800N/EG912N平台当下载状态是成功时表示百分比，下载状态是失败时表示错误码)。 |

**返回值描述：**

执行成功返回整形值0，执行失败返回整形值-1。注：EC600N/EC800N/EG912N/EC600M/EC800M/EG810M/BC25PA型号，返回值只代表接口执行成功或失败，升级状态和结果需通过回调反馈。其他型号返回0表示下载和校验成功，返回-1表示下载或校验失败。

**示例**：

```python
def result(args):
    print('download status:',args[0],'download process:',args[1])
    
#差分升级HTTP方式  
fota_obj.httpDownload(url1="http://www.example.com/fota.bin",callback=result)
#差分升级FTP方式  
fota_obj.httpDownload(url1="ftp://user:password@ip:port/fota.bin",callback=result) #其中user,password,ip,port需要填写具体使用的FTP服务器信息
#mini fota方式
fota_obj.httpDownload(url1="http://www.example.com/fota1.bin",url2="http://www.example.com/fota2.bin")
```

### `fota_obj.apn_set`

```python
fota_obj.apn_set(fota_apn=,ip_type=,fota_user=,fota_password=)
```

设置FOTA下载使用的APN信息。

**参数描述：**

- `fota_apn`-可选参数，APN，类型为str。
- `ip_type`-可选参数，IP类型：0-IPV4，1-IPV6，类型为int。
- `fota_user`-可选参数，用户名，类型为str。
- `fota_password`-可选参数，密码，类型为str。

**返回值描述：**

写入成功返回整型值0，写入失败返回整型值-1。

**示例**：

```python
fota_obj.apn_set(fota_apn="CMNET",ip_type=0,fota_user="abc",fota_password="123")
```



> 该接口目前支持型号：BG95。



### `fota_obj.download_cancel`

```python
fota_obj.download_cancel()
```

取消正在进行的FOTA下载。

**返回值描述：**

取消成功返回整型值0，取消失败返回整型值-1。

**示例**：

```python
import fota
import _thread
import utime

def th_func():
    utime.sleep(40) #时间根据升级包的大小来定,确保在下载完之前取消
    fota_obj.download_cancel()

def result(args):
    print('download status:',args[0],'download process:',args[1])

fota_obj = fota()
_thread.start_new_thread(th_func, ())
fota_obj.httpDownload(url1="http://www.example.com/fota.bin",callback=result)
```



> 该接口目前支持型号：BG95。



## 本地升级相关功能

已经获取到升级包内容，调用如下接口实现升级包内容写入flash、校验及重启升级。

### `fota_obj.write`

```python
fota_obj.write(bytesData, file_size)
```

写入升级包数据流。

**参数描述：**

- `bytesData`-升级包内容数据，类型为bytes。
- `file_size`-升级包文件总大小(单位：字节)，类型为int。

**返回值描述：**

写入成功返回整型值0，写入失败返回整型值-1。

### `fota_obj.flush`

```python
fota_obj.flush()
```

刷新RAM缓存数据到flash。由于升级包文件的大小和代码中的RAM缓存大小不一定是整数倍的关系，所以最后一次调用`fota_obj.write`之后需要调用`fota_obj.flush`将RAM缓存中的数据写入flash。

**返回值描述：**

刷新成功返回整型值0，刷新失败返回整型值-1。

### `fota_obj.verify`

```python
fota_obj.verify()
```

升级包校验。

**返回值描述：**

升级包校验成功返回整型值0，校验失败返回整型值-1。



> 本地升级相关功能，目前支持型号：EC600NCNLC/EC600NCNLF/EG912N/EC600U/EC200U/EG915U/EG912U/EC800G/EC600E/EC800E。
>

