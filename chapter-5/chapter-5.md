# CHAPTER 5: The network layer: control plane

## Review questions

### Section 5.1

#### 1

What is meant by a control plane that is based on per-router control? 
This means the part that compute the forwarding table is directly baked into the router.

In such cases, when we say the network control and data planes are implemented
“monolithically,” what do we mean?

It means that there is no separation physical separation between the control and data planes, they are tightly coupled.

#### 2

What is meant by a control plane that is based on logically centralized
control? In such cases, are the data plane and the control plane implemented
within the same device or in separate devices? Explain.

It means that every routers access the same centralized controller via their control agent (the controller is on the server). In such a case the controller is in separate devices since you can't have a single physical controller for every router.


### Section 5.2

#### 3

Compare and contrast the properties of a centralized and a distributed routing
algorithm. Give an example of a routing protocol that takes a centralized and
a decentralized approach.

A centralized routing algorithm (linked sate) have an entire picture of the network it computes eagerly the shortest path from one node to another and put it in their forwarding table using the Dijkstra algorithm usually. This is great for scoped network and robust to link changes but it is synchronous so the bigger the network the heavier the computation and your waiting time is.It is used by the OSPF protocol inside the ISP AS network.


A decentralized routing algorithm (distance vector) do not have the entire picture of the network it compute the shortest path lazily using the Bellman-Ford algorithm usually, each node exchange their distance vector any time they discover a new neighbor or when there is an update, any time there is an update the node recalculate its forwarding table and dispatch the changes to its neighbor. It is great for big non scoped network because the all nodes converge in an async manner but it is also less robus than the centralized routing because it can suffer of the count to infinity problem when there is a link update. It is used by the BGP protocol an inter AS network protocol.

#### 4

Compare and contrast link-state and distance-vector routing algorithms.

Already done in question 3.

#### 5

What is the “count to infinity” problem in distance vector routing?

It is the problem that occurs when node spread incorrect informations that cascade and increase the count of a path to infinity. It usually happen during a link failure, a node choose another dead route by another router that were already relying on the first one to get to that destination so those nodes will keep sharing update and update their forwarding tables to infinity.

#### 6

Is it necessary that every autonomous system use the same intra-AS routing
algorithm? Why or why not?

No it is not necessary every intra-AS routing can use their own routing algorithm (chosen for their needs) and use an inter routing algorithm to communicate with other AS.


### Section 5.3-5.4

#### 7

Why are different inter-AS and intra-AS protocols used in the Internet?

Because they all have their advantages and drawbacks and the best protocol must be choose according to the network that you need to manage.
like i said in question 3 intra-AS are more scoped and have different needs than a big inter-AS network for example.
The protocol is chosen according to these 3 pillars policy, performance and scale.

#### 8

True or false: When an OSPF route sends its link state information, it is sent
only to those nodes directly attached neighbors. Explain.

False.

Since OSPF use a link state algorithm and that each router construct a topological map and then run a Dijkstra algorithm to determine the shortest-path tree to all subnet then when an OSPF route sends its link state information to all nodes in the network since each router needs the entire view of the network to correctly build its forwarding table.

#### 9

What is meant by an area in an OSPF autonomous system? 

An area is a set of routers inside an OPSF AS, it communicate with other area via their border routers.

Why was the concept of an area introduced?

It was introduced to help manage big intra-network, the link state algorithm is less costly to run within an area than within a whole big network.

#### 10

Define and contrast the following terms: subnet, prefix, and BGP route.


subnet: A subnet (subnetwork) is a range of address, you can evaluate the number of addresses by reading at the CIDR notation prefix x.x.x.x/x

Analogy: a set of room in a building, let's say a floor where the floor represent a department

prefix: A prefix defined the address range, it is often represented by the CIDR notation prefix x.x.x.x/x.

Analogy: the number of the floor.


BGP route: A BGP route is a route that connect two AS (eBGP) or two router (iBGP), the route have a cost.
The route is an entry in the forwarding table that tells the world of to reach a router.
Route = prefix + attributes (such as AS_PATH and NEXT_HOP).

Analogy: the floor number + the room number.

#### 11

How does BGP use the NEXT-HOP attribute? 

It use to know the left most router ip of the next AS

How does it use the AS-PATH attribute?

It use it to know which AS to traverse before reaching the destination router.


#### 12

Describe how a network administrator of an upper-tier ISP can implement
policy when configuring BGP.

It can configure its border routers either via a SDN or every border router if the controllers are embeded.
it then set up the local attributes as they want using route selection and route advertisement.

Route selection: they prefer to use their own links as much as possible to not pay the cost of a providers link.

Route advertisement: they accept to forward packet from a source or destination or both that are paying customer only.

#### 13

True or false: When a BGP router receives an advertised path from its neigh-
bor, it must add its own identity to the received path and then send that new
path on to all of its neighbors. Explain.

False

it only it only add the AS-PATH when it is when this is a link that connect a border router to an external AS border router.
And it only send that new path when the policy allow it to do that.


### Section 5.5


#### 14

Describe the main role of the communication layer, the network-wide state-
management layer, and the network-control application layer in an SDN
controller. 

Communication layer: this layer takes care of the communication with the controlled device (the routers) and the SDN via protocols.
The api used is called "southbound".

Network-wide state-management layer: this layer is the heart of the control (it's operating system) that contains the flow tables for the different devices and read/write to them.

Network-control application layer: this layer enable the controller to interact with network-control applications through its "northbound" api.
This api can read/write network state and flow table within the Network-wide state management layer.

#### 15

Suppose you wanted to implement a new routing protocol in the SDN control
plane. At which layer would you implement that protocol? Explain.

At the Network-control application layer because it is an independent application that would need to communicate with the Network-wide state-management layer to read/write to the flow tables.

#### 16

What types of messages flow across an SDN controller’s northbound and
southbound APIs?

For example a device communicate via the southbound api to the SDN controller that a link went down, the SDN communicate to the routing application via the northbound api that the link went down, the routing algorithm recompute the paths for the devices and then again via the northbound api transmit the infos to the controllers which update it's flow tables then it transmit back the new path when a devices request it via the southbound api.

Who is the recipient of these messages sent from the
controller across the southbound interface, and who sends messages to the
controller across the northbound interface?

recipient for the message sent by the controller via southbound api = devices
sender of the message to the controller across the northbound api = network applications such as routing, access control application and load balancer.

#### 17

Describe the purpose of two types of OpenFlow messages (of your choosing)
that are sent from a controlled device to the controller. 

- Port-status: This message is used by a switch to inform the controller of a change in port status.

- Packet-in: send a packet to the controller that didn't match any flow tables entry in the switch for additional processing.


Describe the purpose
of two types of Openflow messages (of your choosing) that are send from the
controller to a controlled device.

- Read-State: to collect stats and counter values from the switch.

- Modify-State: to add/delete or modify entries in the switch's flow table, and to set switch port properties.

#### 18

What is the purpose of the service abstraction layer in the OpenDaylight SDN
controller?

It's purpose is to abstract which protocol is used to communicate with a device.

### Section 5.6-5.7

#### 19

Names four different types of ICMP messages

Type 0 = ping response
Type 8 = ping request
Type 11 = TTL expired
Type 4 = source quench (congestion control)

#### 20

What two types of ICMP messages are received at the sending host executing
the Traceroute program?

Type 11, code 0 = TTL expired
Type 3, code 3 = port unreachable

#### 21

Define the following terms in the context of SNMP: managing server,
managed device, network management agent and MIB

Managing server: An application that has the purpose to be able to initiate actions to configure, monitor and control the network's maanged devices. A managed network can have several of them.

Managed device: Any device (router host etc...) belonging to a manage network, the device itself can have many configurable components.

Network Management agent: a software process inside the managed device that enable the communication between the managed device and the managed server.

MIB: Management Information Base where is stored the info of the managed devices. this base can be queried by network admin via the Simple Network Management Protocol (SNMP). An MIB is often vendor specific.

#### 22

What are the purposes of the SNMP GetRequest and SetRequest messages?

- GetRequest get an info contained in the MIB of a managed device.
- SetRequest add/delete or update an info in the MIB of a managed device.

#### 23

What is the purpose of the SNMP trap message?

A trap message is an unrequested message sent by the network Management agent inside the managed device to the managing server to notify the admin about something.

## Problems

#### 1

Looking at Figure 5.3, enumerate the paths from y to u that do not contain
any loops.

y -> x -> w -> v -> u
y -> x -> w -> u
y -> x -> v -> w -> u
y -> x -> v -> u
y -> x -> u
y -> w -> x -> v -> u
y -> w -> x -> u
y -> w -> v -> u
y -> w -> v -> x -> u
y -> w -> u
y -> z -> w -> x -> v -> u
y -> z -> w -> x -> u
y -> z -> w -> v -> u
y -> z -> w -> v -> x -> u
y -> z -> w -> u

#### 2

Repeat Problem P1 for paths from x to z, z to u, and z to w

x -> z:

x -> y -> w -> z
x -> y -> z
x -> w -> z
x -> w -> y -> z
x -> v -> w -> z
x -> v -> w -> y -> z
x -> v -> u -> w -> z
x -> v -> u -> w -> y -> z
x -> u -> v -> w -> z
x -> u -> v -> w -> y -> z
x -> u -> w -> z
x -> u -> w -> y -> z

z -> u:

z -> w -> x -> v -> u
z -> w -> x -> u
z -> w -> v -> u
z -> w -> v -> x -> u
z -> w -> u
z -> w -> y -> x -> v -> u
z -> w -> y -> x -> u
z -> y -> x -> w -> v -> u
z -> y -> x -> w -> u
z -> y -> x -> v -> w -> u
z -> y -> x -> v -> u
z -> y -> x -> u
z -> y -> w -> x -> v -> u
z -> y -> w -> x -> u
z -> y -> w -> v -> u
z -> y -> w -> v -> x -> u
z -> y -> w -> u

z -> w:

z -> w
z -> y -> x -> w
z -> y -> x -> v -> w
z -> y -> x -> v -> u -> w
z -> y -> x -> u -> v -> w
z -> y -> x -> u -> w
z -> y -> w

#### 3

Consider the following network. With the indicated link costs, use Dijkstra’s
shortest-path algorithm to compute the shortest path from x to all network nodes.
Show how the algorithm works by computing a table similar to Table 5.1.

Node        | Distance         | Parent
x             0                   /
y             6                   x
z             8                   x
v             3                   x
w             6                   x
u             6                   v
t             7                   v

#### 4

Consider the network shown in Problem P3. Using Dijkstra’s algorithm, and
showing your work using a table similar to Table 5.1, do the following:

a - Compute the shortest path from t to all network nodes.

Node        | Distance         | Parent
x             7                   v
y             7                   t
z             15                  x
v             4                   t
w             5                   u
u             2                   t
t             0                   / 


b - Compute the shortest path from u to all network nodes.

Node        | Distance         | Parent
x             6                   v
y             9                   t
z             14                  x
v             3                   u
w             3                   u
u             0                   /
t             2                   u                  


c - Compute the shortest path from v to all network nodes.

Node        | Distance         | Parent
x             3                   v
y             8                   v
z             11                  x 
v             0                   /
w             4                   v
u             3                   v
t             4                   v                  


d - Compute the shortest path from w to all network nodes.

Node        | Distance         | Parent
x             6                   w
y             12                  x or v or t
z             14                  x
v             4                   w
w             0                   /
u             3                   w
t             5                   u                  

e - Compute the shortest path from y to all network nodes.

Node        | Distance         | Parent
x             6                   y
y             0                   /
z             12                  y
v             8                   y
w             12                  x or v
u             9                   t
t             7                   y                  

f - Compute the shortest path from z to all network nodes.

Node        | Distance         | Parent
x             8                   z
y             12                  z
z             0                   /
v             11                  x
w             14                  x 
u             14                  v
t             15                  v                  

#### 5

Consider the network shown below, and assume that each node initially
knows the costs to each of its neighbors. Consider the distance-vector algo-
rithm and show the distance table entries at node z.

z = 0
u = 6 z -> x -> v -> u
v = 5 z -> x -> v
y = 5 z -> x -> y
x = 2 z -> x

#### 6

Consider a general topology (that is, not the specific network shown above) and a
synchronous version of the distance-vector algorithm. Suppose that at each itera-
tion, a node exchanges its distance vectors with its neighbors and receives their
distance vectors. Assuming that the algorithm begins with each node knowing
only the costs to its immediate neighbors, what is the maximum number of itera-
tions required before the distributed algorithm converges? Justify your answer.

Given that N is the number of nodes the maximum number of iterations required before the distributed algorithm converges if synchronous is N - 1 because it would take N - 1 hop to spread it's table to the nodes that are the most far away from each other.

#### 7

Consider the network fragment shown below. x has only two attached neigh-
bors, w and y. w has a minimum-cost path to destination u (not shown) of 5,
and y has a minimum-cost path to u of 6. The complete paths from w and y
to u (and between w and y) are not shown. All link costs in the network have
strictly positive integer values.

a - Give x’s distance vector for destinations w, y, and u.

x distance vector for w = 2
x distance vector for y = 4
x distance vector for u = 7

b - Give a link-cost change for either c(x,w) or c(x,y) such that x will inform
its neighbors of a new minimum-cost path to u as a result of executing the
distance-vector algorithm.

if c(x,w) changes from 2 to 1 then it will inform its neighbors which themselves will inform u.


c - Give a link-cost change for either c(x,w) or c(x,y) such that x will not
inform its neighbors of a new minimum-cost path to u as a result of
executing the distance-vector algorithm.


if c(x, y) changes from 5 to 6 x will not inform its neighbors since the cost is higher than 4 to reach y.

#### 8

Consider the three-node topology shown in Figure 5.6. Rather than having
the link costs shown in Figure 5.6, the link costs are c(x,y) = 3, c(y,z) = 6,
c(z,x) = 4. Compute the distance tables after the initialization step and after
each iteration of a synchronous version of the distance-vector algorithm (as
we did in our earlier discussion of Figure 5.6).

x

  x y z     x y z 
x 0 3 4   x 0 3 4
y / / /   y 3 0 6
z / / /   z 4 6 0

y

  x y z     x y z 
x / / /   x 0 3 4
y 3 0 6   y 3 0 6
z / / /   z 4 6 0

z

  x y z     x y z 
x / / /   x 0 3 4
y / / /   y 3 0 6
z 4 6 0   z 4 6 0

#### 9

Consider the count-to-infinity problem in the distance vector routing. Will
the count-to-infinity problem occur if we decrease the cost of a link? Why?
No it won't happen since good news travel fast and bad news travel slow because it will take (n - 1) iteration to reach the most far node.
If a the cost of a link increase it is (new cost - old cost) / step size where step size is the cost of the link of the neighbor that route back trough you. 

How about if we connect two nodes which do not have a link?

if we connect a new node that doesn't have a link it will take (n - 1) iterations to reach the most far node.
So it won't occur.

#### 10

Argue that for the distance-vector algorithm in Figure 5.6, each value in the
distance vector D(x) is non-increasing and will eventually stabilize in a finite
number of steps.

As soon as c(x,y) will stay 2 but in 2 iterations c(x,z) will go from 7 to 3 and it will achieve the optimal path and stabilize since the network as finite number of nodes.

#### 11

Consider Figure 5.7. Suppose there is another router w, connected to router
y and z. The costs of all links are given as follows: c(x,y) = 4, c(x,z) = 50,
c(y,w) = 1, c(z,w) = 1, c(y,z) = 3. Suppose that poisoned reverse is used in
the distance-vector routing algorithm.

a - When the distance vector routing is stabilized, router w, y, and z inform their
distances to x to each other. What distance values do they tell each other?

c(w, x) = 5
c(z,x) = 7
c(y,x) = 4

b - Now suppose that the link cost between x and y increases to 60. Will there be
a count-to-infinity problem even if poisoned reverse is used? Why or why not?

yes there will be a count to infinity problem it will slowly increase to 50 before the loop breaks.

If there is a count-to-infinity problem, then how many iterations are needed for

50 - 6 / 2 = 22

c - How do you modify c(y,z) such that there is no count-to-infinity problem
at all if c(y,x) changes from 4 to 60?

x will first propagate propagate c(z,y) = > 50 

#### 12

Describe how loops in paths can be detected in BGP.

if the same AS id is in the path

#### 13

Will a BGP router always choose the loop-free route with the shortest ASpath
length? Justify your answer

No BGP router don't optimize performance but for the AS interest of the ISP owning the router.

#### 14

Consider the network shown below. Suppose AS3 and AS2 are running
OSPF for their intra-AS routing protocol. Suppose AS1 and AS4 are running
RIP for their intra-AS routing protocol. Suppose eBGP and iBGP are used
for the inter-AS routing protocol. Initially suppose there is no physical link
between AS2 and AS4.

- a Router 3c learns about prefix x from which routing protocol: OSPF, RIP,
eBGP, or iBGP?

eBGP

- b Router 3a learns about x from which routing protocol?

IBGP

- c Router 1c learns about x from which routing protocol?

eBGP

- d Router 1d learns about x from which routing protocol?

IBGP

#### 15

Referring to the previous problem, once router 1d learns about x it will put an
entry (x, I) in its forwarding table.

a - Will I be equal to I1 or I2 for this entry? Explain why in one sentence.

I1, since it got notified by 1c and the shortest path is to take I1.

b - Now suppose that there is a physical link between AS2 and AS4, shown
by the dotted line. Suppose router 1d learns that x is accessible via AS2 as
well as via AS3. Will I be set to I1 or I2? Explain why in one sentence.

I2 since the path is shorter.

c - Now suppose there is another AS, called AS5, which lies on the path
between AS2 and AS4 (not shown in diagram). Suppose router 1d learns
that x is accessible via AS2 AS5 AS4 as well as via AS3 AS4. Will I be
set to I1 or I2? Explain why in one sentence.

I1 since AS3 AS4 is shorter than AS2 AS5 AS4

#### 16

Consider the following network. ISP B provides national backbone service
to regional ISP A. ISP C provides national backbone service to regional
ISP D. Each ISP consists of one AS. B and C peer with each other in two
places using BGP. Consider traffic going from A to D. B would prefer
to hand that traffic over to C on the West Coast (so that C would have
to absorb the cost of carrying the traffic cross-country), while C would
prefer to get the traffic via its East Coast peering point with B (so that B
would have carried the traffic across the country). What BGP mechanism
might C use, so that B would hand over A-to-D traffic at its East Coast
peering point? To answer this question, you will need to dig into the BGP
specification.

Answer: ISP C would use the Multi-Exit Discriminator (MED) attribute.Justification: C can advertise routes to destination D with a low MED value at the East Coast peering point and a high MED value at the West Coast peering point. Because BGP routers prefer the path with the lowest MED value when all other attributes are equal, this forces ISP B to hand over the traffic on the East Coast. Alternatively, C could use AS-PATH prepending on the West Coast to make that path look artificially longer and less desirable to B.

#### 17

In Figure 5.13, consider the path information that reaches stub networks W,
X, and Y. Based on the information available at W and X, what are their
respective views of the network topology? Justify your answer. The topology
view at Y is shown below.

[answer](./p-17.png)

#### 18

Consider Figure 5.13. B would never forward traffic destined to Y via X based
on BGP routing. But there are some very popular applications for which data
packets go to X first and then flow to Y. Identify one such application, and
describe how data packets follow a path not given by BGP routing.

The application is P2P.

#### 19

In Figure 5.13, suppose that there is another stub network V that is a cus-
tomer of ISP A. Suppose that B and C have a peering relationship, and A is
a customer of both B and C. Suppose that A would like to have the traffic
destined to W to come from B only, and the traffic destined to V from either
B or C. How should A advertise its routes to B and C? What AS routes does
C receive?


[answer](./p-19.png)

#### 20

Suppose ASs X and Z are not directly connected but instead are connected
by AS Y. Further suppose that X has a peering agreement with Y, and that Y
has a peering agreement with Z. Finally, suppose that Z wants to transit all
of Y’s traffic but does not want to transit X’s traffic. Does BGP allow Z to
implement this policy?

Yes it does

#### 21

Consider the two ways in which communication occurs between a managing
entity and a managed device: request-response mode and trapping. What are
the pros and cons of these two approaches, in terms of (1) overhead, (2) noti-
fication time when exceptional events occur, and (3) robustness with respect
to lost messages between the managing entity and the device?

1) overhead here trapping wins since there is only one request  sent via UDP and one response, request response use TCP so handshaking + the request + the response is more overhead.

2) here again trapping wins since it will have the exceptional events in real time, with the request response model the managed server will only have the exceptional when the it send a request to the managed device.

3) robustness, here request-response wins since the notification sent from the managed device is unreliable since it uses UDP, the request-response model use TCP so it can retry and alert when something wrong happens.

#### 22

In Section 5.7, we saw that it was preferable to transport SNMP messages in
unreliable UDP datagrams. Why do you think the designers of SNMP chose
UDP rather than TCP as the transport protocol of choice for SNMP?
The designers of SNMP choose to prioritize speed over robustness.

### ICMP socket programming

(program)[./icmp_pinger.py]

### Routing algorithm assignment

(program)[./distance_vector.c]
