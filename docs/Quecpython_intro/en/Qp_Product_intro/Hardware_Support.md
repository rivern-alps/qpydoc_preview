

## About Document

**Revision History**

| Version | Date       | Author | Description                  |
| ------- | ---------- | ------ | ---------------------------- |
| 1.0     | 2021-04-07 | Chic   | Initial Version              |
| 1.1     | 2021-07-08 | Chic   | Added EC200U                 |
| 1.2     | 2021-08-10 | Chic   | Added Network mode in tablet |
| 1.3     | 2021-09-08 | Chic   | Modified Figure              |



## Hardware Support

Mainly support currently

EC200U_CNLB，EUAB

EC600U-CNLB，CNLC

EC600N-CNLA，CNLC

EC600S-CNLA，CNLB 



EC200U： The ”U“ represents RDA 8910 Platform

EC600U： The ”U“ represents RDA 8910 Platform

EC600N： The ”N“ means ASR 1603 Platform

EC600S： The ”S“ means ASR 1601 Platform

EC100Y： The ”Y“ means ASR 3601 Platform

The kernel is ASR3601, while the system is ThreadX - A Hard RTOS（Real-time operating system) with source code.![Qp_Product_intro_Hardware_Support_01](media\Qp_Product_intro_Hardware_Support_01.png)



## Details

| **Part number** | Network                                                      | Frequency                                                    | CPU    | Flash size (Kbytes)       | **RAM size** (Kbytes) | GPIO | UART | SPI  | IIC  | ADC  | Timer | Volte | LCD  | Camera | POC  | SD   | WIFI | BT   | FOTA | Supply voltage (V) | Maximum operating temperature range (°C) |
| :-------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------ | ------------------------- | --------------------- | ---- | ---- | ---- | ---- | ---- | ----- | ----- | ---- | ------ | ---- | ---- | ---- | ---- | ---- | ------------------ | ---------------------------------------- |
| EC200U_CNLB     | All Netcom; China Mobile 4G; China Unicom 4G; China Telecom 4G | LTE-FDD: B1/B3/B5/B8<br/>LTE-TDD: B34/B38/B39/B40/B41<br/>   | 624MHz | total：8M     free：≈0.3M | free：≈450K           | 16   | 3    | 1    | 1    | 3    | 4     | *     | Y    | Y      | Y    | *    | *    | Y    | Y    | 3.4 to 4.3         | -40 to +105                              |
| EC200U_EUAB     | All Netcom; China Mobile 4G; China Unicom 4G; China Telecom 4G; China Mobile 2G; China Unicom 2G; China Telecom 2G， | LTE-FDD: B1/B3/B5/B8<br/>LTE-TDD: B34/B38/B39/B40/B41<br/>GSM: 900/1800 MHz | 624MHz | total：8M     free：≈0.3M | free：≈450K           | 16   | 3    | 1    | 1    | 3    | 4     | *     | Y    | Y      | Y    | *    | *    | Y    | Y    | 3.4 to 4.3         | -40 to +105                              |
| EC600U_CNLB     | All Netcom; China Mobile 4G; China Unicom4G;  China Telecom 4G | FDD B1/B3/B5/B8<br/>TDD B34/B38/B39/B40/B41                  | 624MHz | total：8M     free：≈0.3M | free：≈450K           | 16   | 3    | 1    | 1    | 4    | 4     | *     | Y    | Y      | Y    | *    | *    | Y    | Y    | 3.4 to 4.3         | -40 to +105                              |
| EC600U_EUAB     | All Netcom; China Mobile 4G; China Unicom4G; China Telecom 4G | FDD B1/B3/B5/B7/B8/B20/B28<br/>TDD B38/B40/B41<br/>GSM B2/B3/B5/B8 | 624MHz | total：8M     free：≈0.3M | free：≈450K           | 16   | 3    | 1    | 1    | 4    | 4     | *     | Y    | Y      | Y    | *    | *    | Y    | Y    | 3.4 to 4.3         | -40 to +105                              |
| EC600N_CNLC     | All Netcom; China Mobile 4G; China Unicom4G; China Telecom 4G | FDD B1/B3/B5/B8<br/>TDD B34/B38/B39/B40/B41                  | 624MHz | total：16M     free：≈1M  | free：≈450K           | 29   | 3    | 1    | 1    | 1    | 4     | Y     | Y    | N      | *    | *    | *    | N    | Y    | 3.4 to 4.3         | -40 to +105                              |
| EC600N_CNLA     | All Netcom; China Mobile 4G; China Unicom4G; China Telecom 4G | FDD B1/B3/B5/B8<br/>TDD B34/B38/B39/B40/B41                  | 624MHz | total：8M     free：≈0.3M | free：≈450K           | 29   | 3    | 1    | 1    | 1    | 4     | N     | Y    | N      | N    | N    | *    | N    | Y    | 3.4 to 4.3         | -40 to +105                              |
| EC600S_CNLA     | All Netcom; China Mobile 4G; China Unicom4G; China Telecom 4G | FDD B1/B3/B5/B8<br/>TDD B34/B38/B39/B40/B41                  | 624MHz | total：16M     free：≈1M  | free：≈450K           | 29   | 3    | 1    | 1    | 2    | 4     | N     | Y    | N      | N    | N    | *    | N    | Y    | 3.4 to 4.3         | -40 to +105                              |
| EC600S_CNLB     | All Netcom; China Mobile 4G;China Unicom4G， China Telecom 4G | FDD B1/B3/B5/B8<br/>TDD B34/B38/B39/B40/B41                  | 624MHz | total：8M     free：≈0.3M | free：≈350K           | 29   | 3    | 1    | 1    | 2    | 4     | N     | Y    | Y      | N    | N    | *    | N    | Y    | 3.4 to 4.3         | -40 to +105                              |

The * means under development

The "Y" means support

The "N" means do not support



**Supported external sensors directly**

| Part number | Sunlight                | 3-axis             | Temperature and | Amplifier  |
| ----------- | ----------------------- | ------------------ | --------------- | ---------- |
| EC200U_EUAB | GL5528、GL5516、OPT3001 | LIS2DH12TR、BMA250 | AHT10、HDC2080  | AW8733ATQR |
| EC200U_CNLB | GL5528、GL5516、OPT3001 | LIS2DH12TR、BMA250 | AHT10、HDC2080  | AW8733ATQR |
| EC600U_CNLB | GL5528、GL5516、OPT3001 | LIS2DH12TR、BMA250 | AHT10、HDC2080  | AW8733ATQR |
| EC600U_EUAB | GL5528、GL5516、OPT3001 | LIS2DH12TR、BMA250 | AHT10、HDC2080  | AW8733ATQR |
| EC600N_CNLA | GL5528、GL5516、OPT3001 | LIS2DH12TR、BMA250 | AHT10、HDC2080  | AW8733ATQR |
| EC600N_CNLC | GL5528、GL5516、OPT3001 | LIS2DH12TR、BMA250 | AHT10、HDC2080  | AW8733ATQR |
| EC600S_CNLA | GL5528、GL5516、OPT3001 | LIS2DH12TR、BMA250 | AHT10、HDC2080  | AW8733ATQR |
| EC600S_CNLB | GL5528、GL5516、OPT3001 | LIS2DH12TR、BMA250 | AHT10、HDC2080  | AW8733ATQR |



## Module footprint dimension

![Hardware_support_03(E)](media\Hardware_support_03.png)