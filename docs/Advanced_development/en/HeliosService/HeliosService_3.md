## About document

**Revision history**

| Version | Date       | Author | Description     |
| ------- | ---------- | ------ | --------------- |
| 1.0     | 2021-09-17 | Chic   | Initial Version |



## The illustration of Senior Helios Services

In this document, it mainly introduces the SW design of Helios Services and functions supported in later stage. Meanwhile, the user can get familiar with inner communication principle via it and learn about the mechanism. 



## SW structure design of Helios Services

### Structure design

![HeliosService_3_en_01](media\HeliosService_3_en_01.png) 

**Explanation**

- `Services`: Service components
- `Config`: Configure storage
  - `app_config`:  The directory used to save the configured files of user
  - `system_config`: The directory for configured files of system 
- `monitos`: Monitor the status of individual service
- `sys_bus`: The bus of session,  which is used to deal with producer and consumer mode. Currently, it only supports asynchronous mode. 
- `queue:` Common queue, which is for communication among threads.
- `event_message`: Asynchronous and senior message queue with name space
- `GuardContext`:  GuardContext of container. Manage all services and configurations unitedly. In addition, monitor is also involved. Moreover, it provides port that obtained by services, configurations and monitors.  
- `third_party`: Directory of third party components, which is embedded with some components that provided and packaged by us for sake of quick and secondary development of user. 

### Design principle

#### Service design principle 

![HeliosService_3_en_02](media\HeliosService_3_en_02.png)

1. We have written and provided some services that specialised for system. As a result,  the publisher of these services may come from the callback who can receive system low layer. Meanwhile, the user can publish it to different subscribers actively. 
2. E. g. If the user just needs to subscribe network service, when the network signal is abnormal or bad, even worse, the network disconnects, the network will carry out automatic re-connection and notify all functions who have subscribed network service the current network status. Therefore, the subscriber will receive relevant info and handle it. 
3. E. g : In log service, the user should be responsible for the role of publisher. 
4. The publisher is irrelevant to subscriber. Meanwhile, the publisher just publishes the data to user instead of paying attention to subscriber. 
5. Whether from publisher to service, or service to subscriber, they are all asynchronous. At the same time, we also provide and support the synchronous configurations. 
6. The service is realized by the combination of these senior queues with name space and other components. 

**Advantage** 

- We have already contrived some services at system level from the view of client and supported further upgrade. By this method, it can solve the issue for client if there is a need to undertake other codes when reserving system and provide external API for client to call. 
- Degrade the coupling among services. And decouple between subscriber and publisher. 
- The subscriber just pay attention to service or use service, that is to use the function that reserved and provided by us. 

**Disadvantage**

- We have limited the service type, as a result, it will be a failure for client to customize. E. g. If the client wants to decouple two or more services, however, the client can't do it by himself as these services are written by us. For detailed scheme, please refer to `sys_bus`.
- First of all, it is composed by series of senior message queues, as a result, it is possible that the service still exists; however, the message queue  collides. Therefore, we should pull it up before the collision of service. For more details, please refer to `monitor`. 



**Case:**

Subscribe service 

![HeliosService_3_en_03](media\HeliosService_3_en_03.png)

#### The realisation principle of sys_bus



![HeliosService_3_en_04](media\HeliosService_3_en_04.png)

We have already provided above services to client and we also make our disadvantages clear. The user can't customize service. However, it is available for client to customize services via *sys_bus*. 

- Asynchronous mode, the client can subscribe, publish and unbind. 
- Separate publication from subscription as well as module. Meanwhile, it supports multiple publishers. Compared with service, the publishers and subscriber are reserved by users. 
- The user only focuses on topic instead of *sys_bus* and subscriber. 
- **Advantage**:
  - The client can customise and publish related data.
  -  We have already maintained the stability of *sys_bus*.
- **Disadvantage**:
  - Users have to maintain some of their subscription codes by themselves owing to the over-flexibility. 

Case: 

![HeliosService_3_en_05](media\HeliosService_3_en_05.png)

#### Design principle of monitor

- It is responsible for monitoring individual service and providing one heartbeat with an interval of every other 15 s. If the service receives the heartbeat package, it will transmit it to the specific recipient. After the monitor receives the heartbeat package, it will judge whether the service runs smoothly.  
- It can be set the corresponding behaviours when there are several failures in running. E. g. when there is a failure after continuous service heartbeats, reboot device or stop this service. [Currently, it has been settled in low layer by default, the user can neglect it. ]

**示例** E. g.  

![HeliosService_3_en_06](media\HeliosService_3_en_06.png) 

#### Design principle of config

In order to facilitate the reading and setting of configured files, we put the configuration file into folder of *config* and set *config.json* file according to following specifications. 

![HeliosService_3_en_07](media\HeliosService_3_en_07.png)

- **app_config** 
  - The following corresponds to the configuration file configured by the user. As above figure implies, in *app_config*:
    - Take the **cloud folder** as an example. the *config.json* is hidden in cloud folder, we will read the mapping file to cloud service and upload the contents in *config.json* automatically. If the cloud is invisible, we will save the mapping relationship between configuration file and service automatically; what's more,  we will get the contents in *config.json* of service and mapping via `guard_context.service_config`. 
- **system_config** 
  - Configure service at system level. On one side, we will read the configuration file of system service. When there exists service, we can match it automatically; otherwise, we can still save the relevant mapping relationship, therefore, the user can obtain mapping contents via `guard_context.service_config`. 

**Case:**

![HeliosService_3_en_08](media\HeliosService_3_en_08.png)

- Following contents are included in *app_config*. 
  - lexin
    - *config.json*
  - abc
    - *config.json*
  -  What we can read in *service_config*: 
    - {'abc': {'a': 1}, 'lexin': {'a': 1}}
    - These abc and lexin serve as the folder name, whose corresponding value is hidden in *config.json*.
- As for corresponding relationship, the *system_config* should be coincide with the *app_config.* 
- **Note**: if you want to read it, you should make the “ **key** ” as the folder name accordingly. And what read by value is contents hidden in *config.json*.  

#### Queue design principle

The common queue serves as message communication. While after building queue, there will be congestion when obtaining data; however, it will be waken up when there exists data signal. 

![HeliosService_3_en_09](media\HeliosService_3_en_09.png)

### Third party and container design 



#### GuardContext design 

We have learnt about the components design above, then, we will introduce the container design. 

- For the convenience of  importing, we have contained existing services and configurations and carried out united management.  
- The user just needs to focus on container design. 

#### Third-Party design

Please refer to API document of third party. 

