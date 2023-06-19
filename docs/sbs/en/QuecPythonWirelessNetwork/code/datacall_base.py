
# reference：https://python.quectel.com/wiki/#/en-us/api/QuecPythonClasslib?id=datacall-data-call

import dataCall
import net
import utime as time


g_net_status = False


def callback(args):
    pdp = args[0]
    nw_sta = args[1]
    if nw_sta == 1:
        g_net_status = True
        print("*** network %d connected! ***" % pdp)
    else:
        g_net_status = False
        print("*** network %d not connected! ***" % pdp)
        # Enter again
        test_datacall_module()


def test_datacall_module():
    # Call
    ret = dataCall.start(1, 0, "3gnet.mnc001.mcc460.gprs", "", "", 0)
    if ret == 0:
        print("datacall start has success")
        g_net_status = True
    # Get info such as IP address
    Info = dataCall.getInfo(1, 0)
    print(Info)
    print("test datacall has exit")
    pass


def test_datacall_callback():
    test_datacall_module()
    # Register callback interrupt
    ret = dataCall.setCallback(callback)
    if ret == 0x00:
        print("set Callback has success")
    net.setModemFun(4)  # Enter flight mode
    time.sleep_ms(1000)
    net.setModemFun(1)  # Come back to normal mode
    print("test_datacall_callback funcation has exited")
    pass


if __name__ == "__main__":
    test_datacall_callback()
