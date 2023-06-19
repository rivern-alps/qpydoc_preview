# SecureData - 安全数据区

模组提供一块裸flash区域及专门的读写接口供客户存贮重要信息，且信息在烧录固件后不丢失(烧录不包含此功能的固件无法保证不丢失)。提供一个存储和读取接口，不提供删除接口。


> 目前除BC25/BG95/EC200A系列外，其余系列均支持本功能

**示例**

```python
import SecureData
# 即将存储的数据buf
databuf = '\x31\x32\x33\x34\x35\x36\x37\x38'
# 在index为1的存储区域中存储长度为8的数据databuf
SecureData.Store(1, databuf, 8)
# 定义一个长度为20的数组用于读取存储的数据
buf = bytearray(20)
# 读取index为1的存储区域中的数据至buf中,将读取到数据的长度存储在变量length中
length = SecureData.Read(1, buf, 20)
# 输出读到的数据
print(buf[:length])
```


## 数据存储

### `SecureData.Store`

```python
SecureData.Store(index,databuf,len)
```

**参数描述**

* `index`，int类型
  
| index序号 | 最大存储量 |
| --------- | ---------- |
| 1 - 8     | 52字节     |
| 9 - 12    | 100字节    |
| 13 - 14   | 500字节    |
| 15 - 16   | 1000字节   |
* `databuf`，待存储的数据数组，bytearray类型
* `len`，要写入数据的长度，int类型

> 存储时按照databuf和len两者中长度较小的进行存储

**返回值描述**

`-1`: 参数有误
`0`: 执行正常

## 数据读取

### `SecureData.Read`

```python
SecureData.Read(index,databuf,len)
```

**参数描述**                              

* `index`，index范围为1-16：待读取数据对应的索引号，int类型
* `databuf`，存储读取到的数据，bytearray类型
* `len`，要读取数据的长度，int类型

> 若存储的数据没有传入的len大，则返回实际存储的数据长度

**返回值描述**

`-2`存储数据不存在且备份数据也不存在
`-1`参数有误
`其他`实际读取到的数据长度
