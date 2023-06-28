# checkNet - Network Detection

The `checkNet` module provides methods to detect whether the QuecPython module's network is ready, while also providing troubleshooting methods and steps for network exceptions.



## Wait for the Network to be Ready

### `checkNet.waitNetworkReady`

```python
checkNet.waitNetworkReady(timeout)
```

Waits for the module's network to be ready. This method checks the SIM card status, module network registration status, and PDP context activation status in order. If PDP context activation is detected successfully within the specified timeout period, it will return a result immediately. Otherwise, it will continue waiting until the timeout is reached. 

**Parameter:**

* `timeout` - Integer type. Timeout. Range: 1–3600. Unit: s. Default value: `60`.

**Return Value:**

Returns a tuple in `(stage, state)` format:

| Parameter | Type    | Description                                                  |
| --------- | ------- | ------------------------------------------------------------ |
| stage     | Integer | The status currently being checked:<br/>1 - Checking SIM card status;<br/>2 - Checking network registration status;<br/>3 - Checking PDP context activation status. |
| state     | Integer | The stage value indicates different status:<br>When stage = 1, it indicates the SIM card status. Range: 0–21. For details of each status value, refer to the return value of the `sim.getStatus()` method;<br>When stage = 2, it indicates the network registration status. Range: 0–11. For details of each status value, refer to the return value of the `net.getState()` method;<br>When stage = 3, it indicates the PDP Context activation status. 0 indicates failed activation and 1 indicates successful activation. |

If the network is ready, `(3,1)` will be returned. Otherwise, refer to the following table to troubleshoot and locate the problem:

<table >
	<tr>
	    <th bgcolor=#ED1922>stage</td>
        <th bgcolor=#ED1922>state</td>
        <th bgcolor=#ED1922>Description</td>
	</tr >
	<tr>
	    <td rowspan="2">1</td>
        <td>0</td>
        <td>It indicates that there is no card inserted or that the card slot is loose, please check and confirm.</td>
	</tr>
	<tr>
	    <td>Other values</td>
        <td>Please refer to the official WiKi documentation for SIM card status values to confirm the current status of the SIM card.</td>
	</tr>
    <tr>
	    <td rowspan="3">2</td>
        <td>-1</td>
        <td>It indicates that within the timeout period, the API for getting the module's network registration status fails continuously. Please give feedback to our FAE if the SIM card is normal and can be recognized by the module.</td>
	</tr>
    <tr>
	    <td>0 or 2</td>
        <td>It indicates that the module has not been successfully registered to the network within the timeout period. Please follow the steps below to troubleshoot:<br>(1) First, confirm whether the SIM card status is normal through the sim.getState() interface of the SIM module. If the return value is 1, the status is normal;<br>(2) If the SIM card status is normal, check the current signal strength through the net.csqQueryPoll() interface of the net module. If the signal strength is weak, the failed network registration in a short period of time may be caused by weak signal strength. You can increase the timeout period or move to a location with better signal strength and retry.<br>(3) If the SIM card status is normal and the signal strength is good, confirm if the SIM card is overdue or out of data traffic.<br>(4) If the SIM card is not overdue or out of data traffic, confirm if the card used is an IoT card and if there is a machine-card binding for the SIM card.<br>(5) If the problem still cannot be solved after the above steps, please contact Quectel Technical Support for assistance. Please provide relevant SIM card information, such as the operator, type, IMSI, etc., and if necessary, please send the SIM card to us for troubleshooting.</td>
	</tr>
    <tr>
	    <td>Other values</td>
        <td>Please refer to the official Wiki documentation for the net.getState() interface to confirm the reason for the network registration failure.</td>
	</tr>
	<tr>
	    <td rowspan="2">3</td>
        <td>0</td>
        <td>It indicates that the PDP Context has not been activated successfully within the timeout period. Please follow the steps below to troubleshoot:<br>(1)Get the SIM card status through the sim.getState() interface of the SIM module. If the return value is 1, the status is normal.<br>(2) Get the network registration status through the net.getState() interface of the net module. If the return value is 1, the status is normal. <br>(3) Manually call the dataCall.activate(profileID) interface to activate it and see if it can be activated successfully.<br>(4) If manual activation is successful but automatic activation fails, please contact Quectel Technical Support for assistance.</td>
	</tr>
    <tr>
	    <td>1</td>
        <td>It is a normal return, indicating that the network is ready, and network-related business operations can be carried out.</td>
	</tr>
</table>









**Example:**

```python
import checkNet

if __name__ == '__main__':
    stage, state = checkNet.waitNetworkReady(30)
    if stage == 3 and state == 1:
        print('Network connection successful.')
    else:
        print('Network connection failed, stage={}, state={}'.format(stage, state))
```

