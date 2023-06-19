# atcmd - Send AT Commands

This module provides a method for sending AT commands, allowing the QuecPython module to send AT commands through Python code.



## Send AT Commands

### `atcmd.sendSync`

```
atcmd.sendSync(atcmd,resp,include_str,timeout)
```

 Sends an AT command to the module.

**Parameter**

* `atcmd` - String type. The AT command to be sent, and  '\r\n' should be included.
* `resp` - String type. The string content returned by the AT command.
* `include_str` - String type. Keyword. The specific values are shown in the table below:

| Value               | Description                                                  |
| ------------------- | ------------------------------------------------------------ |
| `Empty string`      | Gets all data returned by the AT command (excluding result data such as 'OK') and puts the data into the `resp` parameter. |
| `None-empty string` | Filter data containing the keyword and puts the data into the `resp` parameter. |

* `timeout` - Integer type. Timeout. Unit: second.

**Return Value**

Returns an integer value. `0` indicates successful execution and other values indicate failed execution.

**Example:**

```python
>>> import atcmd
>>> resp=bytearray(50)
>>> atcmd.sendSync('at+cpin?\r\n',resp,'',20)
0
>>> print(resp)
bytearray(b'\r\n+CPIN: READY\r\n\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

atcmd.sendSync('at+cpin\r\n',resp,'',20)
1
>>> print(resp)
bytearray(b'\r\nERROR\r\n\n
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
```
