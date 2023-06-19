# class Pin - 控制I/O引脚

该类提供GPIO读写操作。引脚是控制I/O的基本对象，它有设置引脚的模式(输入,输出等)、获取和设置数字逻辑电平的方法。

**示例：**

```python
from machine import Pin

# 创建gpio对象
gpio1 = Pin(Pin.GPIO1, Pin.OUT, Pin.PULL_DISABLE, 1)

# 获取引脚电平
gpio1.read()

# 设置引脚电平
gpio1.write(0)
gpio1.write(1)

# 设置输入输出模式
gpio1.set_dir(Pin.IN)
gpio1.set_dir(Pin.OUT)

# 获取输入输出模式
gpio1.get_dir()
```

## 构造函数

### `machine.Pin`

```python
class machine.Pin(GPIOn, direction, pullMode, level)
```

**参数描述：**

- `GPIOn` - GPIO号，int类型，<a href="#label_pinmap">点此查看</a>GPIO引脚编号与物理引脚的映射关系。
- `direction` - 输入输出模式，int类型，`IN` - 输入模式，`OUT` - 输出模式。
- `pullMode` - 上下拉模式，int类型，说明如下：<br />`PULL_DISABLE` - 浮空模式<br />`PULL_PU` - 上拉模式<br />`PULL_PD` - 下拉模式

- `level` - 引脚电平，int类型，`0` - 设置引脚为低电平, `1`- 设置引脚为高电平。

**示例：**

```python
>>> # 创建gpio对象
>>> from machine import Pin
>>> gpio1 = Pin(Pin.GPIO1, Pin.OUT, Pin.PULL_DISABLE, 0)
```

<span id="label_pinmap">**GPIO引脚编号与物理引脚的映射关系：**</span>

> GPIO对应引脚号说明：文档中提供的GPIO引脚号对应的为模块外部的引脚编号，例如EC100YCN下GPIO1对应引脚号22，这里的引脚号22为模块外部的引脚编号。可参考提供的硬件资料查看模块外部的引脚编号。

<details>
  <summary>EC100Y平台引脚对应关系<br /></summary>
GPIO1 – 引脚号22<br />GPIO2 – 引脚号23<br />GPIO3 – 引脚号38<br />GPIO4 – 引脚号53<br />GPIO5 – 引脚号54<br />GPIO6 – 引脚号104<br />GPIO7 – 引脚号105<br />GPIO8 – 引脚号106<br />GPIO9 – 引脚号107<br />GPIO10 – 引脚号178<br />GPIO11 – 引脚号195<br />GPIO12 – 引脚号196<br />GPIO13 – 引脚号197<br />GPIO14 – 引脚号198<br />GPIO15 – 引脚号199<br />GPIO16 – 引脚号203<br />GPIO17 – 引脚号204<br />GPIO18 – 引脚号214<br />GPIO19 – 引脚号215<br />
</details>

<details>
  <summary>EC600S/EC600N平台引脚对应关系</summary>
GPIO1 – 引脚号10<br />GPIO2 – 引脚号11<br />GPIO3 – 引脚号12<br />GPIO4 – 引脚号13<br />GPIO5 – 引脚号14<br />GPIO6 – 引脚号15<br />GPIO7 – 引脚号16<br />GPIO8 – 引脚号39<br />GPIO9 – 引脚号40<br />GPIO10 – 引脚号48<br />GPIO11 – 引脚号58<br />GPIO12 – 引脚号59<br />GPIO13 – 引脚号60<br />GPIO14 – 引脚号61<br />GPIO15 – 引脚号62<br/>GPIO16 – 引脚号63<br/>GPIO17 – 引脚号69<br/>GPIO18 – 引脚号70<br/>GPIO19 – 引脚号1<br/>GPIO20 – 引脚号3<br/>GPIO21 – 引脚号49<br/>GPIO22 – 引脚号50<br/>GPIO23 – 引脚号51<br/>GPIO24 – 引脚号52<br/>GPIO25 – 引脚号53<br/>GPIO26 – 引脚号54<br/>GPIO27 – 引脚号55<br/>GPIO28 – 引脚号56<br/>GPIO29 – 引脚号57<br />GPIO30 – 引脚号2<br />GPIO31 – 引脚号66<br />GPIO32 – 引脚号65<br />GPIO33 – 引脚号67<br />GPIO34 – 引脚号64<br />GPIO35 – 引脚号4<br />GPIO36 – 引脚号31<br />GPIO37 – 引脚号32<br />GPIO38 – 引脚号33<br />GPIO39 – 引脚号34<br />GPIO40 – 引脚号71<br />GPIO41 – 引脚号72<br />
</details>

<details>
  <summary>EC600M平台引脚对应关系</summary>
GPIO1 – 引脚号10<br />GPIO2 – 引脚号11<br />GPIO3 – 引脚号12<br />GPIO4 – 引脚号13<br />GPIO5 – 引脚号14<br />GPIO6 – 引脚号15<br />GPIO7 – 引脚号16<br />GPIO8 – 引脚号39<br />GPIO9 – 引脚号40<br />GPIO10 – 引脚号48<br />GPIO11 – 引脚号58<br />GPIO12 – 引脚号59<br />GPIO13 – 引脚号60<br />GPIO14 – 引脚号61<br />GPIO15 – 引脚号62<br/>GPIO16 – 引脚号63<br/>GPIO17 – 引脚号69<br/>GPIO18 – 引脚号70<br/>GPIO19 – 引脚号1<br/>GPIO20 – 引脚号3<br/>GPIO21 – 引脚号49<br/>GPIO22 – 引脚号50<br/>GPIO23 – 引脚号51<br/>GPIO24 – 引脚号52<br/>GPIO25 – 引脚号53<br/>GPIO26 – 引脚号54<br/>GPIO27 – 引脚号55<br/>GPIO28 – 引脚号56<br/>GPIO29 – 引脚号57<br />GPIO30 – 引脚号2<br />GPIO31 – 引脚号66<br />GPIO32 – 引脚号65<br />GPIO33 – 引脚号67<br />GPIO34 – 引脚号64<br />GPIO35 – 引脚号4<br />GPIO36 – 引脚号31<br />GPIO37 – 引脚号32<br />GPIO38 – 引脚号33<br />GPIO39 – 引脚号34<br />GPIO40 – 引脚号71<br />GPIO41 – 引脚号72<br />GPIO42 – 引脚号109<br />GPIO43 – 引脚号110<br />GPIO44 – 引脚号112<br />GPIO45 – 引脚号111<br/>
</details>

<details>
  <summary>EC600U平台引脚对应关系</summary>
GPIO1 – 引脚号61(不可与GPIO31同时为gpio)<br />GPIO2 – 引脚号58(不可与GPIO32同时为gpio)<br />GPIO3 – 引脚号34(不可与GPIO41同时为gpio)<br />GPIO4 – 引脚号60(不可与GPIO34同时为gpio)<br />GPIO5 – 引脚号69(不可与GPIO35同时为gpio)<br />GPIO6 – 引脚号70(不可与GPIO36同时为gpio)<br />GPIO7 – 引脚号123(不可与GPIO43同时为gpio)<br />GPIO8 – 引脚号118<br />GPIO9 – 引脚号9(不可与GPIO47同时为gpio)<br />GPIO10 – 引脚号1(不可与GPIO37同时为gpio)<br />GPIO11 – 引脚号4(不可与GPIO38同时为gpio)<br />GPIO12 – 引脚号3(不可与GPIO39同时为gpio)<br />GPIO13 – 引脚号2(不可与GPIO40同时为gpio)<br />GPIO14 – 引脚号54<br />GPIO15 – 引脚号57<br/>GPIO16 – 引脚号56<br/>GPIO17 – 引脚号12<br/>GPIO18 – 引脚号33(不可与GPIO42同时为gpio)<br/>GPIO19 – 引脚号124(不可与GPIO44同时为gpio)<br/>GPIO20 – 引脚号122(不可与GPIO45同时为gpio)<br/>GPIO21 – 引脚号121(不可与GPIO46同时为gpio)<br/>GPIO22 – 引脚号48<br/>GPIO23 – 引脚号39<br/>GPIO24 – 引脚号40<br/>GPIO25 – 引脚号49<br/>GPIO26 – 引脚号50<br/>GPIO27 – 引脚号53<br/>GPIO28 – 引脚号52<br/>GPIO29 – 引脚号51<br/>GPIO30 – 引脚号59(不可与GPIO33同时为gpio)<br/>GPIO31 – 引脚号66(不可与GPIO1同时为gpio)<br/>GPIO32 – 引脚号63(不可与GPIO2同时为gpio)<br/>GPIO33 – 引脚号67(不可与GPIO30同时为gpio)<br/>GPIO34 – 引脚号65(不可与GPIO4同时为gpio)<br/>GPIO35 – 引脚号137(不可与GPIO5同时为gpio)<br/>GPIO36 – 引脚号62(不可与GPIO6同时为gpio)<br/>GPIO37 – 引脚号98(不可与GPIO10同时为gpio)<br/>GPIO38 – 引脚号95(不可与GPIO11同时为gpio)<br/>GPIO39 – 引脚号119(不可与GPIO12同时为gpio)<br/>GPIO40 – 引脚号100(不可与GPIO13同时为gpio)<br/>GPIO41 – 引脚号120(不可与GPIO3同时为gpio)<br/>GPIO42 – 引脚号16(不可与GPIO18同时为gpio)<br/>GPIO43 – 引脚号10(不可与GPIO7同时为gpio)<br/>GPIO44 – 引脚号14(不可与GPIO19同时为gpio)<br/>GPIO45 – 引脚号15(不可与GPIO20同时为gpio)<br/>GPIO46 – 引脚号13(不可与GPIO21同时为gpio)<br/>GPIO47 – 引脚号99(不可与GPIO9同时为gpio)<br/>
</details>

<details>
  <summary>EC200U平台引脚对应关系</summary>
GPIO1 – 引脚号27(不可与GPIO31同时为gpio)<br />GPIO2 – 引脚号26(不可与GPIO32同时为gpio)<br />GPIO3 – 引脚号24(不可与GPIO33同时为gpio)<br />GPIO4 – 引脚号25(不可与GPIO34同时为gpio)<br />GPIO5 – 引脚号13(不可与GPIO17同时为gpio)<br />GPIO6 – 引脚号135(不可与GPIO36同时为gpio)<br />GPIO7 – 引脚号136(不可与GPIO44同时为gpio)<br />GPIO8 – 引脚号133<br />GPIO9 – 引脚号3(不可与GPIO37同时为gpio)<br />GPIO10 – 引脚号40(不可与GPIO38同时为gpio)<br />GPIO11 – 引脚号37(不可与GPIO39同时为gpio)<br />GPIO12 – 引脚号38(不可与GPIO40同时为gpio)<br />GPIO13 – 引脚号39(不可与GPIO41同时为gpio)<br />GPIO14 – 引脚号5<br />GPIO15 – 引脚号141<br/>GPIO16 – 引脚号142<br/>GPIO17 – 引脚号121(不可与GPIO5同时为gpio)<br/>GPIO18 – 引脚号65(不可与GPIO42同时为gpio)<br/>GPIO19 – 引脚号64(不可与GPIO43同时为gpio)<br/>GPIO20 – 引脚号139(不可与GPIO45同时为gpio)<br/>GPIO21 – 引脚号126(不可与GPIO46同时为gpio)<br/>GPIO22 – 引脚号127(不可与GPIO47同时为gpio)<br/>GPIO23 – 引脚号33<br/>GPIO24– 引脚号31<br/>GPIO25 – 引脚号30<br/>GPIO26 – 引脚号29<br/>GPIO27 – 引脚号28<br/>GPIO28 – 引脚号1<br/>GPIO29 – 引脚号2<br/>GPIO30 – 引脚号4<br/>GPIO31 – 引脚号125(不可与GPIO1同时为gpio)<br/>GPIO32 – 引脚号124(不可与GPIO2同时为gpio)<br/>GPIO33 – 引脚号123(不可与GPIO3同时为gpio)<br/>GPIO34 – 引脚号122(不可与GPIO4同时为gpio)<br/>GPIO35 – 引脚号42<br/>GPIO36 – 引脚号119(不可与GPIO6同时为gpio)<br/>GPIO37 – 引脚号134(不可与GPIO9同时为gpio)<br/>GPIO38– 引脚号132(不可与GPIO10同时为gpio)<br/>GPIO39 – 引脚号131(不可与GPIO11同时为gpio)<br/>GPIO40 – 引脚号130(不可与GPIO12同时为gpio)<br/>GPIO41 – 引脚号129(不可与GPIO13同时为gpio)<br/>GPIO42 – 引脚号61(不可与GPIO18同时为gpio)<br/>GPIO43 – 引脚号62(不可与GPIO19同时为gpio)<br/>GPIO44 – 引脚号63(不可与GPIO7同时为gpio)<br/>GPIO45 – 引脚号66(不可与GPIO20同时为gpio)<br/>GPIO46 – 引脚号6(不可与GPIO21同时为gpio)<br/>GPIO47 – 引脚号23(不可与GPIO22同时为gpio)<br/>
</details>

<details>
  <summary>EC200A平台引脚对应关系</summary>
GPIO1 – 引脚号27<br />GPIO2 – 引脚号26<br />GPIO3 – 引脚号24<br />GPIO4 – 引脚号25<br />GPIO5 – 引脚号5<br />GPIO6 – 引脚号135<br />GPIO7 – 引脚号136<br />GPIO9 – 引脚号3<br />GPIO10 – 引脚号40<br />GPIO11 – 引脚号37<br />GPIO12 – 引脚号38<br />GPIO13 – 引脚号39<br />GPIO18 – 引脚号65<br />GPIO19 – 引脚号64<br />GPIO20 – 引脚号139<br />GPIO22 – 引脚号127<br />GPIO28 – 引脚号1<br />GPIO29 – 引脚号2<br />GPIO30 – 引脚号4<br />GPIO35 – 引脚号42<br />GPIO36 – 引脚号119<br />GPIO43 – 引脚号62<br />GPIO44 – 引脚号63(EC200ACN_LA不支持)<br />GPIO45 – 引脚号66<br />GPIO46 – 引脚号6<br />GPIO47 – 引脚号23<br/>
</details>

<details>
  <summary>EC800N平台引脚对应关系</summary>
GPIO1 – 引脚号30<br />GPIO2 – 引脚号31<br />GPIO3 – 引脚号32<br />GPIO4 – 引脚号33<br />GPIO5 – 引脚号49<br />GPIO6 – 引脚号50<br />GPIO7 – 引脚号51<br />GPIO8 – 引脚号52<br />GPIO9 – 引脚号53<br />GPIO10 – 引脚号54<br />GPIO11 – 引脚号55<br />GPIO12 – 引脚号56<br />GPIO13 – 引脚号57<br />GPIO14 – 引脚号58<br />GPIO15 – 引脚号80<br/>GPIO16 – 引脚号81<br/>GPIO17 – 引脚号76<br/>GPIO18 – 引脚号77<br/>GPIO19 – 引脚号82<br/>GPIO20 – 引脚号83<br/>GPIO21 – 引脚号86<br/>GPIO22 – 引脚号87<br/>GPIO23 – 引脚号66<br/>GPIO24 – 引脚号67<br/>GPIO25 – 引脚号17<br/>GPIO26 – 引脚号18<br/>GPIO27 – 引脚号19<br/>GPIO28 – 引脚号20<br/>GPIO29 – 引脚号21<br />GPIO30 – 引脚号22<br />GPIO31 – 引脚号23<br />GPIO32 – 引脚号28<br />GPIO33 – 引脚号29<br />GPIO34 – 引脚号38<br />GPIO35 – 引脚号39<br />GPIO36 – 引脚号16<br />GPIO37 – 引脚号78<br />
</details>

<details>
  <summary>BC25PA平台引脚对应关系</summary>
GPIO1 – 引脚号3<br />GPIO2 – 引脚号4<br />GPIO3 – 引脚号5<br />GPIO4 – 引脚号6<br />GPIO5 – 引脚号16<br />GPIO6 – 引脚号20<br />GPIO7 – 引脚号21<br />GPIO8 – 引脚号22<br />GPIO9 – 引脚号23<br />GPIO10 – 引脚号25<br />GPIO11 – 引脚号28<br />GPIO12 – 引脚号29<br />GPIO13 – 引脚号30<br />GPIO14 – 引脚号31<br />GPIO15 – 引脚号32<br/>GPIO16 – 引脚号33<br/>GPIO17 – 引脚号2<br/>GPIO18 – 引脚号8<br/>
</details>

<details>
  <summary>BG95M3平台引脚对应关系</summary>
GPIO1 – 引脚号4<br />GPIO2 – 引脚号5<br />GPIO3 – 引脚号6<br />GPIO4 – 引脚号7<br />GPIO5 – 引脚号18<br />GPIO6 – 引脚号19<br />GPIO7 – 引脚号22<br />GPIO8 – 引脚号23<br />GPIO9 – 引脚号25<br />GPIO10 – 引脚号26<br />GPIO11 – 引脚号27<br />GPIO12 – 引脚号28<br />GPIO13 – 引脚号40<br />GPIO14 – 引脚号41<br />GPIO15 – 引脚号64<br/>GPIO16 – 引脚号65<br/>GPIO17 – 引脚号66<br />GPIO18 – 引脚号85<br />GPIO19 – 引脚号86<br />GPIO20 – 引脚号87<br />GPIO21 – 引脚号88<br />
</details>

<details>
  <summary>EG915U平台引脚对应关系</summary>
GPIO1 – 引脚号4(不可与GPIO41同时为gpio)<br />GPIO2 – 引脚号5(不可与GPIO36同时为gpio)<br />GPIO3 – 引脚号6(不可与GPIO35同时为gpio)<br />GPIO4 – 引脚号7(不可与GPIO24同时为gpio)<br />GPIO5 – 引脚号18<br />GPIO6 – 引脚号19<br />GPIO7 – 引脚号1(不可与GPIO37同时为gpio)<br />GPIO8 – 引脚号38<br />GPIO9 – 引脚号25<br />GPIO10 – 引脚号26<br />GPIO11 – 引脚号27(不可与GPIO32同时为gpio)<br />GPIO12 – 引脚号28(不可与GPIO31同时为gpio)<br />GPIO13 – 引脚号40<br />GPIO14 – 引脚号41<br />GPIO15 – 引脚号64<br/>GPIO16 – 引脚号20(不可与GPIO30同时为gpio)<br/>GPIO17 – 引脚号21<br/>GPIO18 – 引脚号85<br/>GPIO19 – 引脚号86<br/>GPIO20 – 引脚号30<br/>GPIO21 – 引脚号88<br/>GPIO22 – 引脚号36(不可与GPIO40同时为gpio)<br/>GPIO23 – 引脚号37(不可与GPIO38同时为gpio)<br/>GPIO24 – 引脚号16(不可与GPIO4同时为gpio)<br/>GPIO25 – 引脚号39<br/>GPIO26 – 引脚号42(不可与GPIO27同时为gpio)<br/>GPIO27 – 引脚号78(不可与GPIO26同时为gpio)<br/>GPIO28 – 引脚号83(不可与GPIO33同时为gpio)<br/>GPIO29 – 引脚号84<br />GPIO30 – 引脚号92(不可与GPIO16同时为gpio)<br />GPIO31 – 引脚号95(不可与GPIO12同时为gpio)<br />GPIO32 – 引脚号97(不可与GPIO11同时为gpio)<br />GPIO33 – 引脚号98(不可与GPIO28同时为gpio)<br />GPIO34 – 引脚号104<br />GPIO35 – 引脚号105(不可与GPIO3同时为gpio)<br />GPIO36 – 引脚号106(不可与GPIO2同时为gpio)<br />GPIO37 – 引脚号108(不可与GPIO4同时为gpio)<br />GPIO38 – 引脚号111(不可与GPIO23同时为gpio)<br />GPIO39 – 引脚号114<br />GPIO40 – 引脚号115(不可与GPIO22同时为gpio)<br />GPIO41 – 引脚号116(不可与GPIO1同时为gpio)<br />
</details>

<details>
  <summary>EC800M平台引脚对应关系</summary>
GPIO1 – 引脚号30<br />GPIO2 – 引脚号31<br />GPIO3 – 引脚号32<br />GPIO4 – 引脚号33<br />GPIO5 – 引脚号49<br />GPIO6 – 引脚号50<br />GPIO7 – 引脚号51<br />GPIO8 – 引脚号52<br />GPIO9 – 引脚号53<br />GPIO10 – 引脚号54<br />GPIO11 – 引脚号55<br />GPIO12 – 引脚号56<br />GPIO13 – 引脚号57<br />GPIO14 – 引脚号58<br />GPIO15 – 引脚号80<br/>GPIO16 – 引脚号81<br/>GPIO17 – 引脚号76<br/>GPIO18 – 引脚号77<br/>GPIO19 – 引脚号82<br/>GPIO20 – 引脚号83<br/>GPIO21 – 引脚号86<br/>GPIO22 – 引脚号87<br/>GPIO23 – 引脚号66<br/>GPIO24 – 引脚号67<br/>GPIO25 – 引脚号17<br/>GPIO26 – 引脚号18<br/>GPIO27 – 引脚号19<br/>GPIO28 – 引脚号20<br/>GPIO29 – 引脚号21<br />GPIO30 – 引脚号22<br />GPIO31 – 引脚号23<br />GPIO32 – 引脚号28<br />GPIO33 – 引脚号29<br />GPIO34 – 引脚号38<br />GPIO35 – 引脚号39<br />GPIO36 – 引脚号16<br />GPIO37 – 引脚号78<br />GPIO38 – 引脚号68<br />GPIO39 – 引脚号69<br />GPIO40 – 引脚号74<br />GPIO41 – 引脚号75<br />GPIO42 – 引脚号84<br />GPIO43 – 引脚号85<br />GPIO44 – 引脚号25<br />
</details>

<details>
  <summary>EG912N平台引脚对应关系</summary>
GPIO1 – 引脚号4<br />GPIO2 – 引脚号5<br />GPIO3 – 引脚号6<br />GPIO4 – 引脚号7<br />GPIO5 – 引脚号18<br />GPIO6 – 引脚号19<br />GPIO7 – 引脚号1<br />GPIO8 – 引脚号16<br />GPIO9 – 引脚号25<br />GPIO10 – 引脚号26<br />GPIO11 – 引脚号27<br />GPIO12 – 引脚号28<br />GPIO13 – 引脚号40<br/>GPIO14 – 引脚号41<br/>GPIO15 – 引脚号64<br/>GPIO16 – 引脚号20<br/>GPIO17 – 引脚号21<br/>GPIO18 – 引脚号30<br/>GPIO19 – 引脚号34<br/>GPIO20 – 引脚号35<br/>GPIO21 – 引脚号36<br/>GPIO22 – 引脚号37<br/>GPIO23 – 引脚号38<br/>GPIO24 – 引脚号39<br/>GPIO25 – 引脚号42<br />GPIO26 – 引脚号78<br />GPIO27 – 引脚号83<br />GPIO28 – 引脚号92<br />GPIO29 – 引脚号95<br />GPIO30 – 引脚号96<br />GPIO31 – 引脚号97<br />GPIO32 – 引脚号98<br />GPIO33 – 引脚号103<br />GPIO34 – 引脚号104<br />GPIO35 – 引脚号105<br />GPIO36 – 引脚号106<br />GPIO37 – 引脚号107<br />GPIO38 – 引脚号114<br />GPIO39 – 引脚号115<br />GPIO40 – 引脚号116
</details>

<details>
  <summary>EC600E平台引脚对应关系</summary>
注：<br />1.I&PU：输入模式下，仅支持浮空和上拉模式<br />2.I&PD：输入模式下，仅支持浮空和下拉模式<br />3.EC600E的ExtInt功能不支持上升和下降沿同时触发中断<br />GPIO1 – 引脚号10(I&PU)<br />GPIO2 – 引脚号11(I&PU)(不可与GPIO41同时为gpio)<br />GPIO3 – 引脚号12(I&PU)(不可与GPIO40同时为gpio)<br />GPIO4 – 引脚号13(I&PU)<br />GPIO5 – 引脚号14(I&PU)<br />GPIO6 – 引脚号15(I&PU)<br />GPIO7 – 引脚号16(I&PU)<br />GPIO8 – 引脚号39(I&PD)<br />GPIO9 – 引脚号40(I&PU)<br />GPIO10 – 引脚号48(I&PD)<br />GPIO11 – 引脚号58(I&PD)<br />GPIO12 – 引脚号59(I&PD)<br />GPIO13 – 引脚号60(I&PD)(不可与GPIO36同时为gpio)<br />GPIO14 – 引脚号61(I&PD)<br />GPIO15 – 引脚号62(I&PU)<br />GPIO16 – 引脚号63(I&PD)<br />GPIO17 – 引脚号69(I&PU)<br />GPIO18 – 引脚号70(I&PU)<br/GPIO22 – 引脚号50(I&PD)<br />GPIO23 – 引脚号51(I&PD)<br />GPIO24 – 引脚号52(I&PD)<br />GPIO25 – 引脚号53(I&PD)<br />GPIO26 – 引脚号54(I&PD)<br />GPIO31 – 引脚号66(I&PU)<br />GPIO32 – 引脚号65(I&PU)<br />GPIO33 – 引脚号67(I&PU)<br />GPIO34 – 引脚号64(I&PU)<br />GPIO36 – 引脚号31(I&PU)(不可与GPIO13同时为gpio)<br />GPIO37 – 引脚号32(I&PU)<br />GPIO38 – 引脚号33(I&PU)<br />GPIO39 – 引脚号34(I&PU)<br />GPIO40 – 引脚号71(I&PU)(不可与GPIO3同时为gpio)<br />GPIO41 – 引脚号72(I&PU)(不可与GPIO2同时为gpio)
</details>

<details>
  <summary>EC800E平台引脚对应关系</summary>
注：<br />1.I&PU：输入模式下，仅支持浮空和上拉模式<br />2.I&PD：输入模式下，仅支持浮空和下拉模式<br />3.EC800ECN_LE&LQ不可用：指该型号模块的引脚内部悬空，所以无法使用<br />4.模组的Pin67、Pin66 和Pin57、Pin58 共用内部同一路IO，即改变GPIO13的电平，Pin57和Pin67会同时变化<br />5.在EC800ECN_LE&LQ型号的模组上，Pin57、Pin58内部悬空，所以仅可使用Pin67、Pin66作为GPIO13、14<br />6.EC800E的ExtInt功能不支持上升和下降沿同时触发中断<br />GPIO1 – 引脚号30(I&PD)<br />GPIO2 – 引脚号31(I&PD)<br />GPIO3 – 引脚号32(I&PD)<br />GPIO4 – 引脚号33(I&PD)(不可与GPIO25同时为gpio)<br />GPIO5 – 引脚号49(I&PD)(EC800ECN_LE&LQ不可用)<br />GPIO6 – 引脚号50(I&PU)(EC800ECN_LE&LQ不可用)<br />GPIO7 – 引脚号51(I&PU)(EC800ECN_LE&LQ不可用)<br />GPIO8 – 引脚号52(I&PU)(EC800ECN_LE&LQ不可用)<br />GPIO9 – 引脚号53(I&PU)(EC800ECN_LE&LQ不可用)<br />GPIO10 – 引脚号54(I&PU)(EC800ECN_LE&LQ不可用)<br />GPIO11 – 引脚号55(I&PU)(EC800ECN_LE&LQ不可用)<br />GPIO12 – 引脚号56(I&PU)(EC800ECN_LE&LQ不可用)<br />GPIO13 – 引脚号57(67)(I&PU)(EC800ECN_LE&LQ引脚号57无法使用)(不可与GPIO34同时为gpio)<br />GPIO14 – 引脚号58(66)(I&PU)(EC800ECN_LE&LQ引脚号58无法使用)(不可与GPIO35同时为gpio)<br />GPIO15 – 引脚号80(I&PU)(EC800ECN_LE&LQ不可用)<br/>GPIO16 – 引脚号81(I&PU)(EC800ECN_LE&LQ不可用)<br/>GPIO17 – 引脚号25(I&PD)<br/>GPIO25 – 引脚号17(I&PU)(不可与GPIO4同时为gpio)<br/>GPIO26 – 引脚号18(I&PU)<br/>GPIO27 – 引脚号19(I&PD)<br/>GPIO28 – 引脚号20(I&PU)<br/>GPIO29 – 引脚号21(I&PD)<br />GPIO30 – 引脚号22(I&PU)<br />GPIO31 – 引脚号23(I&PU)<br />GPIO32 – 引脚号28(I&PU)<br />GPIO33 – 引脚号29(I&PU)<br />GPIO34 – 引脚号38(I&PU)(不可与GPIO13同时为gpio)<br />GPIO35 – 引脚号39(I&PU)(不可与GPIO14同时为gpio)<br />GPIO36 – 引脚号16(I&PD)<br />GPIO37 – 引脚号78(I&PU)(EC800ECN_LE&LQ不可用)<br />GPIO38 – 引脚号85(I&PD)(EC800ECN_LE&LQ&LC不可用)<br />GPIO39 – 引脚号108(I&PD)(EC800ECN_LE&LQ&LC不可用)<br />GPIO40 – 引脚号109(I&PD)(EC800ECN_LE&LQ&LC不可用)
</details>



## 方法

### `Pin.read`

```python
Pin.read()
```

该方法用于读取PIN脚电平。

**返回值描述：**

返回引脚电平，`0`表示获取到的引脚电平为低电平，`1` 表示获取到的引脚电平为高电平。

### `Pin.write`

```
Pin.write(value)
```

该方法用于设置PIN脚电平。

> 设置高低电平前需要保证引脚为输出模式。

**参数描述：**

- `value` - 引脚电平，int类型，`0`表示设置当前PIN脚输出低电平，`1`表示设置当前PIN脚输出高电平。

**返回值描述：**

设置成功返回整型值`0`，设置失败返回整型值`-1`。

**示例：**

```python
>>> from machine import Pin
>>> gpio1 = Pin(Pin.GPIO1, Pin.OUT, Pin.PULL_DISABLE, 0)
>>> gpio1.write(1)
0
>>> gpio1.read()
1
```

### `Pin.set_dir`

```python
Pin.set_dir(value)
```

该方法用于设置PIN脚GPIO的输入输出模式。

**参数描述：**

- `value` - 引脚电平，int类型，说明如下：<br />`Pin.IN` : `0` - 输入模式<br />`Pin.OUT` : `1` - 输出模式

**返回值描述：**

设置成功返回整型值`0`，设置失败返回整型值`-1`。

### `Pin.get_dir`

```python
Pin.get_dir()
```

该方法用于获取PIN脚GPIO的输入输出模式。

**返回值描述：**

返回PIN脚输入输出模式，`0`表示输入模式，`1` 表示输出模式。

**示例：**

```python
>>> from machine import Pin
>>> gpio1 = Pin(Pin.GPIO1, Pin.OUT, Pin.PULL_DISABLE, 0)
>>> gpio1.get_dir()
1
>>> gpio1.set_dir(Pin.IN)
0
>>> gpio1.get_dir()
0
```

## 常量

| 常量             | 适配平台                                                     | 说明     |
| ---------------- | ------------------------------------------------------------ | -------- |
| Pin.GPIO1        | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG810M/EG912N/EC600E/EC800E | GPIO1    |
| Pin.GPIO2        | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG810M/EG912N/EC600E/EC800E | GPIO2    |
| Pin.GPIO3        | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG810M/EG912N/EC600E/EC800E | GPIO3    |
| Pin.GPIO4        | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG810M/EG912N/EC600E/EC800E | GPIO4    |
| Pin.GPIO5        | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG810M/EG912N/EC600E/EC800E | GPIO5    |
| Pin.GPIO6        | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG810M/EG912N/EC600E/EC800E | GPIO6    |
| Pin.GPIO7        | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG810M/EG912N/EC600E/EC800E | GPIO7    |
| Pin.GPIO8        | EC600S / EC600N / EC100Y/EC600U/EC200U/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG810M/EG912N/EC600E/EC800E | GPIO8    |
| Pin.GPIO9        | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG810M/EG912N/EC600E/EC800E | GPIO9    |
| Pin.GPIO10       | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG810M/EG912N/EC600E/EC800E | GPIO10   |
| Pin.GPIO11       | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG810M/EG912N/EC600E/EC800E | GPIO11   |
| Pin.GPIO12       | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG810M/EG912N/EC600E/EC800E | GPIO12   |
| Pin.GPIO13       | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG810M/EG912N/EC600E/EC800E | GPIO13   |
| Pin.GPIO14       | EC600S / EC600N / EC100Y/EC600U/EC200U/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG810M/EG912N/EC600E/EC800E | GPIO14   |
| Pin.GPIO15       | EC600S / EC600N / EC100Y/EC600U/EC200U/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG810M/EG912N/EC600E/EC800E | GPIO15   |
| Pin.GPIO16       | EC600S / EC600N / EC100Y/EC600U/EC200U/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG810M/EG912N/EC600E/EC800E | GPIO16   |
| Pin.GPIO17       | EC600S / EC600N / EC100Y/EC600U/EC200U/EC800N/BC25PA/BG95M3/EC600M/EG915U/EC800M/EG810M/EG912N/EC600E/EC800E | GPIO17   |
| Pin.GPIO18       | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/EC800N/BC25PA/BG95M3/EC600M/EG915U/EC800M/EG810M/EG912N/EC600E | GPIO18   |
| Pin.GPIO19       | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/EC800N/BG95M3/EC600M/EG915U/EC800M/EG810M/EG912N | GPIO19   |
| Pin.GPIO20       | EC600S / EC600N/EC600U/EC200U/EC200A/EC800N/BG95M3/EC600M/EG915U/EC800M/EG810M/EG912N | GPIO20   |
| Pin.GPIO21       | EC600S / EC600N/EC600U/EC200U/EC800N/BG95M3/EC600M/EG915U/EC800M/EG810M/EG912N | GPIO21   |
| Pin.GPIO22       | EC600S / EC600N/EC600U/EC200U/EC200A/EC800N/EC600M/EG915U/EC800M/EG810M/EG912N/EC600E | GPIO22   |
| Pin.GPIO23       | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG810M/EG912N/EC600E | GPIO23   |
| Pin.GPIO24       | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG810M/EG912N/EC600E | GPIO24   |
| Pin.GPIO25       | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG810M/EG912N/EC600E/EC800E | GPIO25   |
| Pin.GPIO26       | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG810M/EG912N/EC600E/EC800E | GPIO26   |
| Pin.GPIO27       | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG810M/EG912N/EC800E | GPIO27   |
| Pin.GPIO28       | EC600S / EC600N/EC600U/EC200U/EC200A/EC800N/EC600M/EG915U/EC800M/EG810M/EG912N/EC800E | GPIO28   |
| Pin.GPIO29       | EC600S / EC600N/EC600U/EC200U/EC200A/EC800N/EC600M/EG915U/EC800M/EG810M/EG912N/EC800E | GPIO29   |
| Pin.GPIO30       | EC600S / EC600N/EC600U/EC200U/EC200A/EC800N/EC600M/EG915U/EC800M/EG810M/EG912N/EC800E | GPIO30   |
| Pin.GPIO31       | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG810M/EG912N/EC600E/EC800E | GPIO31   |
| Pin.GPIO32       | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG810M/EG912N/EC600E/EC800E | GPIO32   |
| Pin.GPIO33       | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG810M/EG912N/EC600E/EC800E | GPIO33   |
| Pin.GPIO34       | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG810M/EG912N/EC600E/EC800E | GPIO34   |
| Pin.GPIO35       | EC600S / EC600N/EC600U/EC200U/EC200A/EC800N/EC600M/EG915U/EC800M/EG810M/EG912N/EC800E | GPIO35   |
| Pin.GPIO36       | EC600S / EC600N/EC600U/EC200U/EC200A/EC800N/EC600M/EG915U/EC800M/EG810M/EG912N/EC600E/EC800E | GPIO36   |
| Pin.GPIO37       | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG810M/EG912N/EC600E/EC800E | GPIO37   |
| Pin.GPIO38       | EC600S / EC600N/EC600U/EC200U/EC600M/EG915U/EC800M/EG810M/EG912N/EC600E/EC800E | GPIO38   |
| Pin.GPIO39       | EC600S / EC600N/EC600U/EC200U/EC600M/EG915U/EC800M/EG810M/EG912N/EC600E/EC800E | GPIO39   |
| Pin.GPIO40       | EC600S / EC600N/EC600U/EC200U/EC600M/EG915U/EC800M/EG810M/EG912N/EC600E/EC800E | GPIO40   |
| Pin.GPIO41       | EC600S / EC600N/EC600U/EC200U/EC600M/EG915U/EC800M/EG810M/EC600E/EC800E | GPIO41   |
| Pin.GPIO42       | EC600U/EC200U/EC600M/EC800M/EG810M                           | GPIO42   |
| Pin.GPIO43       | EC600U/EC200U/EC200A/EC600M/EC800M/EG810M                    | GPIO43   |
| Pin.GPIO44       | EC600U/EC200U/EC200A/EC600M/EC800M/EG810M                    | GPIO44   |
| Pin.GPIO45       | EC600U/EC200U/EC200A/EC600M                                  | GPIO45   |
| Pin.GPIO46       | EC600U/EC200U/EC200A                                         | GPIO46   |
| Pin.GPIO47       | EC600U/EC200U/EC200A                                         | GPIO47   |
| Pin.IN           | --                                                           | 输入模式 |
| Pin.OUT          | --                                                           | 输出模式 |
| Pin.PULL_DISABLE | --                                                           | 浮空模式 |
| Pin.PULL_PU      | --                                                           | 上拉模式 |
| Pin.PULL_PD      | --                                                           | 下拉模式 |
