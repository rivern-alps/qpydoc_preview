# FCM360W Introduction

## Quick Start

Supported module model

- [FCM360W](https://python.quectel.com/en/products/fcm360w)

## Feature List

### Basic Overview

The QuecPython_FCM360W-TE-B is specifically designed for QuecPython. It is a small and portable "pocket-sized" EVB. The EVB board is equipped with a Type-C interface, so developers only need a USB Type-C cable to easily manipulate the EVB.

### Feature Description

The main components and interface layout of the EVB are shown in the figure below.

![img](media/board/FCM360W_interface_layout.png)

## Document download

- [Quectel_FCM360W_Wi-Fi&Bluetooth_Module_Specification](https://images.quectel.com/python/sites/2/2023/06/Quectel_FCM360W_Wi-FiBluetooth_Module_Specification_V1.0-1.pdf)
- [Quectel_FCM360W_Footprint&Part](https://images.quectel.com/python/2023/06/Quectel_FCM360W_FootprintPart_V1.0.zip)
- [Quectel_FCM360W_3D_Dimensions](https://images.quectel.com/python/2023/06/Quectel_FCM360W_3D_Dimensions_V1.0.zip)
- [Quectel_FCM360W_2D_Dimensions](https://images.quectel.com/python/2023/06/Quectel_FCM360W_2D_Dimensions_V1.0.zip)

## Module Resources

### EVB Interface

**J1 Pin Assignment**

| Pin Header | Pin No. | Name     | Feature               |
| ---------- | ------- | -------- | --------------------- |
| J1         | -       | VCC_3V3  | 3.3 V                 |
| J1         | 26      | MAIN_RXD | UART0                 |
| J1         | 27      | MAIN_TXD | UART0                 |
| J1         | -       | GND      | Ground                |
| J1         | 5       | CEN      | Module enable control |
| J1         | 13      | IO22     | GPIO22                |
| J1         | 12      | IO21     | GPIO21                |
| J1         | 10      | IO16     | GPIO16                |
| J1         | 9       | IO4      | GPIO4                 |
| J1         | 8       | IO14     | GPIO14                |
| J1         | 7       | IO15     | GPIO15                |
| J1         | 6       | IO20     | GPIO20                |

**J2 Pin Assignment**

| Pin Header | Pin No. | Name  | Feature              |
| ---------- | ------- | ----- | -------------------- |
| J2         | 16      | IO25  | GPIO25               |
| J2         | 15      | IO24  | GPIO24               |
| J2         | 14      | IO23  | GPIO23               |
| J2         | 19      | IO17  | GPIO17               |
| J2         | 20      | IO13  | GPIO13               |
| J2         | 21      | IO1   | GPIO1                |
| J2         | 22      | IO0   | GPIO0                |
| J2         | 23      | IO3   | GPIO3                |
| J2         | 29      | IO2   | GPIO2                |
| J2         | 11      | RESET | Module reset control |
| J2         | 17      | BOOT  | Module boot control  |
| J2         | -       | GND   | Ground               |

The following figure shows the pin assignment.

![img](media/board/FCM360W_pin_layout.png)

------

| <font color='red'>Tips</font>                                |
| ------------------------------------------------------------ |
| For more information about the EVB, please visit https://python.quectel.com/download |

### EVB Configuration

The pins of peripherals are shown in the table below.

| No.  | Name        | Model  | Supported | Interface Type | Pin       |
| ---- | ----------- | ------ | --------- | -------------- | --------- |
| 1    | USB to UART | CH340N | Yes       | USB            | 26 and 27 |
| 2    | Key         | -      | Yes       | GPIO           | 15 and 16 |

