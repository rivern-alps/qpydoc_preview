

# class Record - 录音

该类提供录音功能。

> 目前支持型号：EC600N系列、EC800N系列、EC600M-CN(LA、LE)、EC800M-CN(LA、LE、GA)、EG810MCN_GA、EC600U系列、EC200U系列、EG912U、EG915U、EG915N-EUAG。

## 构造函数

### `audio.Record`

```python
class audio.Record(device)
```

创建Record对象。

> 如果传参，请与audio.Audio(device)的参数保持一致。

**参数描述：**

- `device` - 输出通道，int类型，0表示听筒，1表示耳机，2表示喇叭，缺省值为`0`。具体模块所支持通道详见下表。

**模块输出通道对应表**

| 模块型号              | 听筒   | 耳机   | 喇叭   |
| --------------------- | ------ | ------ | ------ |
| EC600N系列            | 支持   | 不支持 | 不支持 |
| EC800N系列            | 支持   | 不支持 | 不支持 |
| EC600M-CN(LA、LE)     | 支持   | 不支持 | 不支持 |
| EC800M-CN(LA、LE、GA) | 支持   | 不支持 | 不支持 |
| EG810MCN_GA           | 支持   | 不支持 | 不支持 |
| EG915N                | 支持   | 不支持 | 不支持 |
| EG912N                | 支持   | 不支持 | 不支持 |
| EG912U                | 支持   | 不支持 | 不支持 |
| EC200U系列            | 不支持 | 不支持 | 支持   |
| EC600U系列            | 支持   | 支持   | 支持   |
| EG915U                | 支持   | 支持   | 不支持 |



## 方法

### `Record.start`

```python
audio.start(file_name,seconds)
```

该方法用于开始录音。

**参数描述：**

- `file_name` - 录音文件名，string类型。
- `seconds` - 需要录制时长，单位：秒，int类型。

**返回值描述：**

`0`表示成功。

`-1`表示文件覆盖失败。

`-2`表示文件打开失败。

`-3`表示文件正在使用。

`-4`表示通道设置错误。

`-5`表示定时器资源申请失败。

`-6` 表示音频格式检测错误。

### `Record.stop`

```python
Record.stop()
```

该方法用于停止录音。

**返回值描述：**

`0` 表示播放成功，`-1`表示播放失败。

### `Record.getFilePath`

```python
Record.getFilePath(file_name)
```

该方法用于读取录音文件的路径。

**参数描述：**

- `file_name` - 录音文件名，string类型。

**返回值描述：**

成功返回string类型的录音文件路径。

`-1`表示目标文件不存在。

`-2`表示文件名长度为0。

### `Record.getData`

```python
Record.getData(file_name, offset, size)
```

该方法用于读取录音数据。

**参数描述：**

- `file_name` - 录音文件名，string类型。
- `offset`  - 读取数据的偏移量，int类型。
- `size` - 读取大小，单位字节，int类型。注意 ：需小于10K。

**返回值描述：**

成功返回录音数据，bytearray类型。

失败返回值说明如下：

`-1`表示读取数据错误。

`-2`表示文件打开失败。

`-3`表示偏移量设置错误。

`-4`表示文件正在使用。

`-5`表示设置超出文件大小(offset+size > file_size)。

`-6`表示读取size 大于10K。

`-7`表示内存不足10K。

### `Record.getSize`

```python
Record.getSize(file_name)
```

该方法用于读取录音文件大小。

**参数描述：**

- `file_name` - 录音文件名，string类型。

**返回值描述：**

若获取成功，返回文件大小 （EC600N系列、EC800N系列、EC800M系列、EC600M系列、EG915N不返回文件头），单位字节。

> wav格式时，此值会比返回callback返回值大44 bytes(44 bytes为文件头)；amr格式时，此值会比返回callback返回值大6 bytes(6 bytes为文件头)。

失败返回值如下： 

`-1`表示获取文件大小失败。 

`-2`表示文件打开失败。 

`-3`表示文件正在使用 。

`-4`表示文件名长度为0。

### `Record.Delete`

```python
Record.Delete(file_name)
```

该方法用于删除录音文件。

**参数描述：**

- `file_name` - 录音文件名，string类型。

**返回值描述：**

`0`表示成功。

`-1`表示文件不存在。

`-2`表示文件正在使用。

### `Record.exists`

```python
Record.exists(file_name)
```

该方法用于判断录音文件是否存在。

**参数描述：**

- `file_name` - 录音文件名，string类型。

**返回值描述：**

`true`表示文件存在。

`false`表示文件不存在。

### `Record.isBusy`

```python
Record.isBusy()
```

该方法用于判断是否正在录音。

**返回值描述：**

`0`表示不在录音，`1`表示正在录音。

### `Record.end_callback`

```python
Record.end_callback(cb)
```

该方法用于设置录音结束回调。

**参数描述：**

`cb` - 录音结束回调函数，function类型，函数原型：

```python
def cb(audio_msg):
    pass
```

**回调函数参数描述**：

  - `audio_msg` - 录音信息，list类型，其中元素如下：

     ​    `audio_msg[0]`：`file_path` ，文件路径，string类型。

     ​    `audio_msg[1]`：`audio_len` ， 录音长度，int类型。

     ​    `audio_msg[2]`：`audio_state` ，录音状态，int类型，<a href="#label_record_map1">点此查看</a>回调函数参数audio_state说明表。

**返回值描述：**

`0` 表示成功，`-1`表示失败。

<span id="label_record_map1">**audio_state说明表：**</span>

| event | 说明     |
| ----- | -------- |
| -1    | 发生错误 |
| 0     | 录音开始 |
| 3     | 录音结束 |

### `Record.gain`

```python
Record.gain(code_gain,dsp_gain)
```

该方法用于设置录音增益。

> 目前仅EC600N/EC800N系列模组支持该功能。

**参数描述：**

- `code_gain` - 上行编解码器增益，int型，[0,4]。
- `dsp_gain` - 上行数字增益，int型，`-36~12` 。

**返回值描述：**

`0` 表示成功，`-1`表示失败。

### `Record.amrEncDtx_enable`

```python
Record.amrEncDtx_enable(on_off)
```

该方法用于配置amr录音DTX功能开关。

> 目前仅EC600N/EC800N系列模组支持该功能。

**参数描述：**

- `on_off` - 开关，int型，`1`：开启，`0`：关闭 。
- 不传参数 - 获取当前配置

**返回值描述：**

不传参：返回当前配置。

传参：参数正确无返回，参数错误抛异常。

### `Record.stream_start`

```python
Record.stream_start(format, samplerate, time)
```

该方法用于开始录音音频流。注意：录制音频流的同时，应及时读取音频流。目前是采用循环buf，不及时读取，会导致数据丢失。

> 目前仅EC200U/EC600U系列模组支持该功能。

**参数描述：**

- `format` - 音频格式，int型，目前支持 amr 格式，<a href="#label_record_const">见常量</a>。
- `samplerate` - 采样率，int型，目前支持8000 和 16000 。
- `time` - 录音时长，int型，单位 S (秒)。

**返回值描述：**

`0` 表示成功，`-1`表示失败。

### `Record.stream_read`

```python
Record.stream_read(read_buf, len)
```

该方法用于读取录音流。

> 目前仅EC600N/EC800N系列模组支持该功能。

**参数描述**

- `read_buf` - 录音流buf，bytearray型 。
- `len` - 读取的长度，int类型。

**返回值描述：**

成功返回实际读取的字节数，失败返回整型-1。

## 常量

### <span id="label_record_const">`Record.AMRNB`</span>

amr 格式。

**示例：**

```python
# -*- coding: UTF-8 -*-
import utime
import audio
from machine import Pin


flag = 1
'''
外接喇叭播放录音文件，参数选择0
'''
aud = audio.Audio(0)
tts = audio.TTS(0)

aud.setVolume(11)

def record_callback(args):
    global flag
    print('file_name:{}'.format(args[0]))
    print('file_size:{}'.format(args[1]))
    print('record_sta:{}'.format(args[2]))

    record_sta = args[2]
    if record_sta == 3:
        print('The recording is over, play it')
        tts.play(1, 0, 2, '录音结束,准备播放录音文件')
        aud.play(1, 0, record.getFilePath('recordfile.wav'))
        flag = 0
    elif record_sta == -1:
        print('The recording failure.')
        tts.play(1, 0, 2, '录音失败')
        flag = 0

record = audio.Record()
record.end_callback(record_callback)
record.start('recordfile.wav', 10)

while 1:
    if flag:
        utime.sleep_ms(200)
    else:
        break
```
