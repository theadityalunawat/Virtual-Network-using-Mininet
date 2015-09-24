#!/usr/bin/python

"""
This example shows how to create an empty Mininet object
(without a topology object) and add nodes to it manually.
"""
import sys
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink
def emptyNet():
    hos1 = "10.0.0."
    hos2 = "11.0.0."
    "Create an empty network and add nodes to it."

    net = Mininet( controller=Controller )

    info( '*** Adding controller\n' )
    net.addController( 'c0' )

    info( '*** Adding hosts\n' )
    h=[]
    j=1
    for i in range(int(sys.argv[1])):
        if(i % 2 == 0):
            ipallocate=hos1+str(j)
            hostName = "h"+str(j)
            h.append(net.addHost(hostName,ip=ipallocate))
            j+=1
        else:
            ipallocate=hos2+str(j);
            hostName = "h"+str(j)
            h.append(net.addHost(hostName,ip=ipallocate))
            j+=1
    print h
    # h1 = net.addHost( 'h1', ip='10.0.0.1' )
    # h2 = net.addHost( 'h2', ip='10.0.0.2' )

    info( '*** Adding switch\n' )
    k=1
    j=0
    sw=[]
    for i in range(int(sys.argv[2])):

        sw.append(net.addSwitch( 's'+str(k) ))
        k+=1
        info( '*** Creating links\n' )
        tmp=net.addLink( h[j], sw[i] )
        j+=1
        tmp.intf1.config(bw=1)
        tmp=net.addLink( h[j], sw[i]  )
        tmp.intf1.config(bw=2)
        j+=1
    for i in range(len(sw)-1):
        net.addLink(sw[i],sw[i+1])
    info( '*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()
