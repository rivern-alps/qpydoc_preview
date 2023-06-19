# system - System Configuration

This feature is used to configure the system parameter and features.

Applicable modules: EC100Y(V0009) and above; EC600S(V0002) and above.


### `system.replSetEnable`

```python
system.replSetEnable(flag，**kw_args)
```

Enables or disables interaction protection.

**Parameter**

1.  When kw_args is omitted

0 - Disable (default)

1 - Enable

2 - Query the current encryption status

After the interaction protection is enabled, all external commands and codes cannot be executed and the operation is irreversible. Please enable the  interaction protection after confirmation. Default value: 0.

2. When kw_args is configured

Interaction protection can be enabled and disabled by a password. (Few module models do not support password protection, so when you enter a password on a module that does not support password protection, you will receive an error message. For example BC25 series and EC600M series modules.)

* Parameter

| Parameter | Type | Description              |
| :--- | :--- | ---------------------------- |
| flag | Integer | 0 - Disable (default) <br />1 - Enable<br />2-  Query encryption status |
| kw_args | String | Password (optional) |

* Return Value

0 - Successful execution

-1 or errorlist or both - Failed execution

If *flag* is set to 2, the return values are as follows.
-1 - Querying failed
1 - repl enable
2- repl enable but The password has already been set
3 - repl refuse
4 - repl-protection by password


### `system.replChangPswd`

```python
system.replChangPswd(old_password,new_password)
```

Changes the password for interaction protection.

* Parameter

| Parameter    | Type   | Description                       |
| :----------- | :----- | --------------------------------- |
| old_password | String | Old password. Length: 6–12 bytes. |
| new_password | String | New password. Length: 6–12 bytes. |

* Return Value

0 - Successful execution

-1 or errorlist or both - Failed execution

**Example**

```python
>>>import system

>>> system.replSetEnable(1,password='miamia123')//Set a password for the first time upon startup and enable interaction protection. You can set a password with a length of 6 to 12 bytes.
0
>>>                                            //Set successfully. The interaction interface is locked and only can be used after you enter the password.
Please enter password:
>>> ******                                     //Incorrect password.
Incorrect password, please try again:
>>> ********                                   //Incorrect password.
Incorrect password, please try again:
>>> *********                                  //Correct password. The interaction interface is available.
REPL enable
>>> system.replSetEnable(2)
2
>>>

>>> system.replSetEnable(1,password='miamia') //A password has been set. You need to enter the correct password to relock the interaction interface.
Incorrect password!
-1
>>> system.replSetEnable(1,password='miamia123')
0
>>> 
Please enter password:                        //Relock the interaction interface.
>>> miamia123
*********
REPL enable
>>> system.replSetEnable(2)
2


>>> system.replChangPswd(old_password='miamia123',new_password='123456') //Change password.
0
>>> system.replSetEnable(1,password='miamia123')                         //The password has been changed, so the message "incorrect password" will be prompted if you try to lock the interface with the old password.
Incorrect password!
-1
>>> system.replSetEnable(1,password='123456')                            //Relock the interaction interface with the new password successfully.
0
>>> 
Please enter password:
>>> ******
REPL enable

>>> system.replSetEnable(0,password='123456')          //Disable interaction protection, after which you can use any password to relock the interaction interface.

0
>>> 
>>> system.replSetEnable(2)                            //Query the current interaction protection status.
1
>>> system.replSetEnable(0)                           //Default value: 0.
0
>>>system.replSetEnable(1)                            //Enable interaction protection.
>>>
REPL refuse
>>>
```
