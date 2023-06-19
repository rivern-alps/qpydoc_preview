# QuecPython FAQ文档编写注意事项

## 目录结构

FAQ 文档根目录下存在一个名为`README.md`的文件，作为FAQ的首页入口。

> 文档中心使用的[teedoc](https://gitee.com/teedoc)架构要求每个版块的首页文件都要是名为`README.md`的文件。

根目录下有多个以`常见问题`结尾的md文件，每个文件对应一个大类。

所有md文件中引用的图片，均存放于media目录中：
- 图片统一为png格式，命名请见名知意，如`BSP.xxx.png`，其中`xxx`表示用简短英文编写的图片作用描述。

目录结构示例如下：

```
QuecPython官网文档中心/FAQ
├── BSP开发常见问题.md
├── Note.md
├── Python基础常见问题.md
├── QuecPython应用框架常见问题.md
├── README.md
├── media
│   └── BSP.xxx.png
├── 云平台对接常见问题.md
├── 图形化界面开发常见问题.md
├── 外设应用开发常见问题.md
├── 多线程开发常见问题.md
├── 开发工具使用常见问题.md
├── 网络通信开发常见问题.md
├── 蓝牙开发常见问题.md
└── 解决方案开发常见问题.md
```

## README.md

README.md作为板块的首页入口，需要对该板块做综合性描述，并且在最后提供板块的所有二级目录链接。

## 正文内容格式

参照以下格式：

```markdown
# BSP开发常见问题

### **问题1描述**

问题1答案

### **问题2描述**

问题2答案
```

## QuecPython FAQ

[点此查看](./README.md)
