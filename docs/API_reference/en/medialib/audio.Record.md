

# Record - Audio Record

Class feature: Recording.

> Currently supported models: EC600N Series, EC800N Series, EC600M-CN(LA/LE), EC800M-CN(LA/LE/GA), EC600U Series, EC200U Series, EG912U, EG915U and EG915N-EUAG.

**Example:**

```python
# -*- coding: UTF-8 -*-
import utime
import audio
from machine import Pin


flag = 1
'''
External speaker plays recording file, select 0
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
        tts.play(1, 0, 2, 'The recording is over, play it')
        aud.play(1, 0, audio.getFilePath(path))
        flag = 0
    elif record_sta == -1:
        print('The recording failure.')
        tts.play(1, 0, 2, 'The recording failure.')
        flag = 0

record = audio.Record()
record.end_callback(record_callback)
record.start('recordfile.wav', 10)

while 1:
    if flag:
        pass
    else:
        break
```

## Constructor

### `audio.Record`

```python
class audio.Record(device)
```

Creates a record object.

> If a parameter is passed, it should be consistent with the parameter of `audio.Audio(device)`.

**Parameter:**

- `device` - Integer type. The output channel. `0` indicates earpiece, `1` indicates headphone and `2` indicates speaker. Default value: `0`. See the table below for the specific channels supported by each module.

**Channels Supported by the Module:**

| Module Series       | Earpiece    | Headphone   | Speaker     |
| ------------------- | ----------- | ----------- | ----------- |
| EC600N Series       | Supported   | Unsupported | Unsupported |
| EC800N Series       | Supported   | Unsupported | Unsupported |
| EC600M-CN(LA/LE)    | Supported   | Unsupported | Unsupported |
| EC800M-CN(LA/LE/GA) | Supported   | Unsupported | Unsupported |
| EG915N              | Supported   | Unsupported | Unsupported |
| EG912N              | Supported   | Unsupported | Unsupported |
| EG912U              | Supported   | Unsupported | Unsupported |
| EC200U Series       | Unsupported | Unsupported | Supported   |
| EC600U Series       | Supported   | Supported   | Supported   |
| EG915U              | Supported   | Supported   | Unsupported |



## Method

### Record.start

```python
audio.start(file_name,seconds)
```

This method starts recording.

**Parameter:**

- `file_name` - String type. Name of the recording file.
- `seconds` - Integer type. Recording duration. Unit: second. 

**Return Value:**

`0` - Successful execution

`-1` - Failed to overwrite the file

`-2` - Failed to open the file

`-3` - The file is in use.

`-4` - Channel setting error

`-5` - Timer resource request failure

`-6` - Audio format error

### Record.stop

```python
Record.stop()
```

This method stops recording.

**Return Value:**

`0` - Successful execution; `-1` - Failed execution.

### Record.getFilePath

```python
Record.getFilePath(file_name)
```

This method reads the path of the recording file.

**Parameter:**

- `file_name` - String type. Name of the recording file.

**Return Value:**

Returns the recording file path for successful execution.

`-1` - The target file does not exist. 

`-2`- The file name length is 0.

### Record.getData

```python
Record.getData(file_name, offset, size)
```

This method reads the recording data.

**Parameter:**

- `file_name` - String type. The name of the recording file.
- `offset`  - Integer type. The offset of the data to be read.
- `size` - Integer type. Data size. Unit: byte. The size should be less than 10 KB.

**Return Value:**

Returns the recording data (bytearray type) for successful execution.

The following are return values for failed execution: 

`-1` - Failed to read the data.

`-2` - Failed to open the file.

`-3` - Failed to set the offset.

`-4` - The file is in use.

`-5` - The setting is beyond the file size (offset+size > file_size).

`-6` - The data size to be read is greater than 10 KB.

`-7` - The memory is less than 10 K.

### Record.getSize

```python
Record.getSize(file_name)
```

This method reads the size of the recording file.

**Parameter:**

- `file_name` - String type. The name of the recording file.

**Return Value:**

Returns the file size for successful execution. Unit: byte. (EC600N series, EC800N series, EC800M series, EC600M series, and EG915N modules do not return file headers).

> For WAV format, this value is 44 bytes larger than the callback return value (44 bytes is the file header); for AMR format, this value is 6 bytes larger than the callback return value (6 bytes is the file header).

The return values for failed execution are as follows:

`-1` - Failed to get the file size.

`-2` - Failed to open the file.

`-3` - The file is in use.

`-4` - The file name length is 0.

### Record.Delete

```python
Record.Delete(file_name)
```

This method deletes the recording file.

**Parameter:**

- `file_name` - String type. The name of the recording file.

**Return Value:**

`0` - Successful execution

`-1` - The file does not exist.

`-2` - The file is in use.

### Record.exists

```python
Record.exists(file_name)
```

This method determines whether the recording file exists.

**Parameter:**

- `file_name` - String type. The name of  the recording file.

**Return Value:**

`true` - The file exists.

`false` - The file does not exist.

### Record.isBusy

```python
Record.isBusy()
```

This method determines whether recording is in progress.

**Return Value:**

`0` - Not in progress; `1` - In progress.

### Record.end_callback

```python
Record.end_callback(cb)
```

This method sets the callback function for the end of the recording.

**Parameter:**

- `cb` - Function type. Callback function for the end of the recording. The prototype is as follows:

  ```
  cb(audio_msg)
  ```

  **Parameter of the Callback Function**：

  -  `audio_msg` - List type. The recording information. The elements are as follows:
     
     ​    `audio_msg[0]`：`file_path` . String type. The file path.
     
     ​    `audio_msg[1]`：`audio_len` .  Integer type. The recording length. 
     
     ​    `audio_msg[2]`：`audio_state` . Integer type. The recording status. <a href="#label_record_map1">Click here</a> for the description of `audio_state` of the callback function.

**Return Value:**

`0` - Successful execution; `-1` -Failed execution.

<span id="label_record_map1">**Description of `audio_state`：**</span>

| event | Description    |
| ----- | -------------- |
| -1    | Failure        |
| 0     | Start playback |
| 3     | Playback ends  |

### Record.gain

```python
Record.gain(code_gain,dsp_gain)
```

This method sets the recording gain.

> Currently, only the EC600N/EC800N series modules support this function.

**Parameter:**

- `code_gain` - Integer type. Uplink codec gain. Range: [0,4]. 
- `dsp_gain` - Integer type. Uplink digital gain. Range: [-36,12].

**Return Value:**

`0` - Successful execution; `-1`- Failed execution.

### Record.amrEncDtx_enable

```python
Record.amrEncDtx_enable(on_off)
```

This method controls the DTX feature of the AMR recording.

> Currently, only the EC600N/EC800N series modules support this feature.

**Parameter:**

- `on_off` - Integer type. Enable or disable the DTX feature.  `1`- Enable; `0`- Disable.
- No parameter passed - get the current configuration

**Return Value:**

No parameter passed: return the current configuration.

The parameter is passed: no return value if the parameter is correct, and an exception is thrown if the parameter is incorrect. 

### Record.stream_start

```python
Record.stream_start(format, samplerate, time)
```

This method starts recording audio streams. Note that when recording an audio stream, read the audio stream timely. Currently, a loop buffer is used. Failure to read the audio stream in time will result in data loss.

> Currently, only the EC200U/EC600U series modules support this function.

**Parameter:**

- `format` - Integer type. Audio format. Currently supports AMR format. <a href="#label_record_const">See constant</a>. 
- `samplerate` - Integer type. Sample rate. Currently supports 8000 sps and 16000 sps.
- `time` - Integer type. Recording duration. Unit: second. 

**Return Value:**

`0` - Successful execution. `-1`- Failed execution.

### Record.stream_read

```python
Record.stream_read(read_buf, len)
```

This method reads the recording stream.

> Currently, only the EC600N/EC800N series modules support this feature.

**Parameter:**

- `read_buf` - Bytearray type. Recording stream buffer.
- `len` - Integer type. Length to be read.

**Return Value:**

Returns the number of bytes actually read for successful execution or -1 if failed.

## Constant

### <span id="label_record_const">Record.AMRNB</span>

AMR format.