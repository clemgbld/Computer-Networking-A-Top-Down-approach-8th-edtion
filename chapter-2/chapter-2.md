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

### 1

If TCP round trip time, RTT is currently 30m sec and the following acknowledgment comes in after 26, 32 & 24 m sec respectively, what is the new RTT estimate ? (Use α  = 0.9)

EstimatedRTT = (1 - α) *  EstimatedRTT + α  * SampleRTT

EstimatedRTT1 = 0.1 * 30ms + (0.9 * 26) = 26.4ms
EstimatedRTT 2 = 0.1 * 26.4 + (0.9 * 32) = 31.44ms
EstimatedRTTLast = 0.1 * 31.44 + (0.9 * 24) = 24.744 ms

### 2

SMS, iMessage, Wechat, and WhatsApp are all smartphone real-time mes-
saging systems. After doing some research on the Internet, for each of these
systems write one paragraph about the protocols they use. Then write a para-
graph explaining how they differ.

- 1. SMS (The Signaling Approach)
SMS is an outlier. It uses the Mobile Application Part (MAP) protocol, which is part of the SS7 suite. It doesn't use the Internet stack; it "hitches a ride" on the control signals used to manage cellular calls.

- 2. WhatsApp (The Evolution of XMPP)
WhatsApp originally started using XMPP (Extensible Messaging and Presence Protocol), which is an XML-based protocol. However, they heavily modified it into a binary format to save data.

Security: They use the Signal Protocol to provide End-to-End Encryption (E2EE). Even though it runs over a TCP socket, the "Application" layer handles the encryption keys.

- 3. iMessage (The Push Approach)
Apple uses a proprietary protocol that connects to the Apple Push Notification service (APNs).

Mechanism: When you send an iMessage, it is wrapped in TLS and sent over a TCP connection to Apple’s servers. Apple then uses its push service to "wake up" the recipient’s phone and deliver the message.

- 4. WeChat (The "Everything App" Protocol)
WeChat uses a custom protocol called MMP (Mobile Messaging Protocol) and a security layer called MMTLS (a modified version of TLS 1.3).

The core difference is that MAP are not secured because it doesn't encrypt data while the other protocols does.

### 3

Assume you open a browser and enter http://yourbusiness.com/about.html in the address bar. 
What happens until the webpage is displayed? Provide details about the protocol(s) used and a high-level
description of the messages exchanged.

it will make an HTTP GET REQUEST to http://yourbusiness.com/about.html that will hit a DNS local server that will hit a DNS root server to get the IP address of a TLD DNS, then the TLD DNS server will be hit to get the IP address of the authoritative DNS, the authoritative DNS will be hit to get the target IP address, a TCP connection will be opened before the client and the server (3 ways handshaking) and then an HTTP GET request will be forwarded to the IP address/about.html of the server in order to give back a HTTP response with the HTML in the body.

### 4

Consider the following string of ASCII characters that were captured by
Wireshark when the browser sent an HTTP GET message (i.e., this is the
actual content of an HTTP GET message). The characters <cr><lf> are
carriage return and line-feed characters (that is, the italized character string
<cr> in the text below represents the single carriage-return character that was
contained at that point in the HTTP header). Answer the following questions,
indicating where in the HTTP GET message below you find the answer.

GET /cs453/index.html HTTP/1.1<cr><lf>Host: gai
a.cs.umass.edu<cr><lf>User-Agent: Mozilla/5.0 (
Windows;U; Windows NT 5.1; en-US; rv:1.7.2) Gec
ko/20040804 Netscape/7.2 (ax) <cr><lf>Accept:ex
t/xml, application/xml, application/xhtml+xml, text
/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5
<cr><lf>Accept-Language: en-us,en;q=0.5<cr><lf>Accept-
Encoding: zip,deflate<cr><lf>Accept-Charset: ISO
-8859-1,utf-8;q=0.7,*;q=0.7<cr><lf>Keep-Alive: 300<cr>
<lf>Connection:keep-alive<cr><lf><cr><lf>

What is the URL of the document requested by the browser?

http://gaia.cs.umass.edu/cs453/index.html

What version of HTTP is the browser running? 

HTTP/1.1

Does the browser request a non-persistent a  connection or a persistent connection ?

A Persistent connection.

What is the IP address of the host on which the browser is running?

There is no IP in the provided response, all it know is that the host is a Windows.

What type of browser initiates this message ?

The browser is Mozilla Netscape 7.2

Why is the browser type needed in an HTTP request message ?

Probably for compatibility and optimization reasons.

### 5

The text below shows the reply sent from the server in response to the HTTP
GET message in the question above. Answer the following questions, indicating where in the message below you find the answer.

HTTP/1.1 200 OK<cr><lf>Date: Tue, 07 Mar 2008
12:39:45GMT<cr><lf>Server: Apache/2.0.52 (Fedora)
<cr><lf>Last-Modified: Sat, 10 Dec2005 18:27:46
GMT<cr><lf>ETag: ”526c3-f22-a88a4c80”<cr><lf>Accept-
Ranges: bytes<cr><lf>Content-Length: 3874<cr><lf>
Keep-Alive: timeout=max=100<cr><lf>Connection:
Keep-Alive<cr><lf>Content-Type: text/html; charset=
ISO-8859-1<cr><lf><cr><lf><!doctype html public ”-
//w3c//dtd html 4.0transitional//en”><lf><html><lf>
<head><lf> <meta http-equiv=”Content-Type”
content=”text/html; charset=iso-8859-1”><lf> <meta
name=”GENERATOR” content=”Mozilla/4.79 [en] (Windows NT
5.0; U) Netscape]”><lf> <title>CMPSCI 453 / 591 /
NTU-ST550ASpring 2005 homepage</title><lf></head><lf>
<much more document text following here (not shown)>


-   Was the server able to successfully find the document or not?
Yes the document was successfully found, 

What time was the document reply provided?

Tue, 07 Mar 2008 12:39:45GMT

- When was the document last modified?
Sat, 10 Dec2005 18:27:46 GMT
- How many bytes are there in the document being returned?
3874 bytes
- What are the first 5 bytes of the document being returned? Did the server
agree to a persistent connection?

the first 40 chars : <!doctype html public ”-//w3c//dtd html

Yes the server agreed to a persistent connection

### 6

Obtain the HTTP/1.1 specification (RFC 2616). Answer the following
questions:
- Explain the mechanism used for signaling between the client and server
to indicate that a persistent connection is being closed. 
Connection: close in the header
Can the client, the server, or both signal the close of a connection?
the client open a the connection and can close it if the server take too much time to answer, and can ask to keep it alive , the server then decide to either keep it alive or close it when replying.
- What encryption services are provided by HTTP?
Using TLS it encrypt data at the application layer when using https and the receiver decrypt the packets as well at the application layer.
- Can a client open three or more simultaneous connections with a given
server?
Yes a client can open as many concurrent connection than the server can handle.
- Either a server or a client may close a transport connection between them
if either one detects the connection has been idle for some time. Is it
possible that one side starts closing a connection while the other side is
transmitting data via this connection? Explain.
Yes it is possible for example if the client pass a timeout info in the header, if the server doesn't reply fast enough the client can close the connection.

### 7

Suppose within your Web browser, you click on a link to obtain a Web page.
The IP address for the associated URL is not cached in your local host, so
a DNS lookup is necessary to obtain the IP address. Suppose that n DNS
servers are visited before your host receives the IP address from DNS; the
successive visits incur an RTT of RTT1, . . . , RTTn. Further suppose that the
Web page associated with the link contains exactly one object, consisting of
a large amount of HTML text. Let RTT0 denote the RTT between the local
host and the server containing the object. Assuming transmission duration
of 0.002 * RTT0 of the object, how much time elapses from when the client
clicks on the link until the client receives the object?

sum(RTTi) + RTT0 + (RTT0 + 0.002 * RTT0)

### 8

Consider Problem P7 again and assume RTT0 = RTT1 = RTT2 =
RTTn
= RTT, Furthermore, assume a new HTML file, small enough to have
negligible transmission time, which references nine equally small objects on
the same server. How much time elapses with
a. non-persistent HTTP with no parallel TCP connections?
(RTTN) + (RTT0 * 20)
b. non-persistent HTTP with the browser configured for 6 parallel ­ connections?
same.
(RTT * n) + (RTT0 * 6)
c. persistent HTTP?
(RTT * n) +  (RTT0 * 11)

### 9

What are the various DNS record types ?

Type=A  hostname ,IP address
Type=NS to get the hostname ,hostname of a dns
Type=CNAME for alias 
Type=MX hostname, mail server hostname

### 10

Consider a 30-meter link, over which a sender can transmit at a rate of
300 bits/sec in both directions. Suppose that packets containing data are
100,000 bits long, and packets containing only control (e.g., ACK or
 ­ handshaking) are 200 bits long. Assume that N parallel connections each get
1/N of the link bandwidth. Now, consider the HTTP protocol and suppose
that each downloaded object is 100 Kbits long, and that the initial down-
loaded object contains 10 referenced objects from the same sender. Would
parallel downloads via parallel instances of non-persistent HTTP make sense
in this case? 
In that case i don't think parallel TCP connections would help that much since the rate is so low 300bits/sec and we have packets of 200 bits for handshaking and packets of 100,000 bits for requests we can't really do parallel work since the bandwidth is divided by 1/N and if we look at the size of the packets we can only send one packet at the time even though we can parallel work.
Now consider persistent HTTP. Do you expect significant gains
over the non-persistent case? Justify and explain your answer.

Yes i would expect significant gain since it would save 10 RTT.

### 11

Consider the scenario introduced in the previous problem. Now, suppose that
the link is shared by Alice with Bob. Alice does not use parallel instances of
non-persistent HTTP while Bob uses non-persistent HTTP with five parallel
downloads each.
- Does Alice have any advantage over Bob? Why or why not?
I would say that Alice has a disadvantage because Bob has more chances to get one of his packets into the link that Alice does.
- If Alice opens five parallel instances of non-persistent HTTP, then would
her parallel connections be beneficial? Why or why not?
It would be beneficial now she will have has much chance as bob to get one of her packets into the link.

### 12

Write a simple TCP program for a server that accepts lines of input from a cli-
ent and prints the lines onto the server’s standard output. (You can do this by
modifying the TCPServer.py program in the text.) Compile and execute your
program. On any other machine that contains a Web browser, set the proxy
server in the browser to the host that is running your server program; also con-
figure the port number appropriately. Your browser should now send its GET
request messages to your server, and your server should display the messages
on its standard output. Use this platform to determine whether your browser
generates conditional GET messages for objects that are locally cached.

[the program](ex-12.py)

My browser is chrome and it does not seem to use conditional GET.

### 13

Consider sending over HTTP/2 a Web page that consists of one video file
and three images. Suppose that the video clip is transported as 5000 frames,
and each image captures four frames.
a. If all the video frames are sent first without interleaving, how many
“frame times” are needed until all images are sent?
It will have to wait the whole 5000 frames , so 5012 frames
b. If frames are interleaved, how many frame times are needed until all three
images are sent? at most 4 * 4 frames which is 16 frames.

### 14

Consider the Web page in problem 13. Now HTTP/2 prioritization is
employed. Suppose all the images are given priority over the video clip, and
that the first image is given priority over the second image, the second image
over the third image, and so on. How many frame times will be needed until
the second image is sent?

Then it would be 8 frames since it the 4 frames of the first image is sent and the 4 frames are the second image are sent after.

### 15

What is the difference between MAIL FROM: in SMTP and From: in the
mail message itself?

MAIL FROM is part of the handshaking command while From: is in the header of each SMTP messages.

### 16

Summarize streaming of videos.
