from machine import ExtInt 
import utime    
def fun1(args):  
    print(args)  
    print("key1 extint")   
def fun2(args):  
    print(args)  
    print("key2 extint")   
extint1 = ExtInt(ExtInt.GPIO12, ExtInt.IRQ_FALLING, ExtInt.PULL_PU, fun1) 
extint2 = ExtInt(ExtInt.GPIO13, ExtInt.IRQ_FALLING, ExtInt.PULL_PU, fun2) 
extint1.enable()
extint2.enable()
while True:  
    utime.sleep_ms(200)
