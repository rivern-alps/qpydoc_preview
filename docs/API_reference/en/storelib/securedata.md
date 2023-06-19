# securedata - Secure-Data Area

The module provides a bare flash area and a dedicated read/write interface for you to store important information, which won't be lost after the firmware burning. (If you burn the firmware that does not provide the secure data area, it cannot be ensured that information won't be lost.) Besides, the module also provides a storage and read interface but deletion interface is not provided.


> All Quectel modules support SecureData area, excluding BC25, BG95 and EC200A series modules.

**Example**

```python
import SecureData
# A cache used to store data
databuf = '\x31\x32\x33\x34\x35\x36\x37\x38'
# In a storage area with index as 1, store data with a length of 8 bytes  
SecureData.Store(1, databuf, 8)
# Define an array with a length of 20 bytes to read stored data 
buf = bytearray(20)
# Read the data from the storage area with index as 1 to buf and the length of the read data is stored in the variable length
length = SecureData.Read(1, buf, 20)
# Output the read data
print(buf[:length])
```


## Data Storage

### `SecureData.Store`

```python
SecureData.Store(index,databuf,len)
```

**Parameter** 

* `index` - Integer type.
| Index Serial Number | Maximum Storage |
| ------------------- | --------------- |
| 1 - 8               | 52 bytes        |
| 9 - 12              | 100 bytes       |
| 13 - 14             | 500 bytes       |
| 15 - 16             | 1000 bytes      |
* `databuf` - Bytearray type. A data array to be stored. 
* `len` - Integer type. The length of data to be written. 

> Store the one with the shorter data length between databuf and len.

**Return Value**

`-1`: Parameter error.
`0`: Normal execution.

## Data Reading

### `SecureData.Read`

```python
SecureData.Read(index,databuf,len)
```

**Parameter**                              

* `index` - Integer type. Index range: 1-16; Index number of the data to be read. 
* `databuf` - Bytearray type. Store the read data. 
* `len` - Integer type. Length of data to be read. 

> If the stored data is not larger than the input parameter len, the actual stored data length is returned.

**Return Value**

`-2`: Both storage and backup data do not exist.
`-1`: Parameter error.
`Other values`: Length of data actually read.