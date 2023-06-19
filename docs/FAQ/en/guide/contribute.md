# 贡献指南

我们欢迎对 QuecPython-FAQ 项目做出贡献，如修复错误，添加文档等。我们通过 [Github Pull Requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) 接受贡献。

## 提交流程

这一节，是对 `新增问题` 和 `修改问题` 两个操作的流程简要介绍，流程中涉及的环节具体要求，请点击链接查看。

针对 git 相关操作不做具体的介绍，可以查看 [Git 相关教程](https://git-scm.com/book/zh/v2)。

### 新增问题

1. 在本地 [新建分支](#新建分支)，遵循 [分支命名规范](#分支命名规范)；

2. 在本地或者 web IDE 找到与问题类型对应的 `*.md` 文件，根据模板格式新增问题；

3. 编辑完成后，打开预览界面查看显示结果是否符合预期，可以使用 [本地编译环境](#本地编译环境) 编译文档，并检查生成网页是否满足；

4. 遵循 [提交信息规范](#提交信息规范)，推送到 github 后并提交 Pull Requests；

5. 若满足上述预期，则 [提交合并请求](#提交合并请求)；

6. 待文档所有讨论解决并成功提交 PR，即完成新增问题的流程。

### 修改问题

1. 在本地 [新建分支](#新建分支)，遵循 [分支命名规范](#分支命名规范)；

2. 在本地或者 web IDE 找到与问题类型对应的 `*.rst` 文件，修改期望修改的问题；

3. 编辑完成后，打开预览界面查看显示结果是否符合预期，可以使用 [本地编译环境](#本地编译环境) 编译文档，并检查生成网页是否满足；

4. 遵循 [提交信息规范](#提交信息规范)，推送到 github 后并提交 Pull Requests；

5. 若满足上述预期，则 [提交合并请求](#提交合并请求)；

6. 待文档所有讨论解决并成功提交 PR，即完成修改的流程

## 新建分支

新建分支都基于 **主分支** 进行；操作时，请留意当前所在分支是否为你期望合入的分支。

操作示例:

```bash
git status # 查看当前分支
git checkout -b add/API-reference_machine_pin # 用于新增问题 "API-reference_machine pin"
```

## 分支命名规范

- 新增问题：`add/API-reference_{q&a}`，`{q&a}` 使用文件名的英语简要，例如新增 `API-reference_machine pin` 问题，分支名：`add/API-reference_machine_pin`。

- 修改问题：`mod/API-reference_{q&a}`，`{q&a}` 使用文件名的英语简要，例如修改 `API-reference_machine pin` 问题，分支名：`mod/API-reference_machine_pin`。

## 问题编辑规范

请按照以下格式规范规则添加或更新 Q&A：

**通用规则：**

- 添加新的 Q&A 时，切记将问题作为三级标题，并添加数字编号。

- 示例：`### 1. CAT1下行带宽是多少？`

**问题格式：**

- 须简洁清晰地描述问题，如：
  - QPYcom 烧录固件失败。**（问题不清晰）**
  - QPYcom 烧录固件失败，如何解决？**（清晰）**

- 问题不宜过长。如描述太多，可精炼出主要的问题作为标题，并在回答的正文中详细描述问题背景及细节。

**答案格式：**

- 如正文中需引用代码，请使用 code 语法将其与文字隔开。

- 如某个问题的回答仅包含一句话，则使用正常段落书写即可，无需使用列表。

- 需要列举多个条目或排列顺序时，请使用列表：

  - 数字列表：有一定顺序（如操作步骤），或后文中需引用列表中的某个条目。

  - 项目符号列表：无特定顺序。

- 列表前需有介绍性文字，说明下述列表的含义或目的，且以冒号“：”结尾。

- 如两项条目是互为选择的关系，应使用项目符号列表罗列（非数字列表），并在段前介绍性文字中说明这二者的关系。

- 正文中（不论列表还是段落），每一行之前需空两格。

- 如某项条目后需跟注释或说明性文字，应缩进该注释，使其成为子条目。

## 本地编译环境

- 测试验证环境使用 Windows10 及以上版本、Ubuntu 或 Debian 系统，配置 python 环境为 `3.6` 及以上版本。
- 推荐使用 python 虚拟环境，或者 docker 环境。

```bash
# 安装 python3 与虚拟环境（Windows系统直接双击 python3 exe 安装包即可）

sudo apt-get install python3 python3-pip python3-venv

# 创建虚拟环境（Windows系统下的路径为 path\to\.pyenv3，path/to意为真实的路径）

python3 -m venv path/to/.pyenv3

# 激活虚拟环境（Windows系统需在工作目录下执行 path\to\.pyenv3\Scripts\activate.bat）

source path/to/.pyenv3/bin/activate

# 安装teedoc

pip3 install teedoc

# 获取源文件

git clone https://gitee.com/qpy-doc-center/teedoc_with_qpydoc.git

# 安装插件

cd teedoc_with_qpydoc
teedoc install

# 编译并启动服务（追加 -s 选项，用于启动服务）
./build.sh -s
```

## 提交信息规范

在分支上添加提交信息，以说明添加/修改/删除问题功能。每个提交都有一条消息，例如：

```text
API-reference_machine_pin: add 'value' method for machine.Pin class.

1. add 'value' method for machine.Pin class.
```

提交信息的第一行应类似于“问题类别：添加/修复/删除/更改内容”。第一行以提交要更改的文件名的名称开头。例如：

`API-reference_machine_pin: add 'value' method for machine.Pin class.`

要添加有关该提交的更多详细信息，请将其放在第一行之后的提交消息中。

一个好的 git 提交消息讲述了一个为什么发生更改的故事，因此，阅读提交日志的人可以了解项目的开发。编写良好的提交信息现在看来似乎是在浪费时间，但是在将来尝试了解某些原因更改时，这对您和您的同事很有用（对我们的客户也有用）。

## 提交合并请求

一旦完成修改就可以对分支进行第一次提交，如果您需要进行更多的更改，请进行更多提交。完成您对该分支的所有提交后，提交合并请求。

我们使用 github 合并请求功能将分支合并到主分支中，步骤：

- 将您的分支推送到 github 仓库；

- 转到 teedoc_with_qpydoc，然后单击 “New pull request”；

- 选择您刚创建准备合并的分支，然后填写“合并请求”详细信息。

### 提交合并请求相关规范

- Title 要求:

    `add: 简要描述`

- Description 要求:

    `分点描述该合并修改的信息。`

- 示例：

    Title:

    `API-reference_machine_pin: add 'value' method for machine.Pin class.`

    Description:

    `1. add 'value' method for machine.Pin class.`
