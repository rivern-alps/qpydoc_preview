## About Document

**Revision history**

| Version | Date       | Author | Description          |
| ------- | ---------- | ------ | -------------------- |
| 1.0     | 2021-04-07 | Chic   | Initial Version      |
| 1.1     | 2021-09-06 | Chic   | Updated Some Figures |



## Code Protection

- Login official website and select"download”, then find " **QPYcom Graphical Tool** "  by selecting the " **Resource** " in first category and " **Tool** " in second category comprehensively. Please refer to the figure below.  

![Mass_production_index_01](media\Mass_production_index_01.png)

- After opening QPYcom, there are " **Encryption **" and " **Backup** " in " **Download** " selection bar.
- The encryption is used to safeguard APP codes, after that, the source codes will be covered.
- Once the backup capability is enabled, if the backup file in **usr** partition is lost or modified on purpose; it will be retrieved in the **bak** partition automatically. 

![Mass_production_index_02](media\Mass_production_index_02.png)



## Generate Mass Production Firmware packages via QPYcom

After merging source codes, the production will be accomplished by flashing Firmware for one time as during the process of merging, the file of **usr** partition has been embedded into the Firmware.

### Condition

- The *main.py* code should be contained in the merged *.py* file. 

- ：While in *main.py* code, following two sentences should be involved: 

  ​		PROJECT_NAME = 'QUEC_TEST'  #  It is a must to have this sentence for merging

  ​		PROJECT_VERSION = '1.0.0'  #  It is a must to have this sentence for merging

**Note** 

In all merged **.py** files,  the *main.py* is used as program entrance, which will not be encrypted by tool automatically. Therefore, when writing in codes, it is safer to call the interface of other file in *main.py*.

### Case

In *main.py* file

```python
from usr import user_file  # User .py file is placed under usr path, therefore, there is a need to import APP via from usr
                             
import utime

PROJECT_NAME = 'QUEC_TEST'  # It is a must to have this sentence for merging merged
PROJECT_VERSION = '1.0.0'  # It is a must to have this sentence for merging

if __name__ == "__main__":  # Standard Version, start to execute from main.py.
    while True:
        user_file.Qprint()
        user_file.Qlistdir()
        utime.sleep_ms(300)
        
```

In *user_file.py* file: 

```python
import uos

def Qprint():
    print('Hello World !')

def Qlistdir():
    print(uos.listdir('/usr'))
    
```

Add *main.py* and *user_file.py* files as above into *usr* partition. In terms of firmware, it is suggested to use the latest version that published on the official website. Or you can find the firmware corresponding to module version in [Download Area.](https://python.quectel.com/download)

The merged firmware shall be saved in the path that assigned by user. Take the firmware package of <QUEC_TEST_1.0.0.zip> as an example,  the name of which is composed by two variates in *main.py* file: **PROJECT_NAME** and **PROJECT_VERSION**.

![Mass_production_index_03](media\Mass_production_index_03.png)

The merging will be done within few seconds. 

![Mass_production_index_04](media\Mass_production_index_04.png)

After merging, the file name is composed by **PROJECT_NAME** and **PROJECT_VERSION **- two variates in *main.py* file.  

![Mass_production_index_05](media\Mass_production_index_05.png)

Flash the merged firmware. the *main.py* will run automatically when starting up. 

![Mass_production_index_06](media\Mass_production_index_06.png)

## Mass Production Tool 

- Login official website and select"download”, then find " **QMulti_DL batch download tool** "  by selecting the " **Resource** " in first category and " **Tool** " in second category comprehensively. For details, please refer to the figure below.  

![Mass_production_index_07](media\Mass_production_index_07.png)

- When Opening SW, select the merged FW in " **Load FW Files** "; then click " **Auto ALL** " ,  these 8 channels will be detected automatically till the flash is accomplished. 

  1. Firstly, Link the fixture to PC via USB.

  2. Secondly, open **" QMulti_DL batch download tool " ** in PC and select the FW that going to be flashed.  The SW will detect the flash automatically afterwards. 

![Mass_production_index_08](media\Mass_production_index_08.png)

**Reminder**

As long as there is one communication module is connected to power supply in fixture, it will be flashed automatically.

Once the flash is a failure or unexpected stop occurs, just power on the module again, the flash will carry on. 

## Download matched codes

 <a href="code/main.zip" target="_blank">Download matched code pattern</a>

 <a href="code/fota.zip" target="_blank">Download DFOTA package lesson and tool</a>



## Appendix A : Referential Document and Abbreviation 

Tablet 1:  Referential documents

| No.  | Document Name                        | Description                   | Location                      |
| ---- | ------------------------------------ | ----------------------------- | ----------------------------- |
| [1]  | Quectel QuecPython_QPYcom_User Guide | Application Note of QPYcom    | Involved in the QPYcom zip    |
| [2]  | Quectel_QMulti_DL_User Guide         | Appilcation Note of QMulti_DL | Involved in the QMulti_DL zip |



Tablet 2: Term Abbreviation 

| Term | Full Name in English |
| ---- | -------------------- |
| USB  | Universal Serial Bus |
