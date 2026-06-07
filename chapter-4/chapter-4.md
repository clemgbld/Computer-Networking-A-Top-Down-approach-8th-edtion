# CHAPTER 4: The network layer: data plane

## Review questions

### Section 4.1

#### 1
  
Let’s review some of the terminology used in this textbook. Recall that the
name of a transport-layer packet is segment and that the name of a link-layer
packet is frame. What is the name of a network-layer packet? 

The name of network-layer packet is a datagram.

Recall that both
routers and link-layer switches are called packet switches. What is the funda-
mental difference between a router and link-layer switch?

- A link-layer switch lives at the layer 2 it forwards frame based on the mac addresses

- A router lives at the layer 3 its forwards data frame based on its ip address from an input link to an output link.

#### 2

We noted that network layer functionality can be broadly divided into
data plane functionality and control plane functionality. What are the main
functions of the data plane? Of the control plane?

- The main function of the data plane (hardware) is to forward datagram from an input link to an output link.

- the main function of the control plane (software) is to handle the routing part by building a forwarding table with ip addresses as key and output link as value, it provides this last to the data plane.

#### 3

We made a distinction between the forwarding function and the routing func-
tion performed in the network layer. What are the key differences between
routing and forwarding?


- the act of routing is to determine the where the datagram goes based on their ip addresses via a routing algorithm to build a forwarding table.  

- the act of forwarding is to physically move one datagram from the input link to an output link, to achieve that it use the forwarding table built by the routing phase.

#### 4

What is the role of the forwarding table within a router?

The role of the forwarding table within a router is to know to which output link to forward based on the ip address of a datagram.

#### 5

We said that a network layer’s service model “defines the characteristics of
end-to-end transport of packets between sending and receiving hosts.” What is
the service model of the Internet’s network layer? What guarantees are made by
the Internet’s service model regarding the host-to-host delivery of datagrams?

The nertwork layer's service model is known as a "best effort" service model, which is an euphemism for no guarantees at all.

### Section 4.2

#### 6

In Section 4.2, we saw that a router typically consists of input ports, output ports,
a switching fabric and a routing processor. Which of these are implemented in
hardware and which are implemented in software? 

Hardware:
- input ports
- output ports
- switching fabric

Software:
- Routing processor

Why? 

Because the hardware part (which represent the data plane) must be really fast (perform action in nano seconds), the routing phase can be slower (can take seconds or ms).

Returning to the
notion of the network layer’s data plane and control plane, which are imple-
mented in hardware and which are implemented in software? 

- data plane = hardware
- control plane = software


Why?

Again it is a question of performance but also with the advent of sdn it is a question of separation of concern.

#### 7

Discuss why each input port in a high-speed router stores a shadow copy of
the forwarding table.

It's faster to have a shadow copy of the forwarding table also the routing processor is potentially not even in the router and we must get the forwarding table from it via a remote controller so it is faster to get it once in each input port.

#### 8

What is meant by destination-based forwarding? 

It means that the decision of where the datagram will be forwarded will be taken based on the destination ip address in the datagram.

How does this differ from
generalized forwarding (assuming you’ve read Section 4.4, which of the two
approaches are adopted by Software-Defined Networking)?

It differ by the fact that generalized forwarding can decide where the datagram goes based on many other factors, such as the destionation madc address, the source or destination port in the transport layer etc...

#### 9

Suppose that an arriving packet matches two or more entries in a router’s
forwarding table. With traditional destination-based forwarding, what rule
does a router apply to determine which of these rules should be applied
to determine the output port to which the arriving packet should be
switched?

There is a longest prefix matching rule.

#### 10

Three types of switching fabrics are discussed in Section 4.2. List and briefly
describe each type. 

- memory

The datagram is copied by the routing processor (a CPU) via memory from the input to the output port.

- bus

The datagram go from the input to the output port via a shared bus which is not the routing processor.

- interconnection network

The datagram go from the input to the output port via multiple bus glued together by a crossbar switch.

Which, if any, can send multiple packets across the fabric
in parallel?

The interconnection one can send multiple packets across the fabric in parallel.

#### 11

Describe how packet loss can occur at input ports. Describe how packet loss
at input ports can be eliminated (without using infinite buffers).

Loss can occur at input port when the queue of the input port is full, the queue grows when one datagram must go into one output port but another one is already there thus blocking the rest of the datagram even if they go in another output port, this phenomena is known as HOL blocking (head of a line blocking).

The amount of buffering needed to avoid loss is B = RTT * C / sqrt(N) where N is TCP flows and C link capacity.

#### 12

Describe how packet loss can occur at output ports. 

A loss can occur when the datagram arival rate temporarily exceeds the rate at which datagram can be forwarded to the output link and the queue arrived at capacity then drop a datagram.

Can this loss be pre-vented by increasing the switch fabric speed?

The bottleneck will then become the capacity of the link so no.

#### 13

What is HOL blocking? 

It is when a datagram that must wait because its destination output port is busy block the other datagrams behind this last even though their destination output may be free.

Does it occur in input ports or output ports?

It occurs at input port.

#### 14

In Section 4.2, we studied FIFO, Priority, Round Robin (RR), and Weighted
Fair Queueing (WFQ) packet scheduling disciplines? Which of these queueing
disciplines ensure that all packets depart in the order in which they arrived?

The FIFO queuing discipline.

#### 15

Give an example showing why a network operator might want one class of
packets to be given priority over another class of packets.

For example reazl-time voice-over-ip packets might receive priority over non-real-time traffic such as email packets.

#### 16

What is an essential different between RR and WFQ packet scheduling? 

the difference is that queue have weight assigned to them when using WFQ.

Is there a case (Hint: Consider the WFQ weights) where RR and WFQ will
behave exactly the same?

RR and WFQ will behave the same when every queue as the same weights when using WFQ.

### Section 4.3

#### 17

Suppose Host A sends Host B a TCP segment encapsulated in an IP data-
gram. When Host B receives the datagram, how does the network layer in
Host B know it should pass the segment (that is, the payload of the datagram)
to TCP rather than to UDP or to some other upper-layer protocol

It known thanks to the upper-layer protocol field.

ipv4 protocol field , ipv6 next header field

#### 18

What field in the IP header can be used to ensure that a packet is forwarded
through no more than N routers?

the ip header is Hop limit in an ipv6 header, TTL in ipv4.

#### 19

Recall that we saw the Internet checksum being used in both transport-layer
segment (in UDP and TCP headers, Figures 3.7 and 3.29 respectively) and in
network-layer datagrams (IP header, Figure 4.17). Now consider a transport
layer segment encapsulated in an IP datagram. Are the checksums in the seg-
ment header and datagram header computed over any common bytes in the IP
datagram? Explain your answer.

Yes the source and destination ip, as well has the protocol field because the checksum of the transport layer is end to end.

#### 20

When a large datagram is fragmented into multiple smaller datagrams, where
are these smaller datagrams reassembled into a single larger datagram?

the datagrams are reassembled by the host in the network layer.

#### 21

Do routers have IP addresses? If so, how many?

In general a router have one IP addresss by physical interface but it can have non as well.

#### 22

What is the 32-bit binary equivalent of the IP address 223.1.3.27?

11011111  00000001 00000011  00011011

#### 23

Visit a host that uses DHCP to obtain its IP address, network mask, default
router, and IP address of its local DNS server. List these values.

DHCP Configuration
IP address: 192.168.178.44
Subnet mask: 255.255.255.0
Router: 192.168.178.1
DNS: 192.168.178.1

#### 24

Suppose there are three routers between a source host and a destination host.
Ignoring fragmentation, an IP datagram sent from the source host to the desti-
nation host will travel over how many interfaces? 

8,  1 source host interface, 3 input ports and 3 output ports and the source interface.

How many forwarding tables
will be indexed to move the datagram from the source to the destination?

3 forwarding tables one at each router.

#### 25

Suppose an application generates chunks of 40 bytes of data every 20 msec,
and each chunk gets encapsulated in a TCP segment and then an IP datagram.
What percentage of each datagram will be overhead, and what percentage
will be application data?

50% of overhead and 50% of application data, since there 40 bytes of application data and 40 bytes of header because a TCP segment header is 5 rows of 32 bits (4 bytes) and same for the ip datagram rows if there is not any options.

#### 26

Suppose you purchase a wireless router and connect it to your cable modem.
Also suppose that your ISP dynamically assigns your connected device (that
is, your wireless router) one IP address. Also suppose that you have five PCs
at home that use 802.11 to wirelessly connect to your wireless router. How
are IP addresses assigned to the five PCs? 

Each PC will send a DHCP discover message, then the DHCP server will send them back a DHCP offer (containing their ip addresses) and then the PC will make a DHCP request then it will receive an ACK message from the DHCP server.


Does the wireless router use NAT?
Why or why not?

Yes it use NAT because you can plug only one device to your cable model so you need a router which has one ip address then when you receive or send packets only one ip addresses is publicly exposes and this is the one of the router so a translation needs to occurs (with the NAT table) to translate the public ip address to one of the 5 ip addresses (the ones of the PC).

#### 27

What is meant by the term “route aggregation”? Why is it useful for a router
to perform route aggregation?

Route aggregation is a space saving trick, it aggregate multiple route into one single route that represent the range of a network.

example:

Subnet A: 192.168.1.0/24
Subnet B: 192.168.2.0/24
Subnet C: 192.168.3.0/24
Subnet D: 192.168.0.0/24

becomes 192.168.0.0/22

#### 28

What is meant by a “plug-and-play” or “zeroconf” protocol?

This mean that you have nothing to configure yourself the protocol handles all the details for you.

#### 29

What is a private network address? 

A private network address is an address that is not publicly exposed, it the address of a device in a private network, it's addresses gets translated by a NAT whenever a datagram is sent or received.

Should a datagram with a private network
address ever be present in the larger public Internet? Explain.

No because the datagram wouldn't reach it's destination because packet or ACK packet would never reach their destinations.

#### 30

Compare and contrast the IPv4 and the IPv6 header fields. Do they have any
fields in common?

IPv4 has many more fields, yes the source and destination addresses, the next header (which is upper protocol layer in the IPV4), The version field, and the payload length

#### 31

It has been said that when IPv6 tunnels through IPv4 routers, IPv6 treats the
IPv4 tunnels as link-layer protocols. Do you agree with this statement? Why
or why not?

Yes i would say since it wraps the IPV6 datagram with an IPV4 one instead of wrapping a frame it will unwrap an IPV6 datagram on the IPV6 router receiving side, you can kind of see that like as a link layer usurpation.

### Section 4.4

#### 32

How does generalized forwarding differ from destination-based forwarding?

it's differs because it's a more generalized action that can achieve destination-based forwarding but also any kind of match + actions.

#### 33

What is the difference between a forwarding table that we encountered in
destination-based forwarding in Section 4.1 and OpenFlow’s flow table that
we encountered in Section 4.4?

The OpenFlow's flow tables are more flexible you can achieve destination based forwarding but also many other match + actions such as load balancing, firewalling etc...

#### 34

What is meant by the “match plus action” operation of a router or switch? In
the case of destination-based forwarding packet switch, what is matched and
what is the action taken? 

IN the case of destination-based forwarding packet switch an ip address is matched and then the action is to forward the packet to the desired output port.

In the case of an SDN, name three fields that can be
matched, and three actions that can be taken.

Examples of fields that can be matched:

- Src MAC, Dest MAC

- Src IP, Dest IP

- Src port, Dest Port

Actions that can be taken:

- Forwarding

- Firewalling (droping a packet)

- Load balancing

- NAT translation

- IPV6 wraped into an IPV4 to ensure compatibility then forward

#### 35

Name three header fields in an IP datagram that can be “matched” in Open-
Flow 1.0 generalized forwarding. 

- IP source
- IP destination
- IP protocol
- IP type of service

What are three IP datagram header fields
that cannot be “matched” in OpenFlow?

- payload length
- hop limit / TTL
- version

### Problems

#### 1

Consider the network below.

a. Show the forwarding table in router A, such that all traffic destined to host
H3 is forwarded through interface 3.

destination host     link interface

H3                        3

b. Can you write down a forwarding table in router A, such that all traffic
from H1 destined to host H3 is forwarded through interface 3, while all
traffic from H2 destined to host H3 is forwarded through interface 4?
(Hint: This is a trick question.)

You cannot use load balancing with traditional forwarding table.

#### 2

Suppose two packets arrive to two different input ports of a router at exactly
the same time. Also suppose there are no other packets anywhere in the
router.


a. Suppose the two packets are to be forwarded to two different output ports.
Is it possible to forward the two packets through the switch fabric at the
same time when the fabric uses a shared bus?

No only one packet can be in the shared bus at the same time.

b. Suppose the two packets are to be forwarded to two different output ports.
Is it possible to forward the two packets through the switch fabric at the
same time when the fabric uses switching via memory?

Only one memory read/write can be done at the same time so no.

c. Suppose the two packets are to be forwarded to the same output port. Is it
possible to forward the two packets through the switch fabric at the same
time when the fabric uses a crossbar?

No because since they should be forwarded to the same output port they share the same path only packets that don't cross paths can be forwarded at the same time.

#### 3

In Section 4.2.4, it was said that if R_switch is N times faster than R_line,
then only negligible queuing will occur at the input ports, even if all the
packets are to be forwarded to the same output port. Now suppose that
R_switch = R_line, but all packets are to be forwarded to different output
ports. Let D be the time to transmit a packet. As a function of D, what is the
maximum input queuing delay for a packet for the (a) memory, (b) bus, and
(c) crossbar switching fabrics?

a and b will always have N - 1 packets waiting in queue that wait that the switch fabric forward another packet so (N  - 1) * D

c will have no queuing

#### 4

Consider the switch shown below. Suppose that all datagrams have the same
fixed length, that the switch operates in a slotted, synchronous manner, and
that in one time slot a datagram can be transferred from an input port to an
output port. The switch fabric is a crossbar so that at most one datagram can
be transferred to a given output port in a time slot, but different output ports
can receive datagrams from different input ports in a single time slot. What is
the minimal number of time slots needed to transfer the packets shown from
input ports to their output ports, assuming any input queue scheduling order
you want (i.e., it need not have HOL blocking)? What is the largest number
of slots needed, assuming the worst-case scheduling order you can devise,
assuming that a non-empty input queue is never idle?

- the minimum time slots required is 2

- the maximum time slots is 3

#### 5

Suppose that the WEQ scheduling policy is applied to a buffer that supports
three classes, and suppose the weights are 0.5, 0.25, and 0.25 for the three
classes.

a. Suppose that each class has a large number of packets in the buffer.
In what sequence might the three classes be served in order to achieve
the WFQ weights? (For round robin scheduling, a natural sequence is
123123123 . . .).
112311231123... .
b. Suppose that classes 1 and 2 have a large number of packets in the buffer,
and there are no class 3 packets in the buffer. In what sequence might the
three classes be served in to achieve the WFQ weights?
112112112... .

#### 6

Consider the figure below. Answer the following questions:

a) 
Assuming FIFO service, indicate the time at which packets 2 through
12 each leave the queue. For each packet, what is the delay between its
arrival and the beginning of the slot in which it is transmitted? What is the
average of this delay over all 12 packets?

packet  D
1       0
2       1
3       1
4       2
5       2
6       2
7       3
8       2
9       3
10      2
11      2
12      3

the average is 1.92 let's say 2.

b)

Now assume a priority service, and assume that odd-numbered packets
are high priority, and even-numbered packets are low priority. Indicate the
time at which packets 2 through 12 each leave the queue. For each packet,
what is the delay between its arrival and the beginning of the slot in which
it is transmitted? What is the average of this delay over all 12 packets?

c)
Now assume round robin service. Assume that packets 1, 2, 3, 6, 11, and
12 are from class 1, and packets 4, 5, 7, 8, 9, and 10 are from class 2.
Indicate the time at which packets 2 through 12 each leave the queue. For
each packet, what is the delay between its arrival and its departure? What
is the average delay over all 12 packets?

d)

Now assume weighted fair queueing (WFQ) service. Assume that odd-
numbered packets are from class 1, and even-numbered packets are from
class 2. Class 1 has a WFQ weight of 2, while class 2 has a WFQ weight
of 1. Note that it may not be possible to achieve an idealized WFQ sched-
ule as described in the text, so indicate why you have chosen the particu-
lar packet to go into service at each time slot. For each packet what is the
delay between its arrival and its departure? What is the average delay over
all 12 packets?

e)
What do you notice about the average delay in all four cases (FIFO, RR,
priority, and WFQ)?
