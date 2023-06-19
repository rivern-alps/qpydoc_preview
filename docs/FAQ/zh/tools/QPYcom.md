# QPYcom工具常见问题

### **上传到模组里面的源码文件安全吗？**

QPYcom下载工具有代码混淆加密功能，确保用户程序不被直接暴露。

### **在QPYCOM操作没有任何反应该怎么排查**

检查选择的串口是否正确并已打开。

### **QPYCOM工具是否有Mac系统，Linux系统的**

没有，目前只有windows系统的，Linux系统的暂不支持。

### **模块打开交互口之后QPYCOM怎么还是显示设备未连接？**

重启QPYcom工具，次之换线、换串口、重刷固件，最后重启电脑跟模块

### **QPYCOM刷固件应该选择哪个串口？**

不用选择并打开串口，工具会自动选择

### **用QPYCOM下载固件失败怎么排查？**

检查固件版本跟模块型号是否匹配，进入强制下模式之后烧录固件是否成功

### **拖动文件到模组工具提示出现语法错误**

请检查''.py''文件的语法问题（多数是缩进问题）

### **Win7运行QPYCOM出现"failed to execute script pyi_rth_multiprocessing"异常是为什么？**

故障现象：python通过pyinstaller打包后，在别的电脑运行失败“failed to execute script pyi_rth_multiprocessing”：在低版本windows7上运行会出现这个问题，在win10上面移植程序没问题。

故障分析：怀疑是windows某些dll文件版本过低，不支持高版本生成的exe，最简单的方法是：在win7机器上单独打个exe，然后在win7运行，移植。

建议客户的方法是：升级win7版本到sp1

### **QPYCOM工具只能烧录Python固件吗？**

QPYCOM工具只支持烧录python固件，不支持其它固件的烧录



