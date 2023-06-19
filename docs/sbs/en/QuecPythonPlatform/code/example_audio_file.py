# -*- coding: UTF-8 -*-
#备注如下：
#(1)对于EC600S和EC600N的话，下面的代码不需要做任何修改，就可以播放
#(2)对于EC600U的通道0的话，注释掉18行（18行的配置对这个播放没有影响）
#(3)对于EC600U的通道2的话，注释掉12行和19行，取消注释13行；
import utime as time
import audio
from machine import Pin


def example_audio_mp3():
    aud = audio.Audio(0)  # 配置通道0
    # aud = audio.Audio(2)  # 配置通道2
    aud.setVolume(9)
    '''
    使能外接喇叭播放
    '''
    # Pin(Pin.GPIO11, Pin.OUT, Pin.PULL_PD, 1)  # 官方板V1.1使用
    Pin(Pin.GPIO9, Pin.OUT, Pin.PULL_PD, 1)  # 官方板V1.2和V1.3使用
    # U: 表示用户目录， GUI下载工具会将文件下载到 /usr 文件下
    aud.play(2, 1, "U:/example.mp3")
    pass

if __name__ == "__main__":
    example_audio_mp3()
