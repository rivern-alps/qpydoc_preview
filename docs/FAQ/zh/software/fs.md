# 文件系统常见问题

### **ql_fs模块的作用是什么**

- 提供`path_exists`方法，判断文件是否存在。

- 提供`file_copy`方法，快速拷贝文件。

- 提供`path_dirname`方法，获取最后一级路径的前缀路径名。

- 提供`path_getsize`方法，获取文件大小。

- 提供`mkdirs`方法，创建嵌套文件夹。

- 提供`rmdirs`方法，删除嵌套文件夹。

- 提供`touch`方法，快速创建文件。

- 提供`write_json`和`read_json`方法，快速读写json文件。

### **为什么用uos.remove()删除不了文件？**

检查文件是否关闭，已经打开的文件不能删除，必须要先关闭才能删除。

### **平台挂载SD卡的接口类型有哪些？**

展锐8910平台支持挂载SDIO-SD卡，ASR1603/1606平台支持挂载SPI-SD卡。

### **内置文件系统的类型是什么？**

- ECxxxM（EC800M-CNLC、EC800M-CNLF、EC800M-CNGC除外）、ECxxxN、ECxxxA、ECxxxG、ECxxxU、BC25 系列模组的内置文件系统类型为 littlefs 1.x。

- EC800M-CNLC、EC800M-CNLF、EC800M-CNGC、ECxxxE 系列模组的内置文件系统类型为 littlefs 2.x。

- BG 系列模组的内置文件系统类型为高通的 EFS 。

### **未关闭的文件直接删除或掉电会怎样？**

未关闭的文件直接删除或此时系统掉电将出现文件碎片，暂时没有脚本可以清理文件碎片。

### **关于flash寿命问题有什么需要注意的地方？**

尽量减少文件系统的写操作，写数据前最好先做数据判同处理，相同的数据不要重复写入。

写文件就是对flash的擦写操作，会加剧对flash寿命的损耗。

> 具有写flash操作的API有文件操作、net.setapn、dataCAll.setapn、system.setRelEnable、fota、appfota、sms存储等；AT指令中具有保存功能或重启生效功能的指令，均会写flash。

### **固件升级会清除文件系统数据吗？**

ECxxxM系列的模组支持最小系统全量升级，用户可根据需要选择升级文件系统数据，此时文件系统数据会被改变或清除。

其余系列的模组只能采用差分固件升级，不会改变或清除文件系统数据。
