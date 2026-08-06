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
these frames? If so, will C’s adapter pass the IP datagrams in these frames
to the network layer C? How would your answers change if A sends frames
with the MAC broadcast address?
