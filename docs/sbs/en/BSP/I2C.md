## Revision History

| Version | Date       | Author | Description                                                  |
| ------- | ---------- | ------ | ------------------------------------------------------------ |
| 1.0     | 2021-09-13 | Kayden | Added revision history, deleted referential codes, and added referential test link |

## Brief introduction

 In this document, it mainly illustrates how to use QuecPython I2C module.

### Quick start

2. About specific API of QuecPython I2C, please refer to [I2C.](https://python.quectel.com/wiki/#/en-us/api/QuecPythonClasslib?id=i2c)
3. About the application test of I2C, please refer to integrated humidity and temperature sensor: [Internal temperature and humidity sensor experiment.](https://python.quectel.com/doc/doc/Advanced_development/en/QuecPythonSub/i2c_aht.html)
4. About the application test of I2C, it is also valid to refer to [Acceleration sensor experiment.](https://python.quectel.com/doc/doc/Advanced_development/en/QuecPythonSub/i2c_lis2dh.html)

### Brief introduction on I2C. 

In this document, it tells how to use th QuexPython I2C Library. For more basic knowledge,please search *I2C* yourself. 

**I2C**, also named **IIC**, is the abbreviation of **Inter-Integrated-Circuit**. It is integrated circuit bus. 

### The base of I2C protocol
E. g. When writing data to Slave by Master, the basic structure is shown as following figure.

**Start signal -- Slave address-Read/Write signal--data bit-- Acknowledgement bit--... ... --Pause bit**

![media_I2C_01(E)](media\media_I2C_01(E).png)

- Start signal(S): When the SCL is in high level, the SDA line is switched from high level to low level. 
- Pause signal(P): When the SCL is in high level, the SDA line is switched from low level to high level.



![media_I2C_02(E)](media\media_I2C_02(E).png)

Frame address: Every device on I2C bus is equipped with its independent address. When the host releases communication, it will transmit slave address to check via SDA signal thread. As for the device address regulated by I2C protocol, both 7 bits and 10 bits are valid; however, in most cases, the 7 bits address is widely applied. 

The SDA signal line is used to transmit data by I2C, while the SCL signal line is to make the data synchronous. The SDA data line will transmit one bit data every clock cycle of SCL. When transmitting, if the SCL is in high level, which means the data is valid. That is to say, the data ”1“ means the high level while the data "0" means the low level from the view of SDA. When SCL is in low level, the SDA data is invalid. Normally, the SDA will carry out level switch at that moment to get ready for data of next time. 

Both I2C data and address transmission are implemented with response, which including in Acknowledgement (ACK) and None Acknowledgement (NACK).

As the data receiving end, if the device (whether master or slave) receives a byte of data or an address transmitted by the I2C. If there is a need for the other party to continue sending data, it will send an ACK signal and the sender will continue to send the next data correspondingly. If the receiver wishes to end the data transmission, it sends a "NACK" signal to the other party. After receiving this signal, the sender generates a stop signal to end the signal transmission.

### Common I2C command format

Several methods are covered in common I2C bus
-   Read the data with fixed length of assigned peripheral and register. 
-   Read assigned peripheral, starting address and data of certain length
-   Write assigned peripheral and fixed data of assigned register
-   Write assigned peripheral, starting address and data of certain length
-   Trigger some behavior via writing the specific register of assigned peripheral, then wait the peripheral returns data. 

