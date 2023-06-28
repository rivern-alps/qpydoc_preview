# checkNet - 网络检测

`checkNet`模块提供了方法来检测模组的网络状态是否已经就绪，同时提供了网络异常的排查方法与步骤。



## 等待网络就绪

### `checkNet.waitNetworkReady`

```python
checkNet.waitNetworkReady(timeout)
```

等待模组网络就绪。该方法会依次检测SIM卡状态、模组网络注册状态和PDP Context激活状态；在设定的超时时间之内，如果检测到PDP Context激活成功，会立即返回，否则直到超时才会退出。

**参数描述：**

* `timeout` - 超时时间，整型值，范围1~3600秒，默认`60`秒。

**返回值描述：**

返回一个元组，格式为：`(stage, state)`

| 参数  | 类型 | 含义                                                         |
| ----- | ---- | ------------------------------------------------------------ |
| stage | 整型 | 表示当前正在检测什么状态：<br/>1 - 正在检测SIM卡状态；<br/>2 - 正在检测网络注册状态；<br/>3 - 正在检测PDP Context激活状态。 |
| state | 整型 | 根据stage值，来表示不同的状态，具体如下：<br>stage = 1时，state表示 SIM卡的状态，范围0~21，每个状态值的详细说明，请参考`sim.getStatus()`方法的返回值说明；<br>stage = 2时，state表示网络注册状态，范围0~11，每个状态值的详细说明，请参考`net.getState()`方法的返回值说明；<br>stage = 3时，state表示PDP Context激活状态，0表示没有激活成功，1表示激活成功。 |

如果网络已经就绪，则返回`(3,1)`，否则可参考如下说明来排查定位问题：

<table >
	<tr>
	    <th bgcolor=#ED1922>stage</td>
        <th bgcolor=#ED1922>state</td>
        <th bgcolor=#ED1922>说明</td>
	</tr >
	<tr>
	    <td rowspan="2">1</td>
        <td>0</td>
        <td>说明没插卡，或者卡槽松动，需要用户去检查确认。</td>
	</tr>
	<tr>
	    <td>其他值</td>
        <td>请参考官方wiki文档中关于sim卡状态值的描述，确认sim卡当前是哪种状态。</td>
	</tr>
    <tr>
	    <td rowspan="3">2</td>
        <td>-1</td>
        <td>这种情况说明在超时时间内，获取模组网络注册状态的API一直执行失败，在确认SIM卡可正常使用且能正常被模组识别的前提下，可联系我们的FAE反馈问题。</td>
	</tr>
    <tr>
	    <td>0或2</td>
        <td>这种情况说明在超时时间内，模组一直没有注网成功，这时请按如下步骤排查问题：<br>（1）首先确认SIM卡状态是正常的，通过 sim 模块的<code><span style="background-color: light grey;">sim.getStatus()</span></code>接口获取，为1说明正常；<br>（2）如果SIM卡状态正常，确认当前信号强度，通过net模块的<code><span style="background-color: light grey;">net.csqQueryPoll()</span></code>接口获取，如果信号强度比较弱，那么可能是因为当前信号强度较弱导致短时间内注网不成功，可以增加超时时间或者换个信号比较好的位置再尝试；<br>（3）如果SIM卡状态正常，信号强度也较好，请确认使用的SIM卡是否已经欠费或流量不足；<br>（4）如果SIM卡没有欠费也没有流量不足，请确认使用的是否是物联网卡，如果是，请确认该SIM卡是否存在机卡绑定的情况；<br>（5）如果按照前述步骤依然没有发现解决问题，请联系我们的FAE反馈问题；最好将相应SIM卡信息，比如哪个运营商的卡、什么类型的卡、卡的IMSI等信息也一并提供，必要时可以将SIM卡寄给我们来排查问题。</td>
	</tr>
    <tr>
	    <td>其他值</td>
        <td>请参考官方Wiki文档中<code><span style="background-color: light grey;">net.getState()</span></code>接口的返回值说明，确认注网失败原因。</td>
	</tr>
	<tr>
	    <td rowspan="2">3</td>
        <td>0</td>
        <td>这种情况说明在超时时间内，PDP Context一直没有激活成功，请按如下步骤尝试：<br>（1）通过 sim 模块的<code><span style="background-color: light grey;">sim.getState()</span></code>接口获取sim卡状态，为1表示正常；<br>（2）通过 net 模块的<code><span style="background-color: light grey;">net.getState()</span></code>接口获取注网状态，为1表示正常；<br>（3）手动调用<code><span style="background-color: light grey;">dataCall.activate(profileID)</span></code>接口尝试激活，看看能否激活成功；<br>（4）如果手动激活成功了，但是开机自动激活失败，可联系我司相关人员协助分析。</td>
	</tr>
    <tr>
	    <td>1</td>
        <td>这是正常返回情况，说明网络已就绪，可进行网络相关业务操作。</td>
	</tr>
</table>







**示例：**

```python
import checkNet

if __name__ == '__main__':
    stage, state = checkNet.waitNetworkReady(30)
    if stage == 3 and state == 1:
        print('Network connection successful.')
    else:
        print('Network connection failed, stage={}, state={}'.format(stage, state))
```

