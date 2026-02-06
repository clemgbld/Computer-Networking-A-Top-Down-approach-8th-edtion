# Chapter 1 exercises

## Book review questions

### SECTION 1.1

#### R1
What is the difference between a host and an end system?
A host and an end system or two synonym they can be used both interchangeably.

List several different types of end systems.

- A computer
- A smart-phone
- A smart-watch 
- Just any systems that is a source or destination or both (they are at the end of the network core).

Is a Web server an end system ?

Yes it is, a web server is a end system (server) that typically talk with another end-systems (a client).

#### R2

Who's controlling the internet ?
The isp internet service providers.

Is the internet damaging the environment ?
Yes in a sense since it require electrical power to connect every net together.

Can anyone shut down the internet.
Not really, you can shut down a network but you can't shut all the networks that the internet is connecting.
You could in theory attack and shut down a tier-1 ISP and cutting out a lot of IPS out of internet.

#### R3

What is a sneaker net ?

A sneaker net is a term for offline data sharing, sharing data between a USB key or a floppy disk with a computer for example.

Explain the main characteristics of networking.

- packets transmissions.

- ruled by protocols (TCP, IP, UDP, etc...)

- Distributed

- Shared Resources

- Scaling

Mention the key design issues of a computer network.

The key design issues: 

- Address finding

- Security risk (DOS, man in the middle, etc...) 

- Congestion control


### SECTION 1.2

#### R4

List four access technologies.

- 4G - 5G
- DSL
- Cable
- FTTH
- WIFI
- Ethernet


Classify each one as home access, enterprise access., or wide-are wireless access.

- 4G - 5G wide-are wireless access
- DSL, Cable, FTTH, WIFI, Ethernet home access
- WIFI and Ethernet enterprise access

#### R5

Is HFC transmission rate dedicated or shared among users?

Yes it is shared among users.

Are collisions possible in a downstream HFC channel?

No you cannot

Why or why not ?

Because there is just one source distributing the packets to the different homes.

#### R6

What access network technologies would be most suitable for providing internet in rural areas.

It would be either 5G fixed Wireless or Terrestrial Radio Channels because it can cover a wide area and you don't need to pull cables to each home since they can be far apart since they are rural areas.

#### R7

Dial-up modems and DSL both use the telephone line (a twisted-pair copper cable) as their transmission medium.
Why then is DSL much faster than dial-up access ?

The data rates that can be achieved depend on the thickness of the wire and the distance between transmitter and receiver.

DSL use more bandwidth than dial-up access

#### R8

Do signals really travel faster in fibre optics ?

No it doe not travel faster, just carry more data, less signal degradation over long distances, lower attenuation.

What are some of the uses of fibre optic cabling in the business world and what principles does fibre optic work on ?

- long-distance overseas connection
- long-distance telephone networks in the US and elsewhere
- residential access network

The principal of fiber optics are:

- conducts pulses of light (each pulse represent a bit)
- high bits rates.
- immune to electromagnetic interference.
- hard to tap.

#### R9

HFC, DSL, and FTTH are all used for residential access. For each of these access technologies, provide a range of transmission rates and comment on whether the transmission rate is shared or dedicated.

- HFC 10Mbps to 1Gbps transmission rate shared
- DSL downstream 24 mbs and 52 Mbs and upstream rates 3.5 Mbps to 16 Mbps, transmission rate dedicated.

FTTH 1 Gbps to 100Gbps, dedicated for home and then shared when arriving at the optical splitter

#### R10

Describe the different wireless technologies you use during the day and their characteristics.

4G - 5G:
- long reach.
- shared
- quality not reliable depends of where you are

WIFI
- small reach.
- private to your local area, and secured by a password.
- quality reliable, you are connection is the same on average.

I prefer the WIFI at home because it is reliable and secure and i can use as much as i want, unlike 4G or 5G.
I don't have much a choice to use 4G or 5G when i'm out or when my WIFI is down.

### SECTION 1.3

#### R11
Suppose there is exacly one packet switch between a sending host and a receiving host.The transmission rates between the sending host and the receiving host are R1 and R2, respectively.
Assuming that switch uses store-and-forward packet switching, what is the total end-to-end delay to send a packet of length L ? (Ignore queuing, propagation delay and processing delay.)

[]--R1--Switch--R2--[]

L/R1 + L/R2

#### R12

What are the three phases of circuit switching.

- network etablishes the circuit ,reserve a constant transmission rate

- hosts exchange stream of data with each other.

- network cut the connection, and free the resources by letting the circuit be used by other hosts.

List the advantages and disadvantages of circuit switching and packet switching ?

Packet switching:

Advantages:
- Dynamic allocation (no waste of resource): the less people using the network the faster it will be for you.
- No Idle periods: If you are not using the network you don't use anything even after you start using it.
- Better scaling (more people can use it at the same time)


Disadvantages:
- Packet loss when the queue is overwhelmed
- more delays (queue delay)


Circuit switching:

Advantages:
- The circuit is dedicated
- Data flows as a continuous stream
- No queuing, no buffers to overflow

Disadvantages:
- Idle periods waste capacity: Even when you're not sending data (silence in a phone call), the circuit is still reserved and unavailable to others
- Fixed allocation: You get 1/4 of the link even if you're the only user and could use more
What are the delay in packet switching.
- Take an initial delay for etablishing the circuit

d nodal = d transmission + d propagation + d queuing + d processing

#### R13

Suppose users share a 2 Mbps link. Also suppose each user transmits continuously at 1 Mbps when transmitting, but each user transmits only 20 percent of the time. (See the discussion of statistical multiplexing in Section 1.3)

- a. When circuit switching is used, how many users can be supported

Only 2 since each users transmits 1 Mbps, and when using circuit switching the circuit is dedicated.

- b. For the remainder of this problem, suppose packet switching is used. 

Why will there be essentially no queuing delay before the link if two of fewer users transmit at the same time?

Because user1 = 1Mbps + user 2 = 1Mbps = 2Mbps and the Link = 2Mbps , the link is not overloaded.

Why will there be a queuing delay if three users transmit at the same time ?

Because user1 = 1Mbps + user 2 = 1Mbps + user 3 = 1Mbps = 3Mbps and the Link = 2Mbps , the link is overloaded.

- c. Find the probability that a given user is transmitting.

The probability is 0.2

- d. Suppose now there are three users. Find the probability that at any given time, all three users are transmitting simultaneously. 

0.2 * 0.2 * 0.2 = 0.008 = 0.08%

Find the fraction of time during which queue grows

The answer is also 0.08% since the queue is overloaded only when L > R and in order it must be when all the user or transmitting at the same time which is 3Mbps > 2Mbps

#### R14

What is the difference between circuit switching and packet switching ?

The big difference if we compared the advantages and disadvantages in my answer in R12 is that packet switching is on demand (sends packet) and circuit switching preallocate resources (stream).

#### R15

Why is a content provider considered a different Internet entity today ?
Because content provider has a network of data center connected together and connected to the internet as well.
Before they were just customer of the ISP now they are provider as well.
How does a content provider connect to other ISPs ? 
It  connects through IXP, the low tier ISP and tier 1 ISP when they really have to.
Why ?
Because connecting directly through IXP and low tier ISP cut the middle man which is the tier 1 ISP and make them save money.


### SECTION 1.4

#### R16

What causes packet loss ?

A queue that is at capacity and can't hold anymore packets because of network congestion, the packet that can't enter into the queue is dropped.

#### R17

A user can directly connect to a server through either long-range wireless or a twisted-pair cable for transmitting 1500-bytes file. The transmission rates of the wireless and wired media are 2 and 100Mbps, respectively. Assume that the propagation speed in air is 3 * 10^8 m/s, while the speed in the twisted pair is 2 * 10^8 m/s. If the user is located 1 KM away from the server, what is the nodal delay when using each of the two technologies?

Formulas: L/R for transmission rate, D/S for propagation.

1500 bytes = 1500 * 8 = 12000 bits

wirless nodal delay = (0,012/2) + (1000/ (3 * 10^8)) = 0.00600333 s

wire nodal delay = (0,012/100) + (1000/ (2 * 10^8)) =  0.000125 s

#### R18

Suppose Host A wants to send a large file to Host B. The path from Host A to Host B has three links, of rates R1 = 500 kbps, R2 = 2 Mbps, and R3 = 1 Mbps.

- a. Assuming no other traffic in the network, what is the throughput for the file transfer

min { R1, R2, R3} = R1 = 500kbps

- b. Suppose the file is 4 million bytes.
Dividing the file size by the throughput, roughly how long will it take to transfer the file to Host B ?

4 million bytes in bytes = 32 Mb

32 Mb / 0,5 Mbps = 64 seconds


- c. Repeat (a) and (b), but now with R2, reduced to 100 kbps.


min { R1, R2, R3} = R2 = 100kbps


32 Mb / 0,1 Mbps = 320 seconds

#### R19

Suppose end system A wants to send a large file to end system B. At a very
high level, describe how end system A creates packets from the file.

System A will divide the file in chunk of bits with a header which contains metadata such as the IP address of the receiver and of system A, the chunk of bits are called packets.

When one of these packets arrives to a router, what information in the packet does
the router use to determine the link onto which the packet is forwarded?

The router will use the IP address or a subset of this last (matching the longest prefix), and determine the link onto which the packet is forwarded with its forwarding table.

Why is packet switching in the Internet analogous to driving from one city to
another and asking directions along the way?

Because each router only knows to which link forward the next packet but not the link of target host, only the last router does.

Like with driving from one city to another and asking directions along the way you will incrementally arrive to the last person who will tell you where is your precise destination.


### SECTION 1.5

#### R20

If two end-systems are connected through multiple routers and the data-link
level between them ensures reliable data delivery, is a transport protocol
­ offering reliable data delivery between these two end-systems necessary?

Yes it is, you need TCP.

Why?
To check the correctness of the message that you receive and deliver an error if a packet is lost.
the data link doesn't shield you against packet lost.

#### R21

What are the five layers in the Internet protocol stack? What are the principal
responsibilities of each of these layers?

Application: where the network application reside and their applications protocol such as HTTP or SMTP. 
Its goal is typically send message and receive message.

Transport: Transport application layer message between application endpoint (TCP, UDP)

Network: Responsible for moving network-layer packets known as datagrams from one host to another and routes them through a series of router (IP protocol)

Link: Responsible to move the datagrams from a node to another via a link

Physical: Move the individual bits within the frame from one node to the next.

#### R22

What do encapsulation and de-encapsulation means ?

encapsulation -> a layer encapsulate the data of the layer above by adding information who will be needed in the other layers or by the routers etc... (for example the transport layer encapsulate the application layer by appending some information in the header who thus become a transport-segment)

de-encapsulation -> basically the inverse encapsulation a  layer receive data from a layer down  who remove informations it added previously.

Why are they needed in a layered protocol stack?

Encapsulation enable some change in a layer without impacting the other as long as they keep the same contract.

#### R23

Which layers in the Internet protocol stack does a router process? 
- network
- link
- physical
Which layers does a link-layer switch process? 
- link
- physical
Which layers does a host process?
- application
- transport
- network
- link
- physical


### SECTION 1.6

#### R24

What is the meaning of AAA in network security ?

Authentication, Authorization, Accounting/Auditing

What are the different methods of user authentication ?

- Something you know (PIN, PASSWORD)

- Something you have (security key, OTP app, or SMS code)

- Something you are (biometrics, face, voice)

- MFA (Mutlifactor authentication) combine multiple of the above methods.

#### R25

Describe how a botnet can be created and how it can be used for a DDoS attack.

An attacker use the machine infected by a self-replicating malware to launch a DDoS attack.

#### R26

What is IPS in network security ?

IPS (intrusion prevention system) a system that aim to detect when an intrusion occurs and something about it.

What are the potential consequences of a network security attack for an organization ?

- Sensible data theft (private users data, private corporate data etc...)

- Data destruction

- Possible down time of the system

- Lost of credibility

- Blackmail

- Financial lost

- Legal consequences

- Regulatory penalties

- Competitive disadvantages

### SECTION 1.7


#### R27

What happens when you type a URL (uniform resource locator) in the web browser ?

- It will first do a DNS lookup with the hostname in the URL to locate the IP

- TCP connection

- TLS/SSL handshake (for htttps)

- Send a get http request to the server

- The server receive the request and process it to serve your content

- browser rendering

#### R28

What are the advantages of distributed processing ?

- Horizontal Scaling (can distribute the load on multiple nodes)

- Availability (can replicate a node that can take the place of the node in use if this last crash)

- Performance

- Resource Sharing

- Cost Effectiveness 

- Geographic distribution

- Modularity/ flexibility

#### R29

What is the criteria to check the network reliability and what makes a network effective

For the first question i would say up-time and the percentage of errors that are due to the network, make sure that the network intensity is less than 1 to avoid packet loss

For the network effectiveness:

- Good Throughput

- Make use of as much bandwidth as possible

- Having redundancy

#### R30

Calculate the latency (total delay from first bit sent to last bit received) for the specification given.

Sender and receiver are separated by two 1Gbps links and a single switch.

The packet size is 10000 bits, and each link introduces a propagation delay of 20 µs.

Assume that the switch begins forwarding immediately after it has received the last bit of the packet and the queue are empty.

Transmission delay formula: N * (l/R) when the transmission rate is the same for all the links.

d nodal in that context: dNodal = N * (dTranmission + dPropagation)

dPropagation in seconds = 0,00002

1Gbps in Mbps = 1000Mbps

10000 bits in Mb = 0,01Mb

2 * (0,01/1000 + 0,00002) = 60µs

#### R31

Consider a switch that uses time division multiplexing (rather than statistical multiplexing) to share a link between four concurrent connections (A,B,C and D) whose packets arrive in bursts. The link's data rate is 1 packet per time slot. Assume that the switch runs for a very long time. The average packet arrival rates of the four connections (A through D), in packets per time slot, are 0.2, 0.1, 0.2, and 0.1 respectively.
The average delays observed at the switch (in time slots) are 10, 5, 10, and 5.
What are the average queue lengths of the queues (A through D) at the switch ?

Little's law = L = L=lambda * W

La =  (10 * 0.2) = 2
Lb = (5 * 0.1) = 0.5
Lc = (10  * 0.2) = 2
Ld = (5 * 0.1) = 0.5

#### R32
Anand has developed a new switch. In this switch, 20% of the packets are processed on the "slow path", which incurs an average delay of 1 millisecond.
All the other packets are processed on the "fast path",incurring an average delay of 0.1 milliseconds. Anand observes the switch over a period of time and finds that the average number of packets in it is 19.
What is the average rate, in packets per second at witch the switch processed packets.

slow = 20% , average delay of 1 millisecond
fast = 80% average delay of 0,1 milliseconds

average packets in 19.


Little's law = L = L=lambda * W

L = 19

W = 0.2 * 0,001 + 0.8 * 0,0001 = 0,00028

lambda = 19/ 0,00028 = 67857,14 packets by seconds

#### R33

Bhaskar designs a switch for a circuit switched network to send data on a 1 Mbps link using time division multiplexing (TDM). 
The switch supports a maximum of 20 different simultaneous conversations on the link, and any given sender transmits data in frames of size 3000 bits. 
Over a period of time. 
Bhaskar finds that the average number of conversations simultaneously using the link is 10. 
The switch forwards a data frame sent by a given sender every x seconds according to TDM.
determine the value of x.

1Mbps / 3000 bits = 333,33 / 20 (the nubmer of users) = 16.67 seconds, 1 / 16.67 = 0.0667 seconds.

The switch forwards a data frame sent by a given sender every 0,0667 seconds.

### Problmes

#### P1

Design and describe an application-level protocol to be used between an
automatic teller machine and a bank’s centralized computer. Your protocol
should allow a user’s card and password to be verified, the account bal-
ance (which is maintained at the centralized computer) to be queried, and an
account withdrawal to be made (that is, money disbursed to the user). Your
protocol entities should be able to handle the all-too-common case in which
there is not enough money in the account to cover the withdrawal. Specify
your protocol by listing the messages exchanged and the action taken by the
automatic teller machine or the bank’s centralized computer on transmission
and receipt of messages. Sketch the operation of your protocol for the case of
a simple withdrawal with no errors, using a diagram similar to that in Figure 1.2.
Explicitly state the assumptions made by your protocol about the underlying
end-to-end transport service.

[answer](./problem-1.png)

#### P2

Equation 1.1 gives a formula for the end-to-end delay of sending one packet
of length L over N links of transmission rate R. Generalize this formula for
sending P such packets back-to-back over the N links.

L = bits in a packet , R = rate in seconds, N = number of links, P = total number of packets

d end to end = (N + P - 1) * ( L / R )

#### P3

What are common network issues and how to resolve them fast ?

Loosing connection to a socket, solution trying to reconnect with exponentional back off
Packets arrive in the wrong order, solution reorder them before sending the message to the receiver
Packets or dropped, solution asking the sender the droped packets
1 packet is already being transfer through a link and only one packet can be transfered at the time,
Solution make the other packet wait in a queu.

we need to ping again to see if the server is still a live, use traceroute to see which link is failing, use Wireshark to monitor the packets.

#### P4

Consider the circuit-switched network in Figure 1.13. Recall that there are
four circuits on each link. Label the four switches A, B, C, and D, going in
the clockwise direction.
a. What is the maximum number of simultaneous connections that can be in
progress at any one time in this network?

The maxium simultaneous connection is 16 since there is 4 links of 4 circuits 4 * 4 = 16.

b. Suppose that all connections are between switches A and C. What is the
maximum number of simultaneous connections that can be in progress?

 A->B->C = 4 + A->D-C = 4 = 8

c. Suppose we want to make four connections between switches A and C,
and another four connections between switches B and D. Can we
route these calls through the four links to accommodate all eight
­ connections?

it's impossible the way through A-C and B->D cross each other.

#### P5

Review the car-caravan analogy in Section 1.4. Assume a propagation speed
of 100 km/hour.
a. Suppose the caravan travels 175 km, beginning in front of one tollbooth,
passing through a second tollbooth, and finishing just after a third toll-
booth. What is the end-to-end delay?

assuming the transmission delay is (10 cars) / (5 cars / minutes) = 2 minutes

and there is 3 tollbooth one start , one intermediate and one at the end

there is 2 links and the propagation speed is 100kmh the cars travel at 175kmh.

so the propagation delay is 175/100 = 1,75 = 60 * 1,75 = 105

+ (2 minutes * (N where N = 3)) which gives us a result 111 minutes.


b. Repeat (a), now assuming that there are eight cars in the caravan instead
of ten.

(8 cars) / (5 cars/ minuts) = 1 minutes and 36 seconds

the propagation delay should be the same then the answer is 105 minutes + (1minutes 36 * 3 = 4m 48) = 109minutes 48 

#### P6

This elementary problem begins to explore propagation delay and transmis-
sion delay, two central concepts in data networking. Consider two hosts, A
and B, connected by a single link of rate R bps. Suppose that the two hosts
are separated by m meters, and suppose the propagation speed along the link
is s meters/sec. Host A is to send a packet of size L bits to Host B.
a. Express the propagation delay, dprop, in terms of m and s.

d prop =  s / m

b. Determine the transmission time of the packet, dtrans, in terms of L and R.

d trans = L / R

c. Ignoring processing and queuing delays, obtain an expression for the end-
to-end delay.

dend = d prop + d trans

d. Suppose Host A begins to transmit the packet at time t = 0. At time t =
dtrans, where is the last bit of the packet?

the last bits of the packet is arrived on the link since L represebt all the bits in a packet.


e. Suppose dprop is greater than dtrans. At time t = dtrans, where is the first
bit of the packet?

if dprop is greater than dtrans the first bit is still on the link.

f. Suppose dprop is less than dtrans. At time t = dtrans, where is the first bit of
the packet?

if dprop is less than dtrans the first bit arrive to the receiver already at t = dtrans.

g. Suppose s = 2.5 * 10^8
, L= 1500 bytes, and R= 10 Mbps. Find the
distance m so that dprop equals dtrans.

L / R = s / m

L = 1500 * 8 = 12000 bits = 12kb
R = 10 Mbps = 10000 kb

dtrans = 12 / 10000 = 1,2ms

2.5 * 10^8 * 0,0012 = 300000 meters

#### P7

In this problem, we consider sending real-time voice from Host A to Host B
over a packet-switched network (VoIP). Host A converts analog voice to a
digital 64 kbps bit stream on the fly. Host A then groups the bits into 56-byte
packets. 
There is one link between Hosts A and B; 
its transmission rate is 10 Mbps and its propagation delay is 10 msec. 
As soon as Host A gathers a packet, it sends it to Host B. As soon as Host B receives an entire packet, it
converts the packet’s bits to an analog signal. 
How much time elapses from
the time a bit is created (from the original analog signal at Host A) until the
bit is decoded (as part of the analog signal at Host B)?

L = 56 * 8 = 448 bits

dtrans = 448 bits / 10Mbps = 0,448ms
dpacket = 488 / 64kbps = 7,6ms

the answer is dtrans + dprop = 0,0448 + 10ms + 7ms =  17.0448 ms.

#### P8

Suppose users share a 10 Mbps link. Also suppose each user requires 200 kbps
when transmitting, but each user transmits only 10 percent of the time. (See
the discussion of packet switching versus circuit switching in Section 1.3.)
a. When circuit switching is used, how many users can be supported?

50 users at max can be supported because 10 Mbps / 200 kbps = 50

b. For the remainder of this problem, suppose packet switching is used. Find
the probability that a given user is transmitting.

There is 10% chance that a given user is transmitting

c. Suppose there are 120 users. Find the probability that at any given time,
exactly n users are transmitting simultaneously. (Hint: Use the binomial
distribution.)

P(k) = C(120,K) * 0,1^k * (0,9)^ 120 - k

the probability i 1 e-120

d. Find the probability that there are 51 or more users transmitting
­ simultaneously.

P(k) = C(120,51) * 0,1^51 * (0,9)^ 120 -51

#### P9

Consider the discussion in Section 1.3 of packet switching versus circuit switch-
ing in which an example is provided with a 1 Mbps link. Users are generating
data at a rate of 100 kbps when busy, but are busy generating data only with
probability p= 0.1. Suppose that the 1 Mbps link is replaced by a 1 Gbps link.
a. What is N, the maximum number of users that can be supported simulta-
neously under circuit switching?

1 Gbps / 100Kbps = 10000 users

b. Now consider packet switching and a user population of M users. Give a
formula (in terms of p, M, N) for the probability that more than N users
are sending data.

P(X > N) = \sum_{k=N+1}^{M} \binom{M}{k} p^k (1-p)^{M-k}

#### P10

Consider the network illustrated in Figure 1.16. Assume the two hosts on the
left of the figure start transmitting packets of 1500 bytes at the same time
towards Router B. Suppose the link rates between the hosts and Router A
is 4-Mbps. One link has a 6-ms propagation delay and the other has a 2-ms
propagation delay. Will queuing delay occur at Router A?

L = 1500 * 8 = 12000 bits

R = 4Mbps

d trans = L/R = 12kbps/4Mbps = 3ms

d prop1 = 2ms

d prop2 = 6ms

t= d trans + dprop 1 = 5ms 
- first packet arrive at the router
- second packet still on the transmission delay at 5ms


t = dtrans + dprop 2 = 9ms
- first packet arrive at the destination
- while the second packet is still in the second transmission delay

So no there is no queuing delay.

the formula is (d_trans + d_prop1) + d_trans <= d_trans + d_prop2 = 8ms <= 9ms

#### P11

Consider the scenario in Problem P10 again, but now assume the links
between the hosts and Router A have different rates R1 and R2 byte/s in addition to different propagation delays d1 and d2.
Assume the packet lengths for the two hosts are of L bytes. 
For what values of the propagation delay will no
queuing delay occur at Router A?

(d_trans_host1 + dprop1) + d_trans_router <= d_trans_host2 + d_prop2

#### P12

Network designers generally attempt to deploy networks that don't have single points of failure,
though they don't always succeed. Network topologies that employ redundancy are of much interest.

- a) Draw an example of a six-node network in which the failure of a single link does not disconnect the entire network
(that is, any node can still reach any other node.)

[answer](./problem-12-a.png)

- b) Draw an example of a six-node network in which the failure of any single link cannot disconnect the
entire network, but the failure of some single node does disconnect it.


[answer](./problem-12-b.png)

- c) Draw an example of a six-node network in which the failure of any single node cannot disconnect
the entire network, but the failure of some single link does disconnect it.

This is not possible since protecting a network from a node failure protects it against a link failure as well.

Not all the cases above may have a feasible example.

#### P13

- a) Suppose N packets arrive simultaneously to a link at which no packets
are currently being transmitted or queued. Each packet is of length L and
the link has transmission rate R. What is the average queuing delay for
the N packets?

Calculate sum formula = k(k + 1)/2

(((N - 1) * N) / 2) * L/R) / N
((N-1)/2) * L/R
(N-1)L / (2R)

the average queuing delay is  (N - 1) L / (2 R)

- b) Now suppose that N such packets arrive to the link every LN/R seconds.
What is the average queuing delay of a packet?

The delay is exactly the same as in part 1.

#### P14

Consider the queuing delay in a router buffer. Let I denote traffic intensity;
that is, I= La/R. Suppose that the queuing delay takes the form IL/R (1- I)
for I < 1.
a. Provide a formula for the total delay, that is, the queuing delay plus the
transmission delay.
IL/R (1-I) + L/R

b. Plot the total delay as a function of L /R.

The total delay increase when L/R increase.

#### P15

When should i use layered architecture ?

When you don't want one part of the implementation details of your systems to break the entire systems
when you change it as long as you respect the contracts, so when you want flexibility and decoupling and separate concerns.

#### P16

Consider a router buffer preceding an outbound link. In this problem, you
will use Little’s formula, a famous formula from queuing theory. Let N
denote the average number of packets in the buffer plus the packet being
transmitted. Let a denote the rate of packets arriving at the link. Let d denote
the average total delay (i.e., the queuing delay plus the transmission delay)
experienced by a packet. Little’s formula is N = a * d. Suppose that on
average, the buffer contains 100 packets, and the average packet queuing
delay is 20 msec. The link’s transmission rate is 100 packets/sec. Using
Little’s formula, what is the average packet arrival rate, assuming there is
no packet loss?

N = a * d.

d_trans = 1sec/100packets = 10ms

d = 20ms + 10ms = 30ms

N = 100

100 = a * 0,03

100 / 0,03 = a

a = 3333,33 packet/s

#### P17

Consider the network illustrated in Figure 1.12.

Would Equation 1.2 hold in such a scenario? If so, under which conditions?

The equation 1.2 = dend - end = N(dproc + dtrans + dprop)

No this equation won't hold in the case of figure 1.12 who illustrate a queuing delay.

If not, why? (Assume N is the number of links between a source and a destination in the figure.)

Because the because of the queuing delay the end to end delay equation changes:

dend - end = Σ(dproc + dtrans + dprop + dqueu)

Where dqueue is the average queuing delay at each router.

#### P18

Perform a Traceroute between source and destination on the same continent
at three different hours of the day.
a. Find the average and standard deviation of the round-trip delays at each of
the three hours.
b. Find the number of routers in the path at each of the three hours. Did the
paths change during any of the hours?
c. Try to identify the number of ISP networks that the Traceroute packets
pass through from source to destination. Routers with similar names and/
or similar IP addresses should be considered as part of the same ISP. In
your experiments, do the largest delays occur at the peering interfaces
between adjacent ISPs?
d. Repeat the above for a source and destination on different continents.
Compare the intra-continent and inter-continent results

#### P19

Reddy has set up an eight-node shared medium network running the carrier sense multiple access (CSMA) MAC protocol.The maximum data rate of the network is 10 megabits/s. Including some retries, each node sends traffic according to some unknown random process at an average rate of 1 megabit/s per node. Reddy measures the network's utilization and finds that it is 0.76. No packets get dropped in the network except due to collisions, and each node's average queue size is 5 packets.Each packet is 10000 bits long.

- a) What fraction of packets sent by the nodes (including retries) experience a collision ?

S = 10Mps * 0.76 = 7.6mps
collision = 1 - (7.6mps / 8) = 5%

there is 5% of loss of data due to collision


- b) What is the average queuing delay, in milliseconds, experienced by a packet before it is sent over the medium?

L = a * W

a = 1mps / 10kbps = 100 packets/s



5 = 100packets/s * dqeue 

5/100packs/s = dqueue 

dqueue = 50ms

#### P20

Consider the throughput example corresponding to Figure 1.20(b). Now
suppose that there are M client-server pairs rather than 10. Denote Rs, Rc,
and R for the rates of the server links, client links, and network link. 
Assume all other links have abundant capacity and that there is no other traffic in the
network besides the traffic generated by the M client-server pairs. Derive a
general expression for throughput in terms of Rs, Rc, R, and M.

throuhput is  min {Rs, R/M,Rc}

#### P21

Assume a client and a server can connect through either network (a) or (b) in
Figure 1.19. Assume that Ri = (Rc + Rs) / i, for i= 1, 2, ..., N. In what case
will network (a) have a higher throughput than network (b)?

Network a will have a higher throughput that network b if:

throughput network a min {Rc,Rs} > min throughput network b {Rc,Rs, R1,...,RN}

min {Rc,Rs} > Rs + Rc/N

#### P22

Consider Figure 1.19(b). Suppose that each link between the server and the
client has a packet loss probability p, and the packet loss probabilities for
these links are independent. What is the probability that a packet (sent by the
server) is successfully received by the receiver? 

p success = (1 - p)^N -2

If a packet is lost in the path
from the server to the client, then the server will re-transmit the packet. On
average, how many times will the server re-transmit the packet in order for
the client to successfully receive the packet?

total transmissions =1/(1 - p)^N -2

average retransmission = (1/(1 - p)^N -2) - 1

#### P23

Consider Figure 1.19(a). Assume that we know the bottleneck link along the
path from the server to the client is the first link with rate Rs bits/sec.
Suppose we send a pair of packets back to back from the server to the client, and there
is no other traffic on this path. Assume each packet of size L bits, and both
links have the same propagation delay dprop.
a. What is the packet inter-arrival time at the destination? That is, how much
time elapses from when the last bit of the first packet arrives until the last
bit of the second packet arrives?

It's L/Rs since packet2 has to wait that the first packet clear the first link.

b. Now assume that the second link is the bottleneck link (i.e., Rc 6 Rs). Is
it possible that the second packet queues at the input queue of the second
link? Explain. 

Yes because when packet 2 will arrive at link2 packet 1 will still be transmitting ?

Now suppose that the server sends the second packet T seconds after sending the first packet. 
How large must T be to ensure no queuing before the second link? Explain

T must be at least L/Rc - L/Rs.

#### P24

You send a stream of packets of size 1000 bits each across a network path from Delhi to Chennai.You find that the one-way delay varies between 40ms (in the absence of any queuing) and 125ms (full queue), with an average
65ms. The transmission rate at the sender is 1 mbit/s; the receiver gets packets at the same rate without any packet loss.

- a) What is the mean number of packets in the queue at the bottleneck link along the path
(assume that any queuing happens at just one switch).

L = a * w

w = 0.065 - 0.04 = 0.025

a = 1mps / 1000 = 1000 packets by seconds

L = 0,025 * 1000 = 25

so the average nubmer of packets in the queue is 25


You now increase the transmission rate to 2 mbits/s.
You find that the receiver gets packets at a rate of 1.6mbits/s.The average queue length does not
change appreciably from before.

-b) What is the packet loss rate at the switch?

p success = 1.6/2 = 80% so p loss = 20%

Also what is the average one way delay now ?

The average delay should be 125ms since we loose packet the queue must be full.

#### P25

Suppose two hosts, A and B, are separated by 20,000 kilometers and are connected by a direct link of R = 5 Mbps. Suppose the propagation speed over the link is 2.5 * 10^8 meters/sec.
- a). Calculate the bandwidth-delay product, R * dprop.
dprop = (20 000 * 1000) / 2.5 * 10^8 = 0,08s

5mps * 0,08s = 400 000 bits = 400Kb

- b). Consider sending a file of 800,000 bits from Host A to Host B. Suppose
the file is sent continuously as one large message. What is the maximum
number of bits that will be in the link at any given time?

Since the bandwidth-delay is 400kb that is the answer.

- c). Provide an interpretation of the bandwidth-delay product.

It's the maximum bits in a link at any given time (the volume of the link).

- d) What is the width (in meters) of a bit in the link? 
Is it longer than a football field?

d = 20 000 * 1000 to get it in metters , b = 400 000

d /b = 50 metters/bit which is not bigger than a football field

- e).Derive a general expression for the width of a bit in terms of the
propagation speed s, the transmission rate R, and the length of the
link m.

m / R * (m/s) = m * s/ R * m = s / R

#### P26

Consider problem P25 but now with a link of R= 1 Gbps.

a. Calculate the bandwidth-delay product, R * dprop.

dprop = (20 000 * 1000) / 2.5 * 10^8 = 0,08s

1Gbps * 0,08s = 80 Mb

b. Consider sending a file of 800,000 bits from Host A to Host B.
Suppose the file is sent continuously as one big message. 
What is the maximum number of bits that will be in the link at any given time?

its 800kbps since 80mb > 800kbps

c. What is the width (in meters) of a bit in the link?

s / R = 2.5 * 10^8 / 1 Gbps = 0,25 bits by metters

#### P27

Consider the scenario illustrated in Figure 1.19(a).
Assume Rs is 20 Mbps, Rc is 10 Mbps, and the server is continuously sending traffic to the client.

Also assume the router between the server and the client can buffer at most
four messages. After how many messages sent by the server will packet loss
starts occurring at the router?

I would say 8 message since 20mps is the double of 10Mps and the q max length is 4

q/ 1 - (rc /rs) = 4/ 1 - (0.5) = 8 messages

#### P28

List one everyday example using layered architecture.

A job lifecycle

apply---------quitting
interview ------  exit interview
onboarding--working---unboarding

apply -> interview->onboarding->->working->unboarding->exit interview-your out of the company each process can be independent and their implementation details change.

#### P29

Suppose there is a 10 Mbps microwave link between a geostationary
satellite and its base station on Earth. Every minute the satellite takes a digital photo and sends it to the base station. Assume a propagation speed
of 2.4 * 10^8 meters/sec.
a. What is the propagation delay of the link?

d = 36 000Km above the earth for a geostationary satellite

s = 2.4 * 10^8 m/s

dprop = d / s

dprop = (36000 * 1000) / 2.4 * 10^8

dprop = 0,15 s

b. What is the bandwidth-delay product, R * dprop?

bandwidth-delay product = R * dprop

bandwidth-delay product = 10 Mbps * 0,15s = 1,5Mb

c. Let x denote the size of the photo. What is the minimum value of x for the
microwave link to be continuously transmitting?

10Mpbs * 60seconds = 600Mb

#### P30

Consider the network topology shown below in Figure 3.
Assume that the processing delay at all nodes is negligible


- a) The sender sends two 1000 byte data packets back-to-back with a negligible inter-packet delay.
The queue has no other packets. What is the time delay between the arrival of the first bit of the second
packet and the first bit of the first packet at the receiver?

Rs = 10^8 * 8 = 800Mbps

L = 1000 * 8 = 8000bits


dtrans1 = L/Rs = 8000bits/8000Mbps = 0,00001s

Rc = 10^6 * 8 = 8Mbps

dtrans2 = L/Rc = 8000 bits/8Mps = 0,001s


the delay is dtrans1 + (dtrans2 - dtrans1) because dtrans1 < dtrans2.

so it become dtrans2 which is 0,001s

- b) The receiver acknowledges each 1000 byte data packet to the sender, and each acknowledgment
has a size A = 100 bytes. What is the minimum possible round trip time between the sender and receiver ?
The round trip time is defined as the duration between the transmission of a packet and the receipt of an
acknowledgment for it.

Rs = 10^8 * 8 = 800Mbps

L1 = 1000 * 8 = 8000bits

dtrans1 = L1/Rs = 8000bits/8000Mbps = 0,00001s


Rc = 10^6 * 8 = 8Mbps

dtrans2 = L1/Rc = 8000 bits/8Mps = 0,001s

first trip = dtrans1 + dprop1 + dtrans2 + dprop2 = 0,00001 + 0,001 + 0,001 + 0,01 = 0,01201s

L2 = 100 * 8 = 800bits

dtrans3 = 800bits/ 8Mps = 0,0001s

dtrans4 = 800bits/ 800Mbps = 0,000001s

second trip = dtrans3 + dprop2 + dtrans4 + dprop1 = 0,0001s + 0,01 + 0,000001 + 0,001 = 0,011101s

round trip = 0,01201 + 0,011101 = 0,023111s = 23,111 ms

#### P31

In modern packet-switched networks, including the Internet, the source host segments long, application-layer messages (for example, an image or a music file)
into smaller packets and sends the packets into the network. The receiver then
reassembles the packets back into the original message. We refer to this process as
message segmentation. Figure 1.27 illustrates the end-to-end transport of a message
with and without message segmentation. Consider a message that is 10^6 bits
long that is to be sent from source to destination in Figure 1.27. Suppose each
link in the figure is 5 Mbps. Ignore propagation, queuing, and processing delays.

- a) Consider sending the message from source to destination without message
segmentation. How long does it take to move the message from the source
host to the first packet switch? Keeping in mind that each switch uses
store-and-forward packet switching, what is the total time to move the
message from source host to destination host?

dtrans = L/R

d end - end = 2(L/R) = 2 (10^6/5Mps) = 2(0,2) = 400ms

- b) Now suppose that the message is segmented into 100 packets, with each
packet being 10,000 bits long. How long does it take to move the first
packet from source host to the first switch?

L/R = 10000/5Mps = 0,002s = 2ms

When the first packet is being
sent from the first switch to the second switch, the second packet is being
sent from the source host to the first switch. At what time will the second
packet be fully received at the first switch?

t = 4ms since it has to wait the transmission of the first packet 2ms then is delay by its 

transmission 2ms, 2ms + 2ms = 4ms

- c) How long does it take to move the file from source host to destination
host when message segmentation is used? Compare this result with your
answer in part (a) and comment.

d end - end = (N + P - 1) * L/R

P = 100

N = 2

L/R = 0,002s

d end - end = (2 + 99) * 0,002 = 101 * 0,002 = 202ms 

it's nearly two time faster because it reduce the time that the second link is idle.

- d) In addition to reducing delay, what are reasons to use message
­ segmentation?

In addition to reducing delay, it enable the sharing of the link easily the second server doesn't have to wait
the first sever to entirely finish to send its packet.

- e) Discuss the drawbacks of message segmentation.

Packet loss can happen when the network is congested and it is slower if there is only 1 link that can
handle the whole message, handling out of order packet , and the memory overhead of having one header by packet.

#### P32

Consider Problem P31 and assume that the propagation delay is 250 ms.
Recalculate the total time needed to transfer the source data with and without
segmentation.

without message segmentation:

d end - end = 2(L/R) = 2 (10^6/5Mps) = 2(200ms + 250) = 900ms

with message segmentation


d end - end = (N + P - 1) * (L/R ) + dprop


d end - end = (2 + 99) * 0,002 = 101 *  (2ms + 250ms) = 702ms 

Is segmentation more beneficial or less if there is propagation
delay?

It is less beneficial for sure, especially when the propagation delay is this outrageous.

#### P33

Consider sending a large file of F bits from Host A to Host B. There are three
links (and two switches) between A and B, and the links are uncongested
(that is, no queuing delays). Host A segments the file into segments of S bits
each and adds 80 bits of header to each segment, forming packets of L = 80 +
S bits. Each link has a transmission rate of R bps. Find the value of S that
minimizes the delay of moving the file from Host A to Host B. Disregard
propagation delay.


d end - end = (N + P - 1) * L/R


L = 80 + S

N = 3

P = F/S

Delay = (3 + F/S - 1) * (80 + S /R ) =  (2 + F/S) * (80 + S /R)

2 S = 80F/S
2S^2 = 80F
S = sqrt(40F)

#### P34

Early versions of TCP combined functions for both forwarding and reliable
delivery. How are these TCP variants located in the ISO/OSI protocol stack?

The early TCP versions  where both doing the work of the network layer (forwarding)
and the one of the transport layer (reliable delivery).

Why were forwarding functions later separated from TCP?

To break the tight coupling of how to forward and how to deliver reliably and be able to change the implementation details of one another without breaking the other.

What were the consequences?

Better separation of concerns and ease of reusabilitiy.

Being able to plug tcp ip or udp with ip without re-implementing ip.
