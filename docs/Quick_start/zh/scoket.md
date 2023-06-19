## 建立你的第一条TCP连接

对于需要连接网络的业务，建议使用 QuecPython 内置的 checkNet 功能，等待网络连接成功后再执行后续步骤；详见[官方 wiki](https://python.quectel.com/wiki/#/zh-cn/api/QuecPythonClasslib?id=checknet-%e7%ad%89%e5%be%85%e7%bd%91%e7%bb%9c%e5%b0%b1%e7%bb%aa)

```python
# -*- coding: UTF-8 -*-
import utime
utime.sleep(10)	# 增加延时，以等待系统就绪

import checkNet
from machine import Pin
from usr import test

# 作为全局变量设置如下项
PROJECT_NAME = "My_Test"	# 用户项目名称
PROJECT_VERSION = "0.2.1"	# 用户项目版本
checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

# ......

if __name__ == '__main__':
    # 在程序入口进行网络就绪状态检测
    stagecode, subcode = checknet.wait_network_connected(30)	
    # 用户可通过两个状态码判断当前的网络状态
    print('stagecode = {}, subcode = {}'.format(stagecode, subcode))

# ......
```

### request

通过request函数访问HTTP网页，详细接口函数见[wiki](https://python.quectel.com/wiki/#/zh-cn/api/QuecPythonThirdlib?id=request-http)

```python
# 在上方代码后添加
if stagecode == 3 and subcode == 1:   # 网络状态就绪
    http_log.info('Network connection successful!')
    response = request.get("http://httpbin.org/get")   # 发起http GET请求
    http_log.info(response.json())  # 以json方式读取返回
```

### socket

[socket使用示例文档](https://python.quectel.com/doc/doc/Quick_start/zh/socket.html)