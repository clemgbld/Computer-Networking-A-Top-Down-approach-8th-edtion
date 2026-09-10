# CHAPTER 7: Wireless and mobile networks

## Review questions

### section 7.1 

#### 1

What does it mean for a wireless network to be operating in “infrastructure
mode”?

It means a host is associated with a base station.

If the network is not in infrastructure mode, what mode of operation
is it in, and what is the difference between that mode of operation and infra-
structure mode?

It is in ad-hoc mode which means there is not AP every hosts in the network communicate with each other.

#### 2

What are the four types of wireless networks identified in our taxonomy in
Section 7.1? 

- Single-hop, infrastructure-based

- Single-hop, infrastructure-less

- Multi-hop, infrastructure-based

- Multi-hop, infrastructure-less

Which of these types of wireless networks have you used?

The two first ones.

### section 7.2

#### 3

What are the differences between the following types of wireless channel
impairments: path loss, multipath propagation, interference from other sources?

- path loss: it is when a signal strength decrease over the distance and obstacles.
- interference from other sources: it is when multiple radio sources are transmitting in the same frequency band thus conflicting with each other.
- multipath propagation: it is when portions of the electromagnetic wave reflect off objects and the ground which result in the blurring of the received signal at the receiver.

#### 4

As a mobile node gets farther and farther away from a base station, what are
two actions that a base station could take to ensure that the loss probability of
a transmitted frame does not increase?

Increasing its transmission power.

### section 7.3

#### 5

Describe the role of the beacon frames in 802.11.

The role of the beacon frames is to letting know to hosts that the WIFI is available and also send SSID and MAC address in the beacon frame to let them know which WIFI is sending the beacon frames.

#### 6

True or false: Before an 802.11 station transmits a data frame, it must first
send an RTS frame and receive a corresponding CTS frame.

False it is optional.

#### 7

Why are acknowledgments used in 802.11 but not in wired Ethernet?

Because 802.11 have a higher rate of bit errors than the wired Ethernet, 802.11 also have the inability to detect collisions.

#### 8

True or false: Ethernet and 802.11 use the same frame structure.

False some of their structure overlap but there is more things in an 802.11 frame structure such as a Seq control field since 802.11 use ACKs.

#### 9

Describe how the RTS threshold works.

There is a setting named the packet size and if the packet is higher than the threshold (the packet size) then the handshake must happen.

#### 10

Suppose the IEEE 802.11 RTS and CTS frames were as long as the standard
DATA and ACK frames. Would there be any advantage to using the CTS and
RTS frames? Why or why not?

I would say no it would defeat the purpose of RTS and CTS because those ones would be prone to collisions like the frames.

#### 11

Section 7.3.4 discusses 802.11 mobility, in which a wireless station moves
from one BSS to another within the same subnet. When the APs are intercon-
nected with a switch, an AP may need to send a frame with a spoofed MAC
address to get the switch to forward the frame properly. Why?

Because since the ARP table are self learning, AP 2 will need to send a broadcast EThernet frame with H1's source address to the switch just after the association to update the forwarding table of the switch allowing H1 to be reach by AP 2.

#### 12

What are the differences between a master device in a Bluetooth network and
a base station in an 802.11 network?

The difference is that the base station will always be the same in the 802.11 network whereas the master device can change for example if multiple devices are connected via Bluetooth and the master device disconnect, another device will be elected master device of the piconet.

and 802.11 is in infrastructure mode while Bluetooth is ad-hoc.

#### 13

What is the role of the base station in 4G/5G cellular architecture? 

The base station is like the AP in 802.11

With which other 4G/5G network elements (mobile device, MME, HSS, Serving
Gateway Router, PDN Gateway Router) does it directly communicate with in
the control plane? 

the MME

In the data plane?

the Serving Gateway


#### 14

What is an International Mobile Subscriber Identity (IMSI)?

The IMSI is kind of the equivalent of a MAC address but for mobile device is enable the Service provider to know if a particular mobile device can access it's network or not.

#### 15

What is the role of the Home Subscriber Service (HSS) in 4G/5G cellular
architecture? 

This a database that persist some information for example the IMSI of the mobile devices that can access the network.


With which other 4G/5G network elements (mobile device,
base station, MME, Serving Gateway Router, PDN Gateway Router) does it
directly communicate with in the control plane? 

the MME

In the data plane?

None

#### 16

What is the role of the Mobility Management Entity (MME) in 4G/5G
cellular architecture? 
This is a middleware that handle:

- Authentication and security

- Session and Bearer management

- Mobility Management

With which other 4G/5G network elements (mobile
device, base station, HSS, Serving Gateway Router, PDN Gateway
Router) does it directly communicate with in the control plane? 

Base Station, HSS and Serving gateway

In the data plane?

None


#### 17

Describe the purpose of two tunnels in the data plane of the 4G/5G cellular
architecture. 

Handling mobility between BSS.

When a mobile device is attached to its own home network, at
which 4G/5G network element (mobile device, base station, HSS, MME,
Serving Gateway Router, PDN Gateway Router) does each end of each of the
two tunnels terminate?

The first tunnel end at the Serving gateway and the second at the PDN gateway.

#### 18

What are the three sublayers in the link layer in the LTE protocol stack?
Briefly describe their functions.

Packet Data Convergence: performs IP header/compression and encryption/decryption of the IP datagram.

Radio Link control: fragmenting and reassembly when an IP datagrams is too big to fit in the underlying link-layer frames.

Medium Access Control: performs transmission scheduling.

#### 19

Does the LTE wireless access network use FDMA, TDMA, or both? Explain
your answer.

Both it can be visually represented as a grid with time slots on the x axis and frequencies on the y axis.

#### 20

Describe the two possible sleep modes of a 4G/5G mobile device. 

Light sleep: periodically synchronize with the AP x ms and is in sleep the rest of the time

Deep sleep: same than the light sleep but the sleep last seconds instead of ms and an host can wakeup in another BSS and would need to establish connection with the base station again in that case.

In each of these sleep modes, will the mobile device remain associated with the same
base station between the time it goes to sleep and the time it wakes up and
first sends/receives a new datagram?

Light sleep: will remain associated to the same base station

Deep sleep: like explained above may not remain associated with the same base station at wake up time.


#### 21

What is meant by a “visited network” and a “home network” in 4G/5G cel-
lular architecture?

A home network contains an MME that is capable of identifying the device with the HSS and track on which visited network the device is, a visited network will reach to the home network whenever it needs an information that i doesn't have.

A visited network is any other network that the device is in when it is not in its home network.

#### 22

List three important differences between 4G and 5G cellular networks.

- eMBB (Enhanced Mobile Broadband)

- URLLC (Ultra Reliable Low-Latency Communications)

- mMTC (Massive Machine Type Communications)

### section 7.5

#### 23

What does it mean that a mobile device is said to be “roaming?”

It means that the device is connected to a visited network and not its home network.

#### 24

What is meant by “hand over” of a network device?

The network that the device is quitting for another network perform a handover which is a transfer of responsibility for forwarding datagrams to/from one AP or base station to the mobile device.

#### 25

What is the difference between direct and indirect routing of datagrams to/
from a roaming mobile host?

With indirect routing the device will always pass by the home network then be re-routed to the visited network and in the direct routing it will only pass once at the begining to retrieve the necessary information from the home network then the visited network will interact in direct with the device without going through the home network.

#### 26

What does “triangle routing” mean?

It means indirect routing.

### section 7.6

#### 27

Describe the similarity and differences in tunnel configuration when a mobile
device is resident in its home network, versus when it is roaming in a visited
network.

The similarity is that there is still a tunnel between the base station and the serving gateway and another between the serving gateway and the PDN gateway in the home network when the device is resident or in the visited network when the device is roaming in it.
The difference is that when a device is roaming in a visited network there is an extract tunnel between the Serving-gateway of the visited network and the PDN-gateway of the home network to ensure data forwarding.

#### 28

When a mobile device is handed over from one base station to another in a
4G/5G network, which network element makes the decision to initiate that
handover? 

The source base station.

Which network element chooses the target base station to which the mobile device will be handed over?

The source base station.

#### 29

Describe how and when the forwarding path of datagrams entering the visited net-
work and destined to the mobile device changes before, during, and after hand over.

- the source base station selects the target base station and sends a handover request message to the target base station.

- the target base station checks if it has the resources to handle the mobile device if it has it preallocate resources for it.
The target base station replay with a Handover request Acknowledge message.

- the source base station received the Handover request acknowledgment message and informs the mobile device of the target base station's identity and channel access information.

At this point the mobile device can start sending datagram to the new base station.

- the source base station will also stop forwarding datagrams to the mobile device and instead forward any tunneled datagrams it receives to the target base station.

- the target base station informs the MME that it will be the new base station servicing the mobile device, the MME in turn informs the Serving Gateway and the target base station to reconfigure the Serving-Gateway-to-base-station tunnel to terminate at the target base station, rather than at the source base station.

- The target base station confirms back to the source base station that the tunnel has been reconfigured, allowing the source base station to release ressources associated with taht mobile device.

- At this point, the target base station can also begin delivering datagrams to the mobile device.

#### 30

Consider the following elements of the Mobile IP architecture: the home net-
work, foreign network permanent IP address, home agent, foreign agent, data
plane forwarding, Access Point (AP), and WLANs at the network edge. What
are the closest equivalent elements in the 4G/5G cellular network architecture?

The home network ,visited network, PDN gateway, Serving gateway  , GPT tunnels, Base station

#### 31

What are three approaches that can be used to avoid having a single wireless
link degrade the performance of an end-to-end transport-layer TCP connection?

- Local recovery

- TCP sender awareness of wireless links

- Split-connection approaches

### Problems

#### 1

 Consider the single-sender CDMA example in Figure 7.5. What would be the
sender’s output (for the 2 data bits shown) if the sender’s CDMA code were
(1, - 1, 1, - 1, 1, 1, 1, - 1)?

d1 = -1 and d0 = 1

Formula: Z im = di * cm

Time slot 1 channel output:

-1, 1, -1, 1, -1, -1, -1, 1

Time slot  0 channel output:


1, - 1, 1, - 1, 1, 1, 1, - 1

#### 2

Consider sender 2 in Figure 7.6. What is the sender’s output to the channel
(before it is added to the signal from sender 1), Z2
i,m?

d1 = -1 and d0 = 1

code 1: 1, 1, 1, -1, 1, -1, -1, -1

code 0: 1, 1, 1, -1, 1, -1, -1, -1

the ouput will be:

-1, -1, -1, 1, -1, 1, 1, 1 | 1, 1, 1, -1, 1, -1, -1, -1

#### 3

Suppose that the receiver in Figure 7.6 wanted to receive the data being sent
by sender 2. Show (by calculation) that the receiver is indeed able to recover
sender 2’s data from the aggregate channel signal by using sender 2’s code.

Receiver 2

Channel output from sender:

0 ,-2, 0 , 2, 0, 0, 2, 2   | 2,0,2,0,2,-2, 0, 0

 time slot 1 received input  time slot 0 received input
-1, -1, -1, 1, -1, 1, 1, 1 | 1, 1, 1, -1, 1, -1, -1, -1

di 2 = (sum zi*i,m * cm2) / M

di1 2 = 1

di0 2 = 1

#### 4

For the two-sender, two-receiver example, give an example of two CDMA
codes containing 1 and 21 values that do not allow the two receivers to
extract the original transmitted bits from the two CDMA senders.

d1 1 = - 1, d2 1 = 1

If the code of sender 1  are  -1 , -1, -1, -1, -1 , -1, -1 , -1

If the sender 0 send 1 , 1 , 1, 1 , 1, 1, 1 ,1

Which will give 2 , 2 , 2 , 2, 2 , 2, 2 , 2 then will lead to an incorrect data at the receiver for both senders.

#### 5

Suppose there are two ISPs providing WiFi access in a particular café, with
each ISP operating its own AP and having its own IP address block.

a) Further suppose that by accident, each ISP has configured its AP to oper-
ate over channel 11. Will the 802.11 protocol completely break down in
this situation? Discuss what happens when two stations, each associated
with a different ISP, attempt to transmit at the same time.

Not completely thanks to CSMA/CA if the code of both sender works well together it will be ok , but for the case when it is not the case then yes the protocol will break down.

b) Now suppose that one AP operates over channel 1 and the other over
channel 11. How do your answers change?

If they operate on different channels no collisions can happen.

#### 6

In step 4 of the CSMA/CA protocol, a station that successfully transmits a
frame begins the CSMA/CA protocol for a second frame at step 2, rather than
at step 1. What rationale might the designers of CSMA/CA have had in mind
by having such a station not transmit the second frame immediately (if the
channel is sensed idle)?

It is a fairness mechanism.

#### 7

Suppose an 802.11b station is configured to always reserve the channel with
the RTS/CTS sequence. Suppose this station suddenly wants to transmit
1,500 bytes of data, and all other stations are idle at this time. As a function of
SIFS and DIFS, and ignoring propagation delay and assuming no bit errors, cal-
culate the time required to transmit the frame and receive the acknowledgment.

1500 * 8 = 12 000 bits

12 000 / 11 000 000 = about 0, 00109 s

0, 00109 * 2 = 0, 00218 s

result = 0,00109s + DIFS + tRTS + TCTS + tAck 

#### 8

Consider the scenario shown in Figure 7.31, in which there are four wireless
nodes, A, B, C, and D. The radio coverage of the four nodes is shown via
the shaded ovals; all nodes share the same frequency. When A transmits, it
can only be heard/received by B; when B transmits, both A and C can hear/
receive from B; when C transmits, both B and D can hear/receive from C;
when D transmits, only C can hear/receive from D.
Suppose now that each node has an infinite supply of messages that it wants
to send to each of the other nodes. If a message’s destination is not an imme-
diate neighbor, then the message must be relayed. For example, if A wants
to send to D, a message from A must first be sent to B, which then sends
the message to C, which then sends the message to D. Time is slotted, with
a message transmission time taking exactly one time slot, e.g., as in slotted
Aloha. During a slot, a node can do one of the following: (i) send a message,
(ii) receive a message (if exactly one message is being sent to it), (iii) remain
silent. As always, if a node hears two or more simultaneous transmissions,
a collision occurs and none of the transmitted messages are received suc-
cessfully. You can assume here that there are no bit-level errors, and thus if
exactly one message is sent, it will be received correctly by those within the
transmission radius of the sender.

a) Suppose now that an omniscient controller (i.e., a controller that knows the
state of every node in the network) can command each node to do whatever
it (the omniscient controller) wishes, that is, to send a message, to receive a
message, or to remain silent. Given this omniscient controller, what is the
maximum rate at which a data message can be transferred from C to A, given
that there are no other messages between any other source/destination pairs?

dtrans c -> b + dtrans b -> a

1 / 2 so 0.5 message a slot

b) Suppose now that A sends messages to B, and D sends messages to C.
What is the combined maximum rate at which data messages can flow
from A to B and from D to C?

1 message a slot for each since the signal of A can't conflict with the signal of D.

c) Suppose now that A sends messages to B, and C sends messages to D.
What is the combined maximum rate at which data messages can flow
from A to B and from C to D?

0.5 message a slot since B can conflict with C A can only send to B when C doesn't send to D and C can only send to D when A doesn't send to B.

d) Suppose now that the wireless links are replaced by wired links. Repeat
questions (a) through (c) again in this wired scenario.

  a) the result doesn't change here 0.5 message a slot since we have to go through node B then node A.
  
  b) the result doesn't change here 1 message a slot.

  c) since it is wired they cannot conflict so for each with got 1 message a slot.

e) Now suppose we are again in the wireless scenario, and that for every
data message sent from source to destination, the destination will send an
ACK message back to the source (e.g., as in TCP). Also suppose that each ACK
message takes up one slot. 

Repeat questions (a)–(c) above for this scenario.

  a) 0.25 message a slot

  b) 0.5 message a slot for each
  
  c) 1 / 3 message a slot for each in the best scenario


#### 9

Describe the format of the Bluetooth frame. You will have to do some read-
ing outside of the text to find this information. 

Access code: preamble, sync, trailer

Packet header: AM address, type , flow, ARQN, SEQN, HEC

Payload: most of the time the IP datagram

Is there anything in the frame
format that inherently limits the number of active nodes in an network to
eight active nodes? Explain.

Yes the AM address a 3-bit field so only 8 devices maximum can be in the piconet.

#### 10

Consider the following idealized LTE scenario. The downstream channel
(see Figure 7.22) is slotted in time, across F frequencies. There are four nodes,
A, B, C, and D, reachable from the base station at rates of 10 Mbps, 5 Mbps,
2.5 Mbps, and 1 Mbps, respectively, on the downstream channel. These rates
assume that the base station utilizes all time slots available on all F frequen-
cies to send to just one station. The base station has an infinite amount of data
to send to each of the nodes, and can send to any one of these four nodes using
any of the F frequencies during any time slot in the downstream sub-frame.

a) What is the maximum rate at which the base station can send to the nodes,
assuming it can send to any node it chooses during each time slot? Is your
solution fair? Explain and define what you mean by “fair.”

1 frame for 10Mpbs, 2 frame for 5 Mps, 4 frame for 2.5 Mpbs and 10 frame for 1Mbps on 16 frequencies at the same time to achieve fairness and the max rate would be 10Mpbs

b) If there is a fairness requirement that each node must receive an equal
amount of data during each one second interval, what is the average
transmission rate by the base station (to all nodes) during the downstream
sub-frame? Explain how you arrived at your answer.

R / 10 + R/ 5 + R / 2.5 + R/ 1 = 1

0.1 R + 0.25R + 0.4 R + 1R = 4/ 1.7R = 2,353 Mbps

c) Suppose that the fairness criterion is that any node can receive at most
twice as much data as any other node during the sub-frame. What is the
average transmission rate by the base station (to all nodes) during the sub-
frame? Explain how you arrived at your answer.



2 *R / 10 + 2 * R/ 5 + 2 * R / 2.5 + 2 * R/ 1 = 1

7 R = 1

7 * 1/2.4 = 2,917 Mpbs

#### 11

In Section 7.5, one proposed solution that allowed mobile users to maintain
their IP addresses as they moved among foreign networks was to have a foreign
network advertise a highly specific route to the mobile user and use the existing

routing infrastructure to propagate this information throughout the network. We
identified scalability as one concern. Suppose that when a mobile user moves
from one network to another, the new foreign network advertises a specific route
to the mobile user, and the old foreign network withdraws its route. Consider
how routing information propagates in a distance-vector algorithm (particularly
for the case of interdomain routing among networks that span the globe).

a) Will other routers be able to route datagrams immediately to the new for-
eign network as soon as the foreign network begins advertising its route?

No we will have to wait that each router on the path update its forwarding table.

b) Is it possible for different routers to believe that different foreign networks
contain the mobile user?

Yes it is possible

c) Discuss the timescale over which other routers in the network will eventu-
ally learn the path to the mobile users.

Seconds to minutes.

#### 12

In 4G/5G networks, what effect will handoff have on end-to-end delays of
datagrams between the source and destination?

there is the dtrans of the handover request + response + the dtrans of every datagram that the source station must forward to the target station.

#### 13

Consider a mobile device that powers on and attaches to an LTE visited
network A, and assume that indirect routing to the mobile device from its
home network H is being used. Subsequently, while roaming, the device
moves out of range of visited network A and moves into range of an LTE
visited network B. You will design a handover process from a base sta-
tion BS.A in visited network A to a base station BS.B in visited network B.
Sketch the series of steps that would need to be taken, taking care to identify
the network elements involved (and the networks to which they belong), to
accomplish this handover. Assume that following handover, the tunnel from
the home network to the visited network will terminate in visiting network B.

(answer)[./problem-13.png]

#### 14

Consider again the scenario in Problem P13. But now assume that the tunnel
from home network H to visited network A will continue to be used. That is,
visited network A will serve as an anchor point following handover. (Aside:
this is actually the process used for routing circuit-switched voice calls to
a roaming mobile phone in 2G GSM networks.) In this case, additional
tunnel(s) will need to be built to reach the mobile device in its resident visited
network B. Once again, sketch the series of steps that would need to be taken,
taking care to identify the network elements involved (and the networks to
which they belong), to accomplish this handover.

It is the same schema than the first version except that the visited network A never stop to reroute.


What are one advantage and one disadvantage of this approach over the
approach taken in your solution to Problem P13?

There is more overhead since now we must go through visited network A and B but the MME of the home network doesn't need to track that the mobile device went from visited network A to B.

### Wireshark lab: WIFI

#### 1

What are the SSIDs of the two access points that are issuing most of the beacon
frames in this trace? [Hint: look at the Info field. To display only beacon frames,
neter wlan.fc.type_subtype == 8 into the Wireshark display filter]

There SSIDs are:

SSID: "30 Munroe St"
SSID: "linksys12"

### 2

What 802.11 channel is being used by both of these access points [Hint: you’ll
need to dig into the radio information in an 802.11 beacon frame]

Channel: 6 for both.

#### 3
What is the interval of time between the transmissions of beacon frames from this
access point (AP)? (Hint: this interval of time is contained in a field within the
beacon frame itself).

Beacon Interval: 0.102400 [Seconds]

#### 4

What (in hexadecimal notation) is the source MAC address on the beacon frame
from this access point? Recall from Figure 7.13 in the text that the source,
destination, and BSS are three addresses used in an 802.11 frame. For a detailed
discussion of the 802.11 frame structure, see section 9.2.3-9.2.4.1in the IEEE
802.11 standards document, excerpted https://gaia.cs.umass.edu/wiresharklabs/802.11-9.2.4.1_spec+wireshark_filters.pdf.

Source address: CiscoLinksys_f7:1d:51 (00:16:b6:f7:1d:51)


#### 5

What (in hexadecimal notation) is the destination MAC address on the beacon
frame from 30 Munroe St??

Destination address: Broadcast (ff:ff:ff:ff:ff:ff)

#### 6

What (in hexadecimal notation) is the MAC BSS ID on the beacon frame from 30
Munroe St?

BSS Id: CiscoLinksys_f7:1d:51 (00:16:b6:f7:1d:51)

#### 7

The beacon frames from the 30 Munroe St access point advertise that the access
point can support four data rates and eight additional “extended supported rates.”
What are these rates? [Note: the traces were taken on a rather old AP

Tag: Supported Rates 1(B), 2(B), 5.5(B), 11(B), [Mbit/sec]

#### 8

Find the 802.11 frame containing the SYN TCP segment for this first TCP session
(that downloads alice.txt) at t=24.8110. What are three MAC address fields in the
802.11 frame? 
Receiver address: CiscoLinksys_f7:1d:51 (00:16:b6:f7:1d:51)

Source address: Intel_d1:b6:4f (00:13:02:d1:b6:4f)

Transmitter address: Intel_d1:b6:4f (00:13:02:d1:b6:4f)

first hop router address:  91:2a:b0:49:b6:4f (91:2a:b0:49:b6:4f)

Which MAC address in this frame corresponds to the wireless host
(give the hexadecimal representation of the MAC address for the host)? 

Source address: Intel_d1:b6:4f (00:13:02:d1:b6:4f)

To the access point? To the first-hop router? What is the IP address of the wireless host
sending this TCP segment? 


Receiver address: CiscoLinksys_f7:1d:51 (00:16:b6:f7:1d:51)



What is the destination IP address for the TCP syn segment? 

Destination Address: 128.119.245.12



#### 9

Does the destination IP address of this TCP SYN correspond to the host, access
point, first-hop router, or the destination web server?

The destination web server.

#### 10

Find the 802.11 frame containing the SYNACK segment for this TCP session
received at t=24.8277 What are three MAC address fields in the 802.11 frame?

Source address: CiscoLinksys_f4:eb:a8 (00:16:b6:f4:eb:a8)

Receiver address: 91:2a:b0:49:b6:4f (91:2a:b0:49:b6:4f)

Destination address: 91:2a:b0:49:b6:4f (91:2a:b0:49:b6:4f)



Which MAC address in this frame corresponds to the host? 

host: Intel_d1:b6:4f (00:13:02:d1:b6:4f)


To the access point?

 CiscoLinksys_f4:eb:a8 (00:16:b6:f4:eb:a8)


To the first-hop router? 

91:2a:b0:49:b6:4f (91:2a:b0:49:b6:4f)


Does the sender MAC address in the frame correspond to
the IP address of the device that sent the TCP segment encapsulated within this
datagram? (Hint: review Figure 6.19 in the text if you are unsure of how to
answer this question, or the corresponding part of the previous question. It’s
particularly important that you understand this).


No it doesn't correspond to it

#### 11

What two actions are taken (i.e., frames are sent) by the host in the trace just after
t=49, to end the association with the 30 Munroe St AP that was initially in place
when trace collection began? (Hint: one is an IP-layer action, and one is an
802.11-layer action).

Authentication request and Association request.

#### 12

Let’s look first at AUTHENTICATION frames. At t = 63.1680, our host tries to
associate with the 30 Munroe St AP. Use the Wireshark display filter
wlan.fc.subtype == 11 to show AUTHENICATION frames sent from the
host to and AP and vice versa. What form of authentication is the host requesting?

Authentication Algorithm: Open System (0)

#### 13

What is the Authentication SEQ value (authentication sequence number) of
this authentication frame from host to AP?

Authentication SEQ: 0x0001

#### 14

The AP response to the authentication request is received at t = 63.1690. Has the
AP accepted the form of authentication requested by the host?


Yes it has it: 

Authentication Algorithm: Open System (0)

#### 15

What is the Authentication SEQ value of this authentication frame from
AP to Host ?

Authentication SEQ: 0x0002

#### 16

What rates are indicated in the frame as SUPPORTED RATES. Do not include in
your answers below any rates that are indicates as EXTENDED SUPPORTE
RATES.

Tag: Supported Rates 1(B), 2(B), 5.5(B), 11(B), [Mbit/sec]

#### 17

Does the ASSOCIATION RESPONSE indicate a Successful or Unsuccessful
association response?

Status code: Successful (0x0000)

#### 18

Does the fastest (largest) Extended Supported Rate the host has offered match the
fastest (largest) Extended Supported Rate the AP is able to provide?

No it doesn't the AP largest extended supported rate is 54 Mpbs and the max in the 11 Mpbs.

