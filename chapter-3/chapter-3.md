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
being asked to consider 8-bit sums.) Show all work. 

01010011
10111001
--------
10111001
--------
00101101
       1
--------
11010001

The overflow get wrapped around, we inverse zeros and ones.

So the resulting checksum is 11010001

Why is it that UDP takes
the 1s complement of the sum; that is, why not just use the sum? 
Because the sum could overflow the 16 bits.

With the 1s complement scheme, how does the receiver detect errors? 

The 1s complement scheme lets the receiver check integrity, by simply adding all values including the checksum, if the result is all 1, no error is detected.

Is it possible that a
1-bit error will go undetected? How about a 2-bit error?

1 bit error will be detected because if one bit is flipped you will have a zero but if 2-bit are flipped one bit can be flipped to 0 and then flipped back to 1 and go undetected.

#### 4

a. Suppose you have the following 2 bytes: 01011100 and 01100101. What
is the 1s complement of the sum of these 2 bytes?

Since their sum doesn't exceed 255 it is just a simple sum 11000001 and if you apply the 1 complement 00111110.

b. Suppose you have the following 2 bytes: 11011010 and 01100101. What
is the 1s complement of the sum of these 2 bytes?

11011010
--------
01100101
--------
101000011
wrap around
01000011
--------
       1
01000100
first complement
10111011

c. For the bytes in part (a), give an example where one bit is flipped in each
of the 2 bytes and yet the 1s complement doesn’t change.

01011101
--------
01100100
--------
00111110
1 complement
11000001

The trick is just to keep the same sum.

#### 5

Suppose that the UDP receiver computes the Internet checksum for the
received UDP segment and finds that it matches the value carried in the
checksum field. Can the receiver be absolutely certain that no bit errors have
occurred? Explain.

Not it can't because if a two bit error happened on the same bit it will be undetected.

#### 6

Consider our motivation for correcting protocol rdt2.1. Show that the
receiver, shown in Figure 3.60, when operating with the sender shown in
Figure 3.11, can lead the sender and receiver to enter into a deadlock state,
where each is waiting for an event that will never occur.

- Sender sends a packet who get acknowledged

- the ACK get corrupted

- the Sender resend the same packet

- The receiver gets confused because it thinks it is a new packet.

- the sender and receiver are out of sync and enter a deadlock state which from they can't recover.

the flaw of the protocol 2.1 is that there is no sequence number.

#### 7

In protocol rdt3.0, the ACK packets flowing from the receiver to the
sender do not have sequence numbers (although they do have an ACK field
that contains the sequence number of the packet they are acknowledging).
Why is it that our ACK packets do not require sequence numbers?

They do not require sequence number because rdt3.0 is a stop and wait protocol (you can't have multiple packets in flight), so the ACK is either the right one or a duplicate and get ignores. 

#### 8

Draw the FSM for the receiver side of protocol rdt3.0.

[answer](./problem-8.png)

#### 9

Give a trace of the operation of protocol rdt3.0 when data packets and
acknowledgment packets are garbled. Your trace should be similar to that
used in Figure 3.16.


[answer](./problem-9.png)


#### 10

Consider a channel that can lose packets but has a maximum delay that is
known. Modify protocol rdt2.1 to include sender timeout and retransmit.
Informally argue why your protocol can communicate correctly over this
channel.


[answer](./problem-10.png)

#### 11

Consider the rdt2.2 receiver in Figure 3.14, and the creation of a new
packet in the self-transition (i.e., the transition from the state back to
itself) in the Wait-for-0-from-below and the Wait-for-1-from-below states:
sndpkt=make_pkt(ACK,1,checksum) and sndpkt=make_
pkt(ACK,0,checksum). Would the protocol work correctly if this action
were removed from the self-transition in the Wait-for-1-from-below state?
Justify your answer. 
This is safe because the receiver can resend the duplicated packet.
What if this event were removed from the self-transition
in the Wait-for-0-from-below state? 
Not it won't the sender needs to resend the packet in case of a corrupted packet or a corrupted ACK.
[Hint: In this latter case, consider what
would happen if the first sender-to-receiver packet were corrupted.]


#### 12

The sender side of rdt3.0 simply ignores (that is, takes no action on)
all received packets that are either in error or have the wrong value in the
acknum field of an acknowledgment packet. Suppose that in such circum-
stances, rdt3.0 were simply to retransmit the current data packet. Would
the protocol still work? (Hint: Consider what would happen if there were
only bit errors; there are no packet losses but premature timeouts can occur.
Consider how many times the nth packet is sent, in the limit as n approaches
infinity.)

The protocol would break because it would trigger a chain where too much packets are in flight (due to the sender constantly resending packets).

#### 13

Consider the rdt 3.0 protocol. Draw a diagram showing that if the
network connection between the sender and receiver can reorder messages
(that is, that two messages propagating in the medium between the sender
and receiver can be reordered), then the alternating-bit protocol will not
work correctly (make sure you clearly identify the sense in which it will
not work correctly). Your diagram should have the sender on the left and
the receiver on the right, with the time axis running down the page, show-
ing data (D) and acknowledgment (A) message exchange. Make sure you
indicate the sequence number associated with any data or acknowledgment
segment


[answer](./problem-13.png)

#### 14

Consider a reliable data transfer protocol that uses only negative acknowledg-
ments. Suppose the sender sends data only infrequently. Would a NAK-only
protocol be preferable to a protocol that uses ACKs? Why? 

A protocol that use ACK is better in that case because you don't want to move to the next packet to send too quickly before being sure that the receiver received the packet and having and sustain a loss that you can't detect.

Now suppose the
sender has a lot of data to send and the end-to-end connection experiences
few losses. In this second case, would a NAK-only protocol be preferable to
a protocol that uses ACKs? Why?

A NAK is preferable because since there is a lot of data to and send and few losses you want to move forward as fast as possible and resend packet when you receive a NAK.

#### 15

Consider the cross-country example shown in Figure 3.17. How big would
the window size have to be for the channel utilization to be greater than
98 percent? Suppose that the size of a packet is 1,500 bytes, including both
header fields and data.

dtrans = L/R = 12000 bits/ 10^9bits/sec = 12 microseconds.

30,012 * 0,98 = 29,401 / 0,012 = a window size of 2451.

#### 16

Suppose an application uses rdt 3.0 as its transport layer protocol. As the
stop-and-wait protocol has very low channel utilization (shown in the cross-
country example), the designers of this application let the receiver keep send-
ing back a number (more than two) of alternating ACK 0 and ACK 1 even if
the corresponding data have not arrived at the receiver. Would this applica-
tion design increase the channel utilization? Why? Are there any potential
problems with this approach? Explain.

Yes that will increase channel utilization but that would cause more than one packet to be in flight and could cause lost packets since the receiver couldn't if the right 0 or 1 packet has arrived.

#### 17

Consider two network entities, A and B, which are connected by a perfect
bi-directional channel (i.e., any message sent will be received correctly; the
channel will not corrupt, lose, or re-order packets). A and B are to deliver
data messages to each other in an alternating manner: First, A must deliver
a message to B, then B must deliver a message to A, then A must deliver a
message to B and so on. If an entity is in a state where it should not attempt
to deliver a message to the other side, and there is an event like rdt_
send(data) call from above that attempts to pass data down for transmis-
sion to the other side, this call from above can simply be ignored with a call
to rdt_unable_to_send(data), which informs the higher layer that it
is currently not able to send data. [Note: This simplifying assumption is made
so you don’t have to worry about buffering data.]
Draw a FSM specification for this protocol (one FSM for A, and one FSM
for B!). Note that you do not have to worry about a reliability mechanism
here; the main point of this question is to create a FSM specification that
reflects the synchronized behavior of the two entities. You should use the
following events and actions that have the same meaning as protocol rdt1.0 in
Figure 3.9: rdt_send(data), packet = make_pkt(data), udt_
send(packet), rdt_rcv(packet), extract (packet,data),
deliver_data(data). Make sure your protocol reflects the strict alter-
nation of sending between A and B. Also, make sure to indicate the initial
states for A and B in your FSM descriptions.


[answer](./problem-17.png)

#### 18

In the generic SR protocol that we studied in Section 3.4.4, the sender
transmits a message as soon as it is available (if it is in the window) without
waiting for an acknowledgment. Suppose now that we want an SR protocol
that sends messages two at a time. That is, the sender will send a pair of mes-
sages and will send the next pair of messages only when it knows that both
messages in the first pair have been received correctly.
Suppose that the channel may lose messages but will not corrupt or reorder
messages. Design an error-control protocol for the unidirectional reliable
transfer of messages. Give an FSM description of the sender and receiver.
Describe the format of the packets sent between sender and receiver, and vice
versa. If you use any procedure calls other than those in Section 3.4
(for example, udt_send(), start_timer(), rdt_rcv(), and so on),
clearly state their actions. Give an example (a timeline trace of sender and
receiver) showing how your protocol recovers from a lost packet.

[sending side](./problem-18-sender.png)
[receiving side](./problem-18-receiver.png)
[timeline](./problem-18-timeline.png)

#### 19

Consider a scenario in which Host A wants to simultaneously send packets
to Hosts B and C. A is connected to B and C via a broadcast channel—a
packet sent by A is carried by the channel to both B and C. Suppose that
the broadcast channel connecting A, B, and C can independently lose and
corrupt packets (and so, for example, a packet sent from A might be cor-
rectly received by B, but not by C). Design a stop-and-wait-like error-control
protocol for reliably transferring packets from A to B and C, such that A will
not get new data from the upper layer until it knows that both B and C have
correctly received the current packet. Give FSM descriptions of A and C.
(Hint: The FSM for B should be essentially the same as for C.) Also, give a
description of the packet format(s) used.

[Host A](./problem-19-A.png)
[Host B and C since they are basically the same](./problem-19-B.png)

packet has the same format that in rdt
ACK has well except for one additional field to track from which host the ACK come from (let's call it ID).

#### 20

Consider a scenario in which Host A and Host B want to send messages to
Host C. Hosts A and C are connected by a channel that can lose and corrupt
(but not reorder) messages. Hosts B and C are connected by another channel
(independent of the channel connecting A and C) with the same properties.
The transport layer at Host C should alternate in delivering messages from
A and B to the layer above (that is, it should first deliver the data from a packet
from A, then the data from a packet from B, and so on). Design a stop-and-
wait-like error-control protocol for reliably transferring packets from A and
B to C, with alternating delivery at C as described above. Give FSM descrip-
tions of A and C. (Hint: The FSM for B should be essentially the same as
for A.) Also, give a description of the packet format(s) used.
