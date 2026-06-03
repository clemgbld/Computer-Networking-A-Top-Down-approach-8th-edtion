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

What is an essential different between RR and WFQ packet scheduling? Is
there a case (Hint: Consider the WFQ weights) where RR and WFQ will
behave exactly the same?

### Section 4.3
