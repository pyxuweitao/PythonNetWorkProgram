#《Python网络编程》读书笔记

@(读书笔记)[2015年|1月|15日]

[TOC]

-----------

##简述

>今天主要配置了vim的Python开发环境，然后接着昨天的阅读进度，继续阅读《Python网络编程》第一章。

-----------

##第一章

**获取设备的网络名称和IPV4地址**

``` python
import socket

#输出设备的网络名称
host_name = socket.gethostname()
#输出设备的IPV4地址（这丫的打印的是本地环回地址）
IP = socket.gethostbyname( host_name )
```



----------



