from misc import PWM
import utime as time
import log


class pwmclass():
    def __init__(self):
        self.Log = log.basicConfig()
        self.Log = log.getLogger("pwm_class")
        # self.Log.setLevel(log.INFO)
        self.Log.setLevel(log.DEBUG)
        self.pwm = None
        pass

    """
        注：EC100YCN平台，支持PWM0~PWM3，对应引脚如下：
        PWM0 – 引脚号19
        PWM1 – 引脚号18
        PWM2 – 引脚号23
        PWM3 – 引脚号22

        注：EC600SCN平台，支持PWM0~PWM3，对应引脚如下：
        PWM0 – 引脚号52
        PWM1 – 引脚号53
        PWM2 – 引脚号70
        PWM3 – 引脚号69
    """

    # fre 频率为K， (0.0 ~ 1000]
    # Duty_Cycle (0~1)
    def init(self, Pwm_pin=PWM.PWM3, fre=1, Duty_Cycle=0.5):
        # https://python.quectel.com/wiki/#/zh-cn/api/QuecPythonClasslib?id=pwm

        # 根据频率，计算出高低电平
        # 计算出周期时间
        if (fre <= 0) or (fre > 1000):
            self.Log.error(
                "ERROR: {0} 不支持的频率参数, 请输入 (0 ~ 1000]k 范围的频率".format(fre))
        if (Duty_Cycle < 0.000) or (Duty_Cycle >= 1):
            self.Log.error(
                "ERROR: {0} 不支持的占空比参数, 请输入 (0~1.0) 范围的频率".format(Duty_Cycle))
        # us 单位
        cycle_time = int(1 * 1000 / fre)
        hight_time = int(cycle_time * Duty_Cycle)
        self.Log.info("""设置 {0} 设备 频率为 {1}khz 
                    周期为 {2}us 占空比 {3}us""".format(Pwm_pin, fre, cycle_time,
                                                  hight_time))
        # ms 周期范围
        # 周期在 (1K us ~ 1000K us)
        if cycle_time > 1000:
            self.pwm = PWM(Pwm_pin, PWM.ABOVE_MS, int(hight_time / 1000),
                           int(cycle_time / 1000))
        # 周期在 10us ~ 15.75ms
        if (cycle_time > 10) and (cycle_time < 15750):
            self.pwm = PWM(Pwm_pin, PWM.ABOVE_10US, int(hight_time / 10),
                           int(cycle_time / 10))
        # 周期在 (0~157us)
        if (cycle_time > 0) and (cycle_time < 157):
            self.pwm = PWM(Pwm_pin, PWM.ABOVE_1US, hight_time, cycle_time)

    def deinit(self, fre=0):
        self.pwm = None
        pass

    def start(self, fre=1):
        self.Log.info("开始输出 PWM 波形".format())
        if self.pwm is not None:
            self.pwm.open()
        pass

    def stop(self):
        if self.pwm is not None:
            self.pwm.close()
        pass


def test_pwm(fre, duty, delay=2):
    obj_pwm = pwmclass()
    obj_pwm.init(fre=fre, Duty_Cycle=duty, Pwm_pin=PWM.PWM3)
    obj_pwm.start()
    time.sleep(delay)
    obj_pwm.stop()
    obj_pwm.deinit()


if __name__ == "__main__":
    # 频率 1K， 占空比 0.1
    test_pwm(fre=1, duty=0.1)
    # 频率 10K， 占空比 0.2
    test_pwm(fre=10, duty=0.2)
    # 频率 100K， 占空比 0.4
    test_pwm(fre=100, duty=0.4)
