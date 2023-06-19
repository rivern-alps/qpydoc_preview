## Revision history

| Version | **Date**   | **Author** | Description     |
| :------ | ---------- | ---------- | --------------- |
| 1.0     | 2021-09-29 | felix      | Initial version |

## Preamble

In this document, it gives the detailed illustration on individual component of POC based on Helios_service. 

## Module explanation

Currently, POC only releases specified firmware for EC600N and EC600S. Customers can develop POC functionality based on this firmware.

About poc interfaces, please refer to wiki poc.  

The POC-related contents will be transplanted to HeliosSDK in the near future. 

## About resources

Then main resource consumption on POC can be divided into following aspects: 

​		（1）POC library itself RO:600KB :  

​		（2）LVGL (mainly on font library and disbuf) RO:500KB

​		（3）LCD: heap (horizontal resolution * vertical resolution*2)

​		（4）Heap consumed by audio when communicating (100K)

## HW configuration 

Currently, we POC supports two platforms- broadPTT and POCSTARS. 

SIM card: When deploying QuecPython POC, there is a need to add the sim into specific above platform; otherwise, the registration will be a failure. 

When deploying POC, normally, the GUI will be matched; as a result, a LCD is needed. As for the LCD driver, you can refer to （[Application notes on LCD](https://python.quectel.com/doc/doc/sbs/zh/sbs/lcd.html)）

A kind of POC, which is controlled by keys. 

​		

## SW components illustration 

It can be divided into following 7 aspects: 

​		（1）mmi :  Master. It plays the role of info center for receiving and handling info of all components 

​		（2）key: Monitor key status and report it to mmi (key: Key function State: Key statue (long press, press, release))

​		（3）led: Response device status, which is controlled by mmi 

​		（4）net: Query SIM and network registration status, then report it to mmi

​		（5）broad: Realize POC and tts play

​		（6）LVGL: Realize the LCD driver and gui drawing 

​		（7）Timer:  Serve as Timer. It provides related timing function and serves component that needs time control, such as lock-screen and lock-keyboard. 

11 threads are scattered correspondingly (Bi-directional communication among these threads are relied on queue.)

![Poc_01(E)](media\Poc_01(E).png)

1. Provide key info to mmi based on queue (key & state)
2. Report network status to mmi based on queue (SIM card is not inserted, Sim ok, successful network register)
3. Provide UI selected by current key to mmi based on queue (enter group, network switch, lightness, ppt hint sound , key hint sound, lock screen lock key, power off, play menu from tts, on/off key sound)
4. Report poc status to mmi based on queue(Group change, member change in group, successful entrance to group, change on dial up status )
5. Report powerkey status to mmi based on queue
6. Control lvgl by mmi based on queue(screen switch, change status, change list, lock screen, unlock screen, key, lightness)
7. Control poc by mmi based on queue(initialize poc, cancel poc, enable poc log, login and logout poc, in/out group, dial up, get group list, get member list, play tts, set tts enabling and volume)
8. Control led by mmi based on queue (set sparkling, long time lightness, and off according to actual need)
9. Control key hint sound play by mmi based on interface. 



## In real scenarios

​      Take ST7789 (character LCD) and UC1603 (Black and white LCD) as examples.

<video id="video" controls="" preload="none"> <source id="mp4" src="media\poc_show_1.mp4" type="video/mp4"> </video>



<video id="video" controls="" preload="none"> <source id="mp4" src="media\poc_show_2.mp4" type="video/mp4"> </video>

## POC_solution directory structure



```
usr																		    # User partition
├─main.py 																	# User code(program entrance)
├─bin																		# Script and starter(some common services and public components are placed here)
│  ├─cloud_service.py														  # Cloud service components
│  ├─exception_service.py       											   # Exception srvice component
│  ├─guard.py                   									            # Guard and configure the starting container of files
│  ├─log_service.py             								       		    # Log service component
│  ├─media_service.py           							  				    # Media service component
│  ├─net_service.py             								 			    # Network service component
│  ├─pm_service.py              	    										# Power management service component
│  └─components                 								 				# Save some public components in this directory
│  │   ├─abstract_service.py   							  						# Abstract service
│  │   ├─blinker_min.py        								 					
│  │   ├─monitor.py            													
│  │   ├─OTA.py                													# OTA upgrade component
│  │   └─service_models.py     							 						# Service models
│  └─third_party                											
│       ├─ql_interrupter.py   								   					# Third party service component, such as external interrupter/watchdog
│       └─ ...
├─etc                            												# Configure file directory(not compulsory)
│   ├─app_config                												# Configure file directory of APP service
│   └─system_config             												# Configure file system of system service
├─log                            												# Log save service(not compulsory, which will be created when saving the log into local)
└─utils                            												# Common utility directory
│  ├─JsonParserUtils.py          												# Handle utils by json
│  ├─resolver.py                												# Reslover for time format
│  └─service_utils.py             												# Realize single case mode
|
|
└─poc_solution                            										# poc solution POC_solution file directory 
│  ├─config.json          														# Configure file,save some luminance values and volume values
│  ├─config_bak.py                												# Configure file backup
│  └─ql_enum.py 																# solution Certain public variant
│  └─ql_key.py 																	# solution Key realization component
│  └─ql_led.py 																	# solution LED realization component
│  └─ql_poc_broad.py 															# solution Poc function realization component
│  └─ql_poc_lvgl.py 															# solution GUI drawing and linkage component
│  └─ql_poc_mmi.py 																# solution mmi component
│  └─ql_poc_network.py 															# solution Network component
│  └─ql_poc_timer.py 															# solution Timer component
│  └─ ...

```

## Further development based on solution

### 1. How to add LCD

​		（1）Compile the driver of corresponding LCD, please refer to （[Application notes on LCD](https://python.quectel.com/doc/doc/sbs/zh/sbs/lcd.html)）

​		（2）Substitute the LCD-related code in LVGL components

​					1. Substitute the initialization parameter

​					2. Substitute the parameter for writing display

​					3. Substitute the parameter of locking screen and lighting up screen. 

​					4. Substitute the screen resolution

E.g. Substitute st7789 as ILI9225

​       Left: st7789 with a screen resolution of 240X240. Right: ILI9225 with a screen resolution of 176X220

| #ST7789<br />lcd_init_param=( <br/>2, 0, 120,<br/>0, 0, 0x11,<br/>0, 1, 0x36,<br/>1, 1, 0x00,<br/>0, 1, 0x36,<br/>1, 1, 0x00,<br/>0, 1, 0x3A,<br/>1, 1, 0x05,<br/>0, 0, 0x21,<br/>0, 5, 0xB2,<br/>1, 1, 0x05,<br/>1, 1, 0x05,<br/>1, 1, 0x00,<br/>1, 1, 0x33,<br/>1, 1, 0x33,<br/>0, 1, 0xB7,<br/>1, 1, 0x23,<br/>0, 1, 0xBB,<br/>1, 1, 0x22,<br/>0, 1, 0xC0,<br/>1, 1, 0x2C,<br/>0, 1, 0xC2,<br/>1, 1, 0x01,<br/>0, 1, 0xC3,<br/>1, 1, 0x13,<br/>0, 1, 0xC4,<br/>1, 1, 0x20,<br/>0, 1, 0xC6,<br/>1, 1, 0x0F,<br/>0, 2, 0xD0,<br/>1, 1, 0xA4,<br/>1, 1, 0xA1,<br/>0, 1, 0xD6,<br/>1, 1, 0xA1,<br/>0, 14, 0xE0,<br/>1, 1, 0x70,<br/>1, 1, 0x06,<br/>1, 1, 0x0C,<br/>1, 1, 0x08,<br/>1, 1, 0x09,<br/>1, 1, 0x27,<br/>1, 1, 0x2E,<br/>1, 1, 0x34,<br/>1, 1, 0x46,<br/>1, 1, 0x37,<br/>1, 1, 0x13,<br/>1, 1, 0x13,<br/>1, 1, 0x25,<br/>1, 1, 0x2A,<br/>0, 14, 0xE1,<br/>1, 1, 0x70,<br/>1, 1, 0x04,<br/>1, 1, 0x08,<br/>1, 1, 0x09,<br/>1, 1, 0x07,<br/>1, 1, 0x03,<br/>1, 1, 0x2C,<br/>1, 1, 0x42,<br/>1, 1, 0x42,<br/>1, 1, 0x38,<br/>1, 1, 0x14,<br/>1, 1, 0x14,<br/>1, 1, 0x27,<br/>1, 1, 0x2C,<br/>0, 0, 0x29,<br/>0, 1, 0x36,<br/>1, 1, 0x00,<br/>0, 4, 0x2a,<br/>1, 1, 0x00,<br/>1, 1, 0x00,<br/>1, 1, 0x00,<br/>1, 1, 0xef,<br/>0, 4, 0x2b,<br/>1, 1, 0x00,<br/>1, 1, 0x00,<br/>1, 1, 0x00,<br/>1, 1, 0xef,<br/>0, 0, 0x2c,<br/>)<br />lcd_invalid_param = (<br/>0,4,0x2a,<br/>1,1,XSTART_H,<br/>1,1,XSTART_L,<br/>1,1,XEND_H,<br/>1,1,XEND_L,<br/>0,4,0x2b,<br/>1,1,YSTART_H,<br/>1,1,YSTART_L,<br/>1,1,YEND_H,<br/>1,1,YEND_L,<br/>0,0,0x2c,<br/>)<br/><br/>lcd_displayon_param = (<br/>0,0,0x11,<br/>2,0,20,<br/>0,0,0x29,<br/>)<br/><br/>lcd_displayoff_param = (<br/>0,0,0x28,<br/>2,0,120,<br/>0,0,0x10,<br/>)<br /># Resolution<br/>LCD_SIZE_W = 240<br/>LCD_SIZE_H = 240 | ILI9225<br />lcd_init_param=( <br/>2, 0, 120,<br/>0,1,0x02,<br/>1,2,0x01,0x00,<br/>0,1,0x01,<br/>1,2,0x01,0x1C,<br/>0,1,0x03,<br/>1,2,0x10,0x30,<br/>0,1,0x08,<br/>1,2,0x08,0x08,<br/>0,1,0x0B,<br/>1,2,0x11,0x00,<br/>0,1,0x0C,<br/>1,2,0x00,0x00,<br/>0,1,0x0F,<br/>1,2,0x14,0x01,<br/>0,1,0x15,<br/>1,2,0x00,0x00,<br/>0,1,0x20,<br/>1,2,0x00,0x00,<br/>0,1,0x21,<br/>1,2,0x00,0x00,<br/>0,1,0x10,<br/>1,2,0x08,0x00,<br/>0,1,0x11,<br/>1,2,0x1F,0x3F,<br/>0,1,0x12,<br/>1,2,0x01,0x21,<br/>0,1,0x13,<br/>1,2,0x00,0x0F,<br/>0,1,0x14,<br/>1,2,0x43,0x49,<br/>0,1,0x30,<br/>1,2,0x00,0x00,<br/>0,1,0x31,<br/>1,2,0x00,0xDB,<br/>0,1,0x32,<br/>1,2,0x00,0x00,<br/>0,1,0x33,<br/>1,2,0x00,0x00,<br/>0,1,0x34,<br/>1,2,0x00,0xDB,<br/>0,1,0x35,<br/>1,2,0x00,0x00,<br/>0,1,0x36,<br/>1,2,0x00,0xAF,<br/>0,1,0x37,<br/>1,2,0x00,0x00,<br/>0,1,0x38,<br/>1,2,0x00,0xDB,<br/>0,1,0x39,<br/>1,2,0x00,0x00,<br/>0,1,0x50,<br/>1,2,0x00,0x01,<br/>0,1,0x51,<br/>1,2,0x20,0x0B,<br/>0,1,0x52,<br/>1,2,0x00,0x00,<br/>0,1,0x53,<br/>1,2,0x04,0x04,<br/>0,1,0x54,<br/>1,2,0x0C,0x0C,<br/>0,1,0x55,<br/>1,2,0x00,0x0C,<br/>0,1,0x56,<br/>1,2,0x01,0x01,<br/>0,1,0x57,<br/>1,2,0x04,0x00,<br/>0,1,0x58,<br/>1,2,0x11,0x08,<br/>0,1,0x59,<br/>1,2,0x05,0x0C,<br/>0,1,0x07,<br/>1,2,0x10,0x17,<br/>0,1,0x22,<br/>)<br />lcd_invalid_param = (<br/>0,1,0x36,<br/>1,2,XEND,<br/>0,1,0x37,<br/>1,2,XSTART,<br/>0,1,0x38,<br/>1,2,YEND,<br/>0,1,0x39,<br/>1,2,YSTART,<br/>0,1,0x20,<br/>1,2,XSTART,<br/>0,1,0x21,<br/>1,2,YSTART,<br/>0,1,0x22,<br/>)<br/><br/>lcd_displayon_param = (<br/>0,1,0x07,<br/>1,2,0x10,0x17,<br/>)<br/><br/>lcd_displayoff_param = (<br/>0,1,0x07,<br/>1,2,0x10,0x04,<br/>)<br /># Resolution<br/>LCD_SIZE_W = 176<br/>LCD_SIZE_H = 220 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |



### 2. How to add KEY

It is simple to add key, however, corresponding function items of individual key should be done in a proper way. 

Step to add key

​		（1）: Confirm key number and function

​		（2）: Handle key function

E. g.

​		Add PTT key

​		（1）: If make the PTT correspond to GPIO14, the call can be realized. 

​				 E. g:  KEY_PTT = Pin.GPIO14

​				Write the corresponding value into key_value in ql_key.py.

```
key_value = [
    (KEY_MENU, QUEC_MMI_KEY_MENU),
    (KEY_EXIT, QUEC_MMI_KEY_EXIT),
    (KEY_UP, QUEC_MMI_KEY_PF1),
    (KEY_DOWN, QUEC_MMI_KEY_PF2),
    (KEY_VOL_UP, QUEC_MMI_KEY_VOL_UP),
    (KEY_PTT, QUEC_MMI_KEY_PTT),		# It is valid to add this line
]
```



​		（2）: The KEY_PTT is reported to MMI in which the corresponding key function can be controlled. 

​              Confirm the PTT location in *ql_enum.py*. If there is none, you can add. 

```
QUEC_MMI_KEY_NULL = 0
QUEC_MMI_KEY_MENU = 1
QUEC_MMI_KEY_OK = 2
QUEC_MMI_KEY_EXIT = 3
QUEC_MMI_KEY_PF1 = 4
QUEC_MMI_KEY_PF2 = 5
QUEC_MMI_KEY_PTT = 6
QUEC_MMI_KEY_EXT_PTT = 7
QUEC_MMI_KEY_VOL_UP = 8
QUEC_MMI_KEY_VOL_DWON = 9
QUEC_MMI_KEY_MAX = 9
```

​			

​				Add the handling contents in *ql_poc_mmi.py*.  

```python
    def mmi_key_ptt(self,para):
        if(para[1] == MMI_MSG_FUNC_KEY_PRESS):
            print("call ...")
            self.ON_SPEAK = 1
            key_to_lvgl_data=[LVGL_CONTROL_STATUE_CHANGE, LVGL_CONTROL_STATUS_CALL, " Call"]
            ui.lvgl_queue_put(key_to_lvgl_data)
            key_to_poc_data=[MSG_TYPE_STACK, POC_CONTROL_SPEAK, 1]
            poc.broad_queue_put(key_to_poc_data)
            quec_mmi_led_set(QUEC_MMI_LED_RED)
            #ql_led.
        elif(para[1] == MMI_MSG_FUNC_KEY_UP):
            print("kongxian")
            self.ON_SPEAK = 0
            key_to_lvgl_data=[LVGL_CONTROL_STATUE_CHANGE, LVGL_CONTROL_STATUS_CALL, "Idle"]
            ui.lvgl_queue_put(key_to_lvgl_data)
            key_to_poc_data=[MSG_TYPE_STACK, POC_CONTROL_SPEAK, 0]
            poc.broad_queue_put(key_to_poc_data)
            quec_mmi_led_set(QUEC_MMI_LED_GREEN_FLASHING)
```



​                  In accord with the location in ql-enum.py. add the key handling function into the *self.mmi_key_handle_func_lis*t of *ql_poc_mmi.py*. 

Take the following case as an example

As for PTT, the corresponding value to QUEC_MMI_KEY_PTT is 6; as a result, the handling function of PTT is *mmi_key_handle_func_lis[QUEC_MMI_KEY_PTT ]*.

```python
        self.mmi_key_handle_func_list = (
            None, self.mmi_key_memu, None, self.mmi_key_exit, self.mmi_key_pf1, self.mmi_key_pf2, self.mmi_key_ptt,
            None, self.mmi_key_vol_up, self.mmi_key_vol_down
        )
```



### 3. The registered platform

Since the platform is depended on FW, if the firm is belonged to broadPTT, then in which the codes registered in broadPTT, so does in POCSTARS. 

### 4. How to modify GUI

It is a little complicated to add GUI in POC, which involves the variation of individual component of current surface as well as the linkage among keys. 

In this chapter, we will the layer relation of each surface in poc solution 

```
#  MenuIndex MasterMenu MasterItem MenuTitle MenuConfig  ItemIndex  ItemTitle
#  MenuConfig[0]:Menu count 
#  MenuConfig[1]：Component to be operated (default as roller when empty)
#  MenuConfig[2]：UP function (default as roller when empty, UP public function is adapted)
# MenuConfig[3]：Down function (default as roller when empty, UP public function is adapted)
# MenuConfig[4]：ENTER function (It is via enter when it is NONE)
# MenuConfig[5]：EXIT function (It is via enter when it is NONE)

self.Menus = [
{'MenuIndex': MENU_WELCOME, 'MenuObj': None, 'MasterMenu': None, 'MasterItem': None, 'MenuTitle': "Initialize Surface", 
'MenuConfig': [0, None, None, None, self.ql_poc_switch_init_to_home_screen,self.ql_poc_switch_init_to_home_screen], 
"ItemIndex" : None, 'ItemTitle':None},

{'MenuIndex': MENU_MAIN, 'MenuObj': None, 'MasterMenu': None, 'MasterItem': None, 'MenuTitle': "main surface", 
'MenuConfig': [1, None, None, None, self.ql_poc_switch_home_to_main_menu_screen, None], 
"ItemIndex" : [MENU_MENU], 'ItemTitle':None},

{'MenuIndex': MENU_MENU, 'MenuObj': None, 'MasterMenu': MENU_MAIN, 'MasterItem': None, 'MenuTitle': "menu surface", 
'MenuConfig': [4, None, None, None, self.ql_poc_switch_main_menu_enter_handle, self.ql_poc_switch_main_menu_to_home_screen], 
"ItemIndex" : [MENU_PUBLIC], 'ItemTitle' : None},

#Sub menu under the main menu
{'MenuIndex': MENU_PUBLIC, 'MenuObj': None, 'MasterMenu': MENU_MENU, 'MasterItem': None, 'MenuTitle': "Public setting", 
'MenuConfig': [1, None, None, None, self.ql_poc_switch_public_menu_enter_handle, self.ql_poc_switch_public_menu_exit_handle], 
"ItemIndex" : None, 'ItemTitle':None},

{'MenuIndex': MENU_ABOUT, 'MenuObj': None, 'MasterMenu': MENU_MENU, 'MasterItem': None, 'MenuTitle': "About PC", 
'MenuConfig': [1, None, None, None, None, self.ql_poc_switch_loacl_informations_to_main_menu_screen], 
"ItemIndex" : None, 'ItemTitle':None},


{'MenuIndex': MENU_POWEROFF, 'MenuObj': None, 'MasterMenu': MENU_MENU, 'MasterItem': None, 'MenuTitle': "Close surface", 
'MenuConfig': [0, None, None, None, self.ql_poc_poweroff_OK_handle, self.ql_poc_switch_poweroff_to_home_screen], 
"ItemIndex" : None, 'ItemTitle':None},
]
```

From above list, we can learn about the communication, linkage of each surface as well as layer relationship. Take PUBLIC surface as an example. 

What we can learn from the dictionary MeunIndex is that the index number of PUBLICde is MENU_PUBLIC. (This value is used to find out exact surface in actual operation)

MenuObj: Refer to the surface lvgl obj

MasterMenu: The Main serves as the master menu of PUBLIC. 

MasterItem: Indicate the menu index of PUBLIC in master menu. However, it is for backup instead of used in solution. 

MenuTitle: Mean the title of PUBLIC, which is vital in solution. 

MenuConfig: Detailed operations are displayed here. 

​		MenuConfig[0]:   Menu item count in menu

​		MenuConfig[1]：Component to be operated (default as roller when empty)

​		MenuConfig[2]：UP function (default as roller when empty, UP public function is adapted)

​		MenuConfig[3]：Down function (default as roller when empty, UP public function is adapted)

​		MenuConfig[4]：ENTER function (It is via enter when it is NONE)

​		MenuConfig[5]：EXIT function (It is via enter when it is NONE)

The ItemIndex ItemTitle is used as backup instead of embedded in solution

Please compile the drawing of one surface with following steps: 

Here shows the details: 

​			（1）Finish the "Power off" dictionary as above list. 

​			（2）Draw "Power off“ and synchronize the value as above dictionary. 

​			（3）Confirm the entrance and exit of “ Power off ” surface 

​			（4）Compile the OK operation function of "Power off" surface

​			（5）Compile how to enter "Power off" surface

（It just takes the "Power off" surface as an example, which is same to other case）

​			（1）Compile dictionary item of "Power off" surface

```
{'MenuIndex': MENU_POWEROFF, #INdex of "power off" surface
'MenuObj': None, 			#lvgl obj of "power off" surface
'MasterMenu': None, 		# No master menu
'MasterItem': None, 		#No master item index
'MenuTitle': "Power off surface", 	#Surface label
'MenuConfig': [0, None, None, None, self.ql_poc_poweroff_OK_handle, self.ql_poc_switch_poweroff_to_home_screen], 
			#No component, whihc means invalid to flip or flap
			#Press Ok, the corresponding handleself.ql_poc_poweroff_OK_handle 
			#Press Exit, the corresponding handle self.ql_poc_switch_poweroff_to_home_screen 
"ItemIndex" : None, 'ItemTitle':None}, # Not used
```

​			（2）Draw surface			

```python
    def ql_poc_poweroff_screen_create(self):
        poweroff_screen = lv.obj(self.middle_obj)
        poweroff_screen.set_style(self.g_poc_style_plain_16)
        poweroff_screen.set_size(LCD_SIZE_W,int(LCD_SIZE_H*0.625))
        # self.poweroff_screen = poweroff_screen
        poweroff_item_Menu = self.getMenusByIndex(MENU_POWEROFF)	# Synchronize the corresponding MenuObj in menu list 
        poweroff_item_Menu['MenuObj'] = poweroff_screen


        poweroff_label = lv.label(poweroff_screen)
        poweroff_label.set_style(lv.label.STYLE.MAIN,self.g_poc_style_plain_16)
        poweroff_label.set_text("Warning")
        poweroff_label.set_pos(int((LCD_SIZE_W- poweroff_label.get_width())/2), int(LCD_SIZE_H*0.025))

        poweroff_information_label = lv.label(poweroff_screen)
        poweroff_information_label.set_style(lv.label.STYLE.MAIN,self.g_poc_style_plain_16)
        poweroff_information_label.set_text("Conform whether to power off！！！")
        poweroff_information_label.set_long_mode(lv.label.LONG.SROLL_CIRC)
        poweroff_information_label.set_align(lv.label.ALIGN.CENTER)
        poweroff_information_label.set_pos(0, int(LCD_SIZE_H*0.31))
        poweroff_information_label.set_size(LCD_SIZE_W, int(LCD_SIZE_H*0.44))
        self.poweroff_information_label = poweroff_information_label
```

​				（3）Confirm the entrance and exit of “ Power off ” surface 

```python
    # Enter "Power off"surface
    def ql_poc_switch_to_poweroff_screen(self):
        active_item_Menu = self.getMenusByIndex(self.Active_Index)	#Find out the dictionary item of current surface
        poweroff_item_Menu = self.getMenusByIndex(MENU_POWEROFF)	#Find out the dictionary item of "power off" surface
        
        lv.obj.set_hidden(active_item_Menu['MenuObj'], True)	#Hide current surface
        lv.obj.set_hidden(poweroff_item_Menu['MenuObj'], False)	#Enter "power off" surface
        self.current_menu_label = poweroff_item_Menu['MenuTitle']	#Synchronize the title of current surface
        self.Active_Index = MENU_POWEROFF		#Synchronize the index of current surface
    
    # Return from the "Power off" surface
    def ql_poc_switch_poweroff_to_home_screen(self):
        active_item_Menu = self.getMenusByIndex(self.Active_Index)	#Find out the dictionary item of current surface(The "Power off" surface)
        main_item_Menu = self.getMenusByIndex(MENU_MAIN)			#Find out the dictionary item of main surface
        
        lv.obj.set_hidden(active_item_Menu['MenuObj'], True)		#Hide "power off" surface
        lv.obj.set_hidden(main_item_Menu['MenuObj'], False)			#Enter the main surface
        self.current_menu_label = main_item_Menu['MenuTitle']		#Synchronize the title of current surface
        self.current_screen = MENU_MAIN								#Synchronize the index of current surface
```

​		（4）Compile the success operation function of "Power off" surface

```python
    def ql_poc_poweroff_OK_handle(self):
        datatommi = [MMI_MSG_TYPE_UI_EVEN, MMI_MSG_FUNC_UI_EVENT_POWEROFF]	#Send message to MMI, which is controlled by MMI. 
        print(datatommi)
        self.mmi.mmi_queue_put(datatommi)
```

​		（5）Compile how to enter "Power off" surface

​                  Long press the exit in solution to enter this surface.

After long pressing the **exit**, the message will be transmitted to MMI, and Lvgl will decide whether enter this component after receiving message from MMI. 

```python
    def ui_lvgl_thread(self,thread_id):
        print("lvgl thread id is:%d" % thread_id)

        global lvgl_queue
        lvgl_queue = queue.Queue(50)
        while(1):
            lvgl_data = lvgl_queue.get()
            if not lvgl_data:
                continue
            if(lvgl_data[0] == LVGL_CONTROL_SCREEN_CHANGE and lvgl_data[1] == LVGL_CONTROL_SCEREN_POWEROFF):
                # Enter the surface to confirm "power off"
                self.ql_poc_switch_to_poweroff_screen()
           
           
           
        ...#Omitted 
```



### 4. TTS usage 

The TTS is applied in the ql_poc_broad component. As for other components, if they want to play TTS, they should send the message to MMI, after which, the result would be sent to ql_poc_broad, finally, the TTS can be played. 

​     E. g. There is  a need for **lvgl componnet** to play TTS

​       The sent queue is datatommi = [MMI_MSG_TYPE_UI_EVEN,        MMI_MSG_FUNC_UI_EVENT_MENU_TTS_PLAY, "Menu selection" ]

​		MMI_MSG_TYPE_UI_EVEN: It means that the message is sent by UI to MMI

​		MMI_MSG_FUNC_UI_EVENT_MENU_TTS_PLAY : The UI surface has a demand to play TTS. 

​	 “Menu Selection” ： The detailed content to be played 

After confirming the queue, call  self.mmi.mmi_queue_put(datatommi)  and send message to MMI. 



### 5. Guide on debugging code

As the feature of poc solution codes, based on module, whose individual component is scattered as one file, makes the independence of each component since it just communicates with mmi. When debugging, we can just run the single component to whether this component can meet your demand. 


## Appendix A: Term Abbreviation

Tablet 2: Term abbreviation 

| Abbreviation | Full name in English        |
| ------------ | --------------------------- |
| LCD          | Liquid Crystal Display      |
| SPI          | Serial Peripheral Interface |



