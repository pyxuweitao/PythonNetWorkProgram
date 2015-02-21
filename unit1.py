#-*- coding:utf-8 -*-
import socket
from binascii import hexlify

#主机字节序和网络字节序之间相互转换
def convert_integer( integer ):
    '''主机字节序和网络字节序之间的转换'''
    long_host_byte = socket.ntohl( integer )
    network_byte   = socket.htons( integer )
    return [long_host_byte, network_byte]


#1.5 通过指定的端口和协议找到服务名
def find_service_name( port, protocol_type ):
    '''根据端口和协议类型获取协议名称'''
    return socket.getservbyport( port, protocol_type )

#1.4 将IPv4地址转换成不同的格式
def convert_ipv4( ip ):
    '''return 字典：{'ip':原始IP地址,'packed':打包转化成32位二进制的ip地址,'unpacked': 解包解析出IP地址字符串, 'hex':32位二进制IP地址转化成16进制 }
    将IPv4地址转换成32位二进制格式
    '''
    packed_ip   = socket.inet_aton( ip )
    unpacked_ip = socket.inet_ntoa( packed_ip )
    return { 'ip':ip, 'packed':packed_ip, 'unpacked':unpacked_ip, 'hex':hexlify( packed_ip ) }

#1.3 获取远程设备的IP地址
def get_remote_name( host_name ):
    '''与1.2章节的方法相同，增加了异常处理'''
    remote_host_name = host_name
    try:
        IPString = socket.gethostbyname( remote_host_name )
        return IPString
    except socket.error, errMsg:
        return errMsg

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

if __name__ == '__main__':
    hostName = getHostName()
    print hostName
    IP       = getHostByName( getHostName() )
    print IP
#    infoTupleByName = getHostInfoTupleByName( hostName )
#    print infoTupleByName
#    infoTupleByIP   = getHostInfoTupleByIP( IP )
#    print infoTupleByIP
#    host            = get_remote_name( 'www.python.org' )
#    print host
    dic = convert_ipv4( IP )
    data_list = convert_integer( 32 )
    print data_list
