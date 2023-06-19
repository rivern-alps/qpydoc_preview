# class Audio - 音频播放

该类提供音频播放功能。

> 目前支持型号：EC600N系列、EC800N系列、EC600M-CN(LA、LE)、EC800M-CN(LA、LE、GA)、EG810MCN_GA、EC600U系列、EC200U系列、EG912U、EG915U、EG915N-EUAG。

## 构造函数

### `audio.Audio`

```python
class audio.Audio(device)
```

创建Audio对象。

**参数描述：**

- `device` - 输出通道，int类型，0表示听筒，1表示耳机，2表示喇叭。具体模块所支持通道详见下表。

**模块输出通道对应表：**

| 模块型号             | 听筒   | 耳机   | 喇叭   |
| -------------------- | ------ | ------ | ------ |
| EC600N系列           | 支持   | 不支持 | 不支持 |
| EC800N系列           | 支持   | 不支持 | 不支持 |
| EC600MCN(LA、LE)     | 支持   | 不支持 | 不支持 |
| EC800MCN(LA、LE、GA) | 支持   | 不支持 | 不支持 |
| EG810MCN_GA          | 支持   | 不支持 | 不支持 |
| EG915N               | 支持   | 不支持 | 不支持 |
| EG912N               | 支持   | 不支持 | 不支持 |
| EG912U               | 支持   | 不支持 | 不支持 |
| EC200U系列           | 不支持 | 不支持 | 支持   |
| EC600U系列           | 支持   | 支持   | 支持   |
| EG915U               | 支持   | 支持   | 不支持 |

## 方法

### `Audio.set_pa`

```python
Audio.set_pa(gpio,num)
```

该方法用于设置输出pa的gpio。

**参数描述：**

- `gpio` - 输出的gpio，int类型，参照[Pin](./machine.Pin.md)。
- `num` - 上电脉冲数，int类型。

**返回值描述：**

`1` 表示成功，`0`表示失败。

### `Audio.play`

```python
Audio.play(priority, breakin, filename)
```

该方法用于音频文件播放。

支持mp3、amr和wav格式文件播放。支持优先级0 ~ 4，数字越大优先级越高，每个优先级组可同时最多加入10个播放任务，与TTS播放共用同一个播放队列。

> **说明：**由于TTS和音频文件播放共用同一个播放队列，所以TTS中设置的播放优先级、打断模式不仅仅是和其他TTS播放任务比较，还会和音频文件播放任务的优先级和打断模式比较，反之，音频文件播放中设置的播放优先级与打断模式对TTS任务同样是有效的。

**参数描述：**

- `priority` - 播放优先级，int类型。支持优先级0 ~ 4，数值越大优先级越高。
- `breakin` - 打断模式，int类型。0表示不允许被打断，1表示允许被打断。
- `filename` - 模式，string类型。待播放的文件名称，包含文件存放路径。<a href="#label_Audio_desc1">点此查看</a>文件播放路径的说明。

**返回值描述：**

`0` 表示播放成功；

`-1`表示播放失败；

`1` 表示无法立即播放，加入播放队列；

`-2`表示无法立即播放，且该请求的优先级组队列任务已达上限，无法加入播放队列。

<span id="label_Audio_desc1">**文件播放路径的说明：**</span>

用户分区路径固定为’U:/‘开头，表示用户分区的根目录，如果用户在根目录下新建audio目录，并将音频文件存放在根目录下的audio目录，那么播放接口中，传入的路径参数应该是：'U:/audio/music.mp3'。

### `Audio.stop`

```python
Audio.stop()
```

该方法用于停止当前正在播放的音频。

**返回值描述：**

`0` 表示成功，`-1`表示失败。

### `Audio.stopAll`

```python
Audio.stopAll()
```

该方法用于停止整个队列的播放。即当前如果正在播放Audio或者音频，并且队列中还有其他待播放内容，调用该方法后，不仅会停止当前播放的内容，还会清除这个队列的内容，不再播放任何内容。如果当前正在播放，且播放队列为空，那么调用该方法效果等同与stop()接口。

**返回值描述：**

`0` 表示成功，`-1`表示失败。

### `Audio.setCallback`

```python
Audio.setCallback(cb)
```

该方法用于注册用户的回调函数，用于通知用户音频文件播放状态。

> 该回调函数中不要进行耗时以及阻塞性的操作，建议只进行简单、耗时短的操作。

**参数描述：**

`cb` - 用户回调函数，function类型，函数原型：

```python
def cb(event):
    pass
```

**回调函数参数描述**：

  - `event` - 播放状态，int类型，<a href="#label_Audio_map2">点此查看</a>回调函数参数event说明表。

**返回值描述：**

`0` 表示成功，`-1`表示失败。

<span id="label_Audio_map2">**回调函数参数event说明表**</span>

| event | 表示状态 |
| ----- | -------- |
| 0     | 开始播放 |
| 7     | 播放完成 |

### `Audio.getState`

```python
Audio.getState()
```

该方法用于获取audio初始化状态。

**返回值描述：**

`0` 表示audio初始化完成，`-1`表示audio初始化未完成。

### `Audio.getVolume`

```python
Audio.getVolume()
```

该方法用于获取当前播放音量大小，音量值在区间[0 ~ 11]，0表示静音，默认值7。

**返回值描述：**

整型音量大小值。

### `Audio.setVolume`

```python
Audio.setVolume(vol)
```

该方法用于设置播放音量大小，音量值在区间[0 ~ 11]，0表示静音。

**参数描述：**

- `vol` - 音量大小，int类型，区间[0 ~ 11]。

**返回值描述：**

`0` 表示成功，`-1`表示失败。

### `Audio.playStream`

```python
Audio.playStream(format, buf)
```

该方法用于音频流播放，支持mp3、amr和wav格式的音频流播放。

**参数描述：**

- `format` - 音频流格式，int类型，`2` - `WAVPCM`，`3` - `MP3`，`4` - `AMRNB`。
- `buf` - 音频流内容，音频流二进制文件内容。

**返回值描述：**

`0`表示播放成功，`-1`表示播放失败。

### `Audio.stopPlayStream`

```python
Audio.stopPlayStream()
```

该方法用于停止音频流播放。

**参数描述：**

无

**返回值描述：**

`0` 表示成功，`-1`表示失败。

### `Audio.aud_tone_play`

```python
Audio.aud_tone_play(tone, time)
```

该方法用于播放tone音，播放一段时间(time)后自动停止播放。

> EC600N/EC800N系列模组调用该接口为立即返回，EC600U/EC200U系列模组调用该接口为阻塞等待。

**参数描述：**

- `tone` - tone类型，int型，`0~15`：按键音(0~9、A、B、C、D、#、*)，`16`：拨号音。
- `time` - 播放时长，单位ms，int型，`0` ： 不停止一直播放。

**返回值描述：**

`0` 表示播放成功，`-1`表示播放失败。

### `Audio.aud_tone_play_stop`

```python
Audio.aud_tone_play_stop()
```

该方法用于主动停止播放tone音。

**返回值描述：**

`0` 表示停止播放成功，`-1`表示停止播放失败。

**示例：**

```python
# -*- coding: UTF-8 -*-
import audio
from machine import Pin
import utime
import uos

def audio_cb(event):
    if event == 0:
        print('audio-play start.')
    elif event == 7:
        print('audio-play finish.')

aud = audio.Audio(0)
aud.setCallback(audio_cb)
# 设置pa
aud.set_pa(Pin.GPIO15,2)
# 播放MP3
aud.play(2, 1, 'U:/music.mp3')
utime.sleep(5)
aud.stop()

# 音频流播放
size = 10*1024 # 保证一次填充的音频数据足够大以便底层连续播放
format = 4

def play_from_fs():
    file_size = uos.stat("/usr/test.amr")[6]  # 获取文件总字节数
    print(file_size)
    with open("/usr/test.amr", "rb")as f:   
        while 1:
            b = f.read(size)   # read
            if not b:
                break
            aud.playStream(format, b)
            utime.sleep_ms(20)


play_from_fs()
# 等待播放完成
utime.sleep_ms(5000) 
# 停止本次播放以便不影响下次播放
aud.stopPlayStream() 
```
