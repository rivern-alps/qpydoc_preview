# FCM360W开发板介绍

## 快速开始

支持的模组列表

- [FCM360W](https://python.quectel.com/en/products/fcm360w)


## 功能列表

### 基本概述

QuecPython_FCM360W-TE-B_Vx.x开发板是专门针对QuecPython设计的，是一款小巧便携的“口袋型”开发板。开发板搭载Type-C接口，开发者仅需一条USB Type-C 数据线即可轻松玩转开发板。

### 功能说明

开发板的主要组件、接口布局见下图

![img](media/board/FCM360W_interface_layout.png)

## 资料下载

- [FCM360W系列模组产品规格书](https://images.quectel.com/python/2023/06/Quectel_FCM360W_Wi-FiBluetooth_%E6%A8%A1%E5%9D%97%E4%BA%A7%E5%93%81%E8%A7%84%E6%A0%BC%E4%B9%A6_V1.0.pdf)

- [FCM360W系列模组封装](https://images.quectel.com/python/2023/06/Quectel_FCM360W_FootprintPart_V1.0.zip)

- [FCM360W系列模组3维PCB封装](https://images.quectel.com/python/2023/06/Quectel_FCM360W_3D_Dimensions_V1.0.zip) 

- [FCM360W系列模组2维PCB封装](https://images.quectel.com/python/2023/06/Quectel_FCM360W_2D_Dimensions_V1.0.zip)


## 模组资源

### 开发板接口

**J1排针管脚分配表**

| **排针** | **编号** | **名称** | **引脚** | **功能** |
| -------- | -------- | -------- | -------- | -------- |
| J1       | 1        | VCC_3V3  | -        | 3.3V     |
| J1       | 2        | MAIN_RXD | 26       | UART0    |
| J1       | 3        | MAIN_TXD | 27       | UART0    |
| J1       | 4        | GND      | -        | 接地     |
| J1       | 5        | CEN      | 5        | 模组使能 |
| J1       | 6        | IO22     | 13       | GPIO22   |
| J1       | 7        | IO21     | 12       | GPIO21   |
| J1       | 8        | IO16     | 10       | GPIO16   |
| J1       | 9        | IO4      | 9        | GPIO4    |
| J1       | 10       | IO14     | 8        | GPIO14   |
| J1       | 11       | IO15     | 7        | GPIO15   |
| J1       | 12       | IO20     | 6        | GPIO20   |

**J2排针管脚分配表**

| **排针** | **编号** | **名称** | **引脚** | **功能**         |
| -------- | -------- | -------- | -------- | ---------------- |
| J2       | 1        | IO25     | 16       | GPIO25           |
| J2       | 2        | IO24     | 15       | GPIO24           |
| J2       | 3        | IO23     | 14       | GPIO23           |
| J2       | 4        | IO17     | 19       | GPIO17           |
| J2       | 5        | IO13     | 20       | GPIO13           |
| J2       | 6        | IO1      | 21       | GPIO1            |
| J2       | 7        | IO0      | 22       | GPIO0            |
| J2       | 8        | IO3      | 23       | GPIO3            |
| J2       | 9        | IO2      | 29       | GPIO2            |
| J2       | 10       | RESET    | 11       | 模组复位         |
| J2       | 11       | BOOT     | 17       | 模组启动方式选择 |
| J2       | 12       | GND      | -        | 接地             |

开发板主要管脚布局见下图

![img](media/board/FCM360W_pin_layout.png)

| <font color='red'>小提示</font>                              |
| ------------------------------------------------------------ |
| 开发板的更多资料，请访问 <https://python.quectel.com/download> |

 

### 开发板配置

外设资源管脚分配表明细如下：

| 序号 | 名称      | 型号   | 是否支持 | 接口类型 | 引脚  |
| ---- | --------- | ------ | -------- | -------- | ----- |
| 1    | USB转串口 | CH340N | 是       | USB      | 26,27 |
| 2    | 按键      | -      | 是       | GPIO     | 15,16 |