# CHAPTER 6: The link layer

## Review questions

### sections 6.1 - 6.2

#### 1

Consider the transportation analogy in Section 6.1.1. If the passenger is
analagous to a datagram, what is analogous to the link layer frame?

In this analogy the link layer is analogous to the transportation mode (eg limousine, plane etc...).

#### 2

If all the links in the Internet were to provide reliable delivery service, would
the TCP reliable delivery service be redundant? Why or why not?

If all the links in the internet were to provide reliable delivery service, the TCP reliable delivery service would not indeed be redundant since the reliable mechanism only guaranty no bits error but not that a router didn't drop a datagram for example.

#### 3

What are some of the possible services that a link-layer protocol can offer
to the network layer? Which of these link-layer services have corresponding
services in IP? In TCP?

- Framing

- Link access

- error detection (CRC) and corection: IP and TCP/UDP can detect error with a checksum mechanism, TCP can correct error as well with ARQ.

- Reliable devliery: TCP can offer reliable delivery

### sections 6.3

#### 4

Suppose two nodes start to transmit at the same time a packet of length L
over a broadcast channel of rate R. Denote the propagation delay between the
two nodes as dprop. Will there be a collision if dprop < L/R? Why or why not?

Yes there will be a collision if they start transmitting at the same time the fact that dprop < L/R and  they start to transmit at the same time the collision is inevitable. if dprop > L/R it would be fine.

#### 5

In Section 6.3, we listed four desirable characteristics of a broadcast channel.
Which of these characteristics does slotted ALOHA have? Which of these
characteristics does token passing have?

The properties:


- 1. When only one node has data to send , that node has a throughput of R bps.

- 2. When M nodes have data to send, each of these nodes has a throughput of R/M bps at least we tend toward that.

- 3. The protocol is decentralized; that is, there is no master node that represents a single point of failure in the network.

- 4. The protocol is simple, so that it is inexpensive to implement.

ALOHA, meet 1, 3 and 4
Token passing meets 1,2,4

#### 6

In CSMA/CD, after the fifth collision, what is the probability that a node
chooses K= 4? 

since the formula is {0,1,2,...2^n -1} then the probability to of k = 4 after the fifth collision is 1/32 so about 3%.

The result K= 4 corresponds to a delay of how many
seconds on a 10 Mbps Ethernet?

(512 * K) / 10Mbps = (512 * 4) / 10 Mbps = 204,8 microseconds 

#### 7

Describe polling and token-passing protocols using the analogy of cocktail
party interactions.

polling:

If i was at a party it would be like if i had a list of person in my head and i would see if the first person of my list has something to say to someone , i would hear him talk until he finishes then go repeat what he said to me to another perosn, then go do the same with the second person of my list until arriving at the end of my list and then going back to person one.

token-passing:

It would be like when someone has an item he can talk to the person he wants directly and then pass the item to someone else and then the other person would do the same.

#### 8

Why would the token-ring protocol be inefficient if a LAN had a very large
perimeter?

It would be inefficient because the more distance between the host, the less efficient the token ring protocol is.

### section 6.4

#### 9

 How big is the MAC address space? 
  
 6 bytes long. 2^48 possibilities.

 The IPv4 address space? 

 4 bytes long. 2 ^32 possibilities.

 The IPv6 address space?

 16 bytes. 2^128

#### 10

Suppose nodes A, B, and C each attach to the same broadcast LAN (through
their adapters). If A sends thousands of IP datagrams to B with each encap-
sulating frame addressed to the MAC address of B, will C’s adapter process
these frames? 

No it since it knows that the frame is not send to it by looking at the destination mac address.

If so, will C’s adapter pass the IP datagrams in these frames
to the network layer C? 

If the frame as not been discarded it will pass the ip datagrams to the network layer.

How would your answers change if A sends frames
with the MAC broadcast address?

If A sends frames with the MAC broadcast address both Node B and C would process it.

#### 11

Why is an ARP query sent within a broadcast frame? 

Because the node sending the ARP query doesn't know the Mac address of the target node but only its ip address.

Why is an ARP response sent within a frame with a specific destination MAC address?

For efficiency purpose only the node that ask for the translation will process the frame and update its address table.

#### 12

For the network in Figure 6.19, the router has two ARP modules, each with its
own ARP table. Is it possible that the same MAC address appears in both tables?

Not it is impossible only the MAC addresses of the machines of in your LAN can be in each router ARP tables.

#### 13

Compare the frame structures for 10BASE-T, 100BASE-T, and Gigabit
Ethernet. How do they differ?

Compare the frame structures for 10BASE-T, 100BASE-T, and Gigabit
Ethernet.

How do they differ?


They all have the same frame format.

#### 14

Consider Figure 6.15. How many subnetworks are there, in the addressing
sense of Section 4.3?

There is only 1 at the ip level.

#### 15

What is the maximum number of VLANs that can be configured on a switch
supporting the 802.1Q protocol? Why?

4096 (with 4094 usable), because 12 bits are reserved for the VLANID so 2^12 = 4096.

#### 16

Suppose that N switches supporting K VLAN groups are to be connected via
a trunking protocol. How many ports are needed to connect the switches?

Justify your answer.

2 * N ports to connect all the switches together the K is irrelevant here. And the minimum would be 2 (N - 1) because one switch does need to be connected with 2 switch with a trunk link.

### Problems

#### 1

Suppose the information content of a packet is the bit pattern 1110 0110 1001
0101 and an even parity scheme is being used. What would the value of the field
containing the parity bits be for the case of a two-dimensional parity scheme?
Your answer should be such that a minimum-length checksum field is used.

1110|1
0110|0
1001|0
0101|0
------
0100|1

#### 2

Show (give an example other than the one in Figure 6.5) that two-dimensional
parity checks can correct and detect a single bit error. Show (give an example
of) a double-bit error that can be detected but not corrected.

Error that can be detected and corrected:

1110|1
0110|0
1001|0
0101|0
------
0100|1


1100|0
0110|0
1001|0
0101|0
------
0110|1

Error detected at d (1,3) and can be corrected

Error that cannot be corrected

1110|1
0110|0
1001|0
0101|0
------
0100|1


1111|1
0110|0
1001|0
0100|0
------
0100|1

#### 3

Suppose the information portion of a packet (D in Figure 6.3) contains
10 bytes consisting of the 8-bit unsigned binary ASCII representation of
string “Internet.” Compute the Internet checksum for this data.

0x6a49 computed with internet_checksum.py

#### 4

Consider the previous problem, but instead suppose these 10 bytes contain

a. the binary representation of the numbers 1 through 10.

0xc5f9

b. the ASCII representation of the letters B through K (uppercase).

0xa098

c. the ASCII representation of the letters b through k (lowercase).


0xfff7

d. Compute the Internet checksum for this data.

Computed with internet_checksum.py

#### 5

Consider the 5-bit generator, G= 10011, and suppose that D has the value
1010101010. What is the value of R?

10101
10011
-----
00110

11001
10011
-----
01010

10100
10011
-----
00111

11110
10011
-----
01101

11010
10011
-----
01001

10010
10011
-----
00001

00100

R = 4

#### 6

Consider the previous problem, but suppose that D has the value

a. 1000100101.

8

b. 0101101010.

15

c. 0110100011.

14

Computed with crc.py

#### 7

In this problem, we explore some of the properties of the CRC. For
the generator G (= 1001) given in Section 6.2.3, answer the following
questions.

a. Why can it detect any single bit error in data D?

Because any single bit error will not make zero when on the receiver side we will do  crc(D + R, G)

b. Can the above G detect any odd number of bit errors? Why?

Yes it can because the remainder is 6 so any odd bit error will cause crc(D + R, G) to not be zero.

#### 8

In Section 6.3, we provided an outline of the derivation of the efficiency of
slotted ALOHA. In this problem we’ll complete the derivation.
a. Recall that when there are N active nodes, the efficiency of slotted
ALOHA is Np(1- p)N-1. Find the value of p that maximizes this
expression.

f'(p) = N(1 - p) (N - 2) * (1 - Np)

N(1 - p) (N - 2) * (1 - Np) = 0

1 - Np = 0

Np = 1

p = 1 / N



b. Using the value of p found in (a), find the efficiency of slotted ALOHA
by letting N approach infinity. Hint: (1- 1/N)N approaches 1/e as N
approaches infinity.

36.8 % efficiency

#### 9

Show that the maximum efficiency of pure ALOHA is 1/(2e). Note: This
problem is easy if you have completed the problem above!

18.4 %

#### 10

Consider two nodes, A and B, that use the slotted ALOHA protocol to con-
tend for a channel. Suppose node A has more data to transmit than node B,
and node A’s retransmission probability pA is greater than node B’s retrans-
mission probability, pB.

a)

Provide a formula for node A’s average throughput. What is the total
efficiency of the protocol with these two nodes?

total efficicency = pA + pB - 2pApB

b)

If pA = 2pB, is node A’s average throughput twice as large as that of node
B? Why or why not? If not, how can you choose pA and pB to make that
happen?

pA = 2pb / 1 + pb

c)

In general, suppose there are N nodes, among which node A has retrans-
mission probability 2p and all other nodes have retransmission probability
p. Provide expressions to compute the average throughputs of node A and
of any other node.

p * (1 - 2p) * (1 - p) N - 2


#### 13

Consider a broadcast channel with N nodes and a transmission rate of R bps.
Suppose the broadcast channel uses polling (with an additional polling node)
for multiple access. Suppose the amount of time from when a node completes
transmission until the subsequent node is permitted to transmit (that is, the
polling delay) is dpoll. Suppose that within a polling round, a given node is
allowed to transmit at most Q bits. What is the maximum throughput of the
broadcast channel?

Throughput = R * Q / R * dpoll + Q

#### 14

Consider three LANs interconnected by two routers, as shown in Figure 6.33.

a. Assign IP addresses to all of the interfaces. For Subnet 1 use
addresses of the form 192.168.1.xxx; for Subnet 2 uses addresses of
the form 192.168.2.xxx; and for Subnet 3 use addresses of the form
192.168.3.xxx.

[diagram](./problem-14.png)

b Assign MAC addresses to all of the adapters.

[diagram](./problem-14.png)

c Consider sending an IP datagram from Host E to Host B. Suppose all of
the ARP tables are up to date. Enumerate all the steps, as done for the
single-router example in Section 6.4.1.

E will send a datagram with a the ip adddress of Host B as destination, wrapped by an ethernet frame with the mac address of the router (1A-25-F6-CD-06-3D)

The router will get the ethernet frame and pass it to the network layer, and thanks to the routing table it will be forwarded in the subnet 2

Then it will be forwarded to the router 1A-25-F6-CD-06-3C then passed to the network layer, and then finally thanks to the routing table it will be forwarded to the subnet A

Where it will finally reach the host B

d Repeat (c), now assuming that the ARP table in the sending host is empty
(and the other tables are up to date).

- First the sending host B will send an ARP frame with the destination ip address of the router wrapped in an ethernet frame with the destination mac address which will be the broadcast address (FF-FF-FF-FF-FF-FF)

- Then the router will get it and send an arp reply with it's mac address (1A-25-F6-CD-06-3D)

- The sending host will receive it and update its ARP table

- Then it can do what we explain in the previous answer

#### 15

Consider Figure 6.33. Now we replace the router between subnets 1 and 2
with a switch S1, and label the router between subnets 2 and 3 as R1.

a Consider sending an IP datagram from Host E to Host F. Will Host E ask router
R1 to help forward the datagram? Why?

No they won't need to ask router R1 to help because they are in the same LAN.

In the Ethernet frame containing the
IP datagram, what are the source and destination IP and MAC addresses?

Destination ip

192.168.3.102

Source ip

192.168.3.101

Destination mac address

1A-25-F6-CD-06-2D

Source mac address

1A-25-F6-CD-06-1D

b Suppose E would like to send an IP datagram to B, and assume that E’s
ARP cache does not contain B’s MAC address. Will E perform an ARP
query to find B’s MAC address? Why? 

No because B and E are not in the same LAN so it will either send datagram with the ip of B + Ethernet frame (with the mac address of R1) to R1 or do an ARP query to get the mac address of R1 and send datagram with the ip of B + Ethernet with the mac address of R1.

In the Ethernet frame (containing
the IP datagram destined to B) that is delivered to router R1, what are the
source and destination IP and MAC addresses?

Destination ip

192.168.1.102

Source ip

192.168.3.101

Destination mac address

1A-25-F6-CD-06-3D

Source mac address

1A-25-F6-CD-06-1D

c  Suppose Host A would like to send an IP datagram to Host B, and neither A’s
ARP cache contains B’s MAC address nor does B’s ARP cache contain A’s
MAC address. Further suppose that the switch S1’s forwarding table contains
entries for Host B and router R1 only. Thus, A will broadcast an ARP request
message. What actions will switch S1 perform once it receives the ARP
request message?

It will forward the frame to all the node that it is attached to.

Will router R1 also receive this ARP request message? 

Yes it will since one of its adapter (the left one) is in the same LAN now

If so, will R1 forward the message to Subnet 3? 

No it won't, ARP request stay within the LAN

Once Host B receives this ARP
request message, it will send back to Host A an ARP response message. 
But will it send an ARP query message to ask for A’s MAC address? Why? 

No it won't send an ARP query message to ask for A's MAC address since the mac address was already in the ARP query.

What will switch S1 do once it receives an ARP response message from Host B?

S1 will forward it only to A. 

#### 16

Consider the previous problem, but suppose now that the router between sub-
nets 2 and 3 is replaced by a switch. Answer questions (a)–(c) in the previous
problem in this new context.

a Consider sending an IP datagram from Host E to Host F. Will Host E ask router
R1 to help forward the datagram? Why?

No they won't need to ask router R1 to help because they are in the same LAN.

In the Ethernet frame containing the
IP datagram, what are the source and destination IP and MAC addresses?

Destination ip

192.168.3.102

Source ip

192.168.3.101

Destination mac address

1A-25-F6-CD-06-2B

Source mac address

1A-25-F6-CD-06-1D

b Suppose E would like to send an IP datagram to B, and assume that E’s
ARP cache does not contain B’s MAC address. Will E perform an ARP
query to find B’s MAC address? Why? 

Yes it will because now they are in the same LAN.

In the Ethernet frame (containing
the IP datagram destined to B) that is delivered to router R1, what are the
source and destination IP and MAC addresses?

There is no router R1 anymore.

c  Suppose Host A would like to send an IP datagram to Host B, and neither A’s
ARP cache contains B’s MAC address nor does B’s ARP cache contain A’s
MAC address. Further suppose that the switch S1’s forwarding table contains
entries for Host B and router R1 only. Thus, A will broadcast an ARP request
message. What actions will switch S1 perform once it receives the ARP
request message?

It will forward the frame to all the node that it is attached to.

Will router R1 also receive this ARP request message? 

Yes it will since one of its adapter (the left one) is in the same LAN now

If so, will R1 forward the message to Subnet 3? 

There is no subnet anymore so yes it will forward the message in the whole LAN that include all hosts.

Once Host B receives this ARP
request message, it will send back to Host A an ARP response message. 
But will it send an ARP query message to ask for A’s MAC address? Why? 

No it won't send an ARP query message to ask for A's MAC address since the mac address was already in the ARP query.

What will switch S1 do once it receives an ARP response message from Host B?

S1 will forward it only to A. 


#### 17

Recall that with the CSMA/CD protocol, the adapter waits K * 512 bit times
after a collision, where K is drawn randomly. For K= 100, how long does
the adapter wait until returning to Step 2 for a 100 Mbps broadcast channel?

100 * K = 51200

At worst  51200 / 100^6 = 0,512 ms

For a 1 Gbps broadcast channel?

At worst 51200 / 10^9 = 51,2 microseconds

#### 18

Suppose nodes A and B are on the same 10 Mbps broadcast channel, and the
propagation delay between the two nodes is 325 bit times. Suppose CSMA/
CD and Ethernet packets are used for this broadcast channel. Suppose node
A begins transmitting a frame and, before it finishes, node B begins transmit-
ting a frame. Can A finish transmitting before it detects that B has transmit-
ted? Why or why not? 

Yes it can if t1 + 325 bits is less than 576 bits. 

If the answer is yes, then A incorrectly believes that its
frame was successfully transmitted without a collision. Hint: Suppose at time
t = 0 bits, A begins transmitting a frame. In the worst case, A transmits a
minimum-sized frame of 512 + 64 bit times. So A would finish transmitting
the frame at t = 512 + 64 bit times. Thus, the answer is no, if B’s signal
reaches A before bit time t = 512 + 64 bits. 

In the worst case, when does B’s signal reach A?

let's say B start transmitting at 324 just before receiving A signal it will thus alert A and the answer will be 324 + 325

At t = 649 bits

#### 19

Suppose nodes A and B are on the same 10 Mbps broadcast channel, and the
propagation delay between the two nodes is 245 bit times. Suppose A and
B send Ethernet frames at the same time, the frames collide, and then A and
B choose different values of K in the CSMA/CD algorithm. Assuming no
other nodes are active, can the retransmissions from A and B collide? 

No it is impossible since the difference between two number will be more than 245 bit times.

For our purposes, it suffices to work out the following example. Suppose A and B
begin transmission at t = 0 bit times. They both detect collisions at t = 245
t bit times. Suppose KA = 0 and KB = 1. At what time does B schedule its
retransmission?


B schedule its retransmission after 512 bits so t = 245 + 48 + 512 bits

At what time does A begin transmission? (Note: The nodes
must wait for an idle channel after returning to Step 2—see protocol.) 

t = 245 + 48 

At what time does A’s signal reach B? 

t = 245 + 48 + 245

Does B refrain from transmitting at its
scheduled time?

Yes because node A won't be done at t = 245 + 48 + 512 bits it will be done at t = 245 + 48 + 576

#### 21

Consider Figure 6.33 in problem P14. Provide MAC addresses and IP
addresses for the interfaces at Host A, both routers, and Host F. Suppose
Host A sends a datagram to Host F. Give the source and destination MAC
addresses in the frame encapsulating this IP datagram as the frame is trans-
mitted 

(i) from A to the left router, 

Source MAC address:

1A-25-F6-CD-06-1B

Destination MAC address:

1A-25-F6-CD-06-3B


(ii) from the left router to the right router,

Source MAC address:

1A-25-F6-CD-06-3C

Destination MAC address:

1A-25-F6-CD-06-4C

(iii) from the right router to F. 

Source MAC address:

1A-25-F6-CD-06-3D

Destination MAC address:

1A-25-F6-CD-06-2D

Also give the source and destination IP
addresses in the IP datagram encapsulated within the frame at each of these
points in time.

Source IP address:

192.168.1.101

Destination IP address:

192.168.3.102

#### 22

Suppose now that the leftmost router in Figure 6.33 is replaced by a switch.
Hosts A, B, C, and D and the right router are all star-connected into this
switch. Give the source and destination MAC addresses in the frame encap-
sulating this IP datagram as the frame is transmitted 

(i) from A to the switch,

Source MAC address:

1A-25-F6-CD-06-1B

Destination MAC address:

1A-25-F6-CD-06-4C

(ii) from the switch to the right router, 

Source MAC address:

1A-25-F6-CD-06-1B

Destination MAC address:

1A-25-F6-CD-06-4C

(iii) from the right router to F. 

Source MAC address:

1A-25-F6-CD-06-3D

Destination MAC address:

1A-25-F6-CD-06-2D


Also give the source and destination IP addresses in the IP datagram encapsulated
within the frame at each of these points in time.

Source IP address:

192.168.1.101

Destination IP address:

192.168.3.102

#### 23

Consider Figure 6.15. Suppose that all links are 1 Gbps. 

What is the maximum total aggregate throughput that can be achieved among the 9 hosts and
2 servers in this network? You can assume that any host or server can send to
any other host or server. Why?

9 hosts + 2 serves = 11 * 1 Gps = 11 Gps

#### 24

Suppose the three departmental switches in Figure 6.15 are replaced by hubs.
All links are 1 Gbps. Now answer the questions posed in problem P23.

5 Gps

#### 25

Suppose that all the switches in Figure 6.15 are replaced by hubs. All links
are 1 Gbps. Now answer the questions posed in problem P23.

1 Gps


#### 26

Let’s consider the operation of a learning switch in the context of a network
in which 6 nodes labeled A through F are star connected into an Ethernet
switch. Suppose that 

(i) B sends a frame to E, 

(ii) E replies with a frame to B,

(iii) A sends a frame to B, 

(iv) B replies with a frame to A. 

The switch table is initially empty. 

Show the state of the switch table before and after each
of these events. For each of these events, identify the link(s) on which the
transmitted frame will be forwarded, and briefly justify your answers.

let's say A is interface 1, B is interface  2 etc...


(i) 

Before:

Empty

After:

Address     interface
B address | 2 

(ii)

Before:

Address     interface
B address | 2 

After:

Address     interface
B address | 2 
E address | 5

(iii)

Before:

Address     interface
B address | 2 
E address | 5

After:

Address     interface
B address | 2 
E address | 5
A address | 1

(iv)

Before:

Address     interface
B address | 2 
E address | 5
A address | 1

After:

Address     interface
B address | 2 
E address | 5
A address | 1

I deliberately not put the time but the time is updated each time as well.

#### 27

In this problem, we explore the use of small packets for Voice-over-IP appli-
cations. One of the drawbacks of a small packet size is that a large fraction of
link bandwidth is consumed by overhead bytes. To this end, suppose that the
packet consists of P bytes and 5 bytes of header.

a. Consider sending a digitally encoded voice source directly. Suppose the
source is encoded at a constant rate of 128 kbps. Assume each packet is
entirely filled before the source sends the packet into the network. The
time required to fill a packet is the packetization delay. In terms of L,
determine the packetization delay in milliseconds.

(P * 8) / 128 kbps = L

P / 16 = L

b. Packetization delays greater than 20 msec can cause a noticeable and
unpleasant echo. Determine the packetization delay for L= 1,500 bytes
(roughly corresponding to a maximum-sized Ethernet packet) and for
L= 50 (corresponding to an ATM packet).

1500 / 16 = 93,75 ms

50/ 16 = 3,125 ms 

c. Calculate the store-and-forward delay at a single switch for a link rate of
R= 622 Mbps for L= 1,500 bytes, and for L= 50 bytes.

(P + 5) * 8 / 622 Mbps

(1500 + 5) * 8 / 622 Mbps = 0,01936 milliseconds

(50 + 5) * 8 / 622 Mbps = 0,71 microseconds

d. Comment on the advantages of using a small packet size.

The smaller the packet the smaller will the delay be

#### 28

Consider the single switch VLAN in Figure 6.25, and assume an external
router is connected to switch port 1. Assign IP addresses to the EE and CS
hosts and router interface. 


Trace the steps taken at both the network layer
and the link layer to transfer an IP datagram from an EE host to a CS host
(Hint: Reread the discussion of Figure 6.19 in the text).

IP addresses:
 EE department host 192.165.89.1
 Router router interface on the EE department side 192.165.89.2
 CS department host 192.165.88.1
 Router router interface on the CS department side 192.165.88.2

 if the EE host don't have the mac address of the router interface it will broadcast an ARP query to get it
 then i will send a frame to the router interface which encapsulate a datagram with the IP address of the CS host (192.165.88.1)
Then the router interface on the CS side will send the frame to the CS host. (the router interface on both side use the same mac address)

#### 29

Consider the MPLS network shown in Figure 6.29, and suppose that rout-
ers R5 and R6 are now MPLS enabled. Suppose that we want to perform
traffic engineering so that packets from R6 destined for A are switched to
A via R6-R4-R3-R1, and packets from R5 destined for A are switched via
R5-R4-R2-R1. Show the MPLS tables in R5 and R6, as well as the modified
table in R4, that would make this possible.

#### 30

Consider again the same scenario as in the previous problem, but suppose
that packets from R6 destined for D are switched via R6-R4-R3, while pack-
ets from R5 destined to D are switched via R4-R2-R1-R3. Show the MPLS
tables in all routers that would make this possible.


