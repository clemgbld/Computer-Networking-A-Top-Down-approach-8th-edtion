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

the average is 1.92.

b)

Now assume a priority service, and assume that odd-numbered packets
are high priority, and even-numbered packets are low priority. Indicate the
time at which packets 2 through 12 each leave the queue. For each packet,
what is the delay between its arrival and the beginning of the slot in which
it is transmitted? What is the average of this delay over all 12 packets?

packet  D
1       0
2       2
3       0
4       5
5       0
6       5
7       1
8       4
9       0
10      3
11      0
12      2


the average is 1.83.

c)
Now assume round robin service. Assume that packets 1, 2, 3, 6, 11, and
12 are from class 1, and packets 4, 5, 7, 8, 9, and 10 are from class 2.
Indicate the time at which packets 2 through 12 each leave the queue. For
each packet, what is the delay between its arrival and its departure? What
is the average delay over all 12 packets?

packet  D
1       0
2       1
3       1
4       2
5       2
6       2
7       3
8       2
9       4
10      4
11      0
12      2


the average is 1.917.


d)

Now assume weighted fair queueing (WFQ) service. Assume that odd-
numbered packets are from class 1, and even-numbered packets are from
class 2. Class 1 has a WFQ weight of 2, while class 2 has a WFQ weight
of 1. Note that it may not be possible to achieve an idealized WFQ sched-
ule as described in the text, so indicate why you have chosen the particu-
lar packet to go into service at each time slot. For each packet what is the
delay between its arrival and its departure? What is the average delay over
all 12 packets?

packet  D
1       0
2       2
3       0
4       4
5       0
6       5
7       1
8       4
9       1
10      3
11      0
12      3



the average is 1.917.

e)
What do you notice about the average delay in all four cases (FIFO, RR,
priority, and WFQ)?

The average delay is pretty much the same in for every queuing strategy.

#### 7

Consider again the figure for P6.

a) 

Assume a priority service, with packets 1, 4, 5, 6, and 11 being high-
priority packets. The remaining packets are low priority. Indicate the slots
in which packets 2 through 12 each leave the queue.

slots 0  1  2  3  4  5  6  7  8  9  10  11

      1  4  6  5  2  3  7  8  11 9  10  12

b)

Now suppose that round robin service is used, with packets 1, 4, 5, 6, and
11 belonging to one class of traffic, and the remaining packets belonging
to the second class of traffic. Indicate the slots in which packets 2 through
12 each leave the queue.

slots 0  1  2  3  4  5  6  7  8  9  10  11

      1  2  4  3  6  7  5  8  11 9  10  12


c)

Now suppose that WFQ service is used, with packets 1, 4, 5, 6, and 11
belonging to one class of traffic, and the remaining packets belonging to the
second class of traffic. Class 1 has a WFQ weight of 1, while class 2 has a
WFQ weight of 2 (note that these weights are different than in the previous
question). Indicate the slots in which packets 2 through 12 each leave the
queue. See also the caveat in the question above regarding WFQ service.

My strategy for the two queues is to let the first packet get out in a FIFO manner.

slots 0  1  2  3  4  5  6  7  8  9  10  11

      2  3  1  7  4  8  9  6  10 12  5  11

#### 8

Consider a datagram network using 32-bit host addresses. Suppose a router
has four links, numbered 0 through 3, and packets are to be forwarded to the
link interfaces as follows:



11100000 00000000 00000000 00000000
through 11100000 00111111 11111111 11111111  0
11100000 01000000 00000000 00000000   
through 11100000 01000000 11111111 11111111  1
11100000 01000001 00000000 00000000
through 11100001 01111111 11111111 11111111  2
otherwise                                    3



Provide a forwarding table that has five entries, uses longest prefix match-
ing, and forwards packets to the correct link interfaces.

11100000 00*                                  0
1110000  01000000 *                           1
11100000 01000001*                            2
11100001 0*                                   2
*                                             3

Describe how your forwarding table determines the appropriate link inter-
face for datagrams with destination addresses:

11001000 10010001 01010001 01010101

it match no prefix in my forwarding table and hit the otherwise case and forward the packet to the link interface 3.

11100001 01000000 11000011 00111100

it match the prefix that forward the packet to the link interface 2. because 2 has the longest prefix.

11100001 10000000 00010001 01110111

it match no prefix in my forwarding table and hit the otherwise case and forward the packet to the link interface 3.

#### 9

Consider a datagram network using 8-bit host addresses. Suppose a router
uses longest prefix matching and has the following forwarding table:

00           0
010          1
011          2
10           3
11           4

For each of the four interfaces, give the associated range of destination host
addresses and the number of addresses in the range.

00000000 through  64 addresses
00111111

01000000 through 32 addresses
01011111

01100000 through 32 addresses
01111111

10000000 through 64 addresses
10111111

11000000 through 64 addresses
11111111


#### 10

Consider a datagram network using 8-bit host addresses. Suppose a router
uses longest prefix matching and has the following forwarding table:

1            0
10           1
111          2
*            3

For each of the four interfaces, give the associated range of destination host
addresses and the number of addresses in the range.

11000000 through 32 addresses
11011111

10000000 through 64 addresses
10111111

11100000 through 32 addresses
11111111

00000000 through 128 addresses
01111111

#### 11

Consider a router that interconnects three subnets: Subnet 1, Subnet 2,
and Subnet 3. Suppose all of the interfaces in each of these three subnets
are required to have the prefix 223.1.17/24. Also suppose that Subnet 1 is
required to support at least 60 interfaces, Subnet 2 is to support at least 90
interfaces, and Subnet 3 is to support at least 12 interfaces. Provide three
network addresses (of the form a.b.c.d/x) that satisfy these constraints.

223.1.17.0/25
223.1.17.128/26
223.1.17.192/28


#### 12

In Section 4.2.2, an example forwarding table (using longest prefix matching)
is given. Rewrite this forwarding table using the a.b.c.d/x notation instead of
the binary string notation

11001000 00010111 00010 = 200.23.16.0/21


11001000 00010111 00011000 = 200.23.24.0/24


11001000 00010111 00011 = 200.23.24.0/21

* = 0.0.0.0/0

#### 13

In Problem P8, you are asked to provide a forwarding table (using longest
prefix matching). Rewrite this forwarding table using the a.b.c.d/x notation
instead of the binary string notation.

11100000 00* = 224.0.0.0/10                                   0
1110000  0100000 * = 224.64.0.0/16                            1
11100000 0100000 1* = 224.64.128.0/17                         2
11100001 0* = 225.0.0.0/9                                     2
* = 0.0.0.0/0                                                 3

#### 14

Consider a subnet with prefix 128.119.40.128/26. Give an example of one
IP address (of form xxx.xxx.xxx.xxx) that can be assigned to this network.

128.119.40.160

Suppose an ISP owns the block of addresses of the form 128.119.40.64/26.
Suppose it wants to create four subnets from this block, with each block
having the same number of IP addresses. What are the prefixes (of form
a.b.c.d/x) for the four subnets?

128.119.40.64/28
128.119.40.80/28
128.119.40.96/28
128.119.40.112/28

#### 15

Consider the topology shown in Figure 4.20.
Denote the three subnets with hosts (starting clockwise at 12:00) as Networks A, B, and C. Denote the
subnets without hosts as Networks D, E, and F.

a. Assign network addresses to each of these six subnets, with the following
constraints: All addresses must be allocated from 214.97.254/23; Subnet A
should have enough addresses to support 250 interfaces; Subnet B should
have enough addresses to support 120 interfaces; and Subnet C should
have enough addresses to support 120 interfaces. Of course, subnets D, E
and F should each be able to support two interfaces. For each subnet, the
assignment should take the form a.b.c.d/x or a.b.c.d/x – e.f.g.h/y.

A 214.97.254.0/24 - 214.97.254.0/30
B 214.97.255.0/24 - 214.97.255.0/25
C 214.97.255.0/25 - 214.97.255.0/30
D 214.97.254.0/31
E 214.97.255.0/31
F 214.97.255.2/31


b. Using your answer to part (a), provide the forwarding tables (using long-
est prefix matching) for each of the three routers.

R1 forwarding table

214.97.254.0/24 -> A
214.97.254.0/31 -> D
214.97.255.128/25 -> R2 
214.97.255.0/25 -> R3 
214.97.255.0/31 -> R2

R2 forwarding table


214.97.254.0/24 -> R1
214.97.255.128/25 -> B
214.97.255.0/31 -> E
* -> R3

R3 forwarding table

214.97.254.0/24 -> R1
214.97.255.0/25 -> C
214.97.255.2/31 -> F
* -> R2

#### 16

Use the whois service at the American Registry for Internet Numbers
(http://www.arin.net/whois) to determine the IP address blocks for three
universities. 

UCLA:

UCLANET4 (NET-169-232-0-0-1)	169.232.0.0 - 169.232.255.255
UCLA-DR-NET1 (NET-192-35-210-0-1)	192.35.210.0 - 192.35.210.255
UCLA-DR-NET2 (NET-192-35-225-0-1)	192.35.225.0 - 192.35.225.255
UCLANET6 (NET6-2607-F010-1)	2607:F010:: - 2607:F010:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF


NYU:

NYU-NET6 (NET6-2607-F600-1)	2607:F600:: - 2607:F600:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF
NYU-NET2 (NET-216-165-0-0-1)	216.165.0.0 - 216.165.127.255

BERKLEY:

BERKLEY (NET-64-38-254-24-1)	64.38.254.24 - 64.38.254.31

Can the whois services be used to determine with certainty the
geographical location of a specific IP address? 

I don't think so the location must have been provided when the universities registered for the first time.
Their servers can be elsewhere now.


Use www.maxmind.com to determine the locations of the Web servers at each of these universities.

UCLA:

UCLANET4 (NET-169-232-0-0-1)	169.232.0.0 - 169.232.255.255 - 
Los Angeles, California, United States (US), North America
UCLA-DR-NET1 (NET-192-35-210-0-1)	192.35.210.0 - 192.35.210.255
United States (US), North America
UCLA-DR-NET2 (NET-192-35-225-0-1)	192.35.225.0 - 192.35.225.255
United States (US), North America
UCLANET6 (NET6-2607-F010-1)	2607:F010:: - 2607:F010:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF
United States (US), North America

NYU:

NYU-NET6 (NET6-2607-F600-1)	2607:F600:: - 2607:F600:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF
United States (US), North America
NYU-NET2 (NET-216-165-0-0-1)	216.165.0.0 - 216.165.127.255
United States (US), North America

BERKLEY:

BERKLEY (NET-64-38-254-24-1)	64.38.254.24 - 64.38.254.31
Phoenix, Arizona, United States (US), North America

#### 17

Suppose datagrams are limited to 1,500 bytes (including header) between
source Host A and destination Host B. Assuming a 20-byte IP header, how
many datagrams would be required to send an MP3 consisting of 5 million
bytes? Explain how you computed your answer.

One datagram = 1500 - 20 (TCP header) - 20 (TCP header) =  1460
5 000 0000 / 1460 = 3425 datagrams

#### 18

Consider the network setup in Figure 4.25. Suppose that the ISP instead
assigns the router the address 24.34.112.235 and that the network address
of the home network is 192.168.1/24.
a. Assign addresses to all interfaces in the home network.
Router 192.168.1.4
HOST 1 192.168.1.1
HOST 2 192.168.1.2
HOST 3 192.168.1.3

b. Suppose each host has two ongoing TCP connections, all to port 80 at
host 128.119.40.86. Provide the six corresponding entries in the NAT
translation table.

24.34.112.235, 5001 , 192.168.1.1, 3345
24.34.112.235, 5002 , 192.168.1.2, 3346
24.34.112.235, 5003 , 192.168.1.3, 3347
24.34.112.235, 5004 , 192.168.1.1, 3348
24.34.112.235, 5005 , 192.168.1.2, 3349
24.34.112.235, 5006 , 192.168.1.3, 3350

#### 19

Suppose you are interested in detecting the number of hosts behind a NAT.
You observe that the IP layer stamps an identification number sequentially on
each IP packet. The identification number of the first IP packet generated by
a host is a random number, and the identification numbers of the subsequent
IP packets are sequentially assigned. Assume all IP packets generated by
hosts behind the NAT are sent to the outside world.

a. Based on this observation, and assuming you can sniff all packets sent by
the NAT to the outside, can you outline a simple technique that detects the
number of unique hosts behind a NAT? Justify your answer.

The technique would be to group each contiguous  packets by id range and then count the number of range which would give us the number of hosts.
This technique would be broken tough if a first randomly generated id is contiguous with one last generated id of another host assuming the message is not the same and that we don't know the size of the message.


b. If the identification numbers are not sequentially assigned but randomly
assigned, would your technique work? Justify your answer.

Not it won't work since we couldn't group by range of id anymore.

#### 20

In this problem, we’ll explore the impact of NATs on P2P applications.
Suppose a peer with username Arnold discovers through querying that a
peer with username Bernard has a file it wants to download. Also suppose
that Bernard and Arnold are both behind a NAT. Try to devise a technique
that will allow Arnold to establish a TCP connection with Bernard without
application-specific NAT configuration. If you have difficulty devising such
a technique, discuss why.

It's impossible Bernard does't have a public direct public ip address because he is behind a NAT and the NAT router is the only one that has a public IP.

While searching online i found the Rendez-vous protocol.

#### 21

Consider the SDN OpenFlow network shown in Figure 4.30. Suppose
that the desired forwarding behavior for datagrams arriving at s2 is as
follows:
• any datagrams arriving on input port 1 from hosts h5 or h6 that are des-
tined to hosts h1 or h2 should be forwarded over output port 2;
• any datagrams arriving on input port 2 from hosts h1 or h2 that are des-
tined to hosts h5 or h6 should be forwarded over output port 1;
• any arriving datagrams on input ports 1 or 2 and destined to hosts h3 or h4
should be delivered to the host specified;
• hosts h3 and h4 should be able to send datagrams to each other.
Specify the flow table entries in s2 that implement this forwarding behavior.

OpenFlow table S2

- Ingress port = 1, IP src = 10.0.3.*, IP dest = 10.0.1.* | Forward(2)
- Ingress port = 2, IP src = 10.0.1.*, IP dest = 10.0.3.* | Forward(1)
- IP dest = 10.0.2.0.4 | Forward(4)
- IP dest = 10.0.2.0.3 | Forward(3)

#### 22

Consider again the SDN OpenFlow network shown in Figure 4.30. Suppose
that the desired forwarding behavior for datagrams arriving from hosts h3 or
h4 at s2 is as follows:

• any datagrams arriving from host h3 and destined for h1, h2, h5 or h6
should be forwarded in a clockwise direction in the network;
• any datagrams arriving from host h4 and destined for h1, h2, h5
or h6 should be forwarded in a counter-clockwise direction in the
network.
Specify the flow table entries in s2 that implement this forwarding behavior.

OpenFlow table S2

Ip Src = 10.0.2.0.3 | Forward(2)
Ip Src = 10.0.2.0.4 | Forward(1)

#### 23

Consider again the scenario from P21 above. Give the flow tables entries at
packet switches s1 and s3, such that any arriving datagrams with a source
address of h3 or h4 are routed to the destination hosts specified in the desti-
nation address field in the IP datagram. (Hint: Your forwarding table rules
should include the cases that an arriving datagram is destined for a directly
attached host or should be forwarded to a neighboring router for eventual
host delivery there.)


OpenFlow table S3

IP dest = 10.3.0.6 | Forward(1)
IP dest = 10.3.0.5 | Forward(2)
IP dest = 10.2.0.* | Forward(4)
IP dest = 10.1.0.* | Forward(3)

OpenFlow table S1

IP dest = 10.1.0.1 | Forward(2)
IP dest = 10.1.0.2 | Forward(3)
IP dest = 10.2.0.* | Forward(4)
IP dest = 10.3.0.* | Forward(1)

#### 24

Consider again the SDN OpenFlow network shown in Figure 4.30. Suppose
we want switch s2 to function as a firewall. Specify the flow table in s2 that
implements the following firewall behaviors (specify a different flow table
for each of the four firewalling behaviors below) for delivery of datagrams
destined to h3 and h4. You do not need to specify the forwarding behavior in
s2 that forwards traffic to other routers.


• Only traffic arriving from hosts h1 and h6 should be delivered to hosts h3
or h4 (i.e., that arriving traffic from hosts h2 and h5 is blocked).


OpenFlow table S2

Ip dest = 10.2.0.4, Ip Src = 10.1.0.1 | Forward(4)
Ip dest = 10.2.0.3, Ip Src = 10.1.0.1 | Forward(3)
Ip dest = 10.2.0.4, Ip Src = 10.3.0.6 | Forward(4)
Ip dest = 10.2.0.3, Ip Src = 10.3.0.6 | Forward(3)


• Only TCP traffic is allowed to be delivered to hosts h3 or h4 (i.e., that
UDP traffic is blocked).


OpenFlow table S2

Transport protocol = TCP , Ip dest = 10.2.0.4 | Forward(4)
Transport protocol = TCP , Ip dest = 10.2.0.3 | Forward(3)

• Only traffic destined to h3 is to be delivered (i.e., all traffic to h4 is
blocked).

OpenFlow table S2

Ip dest = 10.2.0.3 | Forward(3)

• Only UDP traffic from h1 and destined to h3 is to be delivered. All other
traffic is blocked.

OpenFlow table S2

Transport protocol = UDP , Ip dest = 10.2.0.3, Ip src = 10.1.0.1 | Forward(3)

#### 25

Consider the Internet protocol stack in Figures 1.23 and 4.31. Would you
consider the ICMP protocol to be a network-layer protocol or a transport-
layer protocol? Justify your answer.

It is a network layer protocol because it use to diagnose error on the network and it doesn't do multiplexing which is one of the core feature of any transport layer protocol, though what it does looks like the ACK message feature of the TCP protocol. 

### Wireshark-lab ip

#### 1

Select the first UDP segment sent by your computer via the traceroute
command to gaia.cs.umass.edu. (Hint: this is 44th packet in the trace file in the ipwireshark-trace1-1.pcapng file in footnote 2). Expand the Internet Protocol part
of the packet in the packet details window. What is the IP address of your
computer?

Source Address: 192.168.86.61

#### 2

What is the value in the time-to-live (TTL) field in this IPv4 datagram’s header?

Time to Live: 1

#### 3

 What is the value in the upper layer protocol field in this IPv4 datagram’s header?
[Note: the answers for Linux/MacOS differ from Windows here].

Protocol: UDP (17)

#### 4

How many bytes are in the IP header?

20 bytes

#### 5

How many bytes are in the payload of the IP datagram? Explain how you
determined the number of payload bytes.

8 bytes the length of the header of the transport layer (UDP) + 28 the length of the payload of the data = 36 bytes

Or you can do total length = 56 , minus the ip datagram header length = 20 which give 36

#### 6

 Has this IP datagram been fragmented? Explain how you determined whether or
not the datagram has been fragmented.

The more fragments, and the fragment offset are set to zero so no the ip datagram hasn't been fragemented.
#### 7 

Which fields in the IP datagram always change from one datagram to the next within this series of UDP segments sent by your computer destined to 128.119.245.12, via traceroute? Why?  

The identification field, to be able to reassamble fragmented ip datagrams, the checksum as well since the payload and the header are not the same, the TTL is not always the same as well. 

#### 8
Which fields in this sequence of IP datagrams (containing UDP segments) stay
constant? Why?

The ip source and destination, the protocol as well for obvious reasons.
 DSCP stays the same as well since the class of service won't change from one datagram to the other.  

#### 9

Describe the pattern you see in the values in the Identification field of the IP
datagrams being sent by your computer

The pattern i found is that it is always incremented by 1.

#### 10

 What is the upper layer protocol specified in the IP datagrams returned from the
routers? [Note: the answers for Linux/MacOS differ from Windows here].

Protocol: ICMP (1)

#### 11

Are the values in the Identification fields (across the sequence of all of ICMP
packets from all of the routers) similar in behavior to your answer to question 9
above?

Not it is not similar and it's normal since the ip datagrams are not from the same machine hence there are independant counters.

#### 12

Are the values of the TTL fields similar, across all of ICMP packets from all of
the routers?

No they are not.

#### 13

Find the first IP datagram containing the first part of the segment sent to
128.119.245.12 sent by your computer via the traceroute command to
gaia.cs.umass.edu, after you specified that the traceroute packet length
should be 3000. (Hint: This is packet 179 in the ip-wireshark-trace1-1.pcapng trace
file in footnote 2. Packets 179, 180, and 181 are three IP datagrams created by
fragmenting the first single 3000-byte UDP segment sent to 128.119.145.12).
Has that segment been fragmented across more than one IP datagram? (Hint: the
answer is yes
!)

Yes it has been fragmented in 2 ip datagrams and the last one is a segment and it's ip header has the fragmentation flag "more segments" set to zero to indicated that it's the last fragement.

#### 14

What information in the IP header indicates that this datagram been fragmented? 


The fragmentations flags are not all set to zero.

#### 15

 What information in the IP header for this packet indicates whether this is the first
fragment versus a latter fragment?

The first fragment has the fragment offset set to zero and the other not.

#### 16

How many bytes are there in is this IP datagram (header plus payload)?

1500 bytes

#### 17

Now inspect the datagram containing the second fragment of the fragmented UDP
segment. What information in the IP header indicates that this is not the first
datagram fragment?

It's fragment offset is not set to zero.

#### 18

What fields change in the IP header between the first and second fragment?

The fragment offset, the more fragments flags, the header checksum.

#### 19

Now find the IP datagram containing the third fragment of the original UDP
segment. What information in the IP header indicates that this is the last fragment
of that segment

The more framgments flag is set to zero.

#### 20

What is the IPv6 address of the computer making the DNS AAAA request? This
is the source address of the 20th packet in the trace. Give the IPv6 source address
for this datagram in the exact same form as displayed in the Wireshark window.

Source Address: 2601:193:8302:4620:215c:f5ae:8b40:a27a

#### 21

What is the IPv6 destination address for this datagram? Give this IPv6 address in
the exact same form as displayed in the Wireshark window.

Destination Address: 2001:558:feed::1

#### 22

What is the value of the flow label for this datagram?

Flow Label: 0x63ed0

#### 23

How much payload data is carried in this datagram?

Payload Length: 37

#### 24

What is the upper layer protocol to which this datagram’s payload will be
delivered at the destination?

Next Header: UDP (17)

#### 25

How many IPv6 addresses are returned in the response to this AAAA request?

14, 13 if you remove the canonical name.

#### 26

What is the first of the IPv6 addresses returned by the DNS for youtube.com (in
the ip-wireshark-trace2-1.pcapng trace file, this is also the address that is numerically the smallest)? Give this IPv6 address in the exact same shorthand
form as displayed in the Wireshark window.

youtube.com: type AAAA, class IN, addr 2607:f8b0:4006:815::200e
