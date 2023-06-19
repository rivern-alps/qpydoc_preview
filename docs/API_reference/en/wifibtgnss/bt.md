# bt - Classic Bluetooth

The `bt` module provides Classic Bluetooth related features, including HFP, A2DP, AVRCP and SPP.

**Example**：

```python
#HFP demo program

"""
This example demonstrates a feature for automatically answering calls through HFP.
Platform: EC600UCN_LB Uranium development board.
After running this program, search for the device name on phone A and click to connect. Then, make a call from phone B to phone A. When phone A starts ringing and vibrating, the device will automatically answer the call.
"""
import bt
import utime
import _thread
from queue import Queue
from machine import Pin

# If an external PA is connected to the corresponding playback channel and pin control is required to turn on the PA, follow the steps below
# The specific GPIO used depends on the actual pin used.
gpio11 = Pin(Pin.GPIO11, Pin.OUT, Pin.PULL_DISABLE, 0)
gpio11.write(1)

BT_NAME = 'QuecPython-hfp'

BT_EVENT = {
    'BT_START_STATUS_IND': 0,           # bt/ble start
    'BT_STOP_STATUS_IND': 1,            # bt/ble stop
    'BT_HFP_CONNECT_IND': 40,           # bt hfp connected
    'BT_HFP_DISCONNECT_IND': 41,        # bt hfp disconnected
    'BT_HFP_CALL_IND': 42,              # bt hfp call state
    'BT_HFP_CALL_SETUP_IND': 43,        # bt hfp call setup state
    'BT_HFP_NETWORK_IND': 44,           # bt hfp network state
    'BT_HFP_NETWORK_SIGNAL_IND': 45,    # bt hfp network signal
    'BT_HFP_BATTERY_IND': 46,           # bt hfp battery level
    'BT_HFP_CALLHELD_IND': 47,          # bt hfp callheld state
    'BT_HFP_AUDIO_IND': 48,             # bt hfp audio state
    'BT_HFP_VOLUME_IND': 49,            # bt hfp volume type
    'BT_HFP_NETWORK_TYPE': 50,          # bt hfp network type
    'BT_HFP_RING_IND': 51,              # bt hfp ring indication
    'BT_HFP_CODEC_IND': 52,             # bt hfp codec type
}

HFP_CONN_STATUS = 0
HFP_CONN_STATUS_DICT = {
    'HFP_DISCONNECTED': 0,
    'HFP_CONNECTING': 1,
    'HFP_CONNECTED': 2,
    'HFP_DISCONNECTING': 3,
}
HFP_CALL_STATUS = 0
HFP_CALL_STATUS_DICT = {
    'HFP_NO_CALL_IN_PROGRESS': 0,
    'HFP_CALL_IN_PROGRESS': 1,
}

BT_IS_RUN = 0

msg_queue = Queue(30)


def get_key_by_value(val, d):
    for key, value in d.items():
        if val == value:
            return key
    return None

def bt_callback(args):
    global msg_queue
    msg_queue.put(args)

def bt_event_proc_task():
    global msg_queue
    global BT_IS_RUN
    global BT_EVENT
    global HFP_CONN_STATUS
    global HFP_CONN_STATUS_DICT
    global HFP_CALL_STATUS
    global HFP_CALL_STATUS_DICT

    while True:
        print('wait msg...')
        msg = msg_queue.get()  # It will be blocked here when there is no message.
        event_id = msg[0]
        status = msg[1]

        if event_id == BT_EVENT['BT_START_STATUS_IND']:
            print('event: BT_START_STATUS_IND')
            if status == 0:
                print('BT start successfully.')
                BT_IS_RUN = 1
                bt_status = bt.getStatus()
                if bt_status == 1:
                    print('BT status is 1, normal status.')
                else:
                    print('BT status is {}, abnormal status.'.format(bt_status))
                    bt.stop()
                    break

                retval = bt.getLocalName()
                if retval != -1:
                    print('The current BT name is : {}'.format(retval[1]))
                else:
                    print('Failed to get BT name.')
                    bt.stop()
                    break

                print('Set BT name to {}'.format(BT_NAME))
                retval = bt.setLocalName(0, BT_NAME)
                if retval != -1:
                    print('BT name set successfully.')
                else:
                    print('BT name set failed.')
                    bt.stop()
                    break

                retval = bt.getLocalName()
                if retval != -1:
                    print('The new BT name is : {}'.format(retval[1]))
                else:
                    print('Failed to get new BT name.')
                    bt.stop()
                    break

                # Sets the Bluetooth visible mode to discoverable and connectable
                retval = bt.setVisibleMode(3)
                if retval == 0:
                    mode = bt.getVisibleMode()
                    if mode == 3:
                        print('BT visible mode set successfully.')
                    else:
                        print('BT visible mode set failed.')
                        bt.stop()
                        break
                else:
                    print('BT visible mode set failed.')
                    bt.stop()
                    break
            else:
                print('BT start failed.')
                bt.stop()
                break
        elif event_id == BT_EVENT['BT_STOP_STATUS_IND']:
            print('event: BT_STOP_STATUS_IND')
            if status == 0:
                BT_IS_RUN = 0
                print('BT stop successfully.')
            else:
                print('BT stop failed.')
            break
        elif event_id == BT_EVENT['BT_HFP_CONNECT_IND']:
            HFP_CONN_STATUS = msg[2]
            addr = msg[3]  # MAC address of BT host
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_CONNECT_IND, {}, hfp_conn_status:{}, mac:{}'.format(status, get_key_by_value(msg[2], HFP_CONN_STATUS_DICT), mac))
            if status != 0:
                print('BT HFP connect failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_HFP_DISCONNECT_IND']:
            HFP_CONN_STATUS = msg[2]
            addr = msg[3]  # MAC address of BT host
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_DISCONNECT_IND, {}, hfp_conn_status:{}, mac:{}'.format(status, get_key_by_value(msg[2], HFP_CONN_STATUS_DICT), mac))
            if status != 0:
                print('BT HFP disconnect failed.')
            bt.stop()
        elif event_id == BT_EVENT['BT_HFP_CALL_IND']:
            call_sta = msg[2]
            addr = msg[3]  # MAC address of BT host
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_CALL_IND, {}, hfp_call_status:{}, mac:{}'.format(status, get_key_by_value(msg[2], HFP_CALL_STATUS_DICT), mac))
            if status != 0:
                print('BT HFP call failed.')
                bt.stop()
                continue

            if call_sta == HFP_CALL_STATUS_DICT['HFP_NO_CALL_IN_PROGRESS']:
                if HFP_CALL_STATUS == HFP_CALL_STATUS_DICT['HFP_CALL_IN_PROGRESS']:
                    HFP_CALL_STATUS = call_sta
                    if HFP_CONN_STATUS == HFP_CONN_STATUS_DICT['HFP_CONNECTED']:
                        print('call ended, ready to disconnect hfp.')
                        retval = bt.hfpDisconnect(addr)
                        if retval == 0:
                            HFP_CONN_STATUS = HFP_CONN_STATUS_DICT['HFP_DISCONNECTING']
                        else:
                            print('Failed to disconnect hfp connection.')
                            bt.stop()
                            continue
            else:
                if HFP_CALL_STATUS == HFP_CALL_STATUS_DICT['HFP_NO_CALL_IN_PROGRESS']:
                    HFP_CALL_STATUS = call_sta
                    print('set audio output channel to 2.')
                    bt.setChannel(2)
                    print('set volume to 7.')
                    retval = bt.hfpSetVolume(addr, 7)
                    if retval != 0:
                        print('set volume failed.')
        elif event_id == BT_EVENT['BT_HFP_CALL_SETUP_IND']:
            call_setup_status = msg[2]
            addr = msg[3]  # MAC address of BT host
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_CALL_SETUP_IND, {}, hfp_call_setup_status:{}, mac:{}'.format(status, call_setup_status, mac))
            if status != 0:
                print('BT HFP call setup failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_HFP_CALLHELD_IND']:
            callheld_status = msg[2]
            addr = msg[3]  #MAC address of BT host
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_CALLHELD_IND, {}, callheld_status:{}, mac:{}'.format(status, callheld_status, mac))
            if status != 0:
                print('BT HFP callheld failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_HFP_NETWORK_IND']:
            network_status = msg[2]
            addr = msg[3]  # MAC address of BT host
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_NETWORK_IND, {}, network_status:{}, mac:{}'.format(status, network_status, mac))
            if status != 0:
                print('BT HFP network status failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_HFP_NETWORK_SIGNAL_IND']:
            network_signal = msg[2]
            addr = msg[3]  # MAC address of BT host
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_NETWORK_SIGNAL_IND, {}, signal:{}, mac:{}'.format(status, network_signal, mac))
            if status != 0:
                print('BT HFP network signal failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_HFP_BATTERY_IND']:
            battery_level = msg[2]
            addr = msg[3]  # MAC address of BT host
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_BATTERY_IND, {}, battery_level:{}, mac:{}'.format(status, battery_level, mac))
            if status != 0:
                print('BT HFP battery level failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_HFP_AUDIO_IND']:
            audio_status = msg[2]
            addr = msg[3]  # MAC address of BT host
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_AUDIO_IND, {}, audio_status:{}, mac:{}'.format(status, audio_status, mac))
            if status != 0:
                print('BT HFP audio failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_HFP_VOLUME_IND']:
            volume_type = msg[2]
            addr = msg[3]  # MAC address of BT host
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_VOLUME_IND, {}, volume_type:{}, mac:{}'.format(status, volume_type, mac))
            if status != 0:
                print('BT HFP volume failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_HFP_NETWORK_TYPE']:
            service_type = msg[2]
            addr = msg[3]  # MAC address of BT host
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_NETWORK_TYPE, {}, service_type:{}, mac:{}'.format(status, service_type, mac))
            if status != 0:
                print('BT HFP network service type failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_HFP_RING_IND']:
            addr = msg[3]  # MAC address of BT host
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_RING_IND, {}, mac:{}'.format(status, mac))
            if status != 0:
                print('BT HFP ring failed.')
                bt.stop()
                continue
            retval = bt.hfpAnswerCall(addr)
            if retval == 0:
                print('The call was answered successfully.')
            else:
                print('Failed to answer the call.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_HFP_CODEC_IND']:
            codec_type = msg[2]
            addr = msg[3]  # MAC address of BT host
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_CODEC_IND, {}, codec_type:{}, mac:{}'.format(status, codec_type, mac))
            if status != 0:
                print('BT HFP codec failed.')
                bt.stop()
                continue
    print('Ready to release hfp.')
    bt.hfpRelease()
    bt.release()


def main():
    global BT_IS_RUN

    _thread.start_new_thread(bt_event_proc_task, ())

    retval = bt.init(bt_callback)
    if retval == 0:
        print('BT init successful.')
    else:
        print('BT init failed.')
        return -1
    retval = bt.hfpInit()
    if retval == 0:
        print('HFP init successful.')
    else:
        print('HFP init failed.')
        return -1
    retval = bt.start()
    if retval == 0:
        print('BT start successful.')
    else:
        print('BT start failed.')
        retval = bt.hfpRelease()
        if retval == 0:
            print('HFP release successful.')
        else:
            print('HFP release failed.')
        retval = bt.release()
        if retval == 0:
            print('BT release successful.')
        else:
            print('BT release failed.')
        return -1

    count = 0
    while True:
        utime.sleep(1)
        count += 1
        cur_time = utime.localtime()
        timestamp = "{:02d}:{:02d}:{:02d}".format(cur_time[3], cur_time[4], cur_time[5])

        if count % 5 == 0:
            if BT_IS_RUN == 1:
                print('[{}] BT HFP is running, count = {}......'.format(timestamp, count))
                print('')
            else:
                print('BT HFP has stopped running, ready to exit.')
                break


if __name__ == '__main__':
    main()

```

```python
#A2DP/AVRCP demo program

"""
This example demonstrates a simple Bluetooth music playback control feature through A2DP/AVRCP. 
Once you run the example code, search for the device name on your phone and connect to it. Open your music playback software, then return to the demo program interface to follow the prompt menu to input the corresponding command to control your music playback. You can play, pause, switch to the previous or next song, and adjust the volume.
"""
import bt
import utime
import _thread
from queue import Queue
from machine import Pin

BT_STATUS_DICT = {
    'BT_NOT_RUNNING': 0,
    'BT_IS_RUNNING': 1
}

A2DP_AVRCP_CONNECT_STATUS = {
    'DISCONNECTED': 0,
    'CONNECTING': 1,
    'CONNECTED': 2,
    'DISCONNECTING': 3
}

host_addr = 0
msg_queue = Queue(10)

# If an external PA is connected to the corresponding playback channel and pin control is required to turn on the PA, follow the steps below
# The specific GPIO used depends on the actual pin used.
gpio11 = Pin(Pin.GPIO11, Pin.OUT, Pin.PULL_DISABLE, 0)
gpio11.write(1)


def cmd_proc(cmd):
    cmds = ('1', '2', '3', '4', '5')
    vols = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11')

    if cmd in cmds:
        if cmd == '5':
            while True:
                tmp = input('Please input volume: ')
                if len(tmp) != 1:
                    vol = tmp.split('Please input volume: ')[1]
                else:
                    vol = tmp
                if vol in vols:
                    return cmd, int(vol)
                else:
                    print('Volume should be in [0,11], try again.')
        else:
            return cmd, 0
    else:
        print('Command {} is not supported!'.format(cmd))
        return -1

def avrcp_play(args):
    return bt.avrcpStart()

def avrcp_pause(args):
    return bt.avrcpPause()

def avrcp_prev(args):
    return bt.avrcpPrev()

def avrcp_next(args):
    return bt.avrcpNext()

def avrcp_set_volume(vol):
    return bt.avrcpSetVolume(vol)

def bt_callback(args):
    pass

def bt_a2dp_avrcp_proc_task():
    global msg_queue

    cmd_handler = {
        '1': avrcp_play,
        '2': avrcp_pause,
        '3': avrcp_prev,
        '4': avrcp_next,
        '5': avrcp_set_volume,
    }
    while True:
        # print('wait msg...')
        msg = msg_queue.get()
        print('recv msg: {}'.format(msg))
        cmd_handler.get(msg[0])(msg[1])


def main():
    global host_addr
    global msg_queue

    _thread.start_new_thread(bt_a2dp_avrcp_proc_task, ())
    bt.init(bt_callback)
    bt.setChannel(2)
    retval = bt.a2dpavrcpInit()
    if retval == 0:
        print('BT A2DP/AVRCP initialization succeeded.')
    else:
        print('BT A2DP/AVRCP initialization failed.')
        return -1

    retval = bt.start()
    if retval != 0:
        print('BT start failed.')
        return -1

    utime.sleep_ms(1500)

    old_name = bt.getLocalName()
    if old_name == -1:
        print('Get BT name error.')
        return -1
    print('The current BT name is {}'.format(old_name[1]))
    new_name = 'QuecPython-a2dp'
    print('Set new BT name to {}'.format(new_name))
    retval = bt.setLocalName(0, new_name)
    if retval == -1:
        print('Set BT name failed.')
        return -1
    cur_name = bt.getLocalName()
    if cur_name == -1:
        print('Get new BT name error.')
        return -1
    else:
        if cur_name[1] == new_name:
            print('BT name changed successfully.')
        else:
            print('BT name changed failed.')

    visible_mode = bt.getVisibleMode()
    if visible_mode != -1:
        print('The current BT visible mode is {}'.format(visible_mode))
    else:
        print('Get BT visible mode error.')
        return -1

    print('Set BT visible mode to 3.')
    retval = bt.setVisibleMode(3)
    if retval == -1:
        print('Set BT visible mode error.')
        return -1

    print('BT reconnect check start......')    
    bt.reconnect_set(25, 2)
    bt.reconnect()

    count = 0
    while True:
        count += 1
        if count % 5 == 0:
            print('waiting to be connected...')
        if count >= 10000:
            count = 0
        a2dp_status = bt.a2dpGetConnStatus()
        avrcp_status = bt.avrcpGetConnStatus()
        if a2dp_status == A2DP_AVRCP_CONNECT_STATUS['CONNECTED'] and avrcp_status == A2DP_AVRCP_CONNECT_STATUS['CONNECTED']:
            print('========== BT connected! =========')
            addr = bt.a2dpGetAddr()
            if addr != -1:
                mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
                print('The BT address on the host side: {}'.format(mac))
                host_addr = addr
            else:
                print('Get BT addr error.')
                return -1
            print('Please open the music player software on your phone first.')
            print('Please enter the following options to select a function:')
            print('========================================================')
            print('1 : play')
            print('2 : pause')
            print('3 : prev')
            print('4 : next')
            print('5 : set volume')
            print('6 : exit')
            print('========================================================')
            while True:
                tmp = input('> ')
                if len(tmp) != 1:
                    cmd = tmp.split('> ')[1]
                else:
                    cmd = tmp
                if cmd == '6':
                    break
                retval = cmd_proc(cmd)
                if retval != -1:
                    msg_queue.put(retval)
            break
        else:
            utime.sleep_ms(1000)
    print('Ready to disconnect a2dp.')
    retval = bt.a2dpDisconnect(host_addr)
    if retval == 0:
        print('a2dp connection disconnected successfully')
    else:
        print('Disconnect a2dp error.')
    print('Ready to stop BT.')
    retval = bt.stop()
    if retval == 0:
        print('BT has stopped.')
    else:
        print('BT stop error.')
    bt.a2dpavrcpRelease()
    bt.release()


if __name__ == '__main__':
    main()
```

```python
#SPP demo program

"""
This example demonstrates how to transmit data between a mobile phone and a device through SPP. To use this example:
1. Install a Bluetooth serial port APP, such as BlueSPP, on your Android phone and open the APP before running the program.
2. Modify the target device's Bluetooth name in the program by changing the value of DST_DEVICE_INFO['dev_name'] to the name of the phone you want to connect to.
3. Run the program, which will search for nearby devices until the target device is found and connect to the target device through SPP.
4. Check your phone for a Bluetooth pairing request and click "Pair" if prompted.
5. Once the pairing is successful, you can use the Bluetooth serial port interface to send data to the device. The device will respond with "I have received the data you sent" after receiving the data.
6. To end the program, click "Disconnect" in the mobile APP.
"""
import bt
import utime
import _thread
from queue import Queue


BT_NAME = 'QuecPython-SPP'

BT_EVENT = {
    'BT_START_STATUS_IND': 0,          # bt/ble start
    'BT_STOP_STATUS_IND': 1,           # bt/ble stop
    'BT_SPP_INQUIRY_IND': 6,           # bt spp inquiry ind
    'BT_SPP_INQUIRY_END_IND': 7,       # bt spp inquiry end ind
    'BT_SPP_RECV_DATA_IND': 14,        # bt spp recv data ind
    'BT_SPP_CONNECT_IND': 61,          # bt spp connect ind
    'BT_SPP_DISCONNECT_IND': 62,       # bt spp disconnect ind
}

DST_DEVICE_INFO = {
    'dev_name': 'HUAWEI Mate40 Pro', # The Bluetooth name of the device you want to connect to
    'bt_addr': None
}

BT_IS_RUN = 0
msg_queue = Queue(30)


def bt_callback(args):
    global msg_queue
    msg_queue.put(args)


def bt_event_proc_task():
    global msg_queue
    global BT_IS_RUN
    global DST_DEVICE_INFO

    while True:
        print('wait msg...')
        msg = msg_queue.get()  # It will be blocked here when there is no message.
        event_id = msg[0]
        status = msg[1]

        if event_id == BT_EVENT['BT_START_STATUS_IND']:
            print('event: BT_START_STATUS_IND')
            if status == 0:
                print('BT start successfully.')
                BT_IS_RUN = 1

                print('Set BT name to {}'.format(BT_NAME))
                retval = bt.setLocalName(0, BT_NAME)
                if retval != -1:
                    print('BT name set successfully.')
                else:
                    print('BT name set failed.')
                    bt.stop()
                    continue

                retval = bt.setVisibleMode(3)
                if retval == 0:
                    mode = bt.getVisibleMode()
                    if mode == 3:
                        print('BT visible mode set successfully.')
                    else:
                        print('BT visible mode set failed.')
                        bt.stop()
                        continue
                else:
                    print('BT visible mode set failed.')
                    bt.stop()
                    continue

                retval = bt.startInquiry(15)
                if retval != 0:
                    print('Inquiry error.')
                    bt.stop()
                    continue
            else:
                print('BT start failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_STOP_STATUS_IND']:
            print('event: BT_STOP_STATUS_IND')
            if status == 0:
                BT_IS_RUN = 0
                print('BT stop successfully.')
            else:
                print('BT stop failed.')

            retval = bt.sppRelease()
            if retval == 0:
                print('SPP release successfully.')
            else:
                print('SPP release failed.')
            retval = bt.release()
            if retval == 0:
                print('BT release successfully.')
            else:
                print('BT release failed.')
            break
        elif event_id == BT_EVENT['BT_SPP_INQUIRY_IND']:
            print('event: BT_SPP_INQUIRY_IND')
            if status == 0:
                rssi = msg[2]
                name = msg[4]
                addr = msg[5]
                mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
                print('name: {}, addr: {}, rssi: {}'.format(name, mac, rssi))

                if name == DST_DEVICE_INFO['dev_name']:
                    print('The target device is found, device name {}'.format(name))
                    DST_DEVICE_INFO['bt_addr'] = addr
                    retval = bt.cancelInquiry()
                    if retval != 0:
                        print('cancel inquiry failed.')
                        continue
            else:
                print('BT inquiry failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_SPP_INQUIRY_END_IND']:
            print('event: BT_SPP_INQUIRY_END_IND')
            if status == 0:
                print('BT inquiry has ended.')
                inquiry_sta = msg[2]
                if inquiry_sta == 0:
                    if DST_DEVICE_INFO['bt_addr'] is not None:
                        print('Ready to connect to the target device : {}'.format(DST_DEVICE_INFO['dev_name']))
                        retval = bt.sppConnect(DST_DEVICE_INFO['bt_addr'])
                        if retval != 0:
                            print('SPP connect failed.')
                            bt.stop()
                            continue
                    else:
                        print('Not found device [{}], continue to inquiry.'.format(DST_DEVICE_INFO['dev_name']))
                        bt.cancelInquiry()
                        bt.startInquiry(15)
            else:
                print('Inquiry end failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_SPP_RECV_DATA_IND']:
            print('event: BT_SPP_RECV_DATA_IND')
            if status == 0:
                datalen = msg[2]
                data = msg[3]
                print('recv {} bytes data: {}'.format(datalen, data))
                send_data = 'I have received the data you sent.'
                print('send data: {}'.format(send_data))
                retval = bt.sppSend(send_data)
                if retval != 0:
                    print('send data faied.')
            else:
                print('Recv data failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_SPP_CONNECT_IND']:
            print('event: BT_SPP_CONNECT_IND')
            if status == 0:
                conn_sta = msg[2]
                addr = msg[3]
                mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
                print('SPP connect successful, conn_sta = {}, addr {}'.format(conn_sta, mac))
            else:
                print('Connect failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_SPP_DISCONNECT_IND']:
            print('event: BT_SPP_DISCONNECT_IND')
            conn_sta = msg[2]
            addr = msg[3]
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('SPP disconnect successful, conn_sta = {}, addr {}'.format(conn_sta, mac))
            bt.stop()
            continue


def main():
    global BT_IS_RUN

    _thread.start_new_thread(bt_event_proc_task, ())
    retval = bt.init(bt_callback)
    if retval == 0:
        print('BT init successful.')
    else:
        print('BT init failed.')
        return -1
    retval = bt.sppInit()
    if retval == 0:
        print('SPP init successful.')
    else:
        print('SPP init failed.')
        return -1
    retval = bt.start()
    if retval == 0:
        print('BT start successful.')
    else:
        print('BT start failed.')
        retval = bt.sppRelease()
        if retval == 0:
            print('SPP release successful.')
        else:
            print('SPP release failed.')
        return -1

    count = 0
    while True:
        utime.sleep(1)
        count += 1
        cur_time = utime.localtime()
        timestamp = "{:02d}:{:02d}:{:02d}".format(cur_time[3], cur_time[4], cur_time[5])

        if count % 5 == 0:
            if BT_IS_RUN == 1:
                print('[{}] BT SPP is running, count = {}......'.format(timestamp, count))
                print('')
            else:
                print('BT SPP has stopped running, ready to exit.')
                break


if __name__ == '__main__':
    main()
```

**Note**：

Currently, only EC200U/EC600U/EG915U/EG912U series module supports `bt` feature.

## Initialization Related Features

### bt.init

```python
bt.init(user_cb)
```

Initializes the Bluetooth and registers a callback function.

**Parameter:**

- `user_cb`- Function type. Callback function. The meaning of the callback function parameters: `args[0]` is fixed to represent event_id; `args[1]` is fixed to represent the status, `0` indicating successful execution and non-`0` indicating failed execution. The number of callback function parameters is not fixed at two, but depends on the first parameter `args[0]`. The following table lists the number of parameters and explanations for different event IDs.

| event_id | Parameter Number | Description                                                  |
| :------: | :--------------: | ------------------------------------------------------------ |
|    0     |        2         | args[0]: event_id. BT/BLE start event.<br>args[1]: status. The operation status. 0 - successful operation; other values - failed operation. |
|    1     |        2         | args[0]: event_id. BT/BLE stop event.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation. |
|    6     |        6         | args[0]: event_id. BT inquiry event.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: rssi. Signal strength.<br/>args[3]: device_class. <br/>args[4]: device_name. Device name. String type.<br/>args[5]: addr. The MAC address of the discovered Bluetooth device. |
|    7     |        3         | args[0]: event_id. BT inquiry end event.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: end_status. 0 - End normally, 8 - End forcefully. |
|    14    |        4         | args[0]: event_id. BT SPP receive event.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: data_len. The length of the received data.<br/>args[3]: data. The received data in bytearray type. |
|    40    |        4         | args[0]: event_id. BT HFP connect event.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: hfp_connect_status. HFP connection status.<br/>               0 - Disconnected<br/>               1 - Connecting<br/>               2 - Connected<br/>               3 - Disconnecting<br/>args[3]: addr. The address of the BT master in bytearray type. |
|    41    |        4         | args[0]: event_id. BT HFP disconnect event.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: hfp_connect_status. HFP connection status.<br/>               0 - Disconnected<br/>               1 - Connecting<br/>               2 - Connected<br/>               3 - Disconnecting<br/>args[3]: addr. The address of the BT master in bytearray type. |
|    42    |        4         | args[0]: event_id. BT HFP call status event.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: hfp_call_status. HFP call status.<br/>               0 - There are currently no calls in progress<br/>               1 - There is currently at least one call in progress<br/> args[3]: addr. The address of the BT master in bytearray type. |
|    43    |        4         | args[0]: event_id. BT HFP call setup status event.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: hfp_call_setup_status. HFP call setup status.<br/>               0 - There are no call to be connected<br/>               1 - There is an incoming call that has not yet been connected<br/>               2 - There is an outgoing call that has not yet been connected<br/>               3 - The other end of the Bluetooth connection for an outgoing call is ringing<br/> args[3]: addr. The address of the BT master in bytearray type. |
|    44    |        4         | args[0]: event_id. BT HFP network status event.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: hfp_network_status. AG network status.<br/>               0 - The network is not available<br/>               1 - The network is normal<br/>args[3]: addr. The address of the BT master in bytearray type. |
|    45    |        4         | args[0]: event_id. BT HFP network signal event.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: hfp_network_signal. AG signal. Range: 0–5.<br/>args[3]: addr. The address of the BT master in bytearray type. |
|    46    |        4         | args[0]: event_id. BT HFP battery level event.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: hfp_battery_level. The AG battery level. Range: 0–5. <br/>args[3]: addr. The address of the BT master in bytearray type. |
|    47    |        4         | args[0]: event_id. BT HFP call held status event.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: hfp_call_held_status. HFP call held status.<br/>               0 - There is no call on hold.<br/>               1 - The call is held and either paused or there is an active     call/hold call switching.<br/>               2 - The call is held and there is no active call<br/>args[3]: addr. The address of the BT master in bytearray type. |
|    48    |        4         | args[0]: event_id. BT HFP audio status event.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: hfp_audio_status. Audio connection status.<br/>               0 - Disconnected<br/>               1 - Connecting<br/>               2 - Connected<br/>               3 - Disconnecting<br>args[3]: addr. The address of the BT master in bytearray type. |
|    49    |        4         | args[0]: event_id. BT HFP volume type event.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: hfp_volume_type.<br/>               0 - The volume type is speaker<br/>               1 - The volume type is microphone<br/>args[3]: addr. The address of the BT master in bytearray type. |
|    50    |        4         | args[0]: event_id. BT HFP service type event.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: hfp_service_type. The current AG network service mode.<br/>               0 - Normal network mode<br/>               1 - Roaming mode<br/>args[3]: addr. The address of the BT master in bytearray type. |
|    51    |        4         | args[0]: event_id. BT HFP ring event, that is, ringing event on incoming call.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: Reserved parameter.<br/>args[3]: addr. The address of the BT master in bytearray type. |
|          |                  | args[0]: event_id. BT HFP codec type event.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: hfp_codec_type. Which codec mode is currently in use.<br/>               1 - CVDS, 8 kHz sample rate<br/>               2 - mSBC, 16 kHz sample rate<br/>args[3]: addr. The address of the BT master in bytearray type. |
|    61    |        4         | args[0]: event_id. BT SPP connect event.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: spp_connect_status. SPP connection status.<br/>               0 - Disconnected<br/>               1 - Connecting<br/>               2 - Connected<br/>               3 - Disconnecting<br/> args[3]: addr. The MAC address of the peer device in bytearray type. |
|    62    |        4         | args[0]: event_id. BT SPP disconnect event.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: spp_connect_status. SPP connection status.<br/>               0 - Disconnected<br/>               1 - Connecting<br/>               2 - Connected<br/>               3 - Disconnecting<br/> args[3]: addr. The MAC address of the peer device in bytearray type. |

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

**Example**：

```python
def bt_callback(args):
	event_id = args[0]  # The first parameter is fixed to represent event ID.
	status = args[1] # The second parameter is fixed to represent status, indicating whether the execution result of an operation is successful or failed.
	......
```

### bt.release

```python
bt.release()
```

Releases Bluetooth resources.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### bt.start

```python
bt.start()
```

Enables Bluetooth feature.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### bt.stop

```python
bt.stop()
```

Disables Bluetooth feature.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### bt.getStatus

```python
bt.getStatus()
```

Gets the Bluetooth status.

**Return Value：**

- Returns Bluetooth status in integer type. `0`-Stopped, `1`- Working normally, `-1`- Failed execution.

### bt.getLocalAddr

```python
bt.getLocalAddr()
```

Gets the Bluetooth address.

**Return Value：**

- Returns a  Bluetooth address (6 bytes) in bytearray type for successful execution or `-1` for failed execution.

**Example**：

```python
>>> addr = bt.getLocalAddr()
>>> print(addr)
b'\xc7\xa13\xf8\xbf\x1a'
>>> mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
>>> print('mac = [{}]'.format(mac))
mac = [1a:bf:f8:33:a1:c7]
```

**Note**：

This interface needs to be called after Bluetooth has been initialized and successfully started, such as after receiving an event with `event_id` set to 0 in the callback, that is, after the start is successful.

### bt.setLocalName

```python
bt.setLocalName(code, name)
```

Sets the Bluetooth name.

**Parameter：**

- `code`- Integer type. Encoding scheme. 0 - UTF8，1 - GBK.
- `name`- String type. The Bluetooth name. Maximum length: 22 bytes.

**Return Value：**

- Returns a Bluetooth address (6 bytes) in  bytearray type for successful execution or `-1` for failed execution.

**Example**：

```python
>>> bt.setLocalName(0, 'QuecPython-BT')
0
```

### bt.getLocalName

```python
bt.getLocalName()
```

Gets the Bluetooth name.

**Return Value：**

- Returns a tuple `(code, name)` containing the name encoding scheme and the Bluetooth name for successful execution, or `-1` for failed execution. 

**Example**：

```python
>>> bt.getLocalName()
(0, 'QuecPython-BT')
```

### bt.setVisibleMode

```python
bt.setVisibleMode(mode)
```

Sets the Bluetooth visible mode, which means that it configures whether the module can be discovered or connected as a slave when scanning. 

**Parameter：**

- `mode`- Integer type. Visible mode. The specific meanings of the values are shown in the following table: 

| Value | Description                   |
| ----- | ----------------------------- |
| 0     | Undiscoverable, unconnectable |
| 1     | Discoverable, unconnectable   |
| 2     | Undiscoverable, connectable   |
| 3     | Discoverable, connectable     |

**Return Value：**

- Returns Bluetooth address (6 bytes) in bytearray type for successful execution, or `-1` for failed execution.

**Example**：

```python
>>> bt.setVisibleMode(3)
0
```

### bt.getVisibleMode

```python
bt.getVisibleMode()
```

Gets the Bluetooth visible mode.

**Return Value：**

- Returns the current visible mode value of the Bluetooth for successful execution, or `-1` for failed execution.

**Example**：

```python
>>> bt.getVisibleMode()
3
```

### bt.startInquiry

```python
bt.startInquiry(mode)
```

Starts searching for nearby Bluetooth devices.

**Parameter：**

- `mode`-Search mode. Indicates which type of device to query, currently set to 15 to search for all.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

**Example**：

```python
bt.startInquiry(15)
```

### bt.cancelInquiry

```python
bt.cancelInquiry()
```

Cancels the searching.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### bt.setChannel

```python
bt.setChannel(channel)
```

Sets the audio output channel used for answering phone calls or playing audio over Bluetooth.

**Parameter：**

- `channel`- Integer type. Audio channel. 0 - Earpiece，1 - Headphone，2 - Speaker.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### bt.reconnect_set

```python
bt.reconnect_set(max_count, period)
```

Sets the maximum number of reconnection attempts and the time interval between two consecutive reconnection attempts when the module and Bluetooth device are disconnected due to distance.

**Parameter：**

- `max_count`- Integer type. The maximum number of reconnection attempts. `0` indicates disabling automatic reconnection.
- `period`- Integer type. The time interval between two consecutive reconnection attempts. Unit: second.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

**Example**：

```python
bt.reconnect_set(25, 2)#Sets the maximum number of reconnection attempts to 25, with a time interval of 2 seconds between each attempt.
```

### bt.reconnect

```python
bt.reconnect()
```

Actively reconnects to the last paired device, such as a mobile phone. This function should be called when the module reboots and reinitializes the Bluetooth connection, or when the Bluetooth is turned off and then turned back on again without rebooting the module.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

**Example**：

Refer to the A2DP demo program.

## HFP Related Features

Provides Bluetooth call related features.

### bt.hfpInit

```python
bt.hfpInit()
```

Initializes HFP feature.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### bt.hfpRelease

```python
bt.hfpRelease()
```

Releases HFP resources.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### bt.hfpConnect

```python
bt.hfpConnect(addr)
```

Connects to AG and establishes an HFP connection.

**Parameter：**

- `addr`- Bytearray type. 6-bytes‘ AG Bluetooth address. 

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### bt.hfpDisonnect

```python
bt.hfpDisonnect(addr)
```

Disconnects the HFP connection.

**Parameter：**

- `addr`- Bytearray type. 6-bytes’ AG Bluetooth address. 

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### bt.hfpSetVolume

```python
bt.hfpSetVolume(addr, vol)
```

Sets the volume during Bluetooth calls.

**Parameter：**

- `addr`- Bytearray type. 6-bytes‘ AG Bluetooth address. 
- `vol`- Integer type. Call volume. Range: 1–15. 

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### bt.hfpRejectAfterAnswer

```python
bt.hfpRejectAfterAnswer(addr)
```

Hangs up the answered call.

**Parameter：**

- `addr`- Bytearray type. 6-bytes’ AG Bluetooth address.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### bt.hfpRejectCall

```python
bt.hfpRejectCall(addr)
```

Rejects a call.

**Parameter：**

- `addr`- Bytearray type. 6-bytes’ AG Bluetooth address.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### bt.hfpAnswerCall

```python
bt.hfpAnswerCall(addr)
```

Answers a call.

**Parameter：**

- `addr`- Bytearray type. 6-bytes’ AG Bluetooth address. 

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### bt.hfpEnableVR

```python
bt.hfpEnableVR(addr)
```

Enables voice assistant.

**Parameter：**

- `addr`- Bytearray type. 6-bytes’ AG Bluetooth address. 

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### bt.hfpDisableVR

```python
bt.hfpDisableVR(addr)
```

Disables voice assistant.

**Parameter：**

- `addr`-Bytearray type. 6-bytes’ AG Bluetooth address.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### bt.hfpDisableVR

```python
bt.hfpDisableVR(addr, cmd)
```

Controls three-way calling.

**Parameter：**

- `addr`- Bytearray type. 6-bytes’ AG Bluetooth address.
- `cmd`- Integer type. Control command.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

## A2DP/AVRCP Related Features

Provides Bluetooth music related features.

### bt.a2dpavrcpInit

```python
bt.a2dpavrcpInit()
```

Initializes the A2DP and AVRCP features.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### bt.a2dpavrcpRelease

```python
bt.a2dpavrcpRelease()
```

Releases the A2DP and AVRCP resources.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### bt.a2dpDisconnect

```python
bt.a2dpDisconnect(addr)
```

Disconnects the A2DP connection.

**Parameter：**

- `addr`- Bytearray type. 6 bytes' Bluetooth address of the A2DP host.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### bt.a2dpGetAddr

```python
bt.a2dpGetAddr()
```

Gets the Bluetooth address of the A2DP host.

**Return Value：**

- Returns a Bluetooth address of the A2DP host (6 bytes) in bytearray type for successful execution or `-1` for failed execution.

### bt.a2dpGetConnStatus

```python
bt.a2dpGetConnStatus()
```

Gets the A2DP connection status.

**Return Value：**

- Returns the A2DP connection status. The specific meanings of the values are shown in the following table:

| Value | Type | Description      |
| ----- | ---- | ---------------- |
| -1    | int  | Failed execution |
| 0     | int  | Disconnected     |
| 1     | int  | Connecting       |
| 2     | int  | Connected        |
| 3     | int  | Disconnecting    |

### bt.avrcpStart

```python
bt.avrcpStart()
```

Controls the host to start playing.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### bt.avrcpPause

```python
bt.avrcpPause()
```

Controls the host to stop playing.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### bt.avrcpPrev

```python
bt.avrcpPrev()
```

Controls the host to play the previous one.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### bt.avrcpNext

```python
bt.avrcpNext()
```

Controls the host to play the next one.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### bt.avrcpSetVolume

```python
bt.avrcpSetVolume(vol)
```

Sets the host's playback volume.

**Parameter：**

- `vol`- Integer type. Playback volume. Range: 0–11. 

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### bt.avrcpGetVolume

```python
bt.avrcpGetVolume()
```

Gets the host's playback volume.

**Return Value：**

- Returns the volume value in integer type for successful execution or `-1` for failed execution.

### bt.avrcpGetPlayStatus

```python
bt.avrcpGetPlayStatus()
```

Gets the host's playback status.

**Return Value：**

- Returns the playback status. The specific meanings of the values are shown in the following table:

| Value | Type | Description                   |
| ----- | ---- | ----------------------------- |
| -1    | int  | Failed execution              |
| 0     | int  | No playback                   |
| 1     | int  | Play                          |
| 2     | int  | Pause                         |
| 3     | int  | Switching to the previous one |
| 4     | int  | Switching to the next one     |

### bt.avrcpGetConnStatus

```python
bt.avrcpGetConnStatus()
```

Gets the host connection status through the AVRCP protocol.

**Return Value：**

- Returns the connection status. The specific meanings of the values are shown in the following table:

| Value | Type | Description      |
| ----- | ---- | ---------------- |
| -1    | int  | Failed execution |
| 0     | int  | Disconnected     |
| 1     | int  | Connecting       |
| 2     | int  | Connected        |
| 3     | int  | Disconnecting    |

## SPP Related Features

Provides Bluetooth transmission related features.

### bt.sppInit

```python
bt.sppInit()
```

Initializes SPP feature.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### bt.sppRelease

```python
bt.sppRelease()
```

Releases SPP resources.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### bt.sppConnect

```python
bt.sppConnect(addr)
```

Establishes an SPP connection.

**Parameter：**

- `addr`- Bytearray type. 6 bytes' Bluetooth address.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### bt.sppDisconnect

```python
bt.sppDisconnect()
```

Disconnects the SPP connection.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### bt.sppSend

```python
bt.sppSend(data)
```

Sends data through SPP.

**Parameter：**

- `data`- Bytearray type. The data to be sent.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

