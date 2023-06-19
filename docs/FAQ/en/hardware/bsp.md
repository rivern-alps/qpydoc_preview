# BSP开发常见问题

## BSP外设对应PIN关系。

查看WIKI官网machine章节进行确认。新开模组咨询FAE确认。

## 模组BSP外设资源数量。

查看WIKI官网machine章节进行确认。新开模组咨询FAE确认。

## 开发板外设对应PIN关系。

查看开发板对应原理图文件，确认引出外设与模组的PIN脚关系，后查看WIKI官网machine章节进行确认。

## LCD外设最大驱动像素。

屏幕像素不得超过500*500。

## QuecPython是否支持DAC？

QuecPython目前不支持DAC这个功能。

## QuecPython_ADC的电压范围是多少？

EC600U：0~VBAT；EC600N：0~1.3 V“；EC600S：0~1.3 V。其他型号查询模块对应硬件设计手册确认。

## QuecPython_IIC的通信速率。

可以设置标准模式与快速模式。标准模式100KHz，快速模式400KHz。

## USB是否可以进行数据交换。

UART3（USB_CDC口）可用于数据交互，就是模块的交换口。

