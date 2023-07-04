# Import Module
import log
import utime
import _thread
import usocket
import checkNet


socket = None
state = 1

# The following two global variables are mandatory, and users can modify the values of the following two global variables according to their actual projects.
# The values of these two variables are printed before the user code is executed.
PROJECT_NAME = "Grey_Socket"
PROJECT_VERSION = "1.0.0"
checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)


# | Parameter | parameter | description               | type     |
# | --------- | --------- | ------------------------- | -------- |
# | CRITICAL  | constant  | value of logging level 50 | critical |
# | ERROR     | constant  | value of logging level 40 | error    |
# | WARNING   | constant  | value of logging level 30 | warning  |
# | INFO      | constant  | value of logging level 20 | info     |
# | DEBUG     | constant  | value of logging level 10 | debug    |
# | NOTSET    | constant  | value of logging level 0  | notset   |
log.basicConfig(level=log.NOTSET)   # Set the log output level
Grey_log = log.getLogger("Grey")


def debug():
    global state
    run_mun = 0
    while True:
        run_mun += 1
        Grey_log.info('Print run: {:04d}'.format(run_mun))
        utime.sleep_ms(1000)


def socket_read():
    global socket
    global state

    while state:
        data = socket.recv(1024)
        if len(data) > 0 and 'TCPClient End' in data.decode():
            state = 0
            break
        elif len(data) > 0:
            Grey_log.info('----------------TCPclient Recv Data-----------------')
            Grey_log.info('TCPclient Recv Data: {}  Len: {:03d}\r\n'.format(data.decode(), len(data)))
        utime.sleep_ms(1)
    socket.close()  # Disconnect the Socket connection
    Grey_log.info('========================TCPClient END========================\r\n')


if __name__ == "__main__":
    # When running this routine manually, the delay can be removed. If the routine file name is changed to main.py and the startup is expected to run automatically, the delay needs to be added.
    # Otherwise, the information printed in poweron_print_once() below cannot be seen from the CDC port
    # utime.sleep(5)
    checknet.poweron_print_once()

    # If the user program contains network related code, you must execute wait_network_connected() to wait for the network to be ready (the dialing succeeded);
    # If it is network irrelevant code, you can mask it wait_network_connected()
    # attention: The function does not block when the SIM card is not inserted.
    # 【This routine cannot mask the following line！】
    stagecode, subcode = checknet.wait_network_connected(120)
    Grey_log.debug('stagecode: {}   subcode: {}'.format(stagecode, subcode))
    # Network ready     : stagecode = 3, subcode = 1
    # No sim card       : stagecode = 1, subcode = 0
    # Sim card is locked: stagecode = 1, subcode = 2
    # network timeout   : stagecode = 2, subcode = 0
    if stagecode != 3 or subcode != 1:
        Grey_log.warning('【Look Out】 Network Not Available\r\n')
    else:
        Grey_log.error('【Look Out】 Network Ready\r\n')

    Grey_log.info('User Code Start\r\n\r\n')

    socket = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)  # Create a Socket object
    sockinfo = usocket.getaddrinfo('112.125.89.8', 37982)[0][-1]  # resolve a domain name
    socket.connect(sockinfo)  # connect to server

    # _thread.start_new_thread(debug, ())  # thread worker thread
    _thread.start_new_thread(socket_read, ())  # thread worker thread
    while state:
        socket.send('socket_test\r\n')  # Send data
        utime.sleep(5)

    Grey_log.info('========================Main END========================\r\n')
