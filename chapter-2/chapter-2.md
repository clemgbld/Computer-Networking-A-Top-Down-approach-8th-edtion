# CHAPTER 2

## Review Questions

### section 2.1

#### 1

Summarize inter-process communication?

inter-process communication is two are more processes (separate program with they how heap (memory) and stack) exchanging messages with an application protocol if they not on the same machine, if they are in the same machine that is still inter-process communication that can exchange message with shared memory, Unix domain sockets or pipes.

Explain deadlocks and timeout.

Deadlock happens when two threads need a resource but thread 1 has the resource that thread 2 needs and thread 2 has the resource that thread 1 needs so the program is stuck.

A timeout is when something take too much time to execute thus a detection happen and the client get notified either by an error with a specific http code for example if using http.

#### 2

State IPC paradigms and implementation.

TCP services a client and a server communicating when you do a transfer to a beneficiary with your bank app for example because it has to be reliable.

UDP services a call on an application like Skype, because a lost packet is not the end of the world the important thing is to maintain a connection.

Same machine services two program on two different processes that exchange data via Shared memory or an other means.

Also, are function callback and inter-process communication same ?

Not quite since inter-process communication means two isolated island aka process communicating together, a callback is most of the in the same process than with the code that the it interacts with.

#### 3

Explain how IP protects data on the network ?

If we are talking about an application protocol like HTTPS, Encryption, before the data leave the host it is encrypted and when before the receiver receive the message it is decrypted. It is done at the TLS layer.

The IP protocol doesn't protect the data on the network itself.

#### 4

How does TCP protocol provide reliability ?

- first initial handshakes to establish a reliable connection between client and servers.
- reliable transfer of data: detect lost packet and ask them back, reorder packets etc...
- congestion-control mechanism

Write down the name of services provided by TCP ? 

- Connection oriented service.
- Reliable data transfer service.
- Congestion-control service.

Known port used by TCP ?

Port 80.

#### 5

Do port addresses need to be unique ?

Yes

Why or Why not ?

Because if a process is already running on a port another cannot.

Because a machine doesn't have as many addresses than there is IPs on internet.

#### 6

What are the factors that influence round trip time (RTT). 

The different delays (processing, propagation, qeueing and transmission)

Why is calculation of RTT advantageous.

To be able to discover the shortest path.

Also what are the measures to reduce RTT.

Persistent connection , pluging a CDN at an IXP or "Bring it home" to a local ISP , monitor RTT to be able to redirect the user to a closer server etc...

#### 7

Referring to Figure 2.4, we see that none of the applications listed in Figure
2.4 requires both no data loss and timing. Can you conceive of an application
that requires no data loss and that is also highly time-sensitive?

I don't think so, that is the kind the trade-off you either achieve the time-sensitive or the data loss requirement. Maybe an application withing a special network that is dedicated for it like a Surgeon robot can achieve this.

#### 8

List the four broad classes of services that a transport protocol can provide.
For each of the service classes, indicate if either UDP or TCP (or both) pro-
vides such a service.

Connection oriented service = TCP
Data transport reliability = TCP
Congestion-control service = TCP
Connectionless oriented service = UDP
Best effort service = UDP

#### 9

Recall that TCP can be enhanced with TLS to provide process-to-process
security services, including encryption. Does TLS operate at the transport
layer or the application layer?

Application layer.

If the application developer wants TCP to be
enhanced with TLS, what does the developer have to do?

The user has to use the right protocol, for example HTTPS instead of HTTP, the developer use the tls lib.

### section 2.2 - 2.5

#### 10

A response is a message that the client receive after a request.

Status code 2XX when the request has been correctly processed, 3XX for redirection, 4XX client side error (bad usage of the service), 5XX server error.

#### 11

What are the different layers in a distributed system, where cache can be implemented.

You can implement a cache on the Frontend side as well as on the Server side usually (through a proxy that sits on another server, can be a CDN).

What is cache invalidation ?

It is the action of removing stale data from the cache.

What are the three main methods of cache invalidation ?

- TTL
- Purge
- Write-Through / Write-Back

#### 12

Are email addresses case sensitive ? 

No

What are the resolved limiting factors of simple mail transfer protocol (SMTP)

It is asynchronous (PUSH protocol) because it is using queues so you may not get your mail as soon as the sender send it or the mail may never arrived (in that case the mail server will try to resend it x amount of time later.), and you can only send text only.

How to check if an email address exists without sending an email ?

With telnet we can try to do an handshakes with a hello message (it won't send a mail)

#### 13

Describe how Web caching can reduce the delay in receiving a requested object. 
Assuming the cache is nearer the client than the server, Web caching reduce the delay by directly giving the client the response in a constant time rather than hitting the server again for the response, it also reduce the bandwidth on the access link, which prevent the network to be congested.

Will Web caching reduce the delay for all objects requested by a user
or for only some of the objects? Why?

Only for some object because if the requested object is not in the cache, the request will be forwarded to the server, then the cache will put the response in time before sending it to the client.

#### 14

Telnet into a Web server and send a multiline request message. Include in
the request message the If-modified-since: header line to force a
response message with the 304 Not Modified status code.

#### 15

Are there any constraints on the format of the HTTP body?
The HTTP body can be anything

What about the email message body sent with SMTP? 
The email body sent with SMTP has to be text , SMTP works with the ASCII format

How can arbitrary data be transmitted
over SMTP?
MIME (Multipurpose Internet Mail Extensions)

#### 16

Suppose Alice, with a Web-based e-mail account (such as Hotmail or Gmail),
sends a message to Bob, who accesses his mail from his mail server using
IMAP. Discuss how the message gets from Alice’s host to Bob’s host. Be
sure to list the series of application-layer protocols that are used to move the
message between the two hosts.

- Alice sends a message via SMTP to Bob (if from a desktop app or use HTTPS if she sends it from her browser which will then use SMTP).
- Bob access his mail via a client (Outlook for example), the client has a persistent connexion with the IMAP server that notifies him when a new mail arrived via the IMAP protocol.
- if it's client is closed he will see the mail of Alice when he will open it, if it is already open he will get a notification that a new mail arrived and the mail will be pushed on its client.

Application-layer flow:

- Alice to server: HTTPS
- Server to server: SMTP
- Server to Bob: IMAP

#### 17

What are the different DNS zones ?
- Root DNS servers
- Top-level domain (TLD) servers
- Authoritative DNS servers
What is caching only server ?

It is a server explicitly used for caching only (the server is not a source of truth).

#### 18

What is the HOL blocking issue in HTTP/1.1? 
In HTTP/1.1 message are sent one after another which limit the throughput because each message in the queues must wait for the other to be propagated.
How does HTTP/2 attempt to solve it?

HTTP/2 attempt to solve it by using framing / multiplexing which just means that it interleave the packets of the different messages rather that just sending one message after another like it was the case with HTTP/1.1.

#### 19

Why are MX records needed? Would it not be enough to use a CNAME
record? (Assume the email client looks up email addresses through a Type A
query and that the target host only runs an email server.)

MX records are needed to allow you web server and mail server to have the same alias.
It is technically possible to get an Email address IP with a type A, but if you later add a Web-server with the same alias you will get the IP address of the Web-server so it is not a good design choice.

if you use a CNAME for mail server:

- You lose the ability to have Priority (Multiple mail servers for backup).

- You lose the ability to have different destinations for Web and Mail.

#### 20

How does DNS lookup process works ?

Iterative or recursive query or both are made between the 3 layers of DNS.

The local DNS will first get the TLD DNS IP address through the ROOT DNS then the authoritative IP by asking the TLD DNS server then the required hostname by asking the authoritative DNS server.

Anyone of those steps can be skipped faster thanks to caching, thus the ROOT DNS server is rarely queried.

Why do we use DNS ?

To have more human friendly addresses for our website, IP addresses would be a nightmare to remember. A DNS is basically a distributed registry.


### section 2.5

#### 21

What are the three architectures available in peer to peer applications ?

- Mediated architecture (P2P systems but not decentralized, there is still one server with the data, the peers that are downloading just help with the load)

- Pure P2P architecture (There is no central servers, all peers keep their own data source)

- Hybrid architecture (It is a mix of the two above architectures, ultra-peers are connected togehter with a Pure P2P architecture approach while the other peers are connected to an ultra-peer like in the Mediated architecture approach)

#### 22

Consider a new peer Alice that joins BitTorrent without possessing any chunks.
Without any chunks, she cannot become a top-four uploader for any of the other
peers, since she has nothing to upload. How then will Alice get her first chunk?

Alice will get her first chunks by asking for a list of peers from a Tracker or from bootstrapped node in the modern Bitorrent architecture.
she will then start a concurrent TCP connections with the peers and get her first chunk.

#### 23

Summarize bit torrent and difference between seed, leecher, peer.

Bitorrent is P2P application protocol.
That allows peer to get file from each other, the more peers there is in the torrent, the faster the file downloading will be because instead of solely  downloading from one centralized server, each peer in the torrent acts as a uploader for the other peers.
It use an algorithm named "Tit-for-Tat" that prevents selfish behavior (only downloading and not uploading to your peers).

A seed is an uploader that has the entire file but stats in the torrent to serve the other peers, a leecher is a downloader who have nothing to upload to its peers (in the technical term a leecher is just a node that doesn't have the full file yet), if it the leecher keep downloading but not uplading  it will be "choked" by its peers which mean that they stop uploading for him, at first a peer is a leecher but the "Tit-for-Tat" algorithm handle that edge cases by optimistically "unchocking" the peer.
A peer is a node that download and upload at the same time.


### section 2.6

#### 24

How does a content delivery network (CDN) work ?
CDN are geographically distributed caches of static contents (images, videos etc...).
the client will request the content from the CDN, if the CDN does have it, it will request it from the data center and cache it locally.
There is RTT calculation done to determine which CDN the client will hit for advance CDN in advanced systems.
Are all CDN's equal ?
No CDN will not have the same content based on its geography.
On the basis of how content is cached & refreshed what are the two kinds of CDN.

- Bring it home CDN: that are CDN plugged at IXP.
- enter deep: CDN: that are CDN plugged at the leaf of the network to local ISP
- PULL CDN refreshed it's content periodically by pulling the new content from the nearer data center. (example Youtube)
- PUSH CDN get data from the nearer server during off peak hours. (example Netflix)

#### 25

Besides network-related considerations such as delay, loss, and bandwidth
performance, there are other important factors that go into designing a CDN
server selection strategy. What are they

How will you refresh the content of your CDN PULL Vs PUSH.


### section 2.7

#### 26

In Section 2.7, the UDP server described needed only one socket, whereas
the TCP server needed two sockets. Why? If the TCP server were to support
n simultaneous connections, each from a different client host, how many
sockets would the TCP server need?

The TCP server would need N + 1 sockets, 1 for handshaking and establish the connection between the client and the client socket, the other n sockets are the client sockets.

#### 27

For the client-server application over TCP described in Section 2.7, why
must the server program be executed before the client program? 
Because if the server program is not executed, the client socket can't connect to it.

For the client-server application over UDP, why may the client program be executed
before the server program?

Because UDP doesn't use handshaking.

## Problems
