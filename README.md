#《Python网络编程》读书笔记

@(读书笔记)[2015年|1月|15日]

[TOC]

-----------

##简述

>《Python网络编程》读书笔记，1月22日更新完第一章。

-----------

##第一章
**`1.6`主机字节序和网络字节序之间相互转换**
``` python
import socket

#主机字节序和网络字节序之间相互转换
def convert_integer( integer ):
	'''主机字节序和网络字节序之间的转换'''
	long_host_byte = socket.ntohl( integer )
	network_byte   = socket.htons( integer )
	return [long_host_byte, network_byte]
```
>**补充**:
>函数名中:
>- n --> 网络 network
>- h --> 主机 host
>- l  --> 长整形 long 
>- s --> 短整型 short 16位

>主机字节序和网络字节序：
>- 主机字节序：主机字节序由CPU或操作系统决定，这些字节序是指整数在内存中保存的顺序
>>- `little endian`(LE): 将低序字节存储在起始地址，符合人的思维
>>- `big endian`(BE): 将高序字节存储在起始地址，最直观，从低位地址开始顺序写入数值的高位

>- 网络字节序：网络字节序是TCP/IP中规定好的一种数据表示格式，它与具体的CPU类型、操作系统等无关，从而可以保证数据在不同主机之间传输时能够被正确解释

**`1.5`通过指定的端口和协议找到服务名**
``` python
import socket

#1.5根据端口号和协议名称获取服务名
def find_service_name( port, protocol_type ):
	'''根据端口和协议类型获取协议名称'''
	return socket.getservbyport( port, protocol_type )
```
>**补充**:
>类似的socket方法有`getservbyname`,它的参数是一个服务名（如'telnet'或'ftp'）和一个协议（如'tcp'或'udp'），返回服务所使用的端口号

----------
**`1.4`将IPv4地址转换成不同的格式**

``` python
import socket
from binascii import hexlify

#1.4 将IPv4地址转换成不同的格式
def convert_ipv4( ip ):
	'''return 字典：{'ip':原始IP地址,'packed':打包转化成32位二进制的ip地址,'unpacked': 解包解析出IP地址字符串, 'hex':32位二进制IP地址转化成16进制 }
	将IPv4地址转换成32位二进制格式
	'''
	packed_ip   = socket.inet_aton( ip )
	unpacked_ip = socket.inet_ntoa( packed_ip )
	return { 'ip':ip, 'packed':packed_ip, 'unpacked':unpacked_ip, 'hex':hexlify( packed_ip ) }

```
>**补充**:
>- 助记：`ntoa` --> n( number ) to a ( ascii )
>- 助记：`aton` --> a( ascii ) to n ( number )
>- `hex()`和`hexlify()`的区别：
>1. 参数，一个是十进制整数，一个是ascii字符串。所以在hexlify中对32位二进制`packed_ip`做了隐式转换。
>2. 返回值，都是字符串，不同的是`hex`保留了前缀`0x`
>- 常用的`int(p1,p2)`当参数p1为字符串时，第二个参数必须指定进制。例如`int(10,2)`返回十进制数字2。类似的还有`float()`,`long()`。
>- `float`类型转化成16进制数字：`1.2.hex()`
>- `hexlify()`的逆方法是`unhexlify()`

----------
**`1.3`获取远程设备的IP地址**

``` python
import socket

#1.3获取远程设备的IP地址
def get_remote_name( host_name ):
	'''与1.2章节的方法相同，增加了异常处理'''
        remote_host_name = host_name
        try:
            IPString = socket.gethostbyname( remote_host_name )
            return IPString
        except socket.error, errMsg:
            return errMsg

```
>**补充**:
>几个常见的socket异常：
>- `socket.error`：由Socket相关错误引发
>- `socket.herror`：由地址相关错误引发，C API中抛出的异常。例如删去hosts中的条目 127.0.1.1 hostname 就会抛出该异常。
>- `socket.gaierror`：由地址相关错误，如getaddrinfo()或getnameinfo()引发
>- `socket.timeout`：当socket出现超时时引发。超时时间由settimeout()提前设定

--------------
**`1.2`获取设备的网络名称和IPV4地址**

``` python
import socket

#1.2打印本机设备名和IPv4的地址
def getHostName():
	'''输出本机的网络设备名称'''
	hostName = socket.gethostname()
	return hostName
	
def getHostByName( hostName ):
	'''根据网络设备名获得本机IP'''
	ip = socket.gethostbyname( hostName )
	return ip

def getHostInfoTupleByName( host_name ):
	'''获取包括主机名，同一IP的可选主机名的一个列表，同一主机同一接口的其他IP组成的列表'''
	infoTuple = socket.gethostbyname_ex( hostName )
	return infoTuple

def getHostInfoTupleByIP( IPString ):
	'''获取包括主机名，同一IP的可选主机名的一个列表，同一主机同一接口的其他IP组成的列表'''
	infoTuple = socket.gethostbyaddr( IPString )
	return infoTuple

```
>**补充**：
>- 在ubuntu下测试，`socket.gethostbyname(socket.gethostname())`获取的是本地环回测试地址`127.0.1.1`。原因是`\etc\hosts`文件中有条目
>*`127.0.1.1`  `hostname`*
>而计算机在通过DNS解析域名之前，会首先到本机hosts文件中寻找域名与IP的对应关系。所以获取本机真实的外网地址，需要首先将这一条目除去。注意删去该条目会减缓本地用户切换的时间（例如：`sudo`），而且会让`socket.gethostbyaddr( socket.gethostbyname( socket.gethostname() ) )`方法抛出`socket.herror`异常
>- 若将该条目除去之后，仍然获取的不是外网地址，可以通过`socket.gethostbyname_ex(hostName)`方法，它返回包括三个元素的元组，分别是给定地址的主要的主机名、同一IP地址的可选的主机名的一个列表、关于同一主机的同一接口的其它IP地址的一个列表。同样，`gethostbyaddr(IPstring)`方法的返回值与`gethostbyname_ex`相同，但参数是一个IP地址字符串。
>- 非本机执行该方法可正常获取IP

----------



