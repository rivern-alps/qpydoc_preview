# QuecPython API Reference Manual

**Author**

&emsp;&emsp;&emsp;QuecPython Developer Team

**Version**

&emsp;&emsp;&emsp;1.12

QuecPython is a solution created by Quectel, which is based on the open-source project MicroPython. It inherits the basic features of MicroPython and expands the features related to Quectel's communication modules. With QuecPython, developers can easily develop embedded Internet of Things (IoT) projects.

If you are not familiar with QuecPython, you may not know its advantages compared to other embedded IoT project development methods. However, once you get to know QuecPython, you will immediately discover its charm and superiority.

## QuecPython  Overview

QuecPython is a platform name created by combining  "Quectel"  and "microPython". It is compatible with Python 3 grammar specification. The minimum ROM storage space required is 150 KB, and the minimum RAM storage space required is 50 KB.

Thanks to Python's inherent advantages, QuecPython has many advantages, such as `cross-platform compatibility`, `no need for compilation`, `dynamic loading` and `providing a rich and mature application framework`. QuecPython also provides solutions for `smart meters`, `smart locators`, `public network intercoms`, `BMS communication cloud boxes` and more ([click here for details](https://python.quectel.com/en/solutions)).

The QuecPython team also provides rich development tools such as QPYcom, VSCode plugins, and production testing tools, facilitating the development and production testing.

## QuecPython Architecture

With the rapid development of IoT market in recent years, networking of embedded devices has become a trend. Traditional embedded IoT project development still ports or develops functional components based on the RTOS kernel in C language. This approach has low development efficiency, requires high platform adaptation workloads, and requires high developer capabilities.

QuecPython integrates various commonly used components for embedded IoT projects in the system, and users can implement corresponding features by simply calling Python interfaces. The system architecture is shown in the figure below:

![](./media/QuecPython_Architecture.png)

## QuecPython API Reference Manual

- [Python stdlib](./stdlib/README.md)
- [IoT Library](./iotlib/README.md)
- [BSP Library](./peripherals/README.md)
- [networklib](./networklib/README.md)
- [syslib](./syslib/README.md)
- [WIFI/BT/GNSS](./wifibtgnss/README.md)
- [storelib](./storelib/README.md)
- [componentlib](./componentlib/README.md)
- [errcode](./errcode/README.md)

