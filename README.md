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



n网络编程》读书笔记

@(读书笔记)[2015年|1月|15日]

[TOC]

-----------

##简述

>《Python网络编程》读书笔记，1月22日更新完第一章。

-----------

##第一章

**`1.2`获取设备的网络名称和IPV4地址**

``` python
import socket

#输出设备的网络名称
hostName = socket.gethostname()
#输出设备的IPV4地址
IP = socket.gethostbyname( hostName )

#获取主机名，同一IP可选主机名，同一主机同一接口的其他IP地址
info_tuple_by_hostName = socket.gethostbyname_ex( hostName )
info_tuple_by_IP       = socket.gethostbyaddr( IP )
```
>**补充**：
>- 在ubuntu下测试，`socket.gethostbyname(socket.gethostname())`获取的是本地环回测试地址`127.0.1.1`。原因是`\etc\hosts`文件中有条目
>*`127.0.1.1`  `hostname`*
>而计算机在通过DNS解析域名之前，会首先到本机hosts文件中寻找域名与IP的对应关系。所以获取真实的外网地址，需要首先将这一条目除去。
>- 若将该条目除去之后，仍然获取的不是外网地址，可以通过`socket.gethostbyname_ex(hostName)`方法，它返回包括三个元素的元组，分别是给定地址的主要的主机名、同一IP地址的可选的主机名的一个列表、关于同一主机的同一接口的其它IP地址的一个列表。同样，`gethostbyaddr(IPstring)`方法的返回值与`gethostbyname_ex`相同，但参数是一个IP地址字符串。

----------



