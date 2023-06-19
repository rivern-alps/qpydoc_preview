

# class TTS - 文本到语音播放 

该类提供从文本到语音播放功能。

> 目前支持型号：EC600N系列、EC800N系列、EC600M-CN(LA、LE)、EC800M-CN(LA、LE、GA)、EG810MCN_GA、EC600U-CN系列、EC200U-CN系列。

## 构造函数

### `audio.TTS`

```python
class audio.TTS(device)
```

创建TTS对象。

**参数描述：**

- `device` - 输出通道，int类型，0表示听筒，1表示耳机，2表示喇叭。具体模块所支持通道详见下表。

**模块输出通道对应表：**

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
| EC600U-CN系列         | 支持   | 支持   | 支持   |
| EG915U                | 支持   | 支持   | 不支持 |

## 方法

### `TTS.close`

```python
TTS.close()
```

该方法用于关闭TTS功能。

**返回值描述：**

`0` 表示关闭成功，`-1`表示关闭失败。

### `TTS.play`

```python
TTS.play(priority, breakin, mode, str)
```

该方法用于开始语音播放。<a href="#label_tts_playdemo">点此查看</a>TTS.play方法使用实例。

支持优先级0 ~ 4，数字越大优先级越高，每个优先级组可同时最多加入10个播放任务；播放策略说明如下：

1. 如果当前正在播放任务A，并且允许被打断，此时有高优先级播放任务B，那么会打断当前低优先级播放任务A，直接播放高优先级任务B。

2. 如果当前正在播放任务A，并且不允许被打断，此时有高优先级播放任务B，那么B播放任务将会加入到播放队列中合适的位置，等待A播放完成，再依次从队列中按照优先级从高到低播放其他任务。

3. 如果当前正在播放任务A，且不允许被打断，此时来了一个同优先级播放任务B，那么B会被加入到该优先级组播放队列队尾，等待A播放完成，再依次从队列中按照优先级从高到低播放其他任务。

4. 如果当前正在播放任务A，且允许被打断，此时来了一个同优先级播放任务B，那么会打断当前播放任务A，直接播放任务B。

5. 如果当前正在播放任务A，且任务A的优先级组播放队列中已经有几个播放任务存在，且该优先级组播放队列最后一个任务N是允许被打断的，此时如果来了一个同样优先级的播放任务B，那么任务B会直接覆盖掉任务N；也就是说，某个优先级组，只有最后一个元素是允许被打断的，即breakin为1，其他任务都是不允许被打断的。

6. 如果当前正在播放任务A，不管任务A是否允许被打断，此时来了一个优先级低于任务A的请求B，那么将B加入到B对应优先级组播放队列。

**参数描述：**

- `priority` - 播放优先级，int类型。支持优先级0 ~ 4，数值越大优先级越高。
- `breakin` - 打断模式，int类型。0表示不允许被打断，1表示允许被打断。
- `mode` - 模式，int类型。由低四位和高四位构成，其中低四位是编码模式，高四位是WTTS模式。<a href="#label_tts_map1">点此查看</a>TTS模式说明表。
- `str` - 待播放字符串，string类型。

**返回值描述：**

`0` 表示播放成功；

`-1`表示播放失败；

`1` 表示无法立即播放，加入播放队列；

`-2`表示无法立即播放，且该请求的优先级组队列任务已达上限，无法加入播放队列。

<span id="label_tts_map1">**TTS模式说明表：**</span>

| 模式     | 说明                                                         |
| -------- | ------------------------------------------------------------ |
| 编码模式 | 1 - UNICODE16(UTF-16大端模式)<br />2 - UTF-8<br />3 - UNICODE16(UTF-16小端模式) |
| WTTS模式 | 仅600N系列支持VOLTE的版本支持，<br />wtts_enable - wtts总开关<br />wtts_ul_enable - wtts上行使能 <br />wtts_dl_enable - wtts下行使能 |

<span id="label_tts_playdemo">**TTS.play方法使用实例：**</span>

- **TTS播放策略实例：**

```python
>>> import audio
>>> tts = audio.TTS(1)
# case1：正在播放任务A，且A允许被打断，此时任务B到来，且优先级高于任务A，那么A会被打断，直接播放B
>>> tts.play(1, 1, 2, '111')  #任务A
0
>>> tts.play(2, 0, 2, '222')  #任务B
0

# case2：正在播放任务A，且A不允许被打断，此时任务B到来，且优先级高于任务A，那么B会被加入播放队列，等待A播放完成播放B（假设播放队列之前为空）
>>> tts.play(1, 0, 2, '111')  #任务A
0
>>> tts.play(2, 0, 2, '222')  #任务B
1

# case3：正在播放任务A，且A允许被打断，此时任务B到来，且优先级和A优先级一样，那么A会被打断，直接播放B
>>> tts.play(2, 1, 2, '222')  #任务A
0
>>> tts.play(2, 0, 2, '333')  #任务B
0

# case4：正在播放任务A，且A不允许被打断，此时任务B到来，且优先级和A优先级一样，那么B会被加入播放队列，等待A播放完成播放B（假设播放队列之前为空）
>>> tts.play(2, 0, 2, '222')  #任务A
0
>>> tts.play(2, 0, 2, '333')  #任务B
1

# case5：正在播放A，且A不允许被打断，此时任务B到来，且任务B允许被打断，优先级与A相同，那么任务B会被加入到播放队列中，此时任务C到来，且优先级和A、B相同，此时C会被加入播放队列中，且直接覆盖率任务B，A播放完成下一个播放的是C（假设播放队列之前为空）
>>> tts.play(2, 0, 2, '222')  #任务A
0
>>> tts.play(2, 1, 2, '333')  #任务B
1
>>> tts.play(2, 0, 2, '444')  #任务C
1

# 播放UTF16BE模式的语音
>>> tts.play(1,1,1,'6B228FCE4F7F752879FB8FDC901A4FE16A2157573002')
0

# 播放UTF16LE模式的语音
>>> tts.play(1,1,3,'226BCE8F7F4F2875FB79DC8F1A90E14F216A57570230')
0

# 支持VOLTE的版本,可以播放tts到远端
>>> import voiceCall
>>> voiceCall.callStart('1xxxxxxxxxx')
0

# 待电话接通后
# 播放tts语音至通话远端
>>> tts.play(1,1,tts.wtts_enable|tts.wtts_ul_enable|2, '12345')
0
```

- **TTS播放中文示例：**

  > python文件开头需要加上`# -*- coding: UTF-8 -*-`。

```python
# -*- coding: UTF-8 -*-
import audio

tts = audio.TTS(1)
str1 = '移联万物，志高行远' 
tts.play(4, 0, 2, str1)
```

- **TTS播放文本标注实例：**

  如遇TTS播放时不能达到预期的，可以通过文本标注的方式让TTS播放符合预期。

  数字播放的方式：

```python
# 格式：[n*] (*=0/1/2)
# TTS引擎自动决定是以号码形式播放还是以数值的形式播放
>>> tts.play(1,1,2, '12345')
0

# TTS引擎以号码形式播放
>>> tts.play(1,1,2, '[n1]12345')
0

# TTS引擎以数值形式播放
>>> tts.play(1,1,2, '[n2]12345')
0
```

- **TTS语速设置实例：**

```python
# 格式：[s*] (*=0 ~ 10)
# TTS引擎以默认语速5播放语音
>>> tts.play(1,1,2, '12345')
0

# TTS引擎以默认语速的一半播放语音
>>> tts.play(1,1,2, '[s0]12345')
0

# TTS引擎以默认语速的2倍语速播放语音
>>> tts.play(1,1,2, '[s10]12345')
0
```

- **TTS语调设置实例：**

```python
# 格式：[t*] (*=0 ~ 10)
# TTS引擎以默认语调5播放语音
>>> tts.play(1,1,2, '12345')
0

# TTS引擎以默认语调基频减64Hz播放语音
>>> tts.play(1,1,2, '[t0]12345')
0

# TTS引擎以默认语调基频加128Hz播放语音
>>> tts.play(1,1,2, '[t10]12345')
0
```

- **汉字指定拼音实例：**

```python
# 格式：[=*] (*=拼音)
# 汉字：声调用后接一位数字 1 ~ 5 分别表示 阴平、阳平、上声、去声和轻声 5个声调。
>>> tts.play(1,1,2, '乐[=le4]')
0

>>> tts.play(1,1,2, '乐[=yue4]')
0
```



### `TTS.stop`

```python
TTS.stop()
```

该方法用于停止TTS播放。

**返回值描述：**

`0` 表示成功，`-1`表示失败。

### `TTS.stopAll`

```python
TTS.stopAll()
```

该方法用于停止整个队列的播放。即当前如果正在播放TTS或者音频，并且队列中还有其他待播放内容，调用该方法后，不仅会停止当前播放的内容，还会清除这个队列的内容，不再播放任何内容。如果当前正在播放，且播放队列为空，那么调用该方法效果等同与stop()接口。

**返回值描述：**

`0` 表示成功，`-1`表示失败。

### `TTS.setCallback`

```python
TTS.setCallback(cb)
```

该方法用于注册用户的回调函数，用于通知用户TTS播放状态。

> 该回调函数中不要进行耗时以及阻塞性的操作，建议只进行简单、耗时短的操作。

**参数描述：**

`cb` - 用户回调函数，function类型，函数原型：

```python
def cb(event):
    pass
```

**回调函数参数描述**：

  - `event` - 播放状态，int类型，<a href="#label_tts_map2">点此查看</a>回调函数参数event说明表。

**返回值描述：**

`0` 表示成功，`-1`表示失败。

<span id="label_tts_map2">**回调函数参数event说明表：**</span>

| event | 表示状态 |
| ----- | -------- |
| 2     | 开始播放 |
| 3     | 停止播放 |
| 4     | 播放完成 |

### `TTS.getVolume`

```python
TTS.getVolume()
```

该方法用于获取当前播放音量大小，音量值在区间[0 ~ 9]，0表示静音，默认值4。

**返回值描述：**

成功则返回整型音量大小值，`-1`表示失败。

### `TTS.setVolume`

```python
TTS.setVolume(vol)
```

该方法用于设置播放音量大小，音量值应在区间[0 ~ 9]，0表示静音。

**参数描述：**

- `vol` - 音量大小，int类型，区间[0 ~ 9]。

**返回值描述：**

`0` 表示成功，`-1`表示失败。

### `TTS.getSpeed`

```python
TTS.getSpeed()
```

该方法用于获取当前播放速度，速度值在区间[0 ~ 9]，值越大，速度越快，默认值4。

**返回值描述：**

成功则返回整型音量大小值，`-1`表示失败。

### `TTS.setSpeed`

```python
TTS.setSpeed(speed)
```

该方法用于设置TTS播放速度，速度值应在区间[0 ~ 9]。

**参数描述：**

- `speed` - 速度值，int类型，区间[0 ~ 9]。

**返回值描述：**

`0` 表示成功，`-1`表示失败。

### `TTS.getState`

```python
TTS.getState()
```

该方法用于获取TTS状态。

**返回值描述：**

`0` 表示当前无tts播放，`-1`表示当前有tts正在播放。

**示例：**

```python
# -*- coding: UTF-8 -*-
import log
from audio import TTS
import utime


# 设置日志输出级别
log.basicConfig(level=log.INFO)
tts_Log = log.getLogger("TTS")

#定义回调函数
def UsrFunc(event):
    if event == 2:
        print("开始播放")
    elif event == 3:
        print("停止播放")
    elif event == 4:
        print("播放完成")

if __name__ == '__main__':
    # 参数1：device （0：听筒，1：耳机，2：喇叭）
    tts = TTS(0)

    #注册用户回调函数
    tts.setCallback(UsrFunc)

    # 获取当前播放音量大小
    volume_num = tts.getVolume()
    tts_Log.info("Current TTS volume is %d" %volume_num)
    
    # 设置音量为6
    volume_num = 6
    tts.setVolume(volume_num)

    #  参数1：优先级 (0-4)
    #  参数2：打断模式，0表示不允许被打断，1表示允许被打断
    #  参数3：模式 低四位：（1：UNICODE16(Size end conversion)  2：UTF-8  3：UNICODE16(Don't convert)），高四位：wtts_enable，wtts_ul_enable， wtts_dl_enable
    #  参数4：数据字符串 （待播放字符串）
    tts.play(1, 1, 2, 'QuecPython') # 执行播放
    tts.play(1,1,tts.wtts_enable|tts.wtts_ul_enable|2, '12345')
    tts.close()   # 关闭TTS功能
```
