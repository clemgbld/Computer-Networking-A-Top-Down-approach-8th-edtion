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


[Host C](./problem-20-C.png)
[Host A (B is the same)](./problem-20-A.png)

packet and ACK has the same format that in rdt but both have an additional field ID that contains the name of the host.

#### 21

Suppose we have two network entities, A and B. B has a supply of data mes-
sages that will be sent to A according to the following conventions. When A
gets a request from the layer above to get the next data (D) message from B,
A must send a request (R) message to B on the A-to-B channel. Only when B
receives an R message can it send a data (D) message back to A on the B-to-
A channel. A should deliver exactly one copy of each D message to the layer
above. R messages can be lost (but not corrupted) in the A-to-B channel; D
messages, once sent, are always delivered correctly. The delay along both
channels is unknown and variable.
Design (give an FSM description of) a protocol that incorporates the appro-
priate mechanisms to compensate for the loss-prone A-to-B channel and
implements message passing to the layer above at entity A, as discussed
above. Use only those mechanisms that are absolutely necessary.


[Host A](./problem-21-A.png)
[Host B](./problem-21-B.png)

#### 22

Consider the GBN protocol with a sender window size of 4 and a sequence
number range of 1,024. Suppose that at time t, the next in-order packet
that the receiver is expecting has a sequence number of k. Assume that the
medium does not reorder messages. Answer the following questions:
a. What are the possible sets of sequence numbers inside the sender’s
window at time t? Justify your answer.

4 possible windows {k - 3, k - 2, k - 1, k}, {k - 2, k - 1, k, k + 1} , {k - 1, k, k + 1, k + 2}, {k, k + 1, k + 2, k + 3}

b. What are all possible values of the ACK field in all possible messages
currently propagating back to the sender at time t? Justify your answer.

Any values before the max sequence number of the current window is possible even values from a previous window because of the unreliability of the network.

#### 23

Consider the GBN and SR protocols. Suppose the sequence number space
is of size k. What is the largest allowable sender window that will avoid
the occurrence of problems such as that in Figure 3.27 for each of these
protocols?

In the case of SR is should be less than than or half the size of the sequence number space.
IN GBN it for that case it doesn't matter because since it use cumulative acknowledgement the sender will know there is a problem if it receive an ACK that is not the expected K but the window still needs to be k - 1 to avoid confusing an old package with a current one.

#### 24

Answer true or false to the following questions and briefly justify your
answer:
a. With the SR protocol, it is possible for the sender to receive an ACK for a
packet that falls outside of its current window.
true a delayed packet can still arrive later
b. With GBN, it is possible for the sender to receive an ACK for a packet
that falls outside of its current window.
true a delayed packet can still arrive later
c. The alternating-bit protocol is the same as the SR protocol with a sender
and receiver window size of 1.
true
d. The alternating-bit protocol is the same as the GBN protocol with a sender
and receiver window size of 1.
true

#### 25

We have said that an application may choose UDP for a transport protocol
because UDP offers finer application control (than TCP) of what data is sent
in a segment and when.
Why does an application have more control of what data is sent in a segment?

Because UDP put in his data field what the application gives it, no splitting or buffering is happening like it happens with TCP.

Why does an application have more control on when the segment is sent?

Again because since UDP is the simplest a transport layer protocol can be there is no flow control and connection to maintain.

#### 26

Consider transferring an enormous file of L bytes from Host A to Host B.
Assume an MSS of 536 bytes.
a. What is the maximum value of L such that TCP sequence numbers are not
exhausted? Recall that the TCP sequence number field has 4 bytes.

Since the maximum number that we can put in a 4 bytes number field is 4294967296 (4294967295 + 1 which is zero), the maximum L can get's without a wrap around is 4294967296 bytes.

b. For the L you obtain in (a), find how long it takes to transmit the file.
Assume that a total of 66 bytes of transport, network, and data-link header
are added to each segment before the resulting packet is sent out over a
155 Mbps link. Ignore flow control and congestion control so A can pump
out the segments back to back and continuously.

total number of segments = 4294967296 / 536 = 8012998,68656716
d_transmission = (536 + 66) * 8 bits / 155Mpbs = 0,00003107s
d_transmission * total number of segments = around 249 seconds.


#### 27

Host A and B are communicating over a TCP connection, and Host B has
already received from A all bytes up through byte 126. Suppose Host A
then sends two segments to Host B back-to-back. The first and second
segments contain 80 and 40 bytes of data, respectively. In the first segment,
the sequence number is 127, the source port number is 302, and the des-
tination port number is 80. Host B sends an acknowledgment whenever it
receives a segment from Host A.
a. In the second segment sent from Host A to B, what are the sequence num-

ber, source port number, and destination port number?
The sequence number is 207 , the source port number is 302, and the des-
tination port number is 80.

b. If the first segment arrives before the second segment, in the acknowledg-
ment of the first arriving segment, what is the acknowledgment number,
the source port number, and the destination port number?

the acknowledgment will be 207 the source port 80 and the destination port 302

c. If the second segment arrives before the first segment, in the acknowledg-
ment of the first arriving segment, what is the acknowledgment number?

it will send that it expects the first segment so:
sequence number 127, source port 80 and the destination port 302.

d. Suppose the two segments sent by A arrive in order at B. The first
acknowledgment is lost and the second acknowledgment arrives after the
first timeout interval. Draw a timing diagram, showing these segments
and all other segments and acknowledgments sent. (Assume there is no
additional packet loss.) For each segment in your figure, provide the
sequence number and the number of bytes of data; for each acknowledg-
ment that you add, provide the acknowledgment number.

[diagram](./problem-27-D.png)

#### 28

Host A and B are directly connected with a 100 Mbps link. There is one TCP
connection between the two hosts, and Host A is sending to Host B an enor-
mous file over this connection. Host A can send its application data into its
TCP socket at a rate as high as 120 Mbps but Host B can read out of its TCP
receive buffer at a maximum rate of 50 Mbps. Describe the effect of TCP
flow control.

The throughput will be limited to 50Mbps to not overwhelmed the receiver.

#### 29

SYN cookies were discussed in Section 3.5.6.
a. Why is it necessary for the server to use a special initial sequence number
in the SYNACK?
It's necessary to use a special initial sequence number to be sure that the client go to the full workflow of sending a SYN, then get back a SYNACK and then send a ACK, and not bypassing a step by sending directly a ACK because the client must know the sepecial initial number and cannot guess it.
b. Suppose an attacker knows that a target host uses SYN cookies. Can the
attacker create half-open or fully open connections by simply sending an
ACK packet to the target? Why or why not?
No it can't because the ACK must contain the cookie that you can get only by sending a SYN first and get by receiving the SYNACK.
c. Suppose an attacker collects a large amount of initial sequence numbers sent
by the server. Can the attacker cause the server to create many fully open
connections by sending ACKs with those initial sequence numbers? Why?

The cookie have a TTL because it is timestamped so too many connection will not be open because most of the cookie will be expired when the client will try to open many concurrent TCP connection.

#### 30

Consider the network shown in Scenario 2 in Section 3.6.1. Suppose both
sending hosts A and B have some fixed timeout values.
a. Argue that increasing the size of the finite buffer of the router might pos-
sibly decrease the throughput (lout).

Not really a bigger buffer size in that case just means that the segment will spend more time in the buffer since the timeout is fixed. And retransmission will occur.

b. Now suppose both hosts dynamically adjust their timeout values (like
what TCP does) based on the buffering delay at the router. Would increas-
ing the buffer size help to increase the throughput? Why?


Yes because the host could figure out the optimal timeout value and retransmit less (that is what TCP does in fact), and send more segment in less time to the other host.

#### 31

Suppose that the five measured SampleRTT values (see Section 3.5.3)
are 106 ms, 120 ms, 140 ms, 90 ms, and 115 ms. Compute the Estimat-
edRTT after each of these SampleRTT values is obtained, using a value of
α = 0.125 and assuming that the value of EstimatedRTT was 100 ms
just before the first of these five samples were obtained. Compute also the
DevRTT after each sample is obtained, assuming a value of β= 0.25 and
assuming the value of DevRTT was 5 ms just before the first of these five
samples was obtained. Last, compute the TCP TimeoutInterval after
each of these samples is obtained.

I implemented a small [python program](./estimated_Rtt.py) to do the calculations:

Dev RTT 5.25 ms
Estimated RTT: 100.75 ms
Timeout interval 121.75 ms

Dev RTT 8.75 ms
Estimated RTT: 103.15625 ms
Timeout interval 138.15625 ms

Dev RTT 15.7734375 ms
Estimated RTT: 107.76171875 ms
Timeout interval 170.85546875 ms

Dev RTT 16.2705078125 ms
Estimated RTT: 105.54150390625 ms
Timeout interval 170.62353515625 ms

Dev RTT 14.5675048828125 ms
Estimated RTT: 106.72381591796875 ms
Timeout interval 164.99383544921875 ms

Final estimated RTT: 106.72381591796875 ms

#### 32

Consider the TCP procedure for estimating RTT. Suppose that α = 0.1. Let
SampleRTT1 be the most recent sample RTT, let SampleRTT2 be the next
most recent sample RTT, and so on.
a. For a given TCP connection, suppose four acknowledgments have
been returned with corresponding sample RTTs: SampleRTT4,
SampleRTT3, SampleRTT2, and SampleRTT1. Express
EstimatedRTT in terms of the four sample RTTs.


(0.9 * (0.9 *   (0.9 * (0.9 * InitialEstimatedRTT + 0.1 * SampleRTT4) + 0.1 * SampleRTT3 ) + 0.1 * SampleRTT2 ) + 0.1 * SampleRTT1 )


b. Generalize your formula for n sample RTTs.

EstimatedRTT_n = 0.9 × EstimatedRTT_(n-1) + 0.1 × SampleRTT_n

c.
For the formula in part (b) let n approach infinity. Comment on why this
averaging procedure is called an exponential moving average

Since the youngest RTT is given a weight of alpha (in that case 10%) no matter how many previous SampleRTT there was that is was it's called exponnetial moving average the new SampleRTT quickly have more influence than the previous ones in an exponential manner (and logically the oldest RTT loose influence exponentially as well).

#### 33

In Section 3.5.3, we discussed TCP’s estimation of RTT. Why do you think
TCP avoids measuring the SampleRTT for retransmitted segments?

It because ambiguity, the server doesn't know if the ACK segment comes from the retransmitted segment or from the original one since there is no way to know if this last was really lost or not.

#### 34
What is the relationship between the variable SendBase in Section 3.5.4
and the variable LastByteRcvd in Section 3.5.5?

Sendbase - 1 = LastByteRcvd

#### 35

What is the relationship between the variable LastByteRcvd in
Section 3.5.5 and the variable y in Section 3.5.4?

if(y > SendBase) = y - 1 = LastByteRcvd

#### 36

In Section 3.5.4, we saw that TCP waits until it has received three dupli-
cate ACKs before performing a fast retransmit. Why do you think the TCP
designers chose not to perform a fast retransmit after the first duplicate ACK
for a segment is received?

To not do a premature retransmission (which would be expensive and waste work), because it can happen that a segment has been a little delayed and had arrived out of order at the receiver, and it would be expensive to retransmit all the segment after the base.

#### 37

Compare GBN, SR, and TCP (no delayed ACK). Assume that the timeout
values for all three protocols are sufficiently long such that five consecutive
data segments and their corresponding ACKs can be received (if not lost in
the channel) by the receiving host (Host B) and the sending host (Host A)
respectively. Suppose Host A sends five data segments to Host B, and the
second segment (sent from A) is lost. In the end, all five data segments have
been correctly received by Host B.
a. How many segments has Host A sent in total and how many ACKs has
Host B sent in total? 


What are their sequence numbers? Answer this
question for all three protocols.

for GBN: 
Host A sent 9 segments and Host B sent 8 ACK

Host A segment's sequence numbers: 0,1,2,3,4, 1,2,3,4
Host B ACK's sequence numbers: 1, 1, 1, 1, 2, 3, 4, 5

for SR:
Host A sent 6 segments and Host B sent 5 ACK

Host A segment's sequence numbers: 0,1,2,3,4,1
Host B ACK's sequence numbers: 0,2,3,4,1

for TCP

Host A sent 6 segments and Host B sent 5 ACK
Host A segment's sequence numbers: 0, 1, 2, 3, 4, 1
Host B ACK's sequence numbers:  1, 1, 1, 1, 5


b. If the timeout values for all three protocol are much longer than 5 RTT,
then which protocol successfully delivers all five data segments in short-
est time interval?

I would say it is TCP since we don't have to wait the timeout, and just resend the loss packet as soon as we get the 3 duplicate ACK.

#### 38

In our description of TCP in Figure 3.53, the value of the threshold,
ssthresh, is set as ssthresh=cwnd/2 in several places and
ssthresh value is referred to as being set to half the window size when a
loss event occurred. Must the rate at which the sender is sending when the
loss event occurred be approximately equal to cwnd segments per RTT?
Explain your answer. If your answer is no, can you suggest a different
manner in which ssthresh should be set?

I would say not it could be equal to rwnd as well, maybe it should be set to min(cwnd,rwnd)

#### 39

 Consider Figure 3.46(b). If l′in increases beyond R/2, can lout increase
beyond R/3? Explain.
Yes it can increase beyond R/3 if R/2 increase since R/2 is the bottleneck rate
 Now consider Figure 3.46(c). If l′in increases beyond R/2, can lout increase beyond R/4 under the assumption that a packet will be forwarded twice on average from the router to the receiver? Explain.
Same for this case moreover it will be significantly harder.

#### 40

Consider Figure 3.61. Assuming TCP Reno is the protocol experiencing the
behavior shown above, answer the following questions. In all cases, you
should provide a short discussion justifying your answer.
a. Identify the intervals of time when TCP slow start is operating.
From 1 to 6 transmission round and from 23 to 26 (and more).
b. Identify the intervals of time when TCP congestion avoidance is operating.
From 5 to 16 and from 17 to 22.
c. After the 16th transmission round, is segment loss detected by a triple
duplicate ACK or by a timeout?
By duplicate ACK cwnd is divided by 2 at transmission round 17.
d. After the 22nd transmission round, is segment loss detected by a triple
duplicate ACK or by a timeout?
By a timeout , cwnd drops to 1 and the slow start phase is beginning.
e. What is the initial value of ssthresh at the first transmission round?
32 segments.
f. What is the value of ssthresh at the 18th transmission round?
21 segments.
g. What is the value of ssthresh at the 24th transmission round?
14 segments.
h. During what transmission round is the 70th segment sent?
round 7.
i. Assuming a packet loss is detected after the 26th round by the receipt of
a triple duplicate ACK, what will be the values of the congestion window
size and of ssthresh?
It will enter in fast recovery mode and have its ssthresh divided by 2 so it will be 8.
and the congestion window size would have been 7.
j. Suppose TCP Tahoe is used (instead of TCP Reno), and assume that triple
duplicate ACKs are received at the 16th round. What are the ssthresh
and the congestion window size at the 19th round?
It would enter in slow start mode and the congestion window would have been set to 1, then it would have been 8 at the 19th round. the ssthresh would have been the congestion window at the 16th round divided by 2 which is 42 / 2 = 21.
k. 
Again suppose TCP Tahoe is used, and there is a timeout event at
22nd round. How many packets have been sent out from 17th round till
22nd round, inclusive?
52 and we pass in congestion avoidance just after the 21th round.
1 + 2 + 4 + 8 + 16 + 21 = 52.

#### 41

Refer to Figure 3.55, which illustrates the convergence of TCP’s AIMD
algorithm. Suppose that instead of a multiplicative decrease, TCP decreased
the window size by a constant amount. Would the resulting AIAD algorithm
converge to an equal share algorithm? Justify your answer using a diagram
similar to Figure 3.55.

With additive decrease the AIAD algorithm will not converge to an equal share algorithm if the multiple connection does not have the same throughput. 

#### 42

In Section 3.5.4, we discussed the doubling of the timeout interval after a
timeout event. This mechanism is a form of congestion control. Why does
TCP need a window-based congestion-control mechanism (as studied in
Section 3.7) in addition to this doubling-timeout-interval mechanism?

The congestion window helps to prevent the sending host to not send packet at a higher rate that it should.

#### 43

Host A is sending an enormous file to Host B over a TCP connection. Over
this connection there is never any packet loss and the timers never expire.
Denote the transmission rate of the link connecting Host A to the Internet by
R bps. Suppose that the process in Host A is capable of sending data into its
TCP socket at a rate S bps, where S= 10# R. Further suppose that the TCP
receive buffer is large enough to hold the entire file, and the send buffer can
hold only one percent of the file. What would prevent the process in Host
A from continuously passing data to its TCP socket at rate S bps? TCP flow
control? TCP congestion control? Or something else? Elaborate.

Mainly Host can't go higher than R bps that is the physical limitation of the link. So the bottleneck is the link Rate R.

#### 44

Consider sending a large file from a host to another over a TCP connection
that has no loss.
a. Suppose TCP uses AIMD for its congestion control without slow start.
Assuming cwnd increases by 1 MSS every time a batch of ACKs is
received and assuming approximately constant round-trip times, how long
does it take for cwnd increase from 6 MSS to 12 MSS (assuming no loss
events)?

Assuming no loss event 6RTT since assuming cwnd increases by 1 MSS every time a batch of ACKs is received.

b. What is the average throughput (in terms of MSS and RTT) for this con-
nection up through time= 6 RTT?

8.5MSS / RTT

#### 45

Consider Figure 3.54. Suppose that at t3, the sending rate at which conges-
tion loss next occurs drops to 0.75*Wmax (unbeknownst to the TCP senders,
of course). Show the evolution of both TCP Reno and TCP CUBIC for two
more rounds each (Hint: note that the times at which TCP Reno and TCP
CUBIC react to congestion loss may not be the same anymore).

[answer](./problem-45.png)


#### 46

Consider Figure 3.54 again. Suppose that at t3, the sending rate at which conges-
tion loss next occurs increases to 1.5*Wmax. Show the evolution of both TCP
Reno and TCP CUBIC for at two more rounds each (Hint: see the hint in P45).


[answer](./problem-46.png)

#### 47

Recall the macroscopic description of TCP throughput. In the period of time
from when the connection’s rate varies from W/(2 ? RTT) to W/RTT, only one
packet is lost (at the very end of the period).

a show that the loss rate fraction is equal to 

L=83​W2+43​W1​

i=W/2∑W​i=2W​+(2W​+1)+...+W

83W2​+43W

L=83W2​+43W​1​

b Use the result above to show that if a connection has loss rate L, then its
average rate is approximately given by

Average rate≈RTTL​1.22×MSS​

L≈3W28​⇒W≈3L8​​

Average rate≈RTT0.75​3L8​​=RTTL​1.22×MSS​

#### 48

Consider that only a single TCP (Reno) connection uses one 10 Mbps link
which does not buffer any data. Suppose that this link is the only congested
link between the sending and receiving hosts. Assume that the TCP sender
has a huge file to send to the receiver, and the receiver’s receive buffer
is much larger than the congestion window. We also make the following
assumptions: each TCP segment size is 1,500 bytes; the two-way propagation
delay of this connection is 150 msec; and this TCP connection is always in
congestion avoidance phase, that is, ignore slow start.
a. What is the maximum window size (in segments) that this TCP connec-
tion can achieve?

We should calculate the bandwidth delay product

BDP = 10,000,000 × 0.150 = 1,500,000 bits

1,500,000 / (1500 × 8) = 1,500,000 / 12,000 = 125 segments.


b. What is the average window size (in segments) and average throughput
(in bps) of this TCP connection?

0,75 * 125 segments = 93,75 segments

93,75 * 12000 / 0,150 = 7500000 bits

c. How long would it take for this TCP connection to reach its maximum
window again after recovering from a packet loss?

it would take = ((maxcwnd - cwnd) / MSS) * RTT 

((125 / 2) * 0,150 =  9,375 s

#### 49

Consider the scenario described in the previous problem. Suppose that the
10 Mbps link can buffer a finite number of segments. Argue that in order for
the link to always be busy sending data, we would like to choose a buffer size
that is at least the product of the link speed C and the two-way propagation
delay between the sender and the receiver.

In order for the lint to always be busy sending data we would like to choose a buffer size that is at least the product of the link spped C and the two-way propagation delay between the sender and the receiver because of flow control the max window is min(bdp, rwnd) so rwnd has to be a least 125 segments.

#### 50

Repeat Problem 48, but replacing the 10 Mbps link with a 10 Gbps link. Note
that in your answer to part c, you will realize that it takes a very long time for the congestion window size to reach its maximum window size after recover-
ing from a packet loss. Sketch a solution to solve this problem.

a - 125 000 segments

b- 0,75 * 125 000 segments = 93750 segments

c  - ((125 000 / 2) * 0,150 =  9375 s

Using TCP Cubic instead of TCP Reno would help us reach the maximum much more quickly.

#### 51

Let T (measured by RTT) denote the time interval that a TCP connection
takes to increase its congestion window size from W/2 to W, where W is the
maximum congestion window size. Argue that T is a function of TCP’s
average throughput.

Average Throughput = 0,75 * W * MSS / RTT
W = Average Throughput * RTT /0,75 * MSS
T = (W - W/2) * RTT = Average Throughput * (RTT * RTT) / 1.5 * MSS
Is a function of TCP's average throughput because TCP stay most of the time in the congestion avoidance state.

#### 52

Consider a simplified TCP’s AIMD algorithm where the congestion window
size is measured in number of segments, not in bytes. In additive increase, the
congestion window size increases by one segment in each RTT. In multipli-
cative decrease, the congestion window size decreases by half (if the result
is not an integer, round down to the nearest integer). Suppose that two TCP
connections, C1 and C2, share a single congested link of speed 30 segments
per second. Assume that both C1 and C2 are in the congestion avoidance
phase. Connection C1’s RTT is 50 msec and connection C2’s RTT is 100 msec.
Assume that when the data rate in the link exceeds the link’s speed, all
TCP connections experience data segment loss.
a. If both C1 and C2 at time t0 have a congestion window of 10 segments,
what are their congestion window sizes after 1000 msec?

cwnd1     |cwnd 2     |rate 1      |rate 2     |time     |total
10    |10   |200.0    |100.0    |0    |20
11    |11   |220.0    |110.0    |0.05    |22
12    |11   |240.0    |110.0    |0.1    |23
13    |12   |260.0    |120.0    |0.15000000000000002    |25
14    |12   |280.0    |120.0    |0.2    |26
15    |13   |300.0    |130.0    |0.25    |28
16    |13   |320.0    |130.0    |0.3    |29
8    |7   |160.0    |70.0    |0.35    |15
9    |7   |180.0    |70.0    |0.39999999999999997    |16
10    |8   |200.0    |80.0    |0.44999999999999996    |18
11    |8   |220.0    |80.0    |0.49999999999999994    |19
12    |9   |240.0    |90.0    |0.5499999999999999    |21
13    |9   |260.0    |90.0    |0.6    |22
14    |10   |280.0    |100.0    |0.65    |24
15    |10   |300.0    |100.0    |0.7000000000000001    |25
16    |11   |320.0    |110.0    |0.7500000000000001    |27
17    |11   |340.0    |110.0    |0.8000000000000002    |28
18    |12   |360.0    |120.0    |0.8500000000000002    |30
9    |6   |180.0    |60.0    |0.9000000000000002    |15
10    |7   |200.0    |70.0    |0.9500000000000003    |17

b. In the long run, will these two connections get the same share of the band-
width of the congested link? Explain.

No they won't get the same share in the long run fairness in TCP works well only for the host with the same RTT, the host with a lower RTT get an advantage and get more share of the congested link.

#### 53

Consider the network described in the previous problem. Now suppose that
the two TCP connections, C1 and C2, have the same RTT of 100 msec.
Suppose that at time t0, C1’s congestion window size is 15 segments but C2’s
congestion window size is 10 segments.

a. What are their congestion window sizes after 2200 msec?

cwnd1     |cwnd 2     |rate 1      |rate 2     |time     |total
10    |10   |100.0    |100.0    |0    |20
11    |11   |110.0    |110.0    |0.1    |22
12    |12   |120.0    |120.0    |0.2    |24
13    |13   |130.0    |130.0    |0.30000000000000004    |26
14    |14   |140.0    |140.0    |0.4    |28
15    |15   |150.0    |150.0    |0.5    |30
8    |8   |80.0    |80.0    |0.6    |16
9    |9   |90.0    |90.0    |0.7    |18
10    |10   |100.0    |100.0    |0.7999999999999999    |20
11    |11   |110.0    |110.0    |0.8999999999999999    |22
12    |12   |120.0    |120.0    |0.9999999999999999    |24
13    |13   |130.0    |130.0    |1.0999999999999999    |26
14    |14   |140.0    |140.0    |1.2    |28
15    |15   |150.0    |150.0    |1.3    |30
8    |8   |80.0    |80.0    |1.4000000000000001    |16
9    |9   |90.0    |90.0    |1.5000000000000002    |18
10    |10   |100.0    |100.0    |1.6000000000000003    |20
11    |11   |110.0    |110.0    |1.7000000000000004    |22
12    |12   |120.0    |120.0    |1.8000000000000005    |24
13    |13   |130.0    |130.0    |1.9000000000000006    |26
14    |14   |140.0    |140.0    |2.0000000000000004    |28
15    |15   |150.0    |150.0    |2.1000000000000005    |30

b. In the long run, will these two connections get about the same share of the
bandwidth of the congested link?

Yes mostly since they have the same RTT.

c. We say that two connections are synchronized, if both connections reach
their maximum window sizes at the same time and reach their minimum
window sizes at the same time. In the long run, will these two connec-
tions get synchronized eventually? 
Yes they will, we can see it in the simulation they because synchronized at 2.2 seconds.
If so, what are their maximum window
sizes?

Their maximum window sizes is bandwidth in segments / 2 which is 15 in this exercise.

d. Will this synchronization help to improve the utilization of the shared
link? Why? Sketch some idea to break this synchronization.

No the synchronization does not help to improve the utilization of the shared link because the utilization will be the average throughput and not the max throughput.

An idea to break the synchronization would be to not divide by 2 the both cwnd but by a random number between 1 and 2.

#### 54

Consider a modification to TCP’s congestion control algorithm. Instead of additive increase, we can use multiplicative increase. A TCP sender increases
its window size by a small positive constant a (0 < a < 1) whenever it
receives a valid ACK. Find the functional relationship between loss rate L
and maximum congestion window W. Argue that for this modified TCP,
regardless of TCP’s average throughput, a TCP connection always spends the
same amount of time to increase its congestion window size from W/2 to W.

Since the congestion window increase by W * a anytime it receives an ACK it means that the increase is proportional to the current W which means that the TCP connection always spends the same amount of time to increase its congestion window size from W/2 to W

for example if W = 5 and a = 0.1

W * a = 0,5 it means that it would take 5 ack to go from W/2 -> W

because 2,5 / 0,5 = 5

and if you take W = 2 and a = 0.1

W *a = 0,2

1 / 0,2 = 5

So W/2 -> W = W/2 / W * a

#### 55

In our discussion of TCP futures in Section 3.7, we noted that to achieve a
throughput of 10 Gbps, TCP could only tolerate a segment loss probability of
2 * 10 ^ -10 (or equivalently, one loss event for every 5,000,000,000 segments).
Show the derivation for the values of 2 * 10 ^ -10 (1 out of 5,000,000) for the
RTT and MSS values given in Section 3.7. If TCP needed to support a
100 Gbps connection, what would the tolerable loss be?

L=(1.464×10−5)2≈2×10−10

for 100 Gbps

L=(101014640​)2≈2×10−12

#### 56

In our discussion of TCP congestion control in Section 3.7, we implicitly
assumed that the TCP sender always had data to send. Consider now the case
that the TCP sender sends a large amount of data and then goes idle (since it
has no more data to send) at t1. TCP remains idle for a relatively long period
of time and then wants to send more data at t2. What are the advantages and
disadvantages of having TCP use the cwnd and ssthresh values from t1
when starting to send data at t2? 

The advantages if it is not in congestion avoidance it will start by sending directly a lot of packets

The disadvantages is that a packet loss can arrive early

What alternative would you recommend?
Why?

An alternative would be to reset the the cwnd and ssthresh to their initial values after a certain time of idleness, to put the congestion mechanism in the same state than at the beginning of a packets exchange because sending packets after being idle for a long time is kind of the same as restarting the process and you would avoid to have a loss too quickly.

#### 57

In this problem, we investigate whether either UDP or TCP provides a degree
of end-point authentication.
a. Consider a server that receives a request within a UDP packet and
responds to that request within a UDP packet (for example, as done by a
DNS server). If a client with IP address X spoofs its address with address
Y, where will the server send its response?
It will send the answer to Y if the Y address is in the datagram
b. Suppose a server receives a SYN with IP source address Y, and after
responding with a SYNACK, receives an ACK with IP source address Y
with the correct acknowledgment number. Assuming the server chooses a
random initial sequence number and there is no “man-in-the-middle,” can
the server be certain that the client is indeed at Y (and not at some other
address X that is spoofing Y)?

Yes it can be sure that it is Y unless some other client X guess the intial random number at the right time which is highly unlikely.

#### 58

In this problem, we consider the delay introduced by the TCP slow-start
phase. Consider a client and a Web server directly connected by one link of
rate R. Suppose the client wants to retrieve an object whose size is exactly
equal to 15 S, where S is the maximum segment size (MSS). Denote the
round-trip time between client and server as RTT (assumed to be constant).
Ignoring protocol headers, determine the time to retrieve the object (includ-
ing TCP connection establishment) when
a. 4 S/R > S/R + RTT > 2S/R
4 RTT + 15 S / R
b. S/R + RTT > 4 S/R
5 RTT + 15 S/ R
c. S/R > RTT.
2 RTT + 15 S / R

### Programming Assignment

#### Implementing a Reliable Transport Protocol

In this laboratory programming assignment, you will be writing the sending and
receiving transport-level code for implementing a simple reliable data transfer pro-
tocol. There are two versions of this lab, the alternating-bit-protocol version and the
GBN version. This lab should be fun—your implementation will differ very little
from what would be required in a real-world situation.
Since you probably don’t have standalone machines (with an OS that you can
modify), your code will have to execute in a simulated hardware/software environ-
ment. However, the programming interface provided to your routines—the code that
would call your entities from above and from below—is very close to what is done
in an actual UNIX environment. (Indeed, the software interfaces described in this
programming assignment are much more realistic than the infinite loop senders and
receivers that many texts describe.) Stopping and starting timers are also simulated,
and timer interrupts will cause your timer handling routine to be activated.
The full lab assignment, as well as code you will need to compile with your own
code, are available at this book’s Web site: www.pearsonhighered.com/cs-resources.

./alternative-bit-protocol.py

### Wireshark labs (TCP)

#### 1

What is the IP address and TCP port number used by the client computer (source)
that is transferring the alice.txt file to gaia.cs.umass.edu? To answer this
question, it’s probably easiest to select an HTTP message and explore the details
of the TCP packet used to carry this HTTP message, using the “details of the
selected packet header window” (refer to Figure 2 in the “Getting Started with
Wireshark” Lab if you’re uncertain about the Wireshark windows).

192.168.178.41:52649

#### 2

 What is the IP address of gaia.cs.umass.edu? On what port number is it sending
and receiving TCP segments for this connection?

128.119.245.12:80

#### 3

What is the sequence number of the TCP SYN segment that is used to initiate the
TCP connection between the client computer and gaia.cs.umass.edu? (Note: this
is the “raw” sequence number carried in the TCP segment itself; it is NOT the
packet # in the “No.” column in the Wireshark window. Remember there is no
such thing as a “packet number” in TCP or UDP; as you know, there are sequence
numbers in TCP and that’s what we’re after here. Also note that this is not the
relative sequence number with respect to the starting sequence number of this
TCP session.). What is it in this TCP segment that identifies the segment as a
SYN segment? Will the TCP receiver in this session be able to use Selective
Acknowledgments (allowing TCP to function a bit more like a “selective repeat”
receiver, see section 3.4.5 in the text)?

The sequence number is zero, the syn flag is set to 1, Yes SACK is permitted.

#### 4

What is the sequence number of the SYNACK segment sent by gaia.cs.umass.edu
to the client computer in reply to the SYN? What is it in the segment that
identifies the segment as a SYNACK segment? What is the value of the
Acknowledgement field in the SYNACK segment? How did gaia.cs.umass.edu
determine that value? 

The sequence number is zero, the syn flag and the ack flag or both set to 1, the acknowledgment number is 1 which is the next expected byte from the sender.

#### 5

What is the sequence number of the TCP segment containing the header of the
HTTP POST command? Note that in order to find the POST message header,
you’ll need to dig into the packet content field at the bottom of the Wireshark
window, looking for a segment with the ASCII text “POST” within its DATA
field4,5. How many bytes of data are contained in the payload (data) field of this
TCP segment? Did all of the data in the transferred file alice.txt fit into this single
segment?

The sequence number is 1, This segment contains 612 bytes and no there is other segments.

#### 6

Consider the TCP segment containing the HTTP “POST” as the first segment in
the data transfer part of the TCP connection.
• At what time was the first segment (the one containing the HTTP POST) in
the data-transfer part of the TCP connection sent?
8h28min11sec 095349
• At what time was the ACK for this first data-containing segment received?
8h28min11sec186849 
• What is the RTT for this first data-containing segment?
186849 - 95349 = 91,5 ms
• What is the RTT value the second data-carrying TCP segment and its ACK?
the RTT is 90,848ms
• What is the EstimatedRTT value (see Section 3.5.3, in the text) after the
ACK for the second data-carrying segment is received? Assume that in
making this calculation after the received of the ACK for the second segment,
that the initial value of EstimatedRTT is equal to the measured RTT for the
first segment, and then is computed using the EstimatedRTT equation on
page 242, and a value of a = 0.125.
Note: Wireshark has a nice feature that allows you to plot the RTT for
each of the TCP segments sent. Select a TCP segment in the “listing of
captured packets” window that is being sent from the client to the
gaia.cs.umass.edu server. Then select: Statistics->TCP Stream Graph-
>Round Trip Time Graph.

0.875 + 91.5 + 0.125 * 90.848 = 91.44185ms

#### 7

What is the length (header plus payload) of each of the first four data-carrying
TCP segments?

the first one has a payload of 612 bytes and a header of 20 bytes = 632 bytes.
And the three others a pyalod of 1452 bytes and a header of 20 bytes = 1472 bytes.

#### 8

What is the minimum amount of available buffer space advertised to the client by
gaia.cs.umass.edu among these first four data-carrying TCP segments7? Does the
lack of receiver buffer space ever throttle the sender for these first four datacarrying segments?

the first ACK output a window size of 63744 bytes wich is good enough to handle 43 segment from the sender.

#### 9

Are there any retransmitted segments in the trace file? What did you check for (in
the trace) in order to answer this question?

Yes there is some retransmission segments, we can analyse that with tcp.analysis.retransmission filter in wireshark.

#### 10

How much data does the receiver typically acknowledge in an ACK among the
first ten data-carrying segments sent from the client to gaia.cs.umass.edu? Can
you identify cases where the receiver is ACKing every other received segment
(see Table 3.2 in the text) among these first ten data-carrying segments?

In the first 10 segments there 3 acknowlegdement segment that each acknowledge 613, 5808, 7260 bytes the average of taht is 4560.3 bytes by acknowledgment
For the second question, it is the case since there is 3 acknowledgment segmnet for 10 segments sent.

#### 11

What is the throughput (bytes transferred per unit time) for the TCP connection?
Explain how you calculated this value.

the formula is the total of data / time i linked the throuput plot by wireshark here: [file](./throuput.PNG) 


Answer the following question for the TCP segments in the packet trace tcp-wiresharktrace1-1

#### 12

Use the Time-Sequence-Graph(Stevens) plotting tool to view the sequence
number versus time plot of segments being sent from the client to the
gaia.cs.umass.edu server. Consider the “fleets” of packets sent around t = 0.025, t
= 0.053, t = 0.082 and t = 0.1. Comment on whether this looks as if TCP is in its
slow start phase, congestion avoidance phase or some other phase. Figure 6 shows
a slightly different view of this data.

It looks like slow start mode.

#### 13

These “fleets” of segments appear to have some periodicity. What can you say
about the period?


These period is the RTT.

#### 14

Answer each of two questions above for the trace that you have gathered when
you transferred a file from your computer to gaia.cs.umass.edu

This is about the same answers than for the trace of the two last question.
