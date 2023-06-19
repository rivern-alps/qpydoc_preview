# osTimer - os定时器

模组提供底层os的定时器接口，os定时器超时会触发其绑定的回调函数。

**示例**

```python
import osTimer

def test_cb(arg):
    print("osTimer Expired!!")
# 创建os定时器
timer = osTimer()
# 启动定时器，参数依次为时间、是否循环、回调函数
timer.start(10000,1,test_cb)
# 停止定时器
timer.stop()
```


## 创建定时器

### `osTimer`

```python
osTimer()
```

创建osTimer定时器对象

> 相比[machine.Timer](./machine.Timer.md)，此定时器不存在创建个数的限制

## 启动定时器

### `osTimer.start`

```python
osTimer.start(initialTime, cyclialEn, callback)
```

**参数描述**                              

* `initialTime`，定时器超时的时间(单位ms)，int类型
* `cyclialEn`，是否循环，0为单次，1为循环，int类型
* `callback`，定时器超时触发的回调，function类型，原型为callback(arg)，`arg`未实际使用，可直接传入`None`

**返回值描述**

int类型，0为成功，其余为失败

## 停止定时器

### `osTimer.stop`

```python
osTimer.stop()
```
停止定时器

**返回值描述**

int类型，0为成功，其余为失败
