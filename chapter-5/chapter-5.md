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
z             /                   /
v             0                   /
w             4                   v
u             3                   v
t             4                   v                  


d - Compute the shortest path from w to all network nodes.

e - Compute the shortest path from y to all network nodes.

f - Compute the shortest path from z to all network nodes.
