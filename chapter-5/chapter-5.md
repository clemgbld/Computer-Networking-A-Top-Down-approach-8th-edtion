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

Communication layer: this layer takes care of the communication with the controlled device (the routers) and the SDN.

Network-wide state-management layer:

Network-control application layer:
