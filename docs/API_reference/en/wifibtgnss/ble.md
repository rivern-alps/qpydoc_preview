# ble-Bluetooth Low Energy

The `ble` module  provides BLE GATT Server (slave) and BLE GATT Client (master) features based on the BLE 4.2 protocol.

**Example**：

```python
#BLE Server

import ble
import utime


BLE_GATT_SYS_SERVICE = 0  # 0-Removes the system default GAP and GATT services  1-Keeps the system default GAP and GATT services
BLE_SERVER_HANDLE = 0
_BLE_NAME = "Quectel_ble"


event_dict = {
    'BLE_START_STATUS_IND': 0,  # Start BLE
    'BLE_STOP_STATUS_IND': 1,   # Stop BLE
    'BLE_CONNECT_IND': 16,  # Connect BLE
    'BLE_DISCONNECT_IND': 17,   # Disconnect BLE
    'BLE_UPDATE_CONN_PARAM_IND': 18,    # BLE update connection parameter
    'BLE_SCAN_REPORT_IND': 19,  # BLE GATT client scan and report other devices
    'BLE_GATT_MTU': 20, # BLE connection mtu
    'BLE_GATT_RECV_WRITE_IND': 21, # When the BLE client writes a characteristic value or descriptor, the server gets the notice.
    'BLE_GATT_RECV_READ_IND': 22, # When the BLE client reads a characteristic value or descriptor, the server gets the notice.
    'BLE_GATT_RECV_NOTIFICATION_IND': 23,   # Client receives notification
    'BLE_GATT_RECV_INDICATION_IND': 24, # Client receives indication
    'BLE_GATT_SEND_END': 25, # Server sends notification, and receives notice sent by the peer end
}

class EVENT(dict):
    def __getattr__(self, item):
        return self[item]

    def __setattr__(self, key, value):
        raise ValueError("{} is read-only.".format(key))


event = EVENT(event_dict)


def ble_callback(args):
    global BLE_GATT_SYS_SERVICE
    global BLE_SERVER_HANDLE
    event_id = args[0]
    status = args[1]
    print('[ble_callback]: event_id={}, status={}'.format(event_id, status))

    if event_id == event.BLE_START_STATUS_IND:  # Start BLE
        if status == 0:
            print('[callback] BLE start success.')
            mac = ble.getPublicAddr()
            if mac != -1 and len(mac) == 6:
                addr = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(mac[5], mac[4], mac[3], mac[2], mac[1], mac[0])
                print('BLE public addr : {}'.format(addr))
            ret = ble_gatt_set_name()
            if ret != 0:
                ble_gatt_close()
                return
            ret = ble_gatt_set_param()
            if ret != 0:
                ble_gatt_close()
                return
            ret = ble_gatt_set_data()
            if ret != 0:
                ble_gatt_close()
                return
            ret = ble_gatt_set_rsp_data()
            if ret != 0:
                ble_gatt_close()
                return
            ret = ble_gatt_add_service()
            if ret != 0:
                ble_gatt_close()
                return
            ret = ble_gatt_add_characteristic()
            if ret != 0:
                ble_gatt_close()
                return
            ret = ble_gatt_add_characteristic_value()
            if ret != 0:
                ble_gatt_close()
                return
            ret = ble_gatt_add_characteristic_desc()
            if ret != 0:
                ble_gatt_close()
                return
            ret = ble_gatt_add_service_complete()
            if ret != 0:
                ble_gatt_close()
                return
            if BLE_GATT_SYS_SERVICE == 0:
                BLE_SERVER_HANDLE = 1
            else:
                BLE_SERVER_HANDLE = 16
            ret = ble_adv_start()
            if ret != 0:
                ble_gatt_close()
                return
        else:
            print('[callback] BLE start failed.')
    elif event_id == event.BLE_STOP_STATUS_IND:  # Stop BLE
        if status == 0:
            print('[callback] ble stop successful.')
            ble_status = ble.getStatus()
            print('ble status is {}'.format(ble_status))
            ble_gatt_server_release()
        else:
            print('[callback] ble stop failed.')
    elif event_id == event.BLE_CONNECT_IND:  # Connect BLE
        if status == 0:
            print('[callback] ble connect successful.')
            connect_id = args[2]
            addr = args[3]
            addr_str = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[0], addr[1], addr[2], addr[3], addr[4], addr[5])
            print('[callback] connect_id = {}, addr = {}'.format(connect_id, addr_str))

            ret = ble_gatt_send_notification()
            if ret == 0:
                print('[callback] ble_gatt_send_notification successful.')
            else:
                print('[callback] ble_gatt_send_notification failed.')
                ble_gatt_close()
                return
        else:
            print('[callback] ble connect failed.')
    elif event_id == event.BLE_DISCONNECT_IND:  # Disconnect BLE
        if status == 0:
            print('[callback] ble disconnect successful.')
            connect_id = args[2]
            addr = args[3]
            addr_str = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[0], addr[1], addr[2], addr[3], addr[4], addr[5])
            ble_gatt_close()
            print('[callback] connect_id = {}, addr = {}'.format(connect_id, addr_str))
        else:
            print('[callback] ble disconnect failed.')
            ble_gatt_close()
            return
    elif event_id == event.BLE_UPDATE_CONN_PARAM_IND:  # BLE update connection parameter
        if status == 0:
            print('[callback] ble update parameter successful.')
            connect_id = args[2]
            max_interval = args[3]
            min_interval = args[4]
            latency = args[5]
            timeout = args[6]
            print('[callback] connect_id={},max_interval={},min_interval={},latency={},timeout={}'.format(connect_id, max_interval, min_interval, latency, timeout))
        else:
            print('[callback] ble update parameter failed.')
            ble_gatt_close()
            return
    elif event_id == event.BLE_GATT_MTU:  # BLE connection MTU
        if status == 0:
            print('[callback] ble connect mtu successful.')
            handle = args[2]
            ble_mtu = args[3]
            print('[callback] handle = {:#06x}, ble_mtu = {}'.format(handle, ble_mtu))
        else:
            print('[callback] ble connect mtu failed.')
            ble_gatt_close()
            return
    elif event_id == event.BLE_GATT_RECV_WRITE_IND:
        if status == 0:
            print('[callback] ble recv successful.')
            data_len = args[2]
            data = args[3]  # a bytearray
            attr_handle = args[4]
            short_uuid = args[5]
            long_uuid = args[6]  # a bytearray
            print('len={}, data:{}'.format(data_len, data))
            print('attr_handle = {:#06x}'.format(attr_handle))
            print('short uuid = {:#06x}'.format(short_uuid))
            print('long uuid = {}'.format(long_uuid))
        else:
            print('[callback] ble recv failed.')
            ble_gatt_close()
            return
    elif event_id == event.BLE_GATT_RECV_READ_IND:
        if status == 0:
            print('[callback] ble recv read successful.')
            data_len = args[2]
            data = args[3]  # a bytearray
            attr_handle = args[4]
            short_uuid = args[5]
            long_uuid = args[6]  # a bytearray
            print('len={}, data:{}'.format(data_len, data))
            print('attr_handle = {:#06x}'.format(attr_handle))
            print('short uuid = {:#06x}'.format(short_uuid))
            print('long uuid = {}'.format(long_uuid))
        else:
            print('[callback] ble recv read failed.')
            ble_gatt_close()
            return
    elif event_id == event.BLE_GATT_SEND_END:
        if status == 0:
            print('[callback] ble send data successful.')
        else:
            print('[callback] ble send data failed.')
    else:
        print('unknown event id.')


def ble_gatt_server_init(cb):
    ret = ble.serverInit(cb)
    if ret != 0:
        print('ble_gatt_server_init failed.')
        return -1
    print('ble_gatt_server_init success.')
    return 0


def ble_gatt_server_release():
    ret = ble.serverRelease()
    if ret != 0:
        print('ble_gatt_server_release failed.')
        return -1
    print('ble_gatt_server_release success.')
    return 0


def ble_gatt_open():
    ret = ble.gattStart()
    if ret != 0:
        print('ble_gatt_open failed.')
        return -1
    print('ble_gatt_open success.')
    return 0


def ble_gatt_close():
    ret = ble.gattStop()
    if ret != 0:
        print('ble_gatt_close failed.')
        return -1
    print('ble_gatt_close success.')
    return 0


def ble_gatt_set_name():
    code = 0  # utf8
    name = _BLE_NAME
    ret = ble.setLocalName(code, name)
    if ret != 0:
        print('ble_gatt_set_name failed.')
        return -1
    print('ble_gatt_set_name success.')
    return 0


def ble_gatt_set_param():
    min_adv = 0x300
    max_adv = 0x320
    adv_type = 0  # Connectable undirected advertising (default)
    addr_type = 0  # Public address
    channel = 0x07
    filter_strategy = 0  # Allow scan request from any, allow connect request from any
    discov_mode = 2
    no_br_edr = 1
    enable_adv = 1
    ret = ble.setAdvParam(min_adv, max_adv, adv_type, addr_type, channel, filter_strategy, discov_mode, no_br_edr, enable_adv)
    if ret != 0:
        print('ble_gatt_set_param failed.')
        return -1
    print('ble_gatt_set_param success.')
    return 0


def ble_gatt_set_data():
    adv_data = [0x02, 0x01, 0x05]
    ble_name = _BLE_NAME
    length = len(ble_name) + 1
    adv_data.append(length)
    adv_data.append(0x09)
    name_encode = ble_name.encode('UTF-8')
    for i in range(0, len(name_encode)):
        adv_data.append(name_encode[i])
    print('set adv_data:{}'.format(adv_data))
    data = bytearray(adv_data)
    ret = ble.setAdvData(data)
    if ret != 0:
        print('ble_gatt_set_data failed.')
        return -1
    print('ble_gatt_set_data success.')
    return 0


def ble_gatt_set_rsp_data():
    adv_data = []
    ble_name = _BLE_NAME
    length = len(ble_name) + 1
    adv_data.append(length)
    adv_data.append(0x09)
    name_encode = ble_name.encode('UTF-8')
    for i in range(0, len(name_encode)):
        adv_data.append(name_encode[i])
    print('set adv_rsp_data:{}'.format(adv_data))
    data = bytearray(adv_data)
    ret = ble.setAdvRspData(data)
    if ret != 0:
        print('ble_gatt_set_rsp_data failed.')
        return -1
    print('ble_gatt_set_rsp_data success.')
    return 0


def ble_gatt_add_service():
    primary = 1
    server_id = 0x01
    uuid_type = 1  # Short UUID
    uuid_s = 0x180F
    uuid_l = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    ret = ble.addService(primary, server_id, uuid_type, uuid_s, uuid_l)
    if ret != 0:
        print('ble_gatt_add_service failed.')
        return -1
    print('ble_gatt_add_service success.')
    return 0


def ble_gatt_add_characteristic():
    server_id = 0x01
    chara_id = 0x01
    chara_prop = 0x02 | 0x10 | 0x20  # 0x02-Readable; 0x10-Notification; 0x20-Indication
    uuid_type = 1  # Short UUID
    uuid_s = 0x2A19
    uuid_l = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    ret = ble.addChara(server_id, chara_id, chara_prop, uuid_type, uuid_s, uuid_l)
    if ret != 0:
        print('ble_gatt_add_characteristic failed.')
        return -1
    print('ble_gatt_add_characteristic success.')
    return 0


def ble_gatt_add_characteristic_value():
    data = []
    server_id = 0x01
    chara_id = 0x01
    permission = 0x0001 | 0x0002
    uuid_type = 1  # short UUID
    uuid_s = 0x2A19
    uuid_l = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    for i in range(0, 244):
        data.append(0x00)
    value = bytearray(data)
    ret = ble.addCharaValue(server_id, chara_id, permission, uuid_type, uuid_s, uuid_l, value)
    if ret != 0:
        print('ble_gatt_add_characteristic_value failed.')
        return -1
    print('ble_gatt_add_characteristic_value success.')
    return 0


def ble_gatt_add_characteristic_desc():
    data = [0x00, 0x00]
    server_id = 0x01
    chara_id = 0x01
    permission = 0x0001 | 0x0002
    uuid_type = 1  # Short UUID
    uuid_s = 0x2902
    uuid_l = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    value = bytearray(data)
    ret = ble.addCharaDesc(server_id, chara_id, permission, uuid_type, uuid_s, uuid_l, value)
    if ret != 0:
        print('ble_gatt_add_characteristic_desc failed.')
        return -1
    print('ble_gatt_add_characteristic_desc success.')
    return 0


def ble_gatt_send_notification():
    global BLE_SERVER_HANDLE
    data = [0x39, 0x39, 0x39, 0x39, 0x39]  # Test data
    conn_id = 0
    attr_handle = BLE_SERVER_HANDLE + 2
    value = bytearray(data)
    ret = ble.sendNotification(conn_id, attr_handle, value)
    if ret != 0:
        print('ble_gatt_send_notification failed.')
        return -1
    print('ble_gatt_send_notification success.')
    return 0


def ble_gatt_add_service_complete():
    global BLE_GATT_SYS_SERVICE
    ret = ble.addOrClearService(1, BLE_GATT_SYS_SERVICE)
    if ret != 0:
        print('ble_gatt_add_service_complete failed.')
        return -1
    print('ble_gatt_add_service_complete success.')
    return 0


def ble_gatt_clear_service_complete():
    global BLE_GATT_SYS_SERVICE
    ret = ble.addOrClearService(0, BLE_GATT_SYS_SERVICE)
    if ret != 0:
        print('ble_gatt_clear_service_complete failed.')
        return -1
    print('ble_gatt_clear_service_complete success.')
    return 0


def ble_adv_start():
    ret = ble.advStart()
    if ret != 0:
        print('ble_adv_start failed.')
        return -1
    print('ble_adv_start success.')
    return 0


def ble_adv_stop():
    ret = ble.advStop()
    if ret != 0:
        print('ble_adv_stop failed.')
        return -1
    print('ble_adv_stop success.')
    return 0


def main():
    ret = ble_gatt_server_init(ble_callback)
    if ret == 0:
        ret = ble_gatt_open()
        if ret != 0:
            return -1
    else:
        return -1
    count = 0
    while True:
        utime.sleep(1)
        count += 1
        if count % 5 == 0:
            print('##### BLE running, count = {}......'.format(count))
        if count > 120:
            count = 0
            print('!!!!! stop BLE now !!!!!')
            ble_gatt_close()
            return 0


if __name__ == '__main__':
    main()

```

```python
#BLE Client

import ble
import utime
import _thread
import checkNet
from queue import Queue

PROJECT_NAME = "QuecPython_BLE_Client_Example"
PROJECT_VERSION = "1.0.0"
checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

event_dict = {
    'BLE_START_STATUS_IND': 0,  # Start BLE
    'BLE_STOP_STATUS_IND': 1,   # Stop BLE
    'BLE_CONNECT_IND': 16,  # Connect BLE
    'BLE_DISCONNECT_IND': 17,   # Disconnect BLE
    'BLE_UPDATE_CONN_PARAM_IND': 18,    # BLE update connection parameter
    'BLE_SCAN_REPORT_IND': 19,  # BLE GATT client scan and report other devices
    'BLE_GATT_MTU': 20, # BLE connection MTU
    'BLE_GATT_RECV_NOTIFICATION_IND': 23,   # Client receive notification
    'BLE_GATT_RECV_INDICATION_IND': 24, # Client receive indication
    'BLE_GATT_START_DISCOVER_SERVICE_IND': 26,  # Start discover service
    'BLE_GATT_DISCOVER_SERVICE_IND': 27,    # Discover service
    'BLE_GATT_DISCOVER_CHARACTERISTIC_DATA_IND': 28,    # Discover characteristic
    'BLE_GATT_DISCOVER_CHARA_DESC_IND': 29, # Discover characteristic descriptor
    'BLE_GATT_CHARA_WRITE_WITH_RSP_IND': 30,   # Write characteristic value with response
    'BLE_GATT_CHARA_WRITE_WITHOUT_RSP_IND': 31, # Write characteristic value without response
    'BLE_GATT_CHARA_READ_IND': 32,  # Read characteristic value by handle
    'BLE_GATT_CHARA_READ_BY_UUID_IND': 33,  # Read characteristic value by UUID
    'BLE_GATT_CHARA_MULTI_READ_IND': 34,    # Read multiple characteristic value
    'BLE_GATT_DESC_WRITE_WITH_RSP_IND': 35, # Write characteristic descriptor
    'BLE_GATT_DESC_READ_IND': 36,   # Read characteristic descriptor
    'BLE_GATT_ATT_ERROR_IND': 37,   # Attribute error
}

gatt_status_dict = {
    'BLE_GATT_IDLE' : 0,
    'BLE_GATT_DISCOVER_SERVICE': 1,
    'BLE_GATT_DISCOVER_INCLUDES': 2,
    'BLE_GATT_DISCOVER_CHARACTERISTIC': 3,
    'BLE_GATT_WRITE_CHARA_VALUE': 4,
    'BLE_GATT_WRITE_CHARA_DESC': 5,
    'BLE_GATT_READ_CHARA_VALUE': 6,
    'BLE_GATT_READ_CHARA_DESC': 7,
}

class EVENT(dict):
    def __getattr__(self, item):
        return self[item]

    def __setattr__(self, key, value):
        raise ValueError("{} is read-only.".format(key))


class BleClient(object):
    def __init__(self):
        self.ble_server_name = 'Quectel_ble' #The BLE name of the target device
        self.connect_id = 0
        self.connect_addr = 0
        self.gatt_statue = 0
        self.discover_service_mode = 0 # 0-discover all service, 1-discover service by uuid

        self.scan_param = {
            'scan_mode' : 1, # Active scanning
            'interval' : 0x100,
            'scan_window' : 0x50,
            'filter_policy' : 0,
            'local_addr_type' : 0,
        }

        self.scan_report_info = {
            'event_type' : 0,
            'name' : '',
            'addr_type' : 0,
            'addr' : 0, # 0 indicates invalid value when initializing. The value is in bytearray
            'rssi' : 0,
            'data_len' : 0,
            'raw_data' : 0,
        }

        self.target_service = {
            'start_handle' : 0,
            'end_handle' : 0,
            'uuid_type' : 1, # Short UUID
            'short_uuid' : 0x180F, # Battery power service
            'long_uuid' : bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
        }

        self.characteristic_list = []
        self.descriptor_list = []
        self.characteristic_count = 0   # ql_ble_gatt_chara_count
        self.chara_descriptor_count = 0 # ql_ble_gatt_chara_desc_count
        self.characteristic_index = 0   # ql_ble_gatt_chara_desc_index
        self.current_chara_index = 0    # ql_ble_gatt_cur_chara
        self.current_desc_index = 0     # ql_ble_gatt_chara_cur_desc
        self.ble_short_uuid_pair_len = 7
        self.ble_long_uuid_pair_len = 21

        ret = ble.clientInit(self.ble_client_callback)
        if ret != 0:
            print('ble client initialize failed.')
            raise ValueError("BLE Client Init failed.")
        else:
            print('ble client initialize successful.')
        print('')

    @staticmethod
    def gatt_open():
        ret = ble.gattStart()
        if ret != 0:
            print('ble open failed.')
        else:
            print('ble open successful.')
        print('')
        return ret

    @staticmethod
    def gatt_close():
        ret = ble.gattStop()
        if ret != 0:
            print('ble close failed.')
        else:
            print('ble close successful.')
        print('')
        return ret

    @staticmethod
    def gatt_get_status():
        return ble.getStatus()

    @staticmethod
    def release():
        ret = ble.clientRelease()
        if ret != 0:
            print('ble client release failed.')
        else:
            print('ble client release successful.')
        print('')
        return ret

    def set_scan_param(self):
        scan_mode = self.scan_param['scan_mode']
        interval = self.scan_param['interval']
        scan_time = self.scan_param['scan_window']
        filter_policy = self.scan_param['filter_policy']
        local_addr_type = self.scan_param['local_addr_type']
        ret = ble.setScanParam(scan_mode, interval, scan_time, filter_policy, local_addr_type)
        if ret != 0:
            print('ble client set scan-parameters failed.')
        else:
            print('ble client set scan-parameters successful.')
        print('')
        return ret

    @staticmethod
    def start_scan():
        ret = ble.scanStart()
        if ret != 0:
            print('ble client scan failed.')
        else:
            print('ble client scan successful.')
        print('')
        return ret

    @staticmethod
    def stop_scan():
        ret = ble.scanStop()
        if ret != 0:
            print('ble client failed to stop scanning.')
        else:
            print('ble client scan stopped successfully.')
        print('')
        return ret

    def connect(self):
        print('start to connect.....')
        addr_type = self.scan_report_info['addr_type']
        addr = self.scan_report_info['addr']
        if addr != 0 and len(addr) == 6:
            addr_str = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[0], addr[1], addr[2], addr[3], addr[4], addr[5])
            print('addr_type : {}, addr : {}'.format(addr_type, addr_str))
            ret = ble.connect(addr_type, addr)
            if ret != 0:
                print('ble client connect failed.')
            else:
                print('ble client connect successful.')
            print('')
            return ret

    def cancel_connect(self):
        ret = ble.cancelConnect(self.scan_report_info['addr'])
        if ret != 0:
            print('ble client cancel connect failed.')
        else:
            print('ble client cancel connect successful.')
        print('')
        return ret

    def disconnect(self):
        ret = ble.disconnect(self.connect_id)
        if ret != 0:
            print('ble client disconnect failed.')
        else:
            print('ble client disconnect successful.')
        print('')
        return ret

    def discover_all_service(self):
        ret = ble.discoverAllService(self.connect_id)
        if ret != 0:
            print('ble client discover all service failed.')
        else:
            print('ble client discover all service successful.')
        print('')
        return ret

    def discover_service_by_uuid(self):
        connect_id = self.connect_id
        uuid_type = self.target_service['uuid_type']
        short_uuid = self.target_service['short_uuid']
        long_uuid = self.target_service['long_uuid']
        ret = ble.discoverByUUID(connect_id, uuid_type, short_uuid, long_uuid)
        if ret != 0:
            print('ble client discover service by uuid failed.')
        else:
            print('ble client discover service by uuid successful.')
        print('')
        return ret

    def discover_all_includes(self):
        connect_id = self.connect_id
        start_handle = self.target_service['start_handle']
        end_handle = self.target_service['end_handle']
        ret = ble.discoverAllIncludes(connect_id, start_handle, end_handle)
        if ret != 0:
            print('ble client discover all includes failed.')
        else:
            print('ble client discover all includes successful.')
        print('')
        return ret

    def discover_all_characteristic(self):
        connect_id = self.connect_id
        start_handle = self.target_service['start_handle']
        end_handle = self.target_service['end_handle']
        ret = ble.discoverAllChara(connect_id, start_handle, end_handle)
        if ret != 0:
            print('ble client discover all characteristic failed.')
        else:
            print('ble client discover all characteristic successful.')
        print('')
        return ret

    def discover_all_characteristic_descriptor(self):
        connect_id = self.connect_id
        index = self.characteristic_index
        start_handle = self.characteristic_list[index]['value_handle'] + 1

        if self.characteristic_index == (self.characteristic_count - 1):
            end_handle = self.target_service['end_handle']
            print('[1]start_handle = {:#06x}, end_handle = {:#06x}'.format(start_handle - 1, end_handle))
            ret = ble.discoverAllCharaDesc(connect_id, start_handle, end_handle)
        else:
            end_handle = self.characteristic_list[index+1]['handle'] - 1
            print('[2]start_handle = {:#06x}, end_handle = {:#06x}'.format(start_handle - 1, end_handle))
            ret = ble.discoverAllCharaDesc(connect_id, start_handle, end_handle)
        self.characteristic_index += 1
        if ret != 0:
            print('ble client discover all characteristic descriptor failed.')
        else:
            print('ble client discover all characteristic descriptor successful.')
        print('')
        return ret

    def read_characteristic_by_uuid(self):
        connect_id = self.connect_id
        index = self.current_chara_index   # Modify the value according to actual needs
        start_handle = self.characteristic_list[index]['handle']
        end_handle = self.characteristic_list[index]['value_handle']
        uuid_type = 1
        short_uuid = self.characteristic_list[index]['short_uuid']
        long_uuid = bytearray([0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00])

        ret = ble.readCharaByUUID(connect_id, start_handle, end_handle, uuid_type, short_uuid, long_uuid)
        if ret != 0:
            print('ble client read characteristic by uuid failed.')
        else:
            print('ble client read characteristic by uuid successful.')
        print('')
        return ret

    def read_characteristic_by_handle(self):
        connect_id = self.connect_id
        index = self.current_chara_index  # Modify the value according to actual needs
        handle = self.characteristic_list[index]['value_handle']
        offset = 0
        is_long = 0

        ret = ble.readCharaByHandle(connect_id, handle, offset, is_long)
        if ret != 0:
            print('ble client read characteristic by handle failed.')
        else:
            print('ble client read characteristic by handle successful.')
        print('')
        return ret

    def read_characteristic_descriptor(self):
        connect_id = self.connect_id
        index = self.current_desc_index  # Modify the value according to actual needs
        handle = self.descriptor_list[index]['handle']
        print('handle = {:#06x}'.format(handle))
        is_long = 0
        ret = ble.readCharaDesc(connect_id, handle, is_long)
        if ret != 0:
            print('ble client read characteristic descriptor failed.')
        else:
            print('ble client read characteristic descriptor successful.')
        print('')
        return ret

    def write_characteristic(self):
        connect_id = self.connect_id
        index = self.current_chara_index  # Modify the value according to actual needs
        handle = self.characteristic_list[index]['value_handle']
        offset = 0
        is_long = 0
        data = bytearray([0x40, 0x00])
        print('value_handle = {:#06x}, uuid = {:#06x}'.format(handle, self.characteristic_list[index]['short_uuid']))
        ret = ble.writeChara(connect_id, handle, offset, is_long, data)
        if ret != 0:
            print('ble client write characteristic failed.')
        else:
            print('ble client read characteristic successful.')
        print('')
        return ret

    def write_characteristic_no_rsp(self):
        connect_id = self.connect_id
        index = self.current_chara_index  # Modify the value according to actual needs
        handle = self.characteristic_list[index]['value_handle']
        data = bytearray([0x20, 0x00])
        print('value_handle = {:#06x}, uuid = {:#06x}'.format(handle, self.characteristic_list[index]['short_uuid']))
        ret = ble.writeCharaNoRsp(connect_id, handle, data)
        if ret != 0:
            print('ble client write characteristic no rsp failed.')
        else:
            print('ble client read characteristic no rsp successful.')
        print('')
        return ret

    def write_characteristic_descriptor(self):
        connect_id = self.connect_id
        index = self.current_desc_index  # Modify the value according to actual needs
        handle = self.descriptor_list[index]['handle']
        data = bytearray([0x01, 0x02])
        print('handle = {:#06x}'.format(handle))

        ret = ble.writeCharaDesc(connect_id, handle, data)
        if ret != 0:
            print('ble client write characteristic descriptor failed.')
        else:
            print('ble client read characteristic descriptor successful.')
        print('')
        return ret

    @staticmethod
    def ble_client_callback(args):
        global msg_queue
        msg_queue.put(args)


def ble_gatt_client_event_handler():
    global msg_queue
    old_time = 0

    while True:
        cur_time = utime.localtime()
        timestamp = "{:02d}:{:02d}:{:02d}".format(cur_time[3], cur_time[4], cur_time[5])
        if cur_time[5] != old_time and cur_time[5] % 5 == 0:
            old_time = cur_time[5]
            print('[{}]event handler running.....'.format(timestamp))
            print('')
        msg = msg_queue.get()  # It will be blocked here when there is no message. 
        # print('msg : {}'.format(msg))
        event_id = msg[0]
        status = msg[1]

        if event_id == event.BLE_START_STATUS_IND:
            print('')
            print('event_id : BLE_START_STATUS_IND, status = {}'.format(status))
            if status == 0:
                print('BLE start successful.')
                ble_status = ble_client.gatt_get_status()
                if ble_status == 0:
                    print('BLE Status : stopped.')
                    break
                elif ble_status == 1:
                    print('BLE Status : started.')
                else:
                    print('get ble status error.')
                    ble_client.gatt_close()
                    break

                ret = ble_client.set_scan_param()
                if ret != 0:
                    ble_client.gatt_close()
                    break
                ret = ble_client.start_scan()
                if ret != 0:
                    ble_client.gatt_close()
                    break
            else:
                print('BLE start failed.')
                break
        elif event_id == event.BLE_STOP_STATUS_IND:
            print('')
            print('event_id : BLE_STOP_STATUS_IND, status = {}'.format(status))
            if status == 0:
                print('ble stop successful.')
            else:
                print('ble stop failed.')
                break
        elif event_id == event.BLE_CONNECT_IND:
            print('')
            print('event_id : BLE_CONNECT_IND, status = {}'.format(status))
            if status == 0:
                ble_client.connect_id = msg[2]
                ble_client.connect_addr = msg[3]
                addr = ble_client.connect_addr
                addr_str = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[0], addr[1], addr[2], addr[3], addr[4], addr[5])
                print('connect_id : {:#x}, connect_addr : {}'.format(ble_client.connect_id, addr_str))
            else:
                print('ble connect failed.')
                break
        elif event_id == event.BLE_DISCONNECT_IND:
            print('')
            print('event_id : BLE_DISCONNECT_IND, status = {}'.format(status))
            if status == 0:
                ble_client.connect_id = msg[2]
                ble_client.connect_addr = msg[3]
                addr = ble_client.connect_addr
                addr_str = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[0], addr[1], addr[2], addr[3], addr[4], addr[5])
                print('connect_id : {:#x}, connect_addr : {}'.format(ble_client.connect_id, addr_str))
            else:
                print('ble disconnect failed.')
            ble_client.gatt_close()
            break
        elif event_id == event.BLE_UPDATE_CONN_PARAM_IND:
            print('')
            print('event_id : BLE_UPDATE_CONN_PARAM_IND, status = {}'.format(status))
            if status == 0:
                connect_id = msg[2]
                max_interval = msg[3]
                min_interval = msg[4]
                latency = msg[5]
                timeout = msg[6]
                print('connect_id={},max_interval={},min_interval={},latency={},timeout={}'.format(connect_id,max_interval,min_interval,latency,timeout))
            else:
                print('ble update parameter failed.')
                ble_client.gatt_close()
                break
        elif event_id == event.BLE_SCAN_REPORT_IND:
            if status == 0:
                # print(' ble scan successful.')

                ble_client.scan_report_info['event_type'] = msg[2]
                ble_client.scan_report_info['name'] = msg[3]
                ble_client.scan_report_info['addr_type'] = msg[4]
                ble_client.scan_report_info['addr'] = msg[5]
                ble_client.scan_report_info['rssi'] = msg[6]
                ble_client.scan_report_info['data_len'] = msg[7]
                ble_client.scan_report_info['raw_data'] = msg[8]

                device_name = ble_client.scan_report_info['name']
                addr = ble_client.scan_report_info['addr']
                rssi = ble_client.scan_report_info['rssi']
                addr_type = ble_client.scan_report_info['addr_type']
                addr_str = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[0], addr[1], addr[2], addr[3], addr[4], addr[5])
                if device_name != '' and rssi != 0:
                    print('name: {}, addr: {}, rssi: {}, addr_type: {}'.format(device_name, addr_str, rssi, addr_type))
                    print('raw_data: {}'.format(ble_client.scan_report_info['raw_data']))

                if device_name == ble_client.ble_server_name: # Stop scanning once the target device is discovered
                    ret = ble_client.stop_scan()
                    if ret != 0:
                        ble_client.gatt_close()
                        break

                    ret = ble_client.connect()
                    if ret != 0:
                        ble_client.gatt_close()
                        break
            else:
                print('ble scan failed.')
                ret = ble_client.stop_scan()
                if ret != 0:
                    ble_client.gatt_close()
                    break
        elif event_id == event.BLE_GATT_MTU:
            print('')
            print('event_id : BLE_GATT_MTU, status = {}'.format(status))
            if status == 0:
                handle = msg[2]
                ble_mtu = msg[3]
                print('handle = {:#06x}, ble_mtu = {}'.format(handle, ble_mtu))
            else:
                print('ble connect mtu failed.')
                ble_client.gatt_close()
                break
        elif event_id == event.BLE_GATT_RECV_NOTIFICATION_IND:
            print('')
            print('event_id : BLE_GATT_RECV_NOTIFICATION_IND, status = {}'.format(status))
            if status == 0:
                data_len = msg[2]
                data = msg[3]
                print('len={}, data:{}'.format(data_len, data))
                handle = (data[1] << 8) | data[0]
                print('handle = {:#06x}'.format(handle))
            else:
                print('ble receive notification failed.')
                break
        elif event_id == event.BLE_GATT_RECV_INDICATION_IND:
            print('')
            print('event_id : BLE_GATT_RECV_INDICATION_IND, status = {}'.format(status))
            if status == 0:
                data_len = msg[2]
                data = msg[3]
                print('len={}, data:{}'.format(data_len, data))
            else:
                print('ble receive indication failed.')
                break
        elif event_id == event.BLE_GATT_START_DISCOVER_SERVICE_IND:
            print('')
            print('event_id : BLE_GATT_START_DISCOVER_SERVICE_IND, status = {}'.format(status))
            if status == 0:
                ble_client.characteristic_count = 0
                ble_client.chara_descriptor_count = 0
                ble_client.characteristic_index = 0
                ble_client.gatt_statue = gatt_status.BLE_GATT_DISCOVER_SERVICE

                if ble_client.discover_service_mode == 0:
                    print('execute the function discover_all_service.')
                    ret = ble_client.discover_all_service()
                else:
                    print('execute the function discover_service_by_uuid.')
                    ret = ble_client.discover_service_by_uuid()
                if ret != 0:
                    print('Execution result: Failed.')
                    ble_client.gatt_close()
                    break
            else:
                print('ble start discover service failed.')
                ble_client.gatt_close()
                break
        elif event_id == event.BLE_GATT_DISCOVER_SERVICE_IND:
            print('')
            print('event_id : BLE_GATT_DISCOVER_SERVICE_IND, status = {}'.format(status))
            if status == 0:
                start_handle = msg[2]
                end_handle = msg[3]
                short_uuid = msg[4]
                print('start_handle = {:#06x}, end_handle = {:#06x}, short_uuid = {:#06x}'.format(start_handle, end_handle, short_uuid))
                if ble_client.discover_service_mode == 0: # discover service all
                    if ble_client.target_service['short_uuid'] == short_uuid: # Finds the characteristic value by the specified UUID after finding all services
                        ble_client.target_service['start_handle'] = start_handle
                        ble_client.target_service['end_handle'] = end_handle
                        ble_client.gatt_statue = gatt_status.BLE_GATT_DISCOVER_CHARACTERISTIC
                        print('execute the function discover_all_characteristic.')
                        ret = ble_client.discover_all_characteristic()
                        if ret != 0:
                            print('Execution result: Failed.')
                            ble_client.gatt_close()
                            break
                else:
                    ble_client.target_service['start_handle'] = start_handle
                    ble_client.target_service['end_handle'] = end_handle
                    ble_client.gatt_statue = gatt_status.BLE_GATT_DISCOVER_CHARACTERISTIC
                    print('execute the function discover_all_characteristic.')
                    ret = ble_client.discover_all_characteristic()
                    if ret != 0:
                        print('Execution result: Failed.')
                        ble_client.gatt_close()
                        break
            else:
                print('ble discover service failed.')
                ble_client.gatt_close()
                break
        elif event_id == event.BLE_GATT_DISCOVER_CHARACTERISTIC_DATA_IND:
            print('')
            print('event_id : BLE_GATT_DISCOVER_CHARACTERISTIC_DATA_IND, status = {}'.format(status))
            if status == 0:
                data_len = msg[2]
                data = msg[3]
                pair_len = data[0]
                print('pair_len={}, len={}, data:{}'.format(pair_len, data_len, data))
                if data_len > 0:
                    if ble_client.gatt_statue == gatt_status.BLE_GATT_DISCOVER_CHARACTERISTIC:
                        i = 0
                        while i < (data_len - 1) / pair_len:
                            chara_dict = {
                                'handle': (data[i * pair_len + 2] << 8) | data[i * pair_len + 1],
                                'properties': data[i * pair_len + 3],
                                'value_handle': (data[i * pair_len + 5] << 8) | data[i * pair_len + 4],
                                'uuid_type': 0,
                                'short_uuid': 0x0000,
                                'long_uuid': bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
                            }
                            print('handle={:#06x}, properties={:#x}, value_handle={:#06x}'.format(chara_dict['handle'], chara_dict['properties'], chara_dict['value_handle']))
                            if pair_len == ble_client.ble_short_uuid_pair_len:
                                chara_dict['uuid_type'] = 1
                                chara_dict['short_uuid'] = (data[i * pair_len + 7] << 8) | data[i * pair_len + 6]
                                print('short_uuid:{:#06x}'.format(chara_dict['short_uuid']))
                            elif pair_len == ble_client.ble_long_uuid_pair_len:
                                start_index = i * pair_len + 6
                                end_index = start_index + 16
                                chara_dict['uuid_type'] = 0
                                chara_dict['long_uuid'] = data[start_index : end_index]
                                print('long_uuid:{}'.format(chara_dict['long_uuid']))
                            i += 1
                            if ble_client.characteristic_count < 5:
                                ble_client.characteristic_list.append(chara_dict)
                                ble_client.characteristic_count = len(ble_client.characteristic_list)
                            print('characteristic_list len = {}'.format(ble_client.characteristic_count))
                    elif ble_client.gatt_statue == gatt_status.BLE_GATT_READ_CHARA_VALUE:
                        print('data_len = {}'.format(data_len))
                        print('pay_load = {:02x},{:02x},{:02x},{:02x}'.format(data[0], data[1], data[2], data[3]))
            else:
                print('ble discover characteristic failed.')
                ble_client.gatt_close()
                break
        elif event_id == event.BLE_GATT_DISCOVER_CHARA_DESC_IND:
            print('')
            print('event_id : BLE_GATT_DISCOVER_CHARA_DESC_IND, status = {}'.format(status))
            if status == 0:
                data_len = msg[2]
                data = msg[3]
                fmt = data[0]
                print('fmt={}, len={}, data:{}'.format(fmt, data_len, data))
                if data_len > 0:
                    i = 0
                    if fmt == 1:  # 16 bit uuid
                        while i < (data_len - 1) / 4:
                            descriptor_dict = {
                                'handle': (data[i * 4 + 2] << 8) | data[i * 4 + 1],
                                'short_uuid': (data[i * 4 + 4] << 8) | data[i * 4 + 3],
                            }
                            print('handle={:#06x}, uuid={:#06x}'.format(descriptor_dict['handle'], descriptor_dict['short_uuid']))
                            i += 1
                            if ble_client.chara_descriptor_count < 5:
                                ble_client.descriptor_list.append(descriptor_dict)
                                ble_client.chara_descriptor_count = len(ble_client.descriptor_list)
                            print('descriptor_list len = {}'.format(ble_client.chara_descriptor_count))
                if ble_client.characteristic_index == ble_client.characteristic_count:
                    print('execute the function read_characteristic_by_uuid.')
                    # ble_client.gatt_statue = gatt_status.BLE_GATT_WRITE_CHARA_VALUE
                    # ret = ble_client.write_characteristic()
                    # ret = ble_client.write_characteristic_no_rsp()

                    ble_client.gatt_statue = gatt_status.BLE_GATT_READ_CHARA_VALUE
                    ret = ble_client.read_characteristic_by_uuid()
                    # ret = ble_client.read_characteristic_by_handle()

                    # ble_client.gatt_statue = gatt_status.BLE_GATT_READ_CHARA_DESC
                    # ret = ble_client.read_characteristic_descriptor()

                    # ble_client.gatt_statue = gatt_status.BLE_GATT_WRITE_CHARA_DESC
                    # ret = ble_client.write_characteristic_descriptor()
                else:
                    print('execute the function discover_all_characteristic_descriptor.')
                    ret = ble_client.discover_all_characteristic_descriptor()
                if ret != 0:
                    print('Execution result: Failed.')
                    ble_client.gatt_close()
                    break
            else:
                print('ble discover characteristic descriptor failed.')
                ble_client.gatt_close()
                break
        elif event_id == event.BLE_GATT_CHARA_WRITE_WITH_RSP_IND:
            print('')
            print('event_id : BLE_GATT_CHARA_WRITE_WITH_RSP_IND, status = {}'.format(status))
            if status == 0:
                if ble_client.gatt_statue == gatt_status.BLE_GATT_WRITE_CHARA_VALUE:
                    pass
                elif ble_client.gatt_statue == gatt_status.BLE_GATT_WRITE_CHARA_DESC:
                    pass
            else:
                print('ble write characteristic with response failed.')
                break
        elif event_id == event.BLE_GATT_CHARA_WRITE_WITHOUT_RSP_IND:
            print('')
            print('event_id : BLE_GATT_CHARA_WRITE_WITHOUT_RSP_IND, status = {}'.format(status))
            if status == 0:
                print('write characteristic value without response successful.')
            else:
                print('write characteristic value without response failed.')
                break
        elif event_id == event.BLE_GATT_CHARA_READ_IND:
            print('')
            # read characteristic value by handle
            print('event_id : BLE_GATT_CHARA_READ_IND, status = {}'.format(status))
            if status == 0:
                data_len = msg[2]
                data = msg[3]
                print('data_len = {}, data : {}'.format(data_len, data))
                if ble_client.gatt_statue == gatt_status.BLE_GATT_READ_CHARA_VALUE:
                    # print('read characteristic value by handle.')
                    pass
            else:
                print('ble read characteristic failed.')
                break
        elif event_id == event.BLE_GATT_CHARA_READ_BY_UUID_IND:
            print('')
            # read characteristic value by uuid
            print('event_id : BLE_GATT_CHARA_READ_BY_UUID_IND, status = {}'.format(status))
            if status == 0:
                data_len = msg[2]
                data = msg[3]
                print('data_len = {}, data : {}'.format(data_len, data))
                handle = (data[2] << 8) | data[1]
                print('handle = {:#06x}'.format(handle))
            else:
                print('ble read characteristic by uuid failed.')
                break
        elif event_id == event.BLE_GATT_CHARA_MULTI_READ_IND:
            print('')
            # read multiple characteristic value
            print('event_id : BLE_GATT_CHARA_MULTI_READ_IND, status = {}'.format(status))
            if status == 0:
                data_len = msg[2]
                data = msg[3]
                print('data_len = {}, data : {}'.format(data_len, data))
            else:
                print('ble read multiple characteristic by uuid failed.')
                break
        elif event_id == event.BLE_GATT_DESC_WRITE_WITH_RSP_IND:
            print('')
            print('event_id : BLE_GATT_DESC_WRITE_WITH_RSP_IND, status = {}'.format(status))
            if status == 0:
                if ble_client.gatt_statue == gatt_status.BLE_GATT_WRITE_CHARA_VALUE:
                    pass
                elif ble_client.gatt_statue == gatt_status.BLE_GATT_WRITE_CHARA_DESC:
                    pass
            else:
                print('ble write characteristic descriptor failed.')
                break
        elif event_id == event.BLE_GATT_DESC_READ_IND:
            print('')
            # read characteristic descriptor
            print('event_id : BLE_GATT_DESC_READ_IND, status = {}'.format(status))
            if status == 0:
                data_len = msg[2]
                data = msg[3]
                print('data_len = {}, data : {}'.format(data_len, data))
                if ble_client.gatt_statue == gatt_status.BLE_GATT_READ_CHARA_DESC:
                    # print('read characteristic descriptor.')
                    pass
            else:
                print('ble read characteristic descriptor failed.')
                break
        elif event_id == event.BLE_GATT_ATT_ERROR_IND:
            print('')
            print('event_id : BLE_GATT_ATT_ERROR_IND, status = {}'.format(status))
            if status == 0:
                errcode = msg[2]
                print('errcode = {:#06x}'.format(errcode))
                if ble_client.gatt_statue == gatt_status.BLE_GATT_DISCOVER_INCLUDES:
                    ble_client.gatt_statue = gatt_status.BLE_GATT_DISCOVER_CHARACTERISTIC
                    print('execute the function discover_all_characteristic.')
                    ret = ble_client.discover_all_characteristic()
                    if ret != 0:
                        print('Execution result: Failed.')
                        ble_client.gatt_close()
                        break
                elif ble_client.gatt_statue == gatt_status.BLE_GATT_DISCOVER_CHARACTERISTIC:
                    ble_client.gatt_statue = gatt_status.BLE_GATT_IDLE
                    print('execute the function discover_all_characteristic_descriptor.')
                    ret = ble_client.discover_all_characteristic_descriptor()
                    if ret != 0:
                        print('Execution result: Failed.')
                        ble_client.gatt_close()
                        break
            else:
                print('ble attribute error.')
                ble_client.gatt_close()
                break
        else:
            print('unknown event id : {}.'.format(event_id))

    # ble_client.release()


event = EVENT(event_dict)
gatt_status = EVENT(gatt_status_dict)
msg_queue = Queue(50)
ble_client = BleClient()


def main():
    checknet.poweron_print_once()
    print('create client event handler task.')
    _thread.start_new_thread(ble_gatt_client_event_handler, ())
    # ble.setScanFilter(0) # Disables scan filter feature.
    ret = ble_client.gatt_open()
    if ret != 0:
        return -1

    count = 0
    while True:
        utime.sleep(1)
        count += 1
        cur_time = utime.localtime()
        timestamp = "{:02d}:{:02d}:{:02d}".format(cur_time[3], cur_time[4], cur_time[5])
        if count % 5 == 0:
            print('[{}] BLE Client running, count = {}......'.format(timestamp, count))
            print('')
        if count > 130: # The count is set here for the program to exit itself after running for a while, which is convenient for testing and is actually processed according your actual needs
            count = 0
            print('!!!!! stop BLE Client now !!!!!')
            ble_status = ble_client.gatt_get_status()
            if ble_status == 1:
                ble_client.gatt_close()
            ble_client.release()
            break
        else:
            ble_status = ble_client.gatt_get_status()
            if ble_status == 0: # stopped
                print('BLE connection has been disconnected.')
                ble_client.release()
                break

if __name__ == '__main__':
    main()

```

**Note**：

Currently, only EC200U/EC600U/EG915U/EG912U series module supports `ble` feature.

## Initialization Related Features

### ble.gattStart

```python
ble.gattStart()
```

Enables BLE GATT feature.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### ble.gattStop

```python
ble.gattStop()
```

Disables BLE GATT feature.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### ble.getStatus

```python
ble.getStatus()
```

Gets the BLE status.

**Return Value：**

- `0` - Disabled;  `1` - Enabled ;  `-1` -  Failed to get the status.

### ble.getPublicAddr

```python
ble.getPublicAddr()
```

Gets the public address used by the BLE protocol stack. This interface can only be called after BLE has been initialized and started successfully. For example, you can call the interface after the event of event_id being 0  (indicating a successful start)  is triggered in the callback.

**Return Value：**

- Returns a bytearray type BLE address (size: 6 bytes) for successful execution and returns `-1` for failed execution.

**Example**：

```python
>>> addr = ble.getPublicAddr()
>>> print(addr)
b'\xdb3\xf5\x1ek\xac'
>>> mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
>>> print('mac = [{}]'.format(mac))
mac = [ac:6b:1e:f5:33:db]
```

**Note**：

If there is a default Bluetooth MAC address set at the factory, the MAC address got by this interface will be the same as the default Bluetooth MAC address. If there is no default setting, the address got by this interface will be a randomly generated static address after the Bluetooth is enabled. Thus, the address will not be the same every time the Bluetooth feature is enabled after the module is rebooted.

## BLE Server Related Features

### ble.serverInit

```python
ble.serverInit(user_cb)
```

Initializes BLE Server and registers a callback function.

**Parameter：**

- `user_cb` - Function type. Callback function. The meaning of the callback function parameters: `args[0]` is fixed to represent event_id; `args[1]` is fixed to represent the status, `0` indicating successful execution and non-`0` indicating failed execution. The number of callback function parameters is not fixed at two, but depends on the first parameter `args[0]`. The following table lists the number of parameters and explanations for different event IDs.

| event_id | Parameter Number | Description                                                  |
| :------: | :--------------: | ------------------------------------------------------------ |
|    0     |        2         | args[0]: event_id. Starts BT/BLE.<br>args[1]: status. The operation status. 0 - successful operation; other values - failed operation. |
|    1     |        2         | args[0]: event_id. Stops BT/BLE.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation. |
|    16    |        4         | args[0]: event_id. Connects BLE.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: connect_id.<br/>args[3]: addr. BT/BLE address in bytearray type. |
|    17    |        4         | args[0]: event_id. Disconnects BLE.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: connect_id.<br/>args[3]: addr. BT/BLE address in bytearray type. |
|    18    |        7         | args[0]: event_id. BLE update connection parameter.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: connect_id.<br/>args[3]: max_interval. Maximum interval. Interval: 1.25 ms. Range: 6–3200. Time range: 7.5 ms–4 s.<br/>args[4]: min_interval. Minimum interval. Interval: 1.25 ms. Range: 6–3200. Time range: 7.5 ms–4 s.<br/>args[5]: latency. The time at which the slave ignored the connection status event. It should meet the following condition:（1+latecy)\*max_interval\*2\*1.25<timeout\*10<br/>args[6]: timeout. Disconnect if there is no interaction during the timeout. Interval: 10 ms，Range: 10–3200 ms. Time range: 100 ms–32 s. |
|    20    |        4         | args[0]: event_id. BLE connection MTU.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: handle.<br/>args[3]: MTU value. |
|    21    |        7         | args[0]: event_id. BLE server. When the BLE client writes a characteristic value or descriptor, the server gets the notice. <br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: data_len. The length of the data to be got.<br/>args[3]: data. An array that stores the data got.<br/>args[4]: attr_handle. Integer type. Attribute handle.<br/>args[5]: short_uuid. Integer type.<br/>args[6]: long_uuid. A 16-byte array that stores long UUID. |
|    22    |        7         | args[0]: event_id. When the BLE client reads a characteristic value or descriptor, the server gets the notice.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: data_len. The length of the data to be got.<br/>args[3]: data. An array that stores the got data.<br/>args[4]: attr_handle. Integer type, attribute handle.<br/>args[5]: short_uuid. Integer type.<br/>args[6]: long_uuid. A 16-byte array that stores long UUID. |
|    25    |        2         | args[0]: event_id. Server sends notification, and receives notice sent by the peer end.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation. |

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

**Example**：

```python
def ble_callback(args):
    event_id = args[0]
    status = args[1]
    print('[ble_callback]: event_id={}, status={}'.format(event_id, status))

    if event_id == 0:  # Start BLE
        if status == 0:
            print('[callback] BLE start success.')
        else:
            print('[callback] BLE start failed.')
    elif event_id == 1:  # Stop BLE
        if status == 0:
            print('[callback] ble stop successful.')
        else:
            print('[callback] ble stop failed.')
    elif event_id == 16:  # Connect BLE
        if status == 0:
            print('[callback] ble connect successful.')
            connect_id = args[2]
            addr = args[3] # a bytearray
            addr_str = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[0], addr[1], addr[2], addr[3], addr[4], addr[5])
            print('[callback] connect_id = {}, addr = {}'.format(connect_id, addr_str))
        else:
            print('[callback] ble connect failed.')
    elif event_id == 17:  # Disconnect BLE
        if status == 0:
            print('[callback] ble disconnect successful.')
            connect_id = args[2]
            addr = args[3] # a bytearray
            addr_str = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[0], addr[1], addr[2], addr[3], addr[4], addr[5])
            print('[callback] connect_id = {}, addr = {}'.format(connect_id, addr_str))
        else:
            print('[callback] ble disconnect failed.')
            ble.gattStop()
            return
    elif event_id == 18:  # BLE update connection parameter
        if status == 0:
            print('[callback] ble update parameter successful.')
            connect_id = args[2]
            max_interval = args[3]
            min_interval = args[4]
            latency = args[5]
            timeout = args[6]
            print('[callback] connect_id={},max_interval={},min_interval={},latency={},timeout={}'.format(connect_id, max_interval, min_interval, latency, timeout))
        else:
            print('[callback] ble update parameter failed.')
            ble.gattStop()
            return
    elif event_id == 20:  # BLE connection MTU
        if status == 0:
            print('[callback] ble connect mtu successful.')
            handle = args[2]
            ble_mtu = args[3]
            print('[callback] handle = {:#06x}, ble_mtu = {}'.format(handle, ble_mtu))
        else:
            print('[callback] ble connect mtu failed.')
            ble.gattStop()
            return
    elif event_id == 21:  # Server：when the BLE client writes a characteristic value or descriptor, the server gets the notice.
        if status == 0:
            print('[callback] ble recv successful.')
            data_len = args[2]
            data = args[3]  # a bytearray
            attr_handle = args[4]
            short_uuid = args[5]
            long_uuid = args[6]  # a bytearray
            print('len={}, data:{}'.format(data_len, data))
            print('attr_handle = {:#06x}'.format(attr_handle))
            print('short uuid = {:#06x}'.format(short_uuid))
            print('long uuid = {}'.format(long_uuid))
        else:
            print('[callback] ble recv failed.')
            ble.gattStop()
            return
    elif event_id == 22:  # Server：when the BLE client reads a characteristic value or descriptor, the server gets the notice.
        if status == 0:
            print('[callback] ble recv read successful.')
            data_len = args[2]
            data = args[3]  # a bytearray
            attr_handle = args[4]
            short_uuid = args[5]
            long_uuid = args[6]  # a bytearray
            print('len={}, data:{}'.format(data_len, data))
            print('attr_handle = {:#06x}'.format(attr_handle))
            print('short uuid = {:#06x}'.format(short_uuid))
            print('long uuid = {}'.format(long_uuid))
        else:
            print('[callback] ble recv read failed.')
            ble.gattStop()
            return
    elif event_id == 25:  # Server sends notification, and receives notice sent by the peer end
        if status == 0:
            print('[callback] ble send data successful.')
        else:
            print('[callback] ble send data failed.')
    else:
        print('unknown event id.')

ble.serverInit(ble_callback)
```

### ble.serverRelease

```python
ble.serverRelease()
```

Releases BLE server resources.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### ble.setLocalName

```python
ble.setLocalName(code, name)
```

Sets the BLE name.

**Parameter：**

- `code`- Integer type. Encoding scheme. 0 - UTF8，1 - GBK.
- `name`- String type. Encoding scheme. BLE name.  The maximum length is 29 bytes.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

**Example**：

```python
>>> ble.setLocalName(0, 'QuecPython-BLE')
0
```

**Note**：

For BLE, when a device is advertising, if you need the scanning software to discover the name of the advertising device during scanning, it is necessary to include the Bluetooth name in the advertising data or include the device name in the scan response data.

### ble.setAdvParam

```python
ble.setAdvParam(min_adv,max_adv,adv_type,addr_type,channel,filter_policy,discov_mode,no_br_edr,enable_adv)
```

Sets advertising parameters.

**Parameter：**

- See the table below for parameter description:

| Parameter     | Type         | Description                                                  |
| ------------- | ------------ | ------------------------------------------------------------ |
| min_adv       | unsigned int | Minimum advertising interval. Range: 0x0020–0x4000. The calculation is as follows:<br>Time interval = min_adv \* 0.625. Unit: ms. |
| max_adv       | unsigned int | Maximum advertising interval. Range: 0x0020–0x4000. The calculation is as follows:<br/>Time interval = max_adv \* 0.625. Unit: ms. |
| adv_type      | unsigned int | Advertising type. The value is as follows:<br>0 - Connectable undirected advertising (default)<br>1 - High duty cycle connectable directed advertising<br>2 - Scannable undirected advertising<br>3 - Non-connectable undirected advertising<br>4 - Low duty cycle connectable directed advertising |
| addr_type     | unsigned int | Local address type. The value is as follows:<br>0 - Public address<br>1 - Random address |
| channel       | unsigned int | Advertising channel. The value is as follows:<br>1 - Channel 37<br>2 - Channel 38<br>4 - Channel 39<br>7 - All three channels above are selected (default) |
| filter_policy | unsigned int | Advertising Filter Policy. The value is as follows:<br>0 - Allow scan request from any, allow connect request from any<br/>1 - Allow scan request from white list only, allow connect request from any. (Not supported currently)<br/>2 - Allow scan request from any, allow connect request from white list only. (Not supported currently)<br/>3 - Allow scan request from white list only, allow connect request from white list only. (Not supported currently) |
| discov_mode   | unsigned int | Discovery mode. Used by GAP protocol. The default value is 2.<br/>1 - Limited discoverable mode<br/>2 - General discoverable mode |
| no_br_edr     | unsigned int | Disables BR/EDR. The default value is 1. Set it to 0 to enable BR/EDR. |
| enable_adv    | unsigned int | Enables advertising. The default value is 1. Set it to 0 to disable advertising. |

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

**Example**：

```python
def ble_gatt_set_param():
    min_adv = 0x300
    max_adv = 0x320
    adv_type = 0  # Connectable undirected advertising (default)
    addr_type = 0  # Public address
    channel = 0x07
    filter_strategy = 0  # Allow scan request from any, allow connect request from any
    discov_mode = 2
    no_br_edr = 1
    enable_adv = 1
    ret = ble.setAdvParam(min_adv, max_adv, adv_type, addr_type, channel, filter_strategy, discov_mode, no_br_edr, enable_adv)
    if ret != 0:
        print('ble_gatt_set_param failed.')
        return -1
    print('ble_gatt_set_param success.')
    return 0
```

### ble.setAdvData

```python
ble.setAdvData(data)
```

Sets the content of the advertising data.

**Parameter：**

- `data`-Bytearray type. Advertising data, with a maximum length of 31 bytes. The content of the advertising data is in the format of `length+type+data`. A combination of multiple sets of data in this format can be included in a single advertising data. In the example below, there are two sets of data combinations: the first one is "0x02, 0x01, 0x05", where 0x02 indicates that there are two data following it, which are 0x01 and 0x05 respectively (0x01 representing the type and 0x05 representing the specific data); the second set is the BLE name data combination, with the length being the BLE name length plus 1, the type being 0x09, and the specific data being the corresponding encoding value of the name. For the specific meanings of the type values, please refer to the official Bluetooth protocol standard document.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

**Example**：

```python
def ble_gatt_set_data():
    adv_data = [0x02, 0x01, 0x05]
    ble_name = "Quectel_ble"
    length = len(ble_name) + 1
    adv_data.append(length)
    adv_data.append(0x09)
    name_encode = ble_name.encode('UTF-8')
    for i in range(0, len(name_encode)):
        adv_data.append(name_encode[i])
    print('set adv_data:{}'.format(adv_data))
    data = bytearray(adv_data)
    ret = ble.setAdvData(data)
    if ret != 0:
        print('ble_gatt_set_data failed.')
        return -1
    print('ble_gatt_set_data success.')
    return 0
```

### ble.setAdvRspData

```python
ble.setAdvRspData(data)
```

Sets the scan response data.

**Parameter：**

- `data`- Bytearray type. Scan response data with a maximum length of 31 bytes. The format for the scan response data is the same as that of the advertising data set by the `setAdvData` function.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

**Example**：

```python
def ble_gatt_set_rsp_data():
    adv_data = []
    ble_name = "Quectel_ble"
    length = len(ble_name) + 1
    adv_data.append(length)
    adv_data.append(0x09)
    name_encode = ble_name.encode('UTF-8')
    for i in range(0, len(name_encode)):
        adv_data.append(name_encode[i])
    print('set adv_rsp_data:{}'.format(adv_data))
    data = bytearray(adv_data)
    ret = ble.setAdvRspData(data)
    if ret != 0:
        print('ble_gatt_set_rsp_data failed.')
        return -1
    print('ble_gatt_set_rsp_data success.')
    return 0
```

**Note**：

It is meaningful to set the scan response data only when the client device is in an active scan mode.

### ble.addService

```python
ble.addService(primary, server_id, uuid_type, uuid_s, uuid_l)
```

Adds a service.

**Parameter：**

- `primary`- Integer type. Service type. 1 indicates primary service and other values indicate non-primary service.
- `server_id`- Integer type. Server ID to identify a service.  
- `uuid_type`- Integer type. The UUID type. 0 - long UUID (128 bit); 1 - short UUID (16 bit).
- `uuid_s`- Integer type. Short UUID with 2 bytes (16 bit). When `uuid_type` is set to 0, the value is 0.
- `uuid_l`- Bytearray type. Long UUID with 16 bytes (128bit). When `uuid_type` is set to 1, the value is bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]).

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

**Example**：

```python
def ble_gatt_add_service():
    primary = 1
    server_id = 0x01
    uuid_type = 1  # Short UUID
    uuid_s = 0x180F
    uuid_l = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    ret = ble.addService(primary, server_id, uuid_type, uuid_s, uuid_l)
    if ret != 0:
        print('ble_gatt_add_service failed.')
        return -1
    print('ble_gatt_add_service success.')
    return 0
```

### ble.addChara

```python
ble.addChara(server_id, chara_id, chara_prop, uuid_type, uuid_s, uuid_l)
```

Adds a characteristic in the service.

**Parameter：**

- `server_id`- Integer type. Server ID to identify a service.
- `chara_id`- Integer type. Characteristic ID.
- `chara_prop`-Integer type. Characteristic property. Hexadecimal number. You can specify multiple attributes at the same time by `OR`, and the specific meanings of the values are as shown in the following table: 

| Value | Description                                       |
| ----- | ------------------------------------------------- |
| 0x01  | Advertising                                       |
| 0x02  | Readable                                          |
| 0x04  | Writable and does not require link-layer response |
| 0x08  | Writable                                          |
| 0x10  | Notification                                      |
| 0x20  | Indication                                        |
| 0x40  | Authenticated signed writes                       |
| 0x80  | Extended property                                 |

- `uuid_type`-Integer type. The UUID type. 0 - long UUID (128 bit); 1 - short UUID (16 bit).
- `uuid_s`- Integer type. Short UUID with 2 bytes (16 bit). When `uuid_type` is set to 0, the value is 0.
- `uuid_l`- Bytearray type. Long UUID with 16 bytes (128bit). When `uuid_type` is set to 1, the value is bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]).

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

**Example**：

```python
def ble_gatt_add_characteristic():
    server_id = 0x01
    chara_id = 0x01
    chara_prop = 0x02 | 0x10 | 0x20  # 0x02-Readable 0x10-Notification 0x20-Indication
    uuid_type = 1  # Short UUID
    uuid_s = 0x2A19
    uuid_l = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    ret = ble.addChara(server_id, chara_id, chara_prop, uuid_type, uuid_s, uuid_l)
    if ret != 0:
        print('ble_gatt_add_characteristic failed.')
        return -1
    print('ble_gatt_add_characteristic success.')
    return 0
```

### ble.addCharaValue

```python
ble.addCharaValue(server_id, chara_id, permission, uuid_type, uuid_s, uuid_l, value)
```

Adds a characteristic value in the characteristic.

**Parameter：**

- `server_id`- Integer type. Server ID to identify a service.
- `chara_id`- Integer type. Characteristic ID. 
- `permission`- Integer type. Permission for characteristic value. 2 bytes. Hexadecimal number. You can specify multiple attributes at the same time by `OR`, and the specific meanings of the values are shown in the following table: 

| Value  | Description                                           |
| ------ | ----------------------------------------------------- |
| 0x0001 | Readable permission                                   |
| 0x0002 | Writable permission                                   |
| 0x0004 | Authentication permission for read                    |
| 0x0008 | Authorization permission for read                     |
| 0x0010 | Encryption permission for read                        |
| 0x0020 | Authorization and authentication permission for read  |
| 0x0040 | Authentication permission for write                   |
| 0x0080 | Authorization permission for write                    |
| 0x0100 | Encryption permission for write                       |
| 0x0200 | Authorization and authentication permission for write |

- `uuid_type`- Integer type. The UUID type. 0 - long UUID (128 bit); 1 - short UUID (16 bit).
- `uuid_s`- Integer type. Short UUID with 2 bytes (16 bit). When `uuid_type` is set to 0, the value is 0.
- `uuid_l`- Bytearray type. Long UUID with 16 bytes (128bit). When `uuid_type` is set to 1, the value is bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]).
- `value`- Bytearray type. Characteristic value data.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

**Example**：

```python
def ble_gatt_add_characteristic_value():
    data = []
    server_id = 0x01
    chara_id = 0x01
    permission = 0x0001 | 0x0002
    uuid_type = 1  # Short UUID
    uuid_s = 0x2A19
    uuid_l = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    for i in range(0, 244):
        data.append(0x00)
    value = bytearray(data)
    ret = ble.addCharaValue(server_id, chara_id, permission, uuid_type, uuid_s, uuid_l, value)
    if ret != 0:
        print('ble_gatt_add_characteristic_value failed.')
        return -1
    print('ble_gatt_add_characteristic_value success.')
    return 0
```

### ble.changeCharaValue

```python
ble.changeCharaValue(server_id, chara_id, value)
```

Changes characteristic value.

**Parameter：**

- `server_id`- Integer type. Server ID to identify a service.
- `chara_id`- Integer type. Characteristic ID. 

- `value`- Bytearray type. Characteristic value data.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### ble.addCharaDesc

```python
ble.addCharaDesc(server_id, chara_id, permission, uuid_type, uuid_s, uuid_l, value)
```

Adds a characteristic description in the characteristic. Note that the characteristic description and the characteristic value share the same characteristic. 

**Parameter：**

- `server_id`- Integer type. Server ID to identify a service.
- `chara_id`- Integer type. Characteristic ID. 
- `permission`- Integer type. Permission for characteristic value. 2 bytes. Hexadecimal number. You can specify multiple attributes at the same time by `OR`, and the specific meanings of the values are as shown in the following table: 

| Value  | Description                                           |
| ------ | ----------------------------------------------------- |
| 0x0001 | Readable permission                                   |
| 0x0002 | Writable permission                                   |
| 0x0004 | Authentication permission for read                    |
| 0x0008 | Authorization permission for read                     |
| 0x0010 | Encryption permission for read                        |
| 0x0020 | Authorization and authentication permission for read  |
| 0x0040 | Authentication permission for write                   |
| 0x0080 | Authorization permission for write                    |
| 0x0100 | Encryption permission for write                       |
| 0x0200 | Authorization and authentication permission for write |

- `uuid_type`- Integer type. The UUID type. 0 - long UUID (128 bit); 1 - short UUID (16 bit).
- `uuid_s`- Integer type. Short UUID with 2 bytes (16 bit). When `uuid_type` is set to 0, the value is 0.
- `uuid_l`- Bytearray type. Long UUID with 16 bytes (128bit). When `uuid_type` is set to 1, the value is bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]).

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

**Example**：

```python
def ble_gatt_add_characteristic_desc():
    data = [0x00, 0x00]
    server_id = 0x01
    chara_id = 0x01
    permission = 0x0001 | 0x0002
    uuid_type = 1  # Short UUID
    uuid_s = 0x2902
    uuid_l = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    value = bytearray(data)
    ret = ble.addCharaDesc(server_id, chara_id, permission, uuid_type, uuid_s, uuid_l, value)
    if ret != 0:
        print('ble_gatt_add_characteristic_desc failed.')
        return -1
    print('ble_gatt_add_characteristic_desc success.')
    return 0
```

### ble.addOrClearService

```python
ble.addOrClearService(option, mode)
```

Adds all the service information that has been added to the module, or clears all the service information that has been added in the module.

**Parameter：**

- `option`- Integer type. Operation type. 0 - Clear all services; 1 - Add all services.
- `mode`- Integer type. Whether to keep the default system GAP and GATT service.  0 - Delete; 1 - Keep.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### ble.sendNotification

```python
ble.sendNotification(connect_id, attr_handle, value)
```

Sends notification.

**Parameter：**

- `connect_id`- Integer type. Connection ID. 
- `attr_handle`- Integer type. Attribute handle.
- `value`- Bytearray type. The data to be sent. The maximum length is MTU.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### ble.sendIndication

```python
ble.sendIndication(connect_id, attr_handle, value)
```

Sends indication.

**Parameter：**

- `connect_id`- Integer type. Connection ID. 
- `attr_handle`- Integer type. Attribute handle.
- `value`- Bytearray type. The data to be sent. The maximum length is MTU.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### ble.advStart

```python
ble.advStart()
```

Starts advertising.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### ble.advStop

```python
ble.advStop()
```

Stops advertising.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

## BLE Client Related Features

### ble.clientInit

```python
ble.clientInit(user_cb)
```

Initializes BLE Client and registers a callback function.

**Parameter：**

- `user_cb`- Function type. Callback function. The meaning of the callback function parameters: `args[0]` is fixed to represent event_id; `args[1]` is fixed to represent the status, `0` indicating successful execution and non-`0` indicating failed execution. The number of callback function parameters is not fixed at two, but depends on the first parameter `args[0]`. The following table lists the number of parameters and explanations for different event IDs.

| event_id | Parameter Number | Description                                                  |
| :------: | :--------------: | ------------------------------------------------------------ |
|    0     |        2         | args[0]: event_id. Starts BT/BLE<br>args[1]: status. The operation status. 0 - successful operation; other values - failed operation. |
|    1     |        2         | args[0]: event_id. Stops BT/BLE.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation. |
|    16    |        4         | args[0]: event_id. Connects BLE.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: connect_id.<br/>args[3]: addr. BT/BLE address in bytearray type. |
|    17    |        4         | args[0]: event_id. Disconnects BLE.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: connect_id.<br/>args[3]: addr. BT/BLE address in bytearray type. |
|    18    |        7         | args[0]: event_id. BLE update connection parameter.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: connect_id.<br/>args[3]: max_interval. Maximum interval. Interval: 1.25 ms. Range: 6–3200. Time range: 7.5 ms–4 s.<br/>args[4]: min_interval. Minimum interval. Interval: 1.25 ms. Range: 6–3200. Time range: 7.5 ms–4 s.<br/>args[5]: latency. The time at which the slave ignored the connection status event. It should meet the following condition:（1+latecy)\*max_interval\*2\*1.25<timeout\*10<br/>args[6]: timeout. Disconnect if there is no interaction during the timeout. Interval: 10ms，Range: 10–3200 ms. Time range: 100 ms–32 s. |
|    19    |        9         | args[0]: event_id. BLE scan report.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: event_type.<br/>args[3]: The name of the scanned device.<br/>args[4]: Device address type.<br/>args[5]: Device address in bytearray type.<br/>args[6]: rssi. Signal strength.<br/>args[7]: data_len. The length of the raw data scanned.<br/>args[8]: data. The raw data scanned. |
|    20    |        4         | args[0]: event_id. BLE connection MTU.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: handle.<br/>args[3]: MTU value. |
|    23    |        4         | args[0]: event_id. Client receives notification.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: data_len. Data length.<br/>args[3]: data. Raw data containing handle and other data. The format and description of the raw data is described in the example at the beginning. |
|    24    |        4         | args[0]: event_id. Client receives indication.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: data_len. Data length.<br/>args[3]: data. Raw data containing indication. The format and description of the raw data is described in the example at the beginning. |
|    26    |        2         | args[0]: event_id. Starts discover service.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation. |
|    27    |        5         | args[0]: event_id. Discovers service.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: start_handle. The start handle of the service.<br/>args[3]: end_handle. The end handle of the service.<br/>args[4]: UUID, indicating the UUID of the service (Short UUID). |
|    28    |        4         | args[0]: event_id. Discovers characteristic.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: data_len. Data length.<br/>args[3]: data. Raw data containing handle, attribute, UUID and other data. The format and description of the raw data is described in the example at the beginning. |
|    29    |        4         | args[0]: event_id. Discovers characteristic descriptor.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: data_len. Data length.<br/>args[3]: data. Raw data containing handle, UUID and other data. The format and description of the raw data is described in the example at the beginning. |
|    30    |        2         | args[0]: event_id. Writes characteristic value with peer response.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation. |
|    31    |        2         | args[0]: event_id. Writes characteristic value without peer response. <br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation. |
|    32    |        4         | args[0]: event_id. Reads characteristic value by handle.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: data_len. Data length.<br/>args[3]: data. Raw data. |
|    33    |        4         | args[0]: event_id. Reads characteristic value by UUID.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: data_len. Data length.<br/>args[3]: data. Raw data. |
|    34    |        4         | args[0]: event_id. Reads multiple characteristic value.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: data_len. Data length.<br/>args[3]: data. Raw data. |
|    35    |        2         | args[0]: event_id. Writes characteristic descriptor.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation. |
|    36    |        4         | args[0]: event_id. Reads characteristic descriptor.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: data_len. Data length.<br/>args[3]: data. Raw data. |
|    37    |        3         | args[0]: event_id. Attribute error.<br/>args[1]: status. The operation status. 0 - successful operation; other values - failed operation.<br/>args[2]: errcode. Error code. |

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### ble.clientRelease

```python
ble.clientRelease()
```

Releases BLE client resources.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### ble.setScanParam

```python
ble.setScanParam(scan_mode, interval, scan_window, filter_policy, addr_type)
```

Sets the scan parameters.

**Parameter：**

- `scan_mode`- Integer type. Scan mode. `0` indicates passive scanning and `1` indicating active scanning. Default value: `1`.
- `interval`- Integer type. Scan interval. Range: 0x0004–0x4000. Time interval = `interval` \* 0.625. Unit: ms.
- `scan_window`- Integer type. Scanning time for a single scan. Range: 0x0004–0x4000. Scan time = `scan_window`\* 0.625. Unit: ms.
- `filter_policy`- Integer type. Scan filter policy. Default value: `0`. `0` - Allow all advertisement packets except directed advertising packets not addressed to this device. `1` - Allow only advertisement packets from devices where the advertiser’s address is in the Whitelist. and directed advertising packets which are not addressed for this device shall be ignored. `2` - Allow all undirected advertisement packets, and directed advertising packets where the initiator address is a resolvable private address, and directed advertising packets addressed to this device. `3` - Allow all advertisement packets from devices where the advertiser’s address is in the Whitelist, and directed advertising packets where the initiator address is a resolvable private address, and directed advertising packets addressed to this device.
- `addr_type`- Integer type. Local address type. 0 - Public address; 1 - Random address.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

**Note**：

The `scan_window` should not be greater than the `interval`. If they are equal, it indicates continuous scanning, and the BLE controller will run continuously, occupying system resources and preventing other tasks from being executed. Therefore, continuous scanning is not allowed. It is also not recommended to set the time interval too short, because more frequent scanning consumes more power.

### ble.scanStart

```python
ble.scanStart()
```

Starts scanning.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### ble.scanStop

```python
ble.scanStop()
```

Stops scanning.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### ble.setScanFilter

```python
ble.setScanFilter(act)
```

Enables or disables scan filtering. If enabled, only one advertising data packet from the same device will be reported during the scan; if disabled, all advertising data packets from the same device will be reported.

**Parameter：**

- `act`-Integer type. Controls whether to enable scan filtering. `0` - Disable; `1` - Enable. Default value: 1.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### ble.connect

```python
ble.connect(addr_type, addr)
```

Connects the device according to the specified device address.

**Parameter：**

- `addr_type`- Integer type. Address type. 0 - Public address; 1 - Random address.
- `addr`- Bytearray type. BLE address. Size: 6 bytes.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### ble.cancelConnect

```python
ble.cancelConnect(addr)
```

Cancels the connection that is being established.

**Parameter：**

- `addr`- Bytearray type. BLE address. Size: 6 bytes.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### ble.disconnect

```python
ble.disconnect(connect_id)
```

Disconnects the connection that has been established.

**Parameter：**

- `connect_id`- Integer type. The connection ID obtained when the connection was established.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### ble.discoverAllService

```python
ble.discoverAllService(connect_id)
```

Discovers all services. 

**Parameter：**

- `connect_id`- Integer type. The connection ID obtained when the connection was established.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### ble.discoverByUUID

```python
ble.discoverByUUID(connect_id, uuid_type, uuid_s, uuid_l)
```

Discovers the services of specified UUID.

**Parameter：**

- `connect_id` - Integer type. The connection ID obtained when the connection was established.
- `uuid_type` - Integer type. UUID type. `0` - Long UUID (128 bit); `1` - Short UUID (16 bit)
- `uuid_s` - Integer type. Short UUID, 2 bytes (16 bit). When `uuid_type` is set to 0, the `uuid_s` is 0.
- `uuid_l` - Bytearray type. Long UUID, 16 bytes (128 bit).  When `uuid_type` is set to 1, the `uuid_l` is bytearray ([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]).

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### ble.discoverAllIncludes

```python
ble.discoverAllIncludes(connect_id, start_handle, end_handle)
```

Discovers all includes. The `start_handle` and `end_handle` should be in the same service.

**Parameter：**

- `connect_id` - Integer type. The connection ID obtained when the connection was established.
- `start_handle`- Integer type. Start handle. Start discovering includes from this handle.
- `end_handle`- Integer type. End handle. Stop discovering includes from this handle.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### ble.discoverAllChara

```python
ble.discoverAllChara(connect_id, start_handle, end_handle)
```

Discovers all characteristics. The `start_handle` and `end_handle` should be in the same service.

**Parameter：**

- `connect_id`- Integer type. The connection ID obtained when the connection was established.
- `start_handle`- Integer type. Start handle. Start discovering characteristics from this handle.
- `end_handle`- Integer type. End handle. Stop discovering characteristics from this handle.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### ble.discoverAllCharaDesc

```python
ble.discoverAllCharaDesc(connect_id, start_handle, end_handle)
```

Discovers all characteristic descriptions. The `start_handle` and `end_handle` should be in the same service. 

**Parameter：**

- `connect_id`- Integer type. The connection ID obtained when the connection was established.
- `start_handle`- Integer type. Start handle. Start discovering characteristic descriptions from this handle.
- `end_handle`- Integer type. End handle. This Stop discovering characteristic descriptions from this handle.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### ble.readCharaByUUID

```python
ble.readCharaByUUID(connect_id, start_handle, end_handle, uuid_type, uuid_s, uuid_l)
```

Reads the characteristic value of specified UUID. The `start_handle` and `end_handle` must contain a characteristic value handle. 

**Parameter：**

- `connect_id`- Integer type. Connection ID. The connection ID obtained when the connection was established.
- `start_handle`- Integer type. Start handle. The `start_handle` and `end_handle` should be in the same service.
- `end_handle`- Integer type. End handle. The `start_handle` and `end_handle` should be in the same service.
- `uuid_type` - Integer type. UUID type. `0` - Long UUID (128 bit); `1` - Short UUID (16 bit)
- `uuid_s`- Integer type. Short UUID, 2 bytes (16 bit). When  `uuid_type` is set to 0, the `uuid_s` is 0.
- `uuid_l`- Bytearray type. Long UUID, 16 bytes (128 bit).  When `uuid_type` is set to 1, the `uuid_l` is bytearray ([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]).

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### ble.readCharaByHandle

```python
ble.readCharaByHandle(connect_id, handle, offset, is_long)
```

Reads the characteristic value of specified handle.

**Parameter：**

- `connect_id`- Integer type. The connection ID obtained when the connection was established.
- `handle`- Integer type. Characteristic value handle.
- `offset`- Integer type. Offset.
- `is_long`- Integer type. Long characteristic value flag. `0` indicates short characteristic value which can be finished reading at one time; `1` indicates long characteristic value which needs to be read by multiple times.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### ble.readCharaDesc

```python
ble.readCharaDesc(connect_id, handle, is_long)
```

Reads the characteristic description.

**Parameter：**

- `connect_id`- Integer type. The connection ID obtained when the connection was established.
- `handle`- Integer type. Characteristic value handle.
- `is_long`- Integer type. Long characteristic value flag. `0` indicates short characteristic value which can be finished reading at one time;`1` indicates long characteristic value which needs to be read by multiple times.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### ble.writeChara

```python
ble.writeChara(connect_id, handle, offset, is_long, data)
```

Writes the characteristic value with peer response.

**Parameter：**

- `connect_id`- Integer type. The connection ID obtained when the connection was established.
- `handle`- Integer type. Characteristic value handle.
- `offset`- Integer type. Offset.
- `is_long`- Integer type. Long characteristic value flag. `0` indicates short characteristic value which can be finished reading at one time;  `1` indicates long characteristic value which needs to be read by multiple times.
- `data`- Bytearray type. Characteristic value data.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### ble.writeCharaNoRsp

```python
ble.writeCharaNoRsp(connect_id, handle, data)
```

Writes the characteristic value without peer response.

**Parameter：**

- `connect_id`- Integer type. The connection ID obtained when the connection was established.
- `handle`- Integer type. Characteristic value handle.
- `data`- Bytearray type. Characteristic value data.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

### ble.writeCharaDesc

```python
ble.writeCharaDesc(connect_id, handle, data)
```

Writes the characteristic description.

**Parameter：**

- `connect_id`- Integer type. The connection ID obtained when the connection was established.
- `handle`- Integer type. Characteristic description handle.
- `data`- Bytearray type. Characteristic description data.

**Return Value：**

- `0`- Successful execution; `-1`- Failed execution.

