# TCP开发常见问题

### **TCP有自动重连功能吗？**

底层没有自动重连，自动重连在应用层做。

### **TCP连接会自动发送ping包吗**

可以设置usocket.TCP_KEEPALIVE保活时间。



# MQTT开发常见问题

### **MQTT支持QoS2吗？**

目前不支持QoS2，支持QoS0、QoS1

