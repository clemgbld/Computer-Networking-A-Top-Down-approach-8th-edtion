# CHAPTER 3: Transport layer

## Review questions

### Sections 3.1 - 3.3

#### 1

Suppose the network layer provides the following service. 
The network layer in the source host accepts a segment of maximum size 1,200 bytes and
a destination host address from the transport layer. The network layer then
guarantees to deliver the segment to the transport layer at the destination
host. Suppose many network application processes can be running at the
destination host.
a. Design the simplest possible transport-layer protocol that will get application data to the desired process at the destination host. Assume the operating system in the destination host has assigned a 4-byte port number to
each running application process.

The simplest transport-layer would be something like UDP but without checksum and the source address, it would be to forward a segment witdth data that does not exist 1,200 bytes - the header, the header would be composed of 1 field containing port. we need the port in order to allow the destination host to use demultiplexing which will allow it to provide the segment to the rigth process. 

b. Modify this protocol so that it provides a “return address” to the destination process.
We just have to add a field in the header which is the source the port.

c. In your protocols, does the transport layer “have to do anything” in the
core of the computer network?

No the transport layer along with the application layer are part of the edges of the computer network.

#### 2

Consider a planet where everyone belongs to a family of six, every family
lives in its own house, each house has a unique address, and each person
in a given house has a unique name. Suppose this planet has a mail service
that delivers letters from source house to destination house. The mail service
requires that (1) the letter be in an envelope, and that (2) the address of the
destination house (and nothing more) be clearly written on the envelope. Suppose each family has a delegate family member who collects and distributes
letters for the other family members. The letters do not necessarily provide
any indication of the recipients of the letters.
a. Using the solution to Problem R1 above as inspiration, describe a protocol
that the delegates can use to deliver letters from a sending family member
to a receiving family member.
Taking inspiration of the first problem, would be to have a person that act as the transport layer on the sending side who gather the letter and write the name of the sender at the top of the letter (the source port) and who ask the sender to tell him the receiver name so he can write it at the top of the letter as well. the gatherer does that with every letter and put the letter in an envelope with the address of the address of the house on it, then give it to the mail service, the mail service gives the letter to the receiver house, who has also a guy that act as a transport layer, that opens every letter and can distribute them to every receiver (the destination proccesses).
b. In your protocol, does the mail service ever have to open the envelope and
examine the letter in order to provide its service?

Not it does not, only the receiver transport layer side needs to. 

#### 3

a. Can we set up a gateway to the internet that translates IP addresses, so that we don't have to change all our internal addresses to an official network ?
Yes we can set up a NAT Network address translation gateway exactly for that purpose.

b. One of the header fields in an IP datagram is the time to live (TTL) Which of the following statements best explains the need for this field ?

This header define the life-span of a packet before it is discarded by a router, to prevent it to let it circulate indefineltly on the network.

c. What is the maximum size of data that the application layer can pass on to the TCP layer below ?
This is defined by the MSS maximum size segment

#### 4

Describe why an application developer might choose to run an application
over UDP rather than TCP

When it does not care about 100% reliability (for example a video chat like Skype, you can afford some packet loss), When the application developer does not want to be constrained by network congestion control.

#### 5

Why is it that voice and video traffic is often sent over TCP rather than UDP
in today’s Internet? (Hint: The answer we are looking for has nothing to do
with TCP’s congestion-control mechanism.)

For simplity i would say to take advantage of HTTP DASH and be able to consume the content in the quality that fits your connection better, and for security as well, with https the content will not be blocked by firewall and stuff like that unlike UDP who can be blocked.

#### 6

What are the responsabilities of the transport layer ?

The big responsability of the transport layer is to get from and give to the network core packets and performing demultiplexing and multiplexing, by ensuring that the segment will be deliver to the correct source or destination process. Some more complex transport layer like TCP have additional responsabilites like ensuring reliablity, congestion control etc...

#### 7

Suppose a process in Host C has a UDP socket with port number 6789.
Suppose both Host A and Host B each send a UDP segment to Host C with
destination port number 6789. Will both of these segments be directed to the
same socket at Host C? 

Yes both segments will be directed at the same socket at Host C

If so, how will the process at Host C know that these
two segments originated from two different hosts?

the process at Host C will know thanks to the source port in the header of the UDP segment and the source address in the header

#### 8

Suppose that a Web server runs in Host C on port 80. Suppose this Web
server uses persistent connections, and is currently receiving requests from
two different Hosts, A and B. Are all of the requests being sent through the
same socket at Host C? 

First the welcoming socket will perform the handshake phase with host A and B.

Creating a client socket for handling the requests of each host.

If they are being passed through different sockets, do
both of the sockets have port 80?

Discuss and explain.

Multiple TCP connections can share port 80 because each connection is uniquely identified by the 4-tuple (source IP, source port, destination IP, destination port), and for different clients the source IP address and source port differ, allowing the server to distinguish them


### Sections 3.4

#### 9

In our rdt protocols, why did we need to introduce sequence numbers?

We need the sequence numbers in our protocols, to detect packets that our out of order, and depending on the implementation either ignore the packet and ask again for the expected one or keep it anyway in a buffer and ask again for the client for the expected packet. It also is mainly to detect duplicated packets and deal with them.

#### 10

In our rdt protocols, why did we need to introduce timers?

Timers are needed so that when no ACK is received within a certain time, the sender can resend a packet despite not knowing whether the packet reached the receiver host or not, or the ACK got lost.

#### 11

Suppose that the roundtrip delay between sender and receiver is constant and known to the sender. Would a timer still be necessary in protocol rdt 3.0, assuming that packets can be lost? Explain.

Yes a timer is still necessary, even though the RTT is known, because the sender cannot make the distinction between a packet that got lost or an ACK that got lost.

#### 12

Visit the Go-Back-N interactive animation at the companion Web site.

a. Have the source send five packets, and then pause the animation before
any of the five packets reach the destination. Then kill the first packet and
resume the animation. Describe what happens.

The first packet get killed then, the 4 others reach the receiver host, and the host ignore the 4 other packets since it expected to receive the first one first, then a timeout is trigger on the sender side and this one resend the 5 packets.

b. Repeat the experiment, but now let the first packet reach the destination
and kill the first acknowledgment. Describe again what happens.

The first acknowledgment get killed, but the sender infers that the first packet reach the receiving host because GO-Back-N use Cumulative acknowledgment, so it moves the window anyway when it gets the second packet ACK.

c. Finally, try sending six packets. What happens?

We cannot send six packets at the same time because the max window is 5 so there must be at most 5 packets in flight.

#### 13

Repeat R12, but now with the Selective Repeat interactive animation. How
are Selective Repeat and Go-Back-N different?

a. Have the source send five packets, and then pause the animation before
any of the five packets reach the destination. Then kill the first packet and
resume the animation. Describe what happens.

In Selective Repeat the 4 other packages are acknowledged by the receiver and the sender receives the 4 ACK thus when the timer of the first packet that got killed is triggered it retransmit only the first packet that got lost.

b. Repeat the experiment, but now let the first packet reach the destination
and kill the first acknowledgment. Describe again what happens.

Unlike the GO-Back-N strategy cumulative ACK does not apply, so the sender retransmit the first packet.

c. Finally, try sending six packets. What happens?

Same than with the GO-Back-N strategy, We cannot send six packets at the same time because the max window is 5 so there must be at most 5 packets in flight.

### Sections 3.5

#### 14

True or false?
a. Host A is sending Host B a large file over a TCP connection. Assume Host
B has no data to send Host A. Host B will not send acknowledgments to
Host A because Host B cannot piggyback the acknowledgments on data.

False. Over TCP the receiver always have to acknowledged a packet.

b. The size of the TCP rwnd never changes throughout the duration of the
connection.

False.

c. Suppose Host A is sending Host B a large file over a TCP connection. The
number of unacknowledged bytes that A sends cannot exceed the size of
the receive buffer.

True. The sender side has a mechanism to not overwhelmed the receiver.

d. Suppose Host A is sending a large file to Host B over a TCP connection.
If the sequence number for a segment of this connection is m, then the
sequence number for the subsequent segment will necessarily be m + 1.

False, the next sequence is m + number of bytes.

e. The TCP segment has a field in its header for rwnd.

True.

f. Suppose that the last SampleRTT in a TCP connection is equal to 1 sec.
The current value of TimeoutInterval for the connection will neces-
sarily be >= 1 sec.

True.

g. Suppose Host A sends one segment with sequence number 38 and 4
bytes of data over a TCP connection to Host B. In this same segment, the
acknowledgment number is necessarily 42.

False.

#### 15

Suppose Host A sends two TCP segments back to back to Host B over a
TCP connection. The first segment has sequence number 90; the second has
sequence number 110.
a. How much data is in the first segment?
20 bytes is in the first segment.
b. Suppose that the first segment is lost but the second segment arrives at
B. In the acknowledgment that Host B sends to Host A, what will be the
acknowledgment number?

the acknowledgment number will be 90.

#### 16

Consider the Telnet example discussed in Section 3.5. A few seconds after
the user types the letter ‘C,’ the user types the letter ‘R.’ After typing the let-
ter ‘R,’ how many segments are sent, and what is put in the sequence number
and acknowledgment fields of the segments?

3 segments are sent in total.

Just to recall the segments sent by when the letter 'C' was typed was:

1. Seq = 42, ACK=79, data='C' (client)
2. Seq = 79, ACK=43, data='C' (server)
3. Seq= 43, ACK=80

And the segments for 'R' will be:

1. Seq = 43, ACK=80, data='R' (client)
2. Seq = 80, ACK=44, data='R' (server)
3. Seq= 44, ACK=81

#### 17

Suppose two TCP connections are present over some bottleneck link of rate R

bps. Both connections have a huge file to send (in the same direction over the

bottleneck link). The transmissions of the files start at the same time. What

transmission rate would TCP like to give to each of the connections?

If we look at the concept of Fairness in TCP the logical rate TCP would like to give each connection is R/2 bps.

#### 18

True or false? Consider congestion control in TCP. When the timer expires at
the sender, the value of ssthresh is set to one half of its previous value.
False the ssthresh is set to cwnd (congestion window) / 2.

#### 19

In the discussion of TCP splitting in the sidebar in Section 3.7, it was
claimed that the response time with TCP splitting is approximately
4 * RTTFE + RTTBE + processing time. Justify this claim.

It's because the frontend maintain a persistent TCP connection with the backend, and the frontend is close to the client.

- 1 RTTFE for http handshake with the frontend server
- 1 RTTFE for http request client
- 1 RTTBE to frontend server -> backend server
- 2 RTTFE response to the client (multiple RTT because of the slow start)
- processing time (the backend needs to build the response)

### Problems

#### 1

Suppose Client A initiates a Telnet session with Server S. At about the same
time, Client B also initiates a Telnet session with Server S. Provide possible
source and destination port numbers for
a. The segments sent from A to S.

source: 5890, destination: 9087

b. The segments sent from B to S.

source: 6790, destination: 9087

c. The segments sent from S to A.

source: 9087, destination: 5890

d. The segments sent from S to B.


source: 9087, destination: 6790

e. If A and B are different hosts, is it possible that the source port number in
the segments from A to S is the same as that from B to S?

Yes it is possible.
Their IP would differentiate them in that case.

f. How about if they are the same host?

No it is not possible, because of the 4 tuple uniqueness requirement.

#### 2

Consider Figure 3.5. What are the source and destination port values in the
segments flowing from the server back to the clients’ processes? What are
the IP addresses in the network-layer datagrams carrying the transport-layer
segments?

There is 3 segments and datagrams:

- segment (source port: 80, destination port: 7532) , datagram ( source IP: B, destination IP: C)
- segment (source port: 80, destination port: 26145) , datagram ( source IP: B, destination IP: C)
- segment (source port: 80, destination port: 26145) , datagram ( source IP: B, destination IP: A)

#### 3

UDP and TCP use 1s complement for their checksums. Suppose you have
the following three 8-bit bytes: 01010011, 01100110, 01110100. What is the
1s complement of the sum of these 8-bit bytes? (Note that although UDP and
TCP use 16-bit words in computing the checksum, for this problem you are
being asked to consider 8-bit sums.) Show all work. Why is it that UDP takes
the 1s complement of the sum; that is, why not just use the sum? With the 1s
complement scheme, how does the receiver detect errors? Is it possible that a
1-bit error will go undetected? How about a 2-bit error?

