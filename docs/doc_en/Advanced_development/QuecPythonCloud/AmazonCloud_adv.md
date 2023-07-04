---
title: Amazon Cloud
keywords: Amazon
description: Amazon Cloud
---
## About document

**Revision history**

| **Version** | **Date**   | **Author** | **Description** |
| ----------- | ---------- | ---------- | --------------- |
| 1.0         | 2021-09-29 | Chic       | Initial version |



# Introduction on QuecPython AmazonCloud Test

In this article, it mainly illustrates how to connect network cloud via AWS  IoT. The AWS IoT  does not only provide Cloud service and device support that can be used to execute IoT solution, but also multiply cloud applications based on IoT.  The user can get access to IoT device as well as the function provided by Cloud service that connected. In next page, we mainly focus on MQTT connection. In addition, you can learn about how to connect QuecPython to AWS IoT from views of operation and verifications on test theory.  

## Cloud setting

The front page of AmazonCloud：https://aws.amazon.com/?nc1=h_ls

#### Login platform

Enter [My account]---[AWS Management Console]---[IoT Core]

![AmazonCloud_01](media/AmazonCloud_01.png)

#### 【Create tactic】

![AmazonCloud_01A](media/AmazonCloud_01A.png)

![AmazonCloud_01B](media/AmazonCloud_01B.png)

#### 【Create product】

![AmazonCloud_02](media/AmazonCloud_02.png)

![AmazonCloud_03](media/AmazonCloud_03.png)

![AmazonCloud_04](media/AmazonCloud_04.png)

![AmazonCloud_05](media/AmazonCloud_05.png)

![AmazonCloud_06](media/AmazonCloud_06.png)

Till now, "Create product" has been finished. It is available to connect AWS IoT platform via certificate. Please note that the same certificate can be used on several devices, and the Client ID of various devices shall be unique. 

![AmazonCloud_07](media/AmazonCloud_07.png)

![AmazonCloud_08](media/AmazonCloud_08.png)

![AmazonCloud_09](media/AmazonCloud_09.png)

#### 【Device communication】

Get the MQTT connection address and port of AWS Server. 

![AmazonCloud_10](media/AmazonCloud_10.png)

![AmazonCloud_11](media/AmazonCloud_11.png)

![AmazonCloud_12](media/AmazonCloud_12.png)

Test communication via MQTT.fx. fill in "#" on subscription topic bar to receive all topics. 



 


