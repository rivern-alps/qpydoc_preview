## About document

**Revision history**

| Version | Date       | Author | Description     |
| ------- | ---------- | ------ | --------------- |
| 1.0     | 2021-09-07 | FAE    | Initial Version |
| 1.1     | 2021-09-08 | Chic   | Added figures   |



## QuecPython_cellLocator base station location

In this document, it briefly introduces how to get base station location via QuecPython_cellLocator .

**Module function**

Provide base station location port to get coordinates info of terminal.

**Corresponding API** 

- cellLocator.getLocation (serverAddr, port, token, timeout, profileID)

The detailed API, please refer to [cellLocator - base station location](https://python.quectel.com/wiki/#/zh-cn/api/QuecPythonClasslib?id=celllocator-基站定位)

## Location Illustration

The location refers to technology or service to get the position(coordinates) on user end via specific method. 

Two ways are commonly used to locate: the first one is based on GPS;  while the second one is based on mobile operation network. As for the first one, it will send its location signal to background with the assist of GPS module. While the second one, it is realized by the distance between the base station and terminal. In terms of QuecPython_cellLocator, it is belonged to base station location. 

The approximate principle of base station: the mobile terminal will measure the down-link pilot signal time of different base stations, as a result, TOA (Time of Arrival) or TDOA (Time Difference of Arrival) of down-link pilot among different base stations will be achieved. Correspondingly, the location (coordinate) of mobile end user will be got according to the measured result  and the coordinates of base station (Usually, it is the formulas of trigonometric functions that is used). Finally, the related location will be provided to user with the assist of electronic map. Actually, the condition of multiple base station location should be considered in estimating the real location, therefore, the algorithm will be more flexible. In general, the more base stations measured by mobile stations, the higher the measurement accuracy and the more obvious the improvement of positioning performance.

## QuecPython_cellLocator features

As for QuecPython_cellLocator, the GPS capacitance and extra HW support are not needed. However, the accuracy depends on the spread and coverage of base station largely. The location accuracy is approximately from 500 m to 1500 m (It varies in base station density and library number). In addition, the Wi-Fi can be used to carry out assisted location in small scope with a  location accuracy of 50 m.  

The base station location is relied on the coverage of base station signal. Currently, the domestic 4G signal has been covered basically. As for 2G network, it can still be used temporarily, however, there is a risk of withdrawal accompanying. While from the view of 3G, it is also listed in the withdrawal plan even though the China Telecom is still persisting. Therefore, there is a need to learn about the signal coverage before deploying this function. 

##  Quick development

### Interaction test

Before that, we should make sure the SIM card status, please refer to documentary of SIM card module. 

We will get the current coordinates info via interaction commands. 

```python
>>> import cellLocator
>>> cellLocator.getLocation("www.queclocator.com", 80, "1111111122222222", 8, 1)
(117.1305, 31.82508, 550)
# The secret key used above is just for test. 
```

![image-20210908140227016](media\image-20210908140227016.png)



### Code test

Calculate the distance between current location and Beijing

```python
import cellLocator
from math import sin, asin, cos, radians, fabs, sqrt

EARTH_RADIUS = 6371           # The earth radius is 6371km


def hav(theta):
    s = sin(theta / 2)
    return s * s


def get_distance_hav(lat0, lng0, lat1, lng1):
    "Calculate the distance of two ponits on sphere via haversine formula" 
    # Convert the latitude and longitude into radians.
    lat0 = radians(lat0)
    lat1 = radians(lat1)
    lng0 = radians(lng0)
    lng1 = radians(lng1)

    dlng = fabs(lng0 - lng1)
    dlat = fabs(lat0 - lat1)
    h = hav(dlat) + cos(lat0) * cos(lat1) * hav(dlng)
    distance = 2 * EARTH_RADIUS * asin(sqrt(h))

    return distance


def test_cellLocator():
    # Test location 
    lon1, lat1 = (22.599578, 113.973129)  # Safari Park Shenzhen (Starting ponit)
    lon2, lat2 = (39.9087202, 116.3974799)  # Beijing Tian'anmen (1938.4KM)
    d2 = get_distance_hav(lon1, lat1, lon2, lat2)
    print(d2)
    # Get current location
    # (latitude, longitude, accuracy)
    ret = cellLocator.getLocation(
        "www.queclocator.com", 80, "1111111122222222", 8, 1)
    lon3, lat3 = ret[1], ret[0]
    d2 = get_distance_hav(lon3, lat3, lon2, lat2)
    print(d2)


if __name__ == "__main__":
    test_cellLocator()

```



## Referential materials 

[cellLocator - Base Station location](https://python.quectel.com/wiki/#/zh-cn/api/QuecPythonClasslib?id=celllocator-基站定位)

## The matched code

<!-- * [Download codes](code/cellLocator_base.py) -->
 <a href="code/cellLocator_base.py" target="_blank">Download codes</a>

