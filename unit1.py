#-*- coding:utf-8 -*-
import socket

#1.2打印设备名和IPv4的地址
def getHostName():
    '''输出本机的网络设备名称'''
    hostName = socket.gethostname()
    return hostName

def getHostByName( hostName ):
    '''根据网络设备名获得本机IP'''
    ip = socket.gethostbyname( hostName )
    return ip

def getHostInfoTupleByName( hostName ):
    '''获取包括主机名，同一IP的可选主机名的一个列表，同一主机同一接口的其他IP组成的列表'''
    infoTuple = socket.gethostbyname_ex( hostName )
    return infoTuple

def getHostInfoTupleByIP( IPString ):
    '''获取包括主机名，同一IP的可选主机名的一个列表，同一主机同一接口的其他IP组成的列表'''
    infoTuple = socket.gethostbyaddr( IPString )
    return infoTuple

if __name__ == '__main__':
    hostName = getHostName()
    IP       = getHostByName( getHostName() )
    infoTupleByName = getHostInfoTupleByName( hostName )
    infoTupleByName = getHostInfoTupleByIP( IP )
    print IP
