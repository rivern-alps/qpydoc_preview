import quecIot
import quecTtlv

key = "p1116T"  # 填入产品key
src = "bGpkVnordkFodFZj"  # 填入产品密钥

DEF_ID_TYPE = ['0', '温度', '湿度', '光照']
DEF_DATA_TYPE0 = 'bool'
DEF_DATA_TYPE1 = 'num'
DEF_DATA_TYPE2 = 'byte'
DEF_DATA_TYPE3 = 'struct'
DEF_DATA_TYPE = [
    DEF_DATA_TYPE0,
    DEF_DATA_TYPE1,
    DEF_DATA_TYPE2,
    DEF_DATA_TYPE3]
# 0 布尔
# 1 数值
# 2 Byt
# 3 结构体


class Quecthing:
    def __init__(self):
        # ''' 初始化qucsdk '''
        quecIot.init()
        # ''' 注册事件回调函数 '''
        quecIot.setEventCB(self.eventCB)
        # ''' 配置产品信息'''
        quecIot.setProductinfo(key, src)
        # ''' 配置服务器信息，可选，默认连接MQTT生产环境服务器 '''
        # quecIot.setServer(1, "http://iot-south.quectel.com:2883")
        # ''' 配置PDP context Id，可选，默认为1 '''
        # quecIot.setPdpContextId(1)
        # ''' 配置lifetime，可选，MQTT默认为120 '''
        # quecIot.setLifetime(120)
        # ''' 配置外部MCU标识号和版本号，可选，如没有外部MCU则不需要配置 '''
        # quecIot.setMcuVersion("MCU1", "1_0_0")
        # ''' 启动云平台连接 '''
        quecIot.setConnmode(1)
        return

    @staticmethod
    def eventCB(data):
        print("event:", data)

        if 5 == data[0] and 10210 == data[1]:
            data = data[2]
            listret = quecTtlv.nodeGet(data)
            print(listret)
            listretlen = len(listret)
            for i in range(listretlen):
                id = listret[i][0]
                type = listret[i][1]
                if DEF_DATA_TYPE[type] == DEF_DATA_TYPE0:
                    ret = quecTtlv.idGetBool(data, id)
                    print(DEF_ID_TYPE[id], ret)
                elif DEF_DATA_TYPE[type] == DEF_DATA_TYPE1:
                    ret = quecTtlv.idGetNum(data, id)
                    print(DEF_ID_TYPE[id], ret)


if __name__ == '__main__':
    Quecthing()
