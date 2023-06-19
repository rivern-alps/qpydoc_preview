# class wifilocator - WIFI定位

该模块提供WIFI定位功能的类，获取模组经纬度坐标信息。



> 当前仅EC600S/EC600N/EC800N/EC200U/EC600U系列支持该功能。



**示例：**

```python
>>> import wifilocator
# 创建wifilocato对象
>>> wifiloc = wifilocator.wifilocator("xxxxxxxxxxxxxxxx")
# 获取模块坐标信息
>>> wifiloc.getwifilocator()
(117.1152877807617, 31.82142066955567, 100)
# 上面使用的密钥"xxxxxxxxxxxxxxxx"指代token，具体需要向移远申请
```



## 构造函数

### `wifilocator.wifilocator`

```python
class wifilocator.wifilocator(token)
```

创建wifilocator对象，配置wifi定位套件token信息。

**参数描述：**

- `token` - 密钥，字符串类型，16位字符组成，需要申请。



## 获取坐标信息

### `wifilocator.getwifilocator`

```python
wifilocator.getwifilocator()
```

该方法用于获取模组经纬度坐标信息。

**返回值描述：**

成功返回模组经纬度坐标信息，元组格式：`(longtitude, latitude, accuracy)`；

`longtitude` ： 经度

`latitude` ：纬度

`accuracy` ：精确度，单位米

失败返回错误码说明如下：

`1` – 当前网络异常，请确认拨号是否正常

`2` – 密钥长度错误，必须为16字节

`3` – 获取坐标出错。



