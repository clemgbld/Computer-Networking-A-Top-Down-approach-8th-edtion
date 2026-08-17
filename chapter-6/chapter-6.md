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


