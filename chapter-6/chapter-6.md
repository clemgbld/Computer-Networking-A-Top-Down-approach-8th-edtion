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

#### sections 6.3

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
