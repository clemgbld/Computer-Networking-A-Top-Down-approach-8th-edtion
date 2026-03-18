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

b. One of the header fields in an IP datagram is the time to live (TTL) Which of the following statements best explains the need for this field ?

c. What is the maximum size of data that the application layer can pass on to the TCP layer below ?
