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

A compressed video is stored in a data source, when requested by a user the server will choose the version of the video based on the rate (bps) decompressed it and stream the video to the user by chunk, videos are a stream of images (the quality is judge on how many images you have by seconds). and images are bits that represent the colors etc..., the user will constantly request chunk till the end of the video.

### 17

Read RFC 5321 for SMTP. What does MTA stand for? 
Mail transport agent (mail servers)
Consider the following received spam e-mail (modified from a real spam e-mail). Assuming only the originator of this spam e-mail is malicious and all other hosts are honest, identify the malacious host that has generated this spam e-mail.

From - Fri Nov 07 13:41:30 2008

Return-Path: <tennis5@pp33head.com>

Received: from barmail.cs.umass.edu (barmail.cs.umass.

edu

[128.119.240.3]) by cs.umass.edu (8.13.1/8.12.6) for

<hg@cs.umass.edu>; Fri, 7 Nov 2008 13:27:10 -0500

Received: from asusus-4b96 (localhost [127.0.0.1]) by

barmail.cs.umass.edu (Spam Firewall) for <hg@cs.umass.

edu>; Fri, 7

Nov 2008 13:27:07 -0500 (EST)

Received: from asusus-4b96 ([58.88.21.177]) by barmail.

cs.umass.edu

for <hg@cs.umass.edu>; Fri, 07 Nov 2008 13:27:07 -0500

(EST)

Received: from [58.88.21.177] by inbnd55.exchangeddd.

com; Sat, 8

Nov 2008 01:27:07 +0700

From: ”Jonny” <tennis5@pp33head.com>

To: <hg@cs.umass.edu>

Subject: How to secure your savings

the malicious host IP is 58.88.21.177.

### 18

- What is a whois database?

This is a database that stores information on a web resource such as its IP, hostname, autonomous systems numbers etc...



- Use various whois databases on the Internet to obtain the names of two
DNS servers. Indicate which whois databases you used.
domain : canalplus.com
name servers:
nsa.perf1.fr
nsb.perf1.com
nsc.perf1.com

Domain: google.com
name servers:
ns1.google.com
ns2.google.com
ns3.google.com
ns4.google.com

i used the whois database on whois.com

Use nslookup on your local host to send DNS queries to three DNS
servers: your local DNS server and the two DNS servers you found in
part (b). Try querying for Type A, NS, and MX reports. Summarize your
findings.

NS often return multiple name servers, MX and A gives back two different IPs wich is normal since the mail server is not the same than the web server.


-Use nslookup to find a Web server that has multiple IP addresses. Does
the Web server of your institution (school or company) have multiple IP
addresses?

My company have mutliple IP addresses, google as well.

- Use the ARIN whois database to determine the IP address range used by
your university.

I'm not in university anymore so i got the IP range of google.com 142.250.0.0 - 142.251.255.255

- Describe how an attacker can use whois databases and the nslookup tool
to perform reconnaissance on an institution before launching an attack.

It can use nslookup to get the IP of the hostname, then with whois he can get the IP ranges and set up a DDOS attack on the server in this IP range.

- Discuss why whois databases should be publicly available.
Because it is essential to know who owns what, and for abuse report, intellectual property and tech troubleshooting

### 19

In this problem, we use the useful dig tool available on Unix and Linux hosts to
explore the hierarchy of DNS servers. Recall that in Figure 2.19, a DNS server
in the DNS hierarchy delegates a DNS query to a DNS server lower in the
hierarchy, by sending back to the DNS client the name of that lower-level DNS
server. First read the man page for dig, and then answer the following questions.

- Starting with a root DNS server (from one of the root servers [a-m].
root-servers.net), initiate a sequence of queries for the IP address for your
department’s Web server by using dig. Show the list of the names of DNS
servers in the delegation chain in answering your query.

dig mit.edu +trace

-  Repeat part (a) for several popular Web sites, such as google.com, yahoo
.com, or amazon.com.

done

### 20

Consider the scenarios illustrated in Figures 2.12 and 2.13. Assume the rate
of the institutional network is Rl and that of the bottleneck link is Rb. Suppose
there are N clients requesting a file of size L with HTTP at the same time.
For what values of Rl would the file transfer takes less time when a proxy is
installed at the institutional network? (Assume the RTT between a client and
any other host in the institutional network is negligible.)

if RL/N < RB/N = RL < RB the file will be downloaded in less time in most client.

### 21

Suppose that your department has a local DNS server for all computers in the
department. You are an ordinary user (i.e., not a network/system administra-
tor). Can you determine if an external Web site was likely accessed from a
computer in your department a couple of seconds ago? Explain.

Sure if the query time with dig is low, and the TTL is far from a round number that is more than 2 digits usally, it means that the local dns cached the response.

### 22

Consider distributing a file of F= 10 Gbits to N peers. The server has
an upload rate of us = 1 Gbps, and each peer has a download rate of
di = 200 Mbps and an upload rate of u. For N= 10, 100, and 1,000 and
u = 2 Mbps, 10 Mbps, and 100 Mbps, prepare a table giving the minimum
distribution time in seconds for each of the combinations of N and u for both
client-server distribution and P2P distribution.

it takes 50 seconds to download a file for a client 10 Gbits/ 0.2 Gbps
The server can handle only 5 users 1 Gbps/ 0.2 Gbps

Client-server | N 
100 s         | 10  |
1000 s        | 100 |
10000 s       | 1000|

DP2P >= {F:us, F/dmin, NF/ us + sum(ui)}




P2P distribution | U        |  N
98s              | 2 Mbps   | 10
                 | 10 Mbps  | 100
909s             | 100 Mpbs | 1000
833s             | 2 Mbps   | 100
91s              | 10 Mpbs  | 10
                 | 100 Mpbs | 1000
3333s            |  2 Mbps   | 1000
                 |  10 Mpbs  | 100 
500s             |   100 Mpbs | 10

#### 23

Consider distributing a file of F bits to N peers using a client-server architecture. Assume a fluid model where the server can simultaneously transmit
to multiple peers, transmitting to each peer at different rates, as long as the
combined rate does not exceed us.
-  Suppose that us/N <= dmin. 

Specify a distribution scheme that has a distribution time of NF/us.

NF/us >= F/dmin or us/N <= dmin wich is when the the peers have a download time >= to us/N.

- Suppose that us/N >= dmin. Specify a distribution scheme that has a distribution time of F/dmin.

  the distribution scheme would be to allocate exactly di bandwidth for each peer and the distribution time would be F/dmin (the distribution time of the slowest peer).

- Conclude that the minimum distribution time is in general given by max {NF/us, F/dmin}.

the distribution time is given by max {NF/us, F/dmin} because the bottleneck is either the server that can't upload fast enough or a peer that has a slow download time.

#### 24

Consider distributing a file of F bits to N peers using a P2P architecture.
Assume a fluid model. For simplicity assume that dmin is very large, so that
peer download bandwidth is never a bottleneck.

- Suppose that us … (us + u1 + . . . + uN)/N. Specify a distribution
scheme that has a distribution time of F/us.

The distribution scheme depicting this scenario, is when the server is the bottleneck, the server serve each peer at a rate of us/n the peer as soon as they get a packet start to upload it to another peer, the distribution time will be F/us

- Suppose that us Ú (us + u1 + . . . + uN)/N. Specify a distribution
scheme that has a distribution time of NF/(us + u1 + . . . + uN).

The distribution scheme depicting this scenario, is when the mean of the upload rate of the peer is the bottleneck, the server serve as much first peer as it can at a rate of us/ as many peers as possible, the peer as soon as they get a packet start to redistribute even when the server finished to uploads to n peeers, i assume it can continue to start uploading to other peers (so go back to step one) thus at the end achieving a distribution time of NF/(us + u1 + . . . + uN).

this is essentially the p2p network working at full capacity

-  Conclude that the minimum distribution time is in general given by
max5 F/us, NF/(us + u1 + . . . + uN).

Either the server is the bottleneck F/us or p2p network has to work at full capacity NF/ (us + u1 + ... + un)


#### 25

Consider an overlay network with N active peers, with each pair of peers hav-
ing an active TCP connection. Additionally, suppose that the TCP connec-
tions pass through a total of M routers. How many nodes and edges are there
in the corresponding overlay network?

number of nodes = N

number of edges = n * (n - 1) / 2

#### 26

Suppose Bob joins a BitTorrent torrent, but he does not want to upload any
data to any other peers (he wants to be a so-called free-rider).
- Alice who has been using BitTorrent tells Bob that he cannot receive a
complete copy of the file that is shared by the swarm. Is Alice correct or
not? Why?
She is right BitTorrent has cut of the node that only download and does not upload to its peers.
- Charlie claims that Alice is wrong and that he has even been using a collection of multiple computers (with distinct IP addresses) in the computer
lab in his department to make his downloads faster, using some additional coordination scripting. What could his script have done?

From first principles his script found a way to by pass BitTorrent mechanism that cut of the selfish nodes, by joining the torrents with multiple selfish nodes (that can get some packets because of optimistic unchocking) until he has every bits of the files even though it is distributed across the different computers, a so called Sybil attack.

#### 27

Consider a DASH system for which there are N video versions (at N different
rates and qualities) and N audio versions (at N different rates and qualities).
Suppose we want to allow the player to choose at any time any of the N video
versions and any of the N audio versions.
- If we create files so that the audio is mixed in with the video, so server
sends only one media stream at given time, how many files will the server
need to store (each a different URL)?

Let's call the total number of audio V and the total number of audio A.
Since we need every combination of V and A.
the total number of file is V * A.
- If the server instead sends the audio and video streams separately and has the
client synchronize the streams, how many files will the server need to store?

The server will only need to store V + A, a file by video and a file by audio.

#### 28

Install the Python programs TCPClient and UDPClient on one host and
TCPServer and UDPServer on another host.

- Suppose you run TCPServer and you try to connect using UDPClient.
What happens? Why?

It won't work, the UDPClient won't be able to connect to any server because it is not the same protocal, TCP require a handshake in order for it to work.

- Suppose you run UDPClient before you run UDPServer. What happens?
Why?

The message may not arrive since it can be sent before that the UDPServer is up and running.

- What happens if you hardwire in the python client and server programs
different port numbers for the client and server sides in either a TCP or
UDP client-server pair?

It won't work, for example the client will try to send a message to a port that may be or not in use by another socket but not the expected socket.

- if nothing is listening an error will occurs
- if a TCP socket is listening the connection will be refused because the handshake didn't happen.
- if a UDP is listening you will most likely receive garbage data, or a processing error will occur.

#### 29

Suppose that in UDPClient.py, after we create the socket, we add the line:
clientSocket.bind((’’, 5432))
Will it become necessary to change UDPServer.py?

No it won't since it dynamically retrieve the client port from the request.

What are the port numbers for the sockets in UDPClient and UDPServer? 

The port number of UDPServer is 12000 and UDPClient for the UDP client 5432


What were they before making this change?

It is assign by the OS.

#### 30

Can you configure your browser to open multiple simultaneous connections
to a Web site? 
Yes you can and this technique was more used by HTTP/1

What are the advantages and disadvantages of having a large
number of simultaneous TCP connections

The disadvantage is that you pay the price of the handshake imposed by TCP multiple time.
That is why HTTP2 has been invented and allows multiple request to shared the same TCP connections achieving multiplexing.
The advantage on the other hand is that when one connection is waiting for data , another connection can be used to retrieve other data.

#### 31

We have seen that Internet TCP sockets treat the data being sent as a byte
stream but UDP sockets recognize message boundaries.

What are one advantage and one disadvantage of byte-oriented API versus having the API
explicitly recognize and preserve application-defined message boundaries?

byte-oriented api you can start to do some work even though you don't have the full message yet, but you have to implement something for detecting the message boundaries.

And an API that explicitly recognize and preserve application boundaries is straightforward only one request , the disadvantage is that it needs to wait the whole message since it is not a stream, it can't start to do some work with the packets that already arrives.

#### 32

What is the Apache Web server? 
It is a webserver.
How much does it cost? 
It is an open source software, so it is free, only hosting it would cost some money.
What functionality does it currently have? You may want to look at Wikipedia to answer this
question.

from wikipedia "Popular authentication modules include mod_access, mod_auth, mod_digest, and mod_auth_digest, the successor to mod_digest. A sample of other features include Secure Sockets Layer and Transport Layer Security support (mod_ssl), a proxy module (mod_proxy), a URL rewriting module (mod_rewrite), custom log files (mod_log_config), and filtering support (mod_include and mod_ext_filter)."

## Wireshark Lab: HTTP

### The Basic HTTP GET/response interaction

#### 1  
Is your browser running HTTP version 1.0, 1.1 or 2 ?

My browser is running HTTP version 1.1

What version of HTTP is the server running ?
The server is alos running HTTP version 1.1

#### 2 

What languages (if any) does your browser indicate taht it can accept to the server ?

English

#### 3 

What is the IP address of your computer?  What is the IP address of the gaia.cs.umass.edu server? 

The ip address of my computer is: 192.168.1.57 


The ip address of the gaia.cs.umass.edu server is: 128.119.245.12

#### 4

What is the status code returned from the server to your browser?

The status code returned by the server is 200

#### 5

When was the HTML file that you are retrieving last modified at the server?

28 october 2025, we can see that in the Last modifed header

#### 6

How many bytes of content are being returned to your browser? 

128 bytes

#### 7 

By inspecting the raw data in the packet content window, do you see any headers within the data that are not displayed in the packet-listing window?  If so, name one.

[Status code description: OK]

### The Conditional HTTP GET/operation

#### 8

Inspect the contents of the first HTTP GET request from your browser to the server.  Do you see an “IF-MODIFIED-SINCE” line in the HTTP GET?

No there is no IF-MODIFED-SINCE header.

#### 9

Inspect the contents of the server response. Did the server explicitly return the contents of the file?   How can you tell?

Yes otherwise the status code would have been 304

#### 10

Now inspect the contents of the second HTTP GET request from your browser to the server.  Do you see an “IF-MODIFIED-SINCE:” line in the HTTP GET ? If so, what information follows the “IF-MODIFIED-SINCE:” header?

Yes there is a IF-MODIFED-SINCE the next inforamtion is the frame of where is the response, and the header before is IF-NONE-MATCH

What is the HTTP status code and phrase returned from the server in response to this second HTTP GET?  
The 304 status code witht the phrase not modifed.
Did the server explicitly return the contents of the file?   Explain.

#### 11

No the server didn't explicitly return the contents of the file, since the server found no changes the last time i made the request the browser gave the response from the local storage.

### Retrieving long document

#### 12

How many HTTP GET request messages did your browser send?  Which packet number in the trace contains the GET message for the Bill or Rights?

The browser sent only one get request, pakcet number 38

#### 13

Which packet number in the trace contains the status code and phrase associated with the response to the HTTP GET request?


The browser sent only one get request, pakcet number 48


#### 14

What is the status code and phrase in the response?

200 OK

#### 15

How many data-containing TCP segments were needed to carry the single HTTP response and the text of the Bill of Rights?

2 TCP segment, one of 4380 bytes and another of 484 bytes

### HTML documents with embeded objects

#### 16

How many HTTP GET request messages did your browser send?  

3 GET request have been sent

To which Internet addresses were these GET requests sent?

the file ip address and persons ip address: 128.119.245.12


the book cover ip address: 2a03:4000:3e:5ca:3813:f3ff:fe33:915d

#### 17

The request appears to be made sequencially since the first response arrive even before that the second request is captured.

### HTTP Authentication

#### 18

What is the server’s response (status code and phrase) in response to the initial HTTP GET message from your browser?

401 Unauthenticated

#### 19

When your browser’s sends the HTTP GET message for the second time, what new field is included in the HTTP GET message? 

The new field what the Authorization header: it was a basic auth so the username and password were sent.

## Wireshark Lab: DNS

### nslookup

#### 1

Run nslookup to obtain the IP address of the web server for the Indian Institute of Technology in Bombay, India: www.iitb.ac.in.  What is the IP address of www.iitb.ac.in 

103.21.124.133

#### 2

What is the IP address of the DNS server that provided the answer to your nslookup command in question 1 above?

Its name is box and its ip address is 192.168.1.1

#### 3

Did the answer to your nslookup command in question 1 above come from an authoritative or non-authoritative server

A non-authoritative server

#### 4

Use the nslookup command to determine the name of the authoritative name server for the iit.ac.in domain.  What is that name?  (If there are more than one authoritative servers, what is the name of the first authoritative server returned by nslookup)?

dns1.iitb.ac.in

If you had to find the IP address of that authoritative name server, how would you do so?

i would do a ns lookup of type A of the domain name of the primary dns server who is dns1.ittb.ac.in, and the ip address is : 103.21.125.129


### Tracing DNS with Wireshark

#### 5

Locate the first DNS query message resolving the name gaia.cs.umass.edu. What is the packet number  in the trace for the DNS query message?  Is this query message sent over UDP or TCP?   

It is the packet number 87, the query message is sent over UDP

#### 6

Now locate the corresponding DNS response to the initial DNS query. What is the packet number in the trace for the DNS response message?  Is this response message received via UDP or TCP?   

the packet is the nubmer 89 and it use UDP as well.

#### 7

What is the destination port for the DNS query message? 

The destination port is 53


What is the source port of the DNS response message?

The source port is 53

#### 8

To what IP address is the DNS query message sent? 

128.119.40.12

#### 9

Examine the DNS query message. How many “questions” does this DNS message contain? How many “answers” answers does it contain?

It contains 1 question and 0 answer

#### 10

Examine the DNS response message to the initial query message. How many “questions” does this DNS message contain? How many “answers” answers does it con

It contains 1 question and 1 answer


#### 11

The web page for the base file http://gaia.cs.umass.edu/kurose_ross/ references the image object http://gaia.cs.umass.edu/kurose_ross/header_graphic_book_8E_2.jpg , which, like the base webpage, is on gaia.cs.umass.edu.  What is the packet number in the trace for the initial HTTP GET request for the base file http://gaia.cs.umass.edu/kurose_ross/?

this is the package 118

What is the packet number in the trace of the DNS query made to resolve gaia.cs.umass.edu so that this initial HTTP request can be sent to the gaia.cs.umass.edu IP address?

it is the package 87

What is the packet number in the trace of the received DNS response? 

it is the package 89

What is the packet number in the trace for the HTTP GET request for the image object http://gaia.cs.umass.edu/kurose_ross/header_graphic_book_8E2.jpg? 

this is the package 137 

What is the packet number in the DNS query made to resolve gaia.cs.umass.edu so that this second HTTP request can be sent to the gaia.cs.umass.edu IP address? 

This is the package 119

the ip address is 10.15.0.2

Discuss how DNS caching affects the answer to this last question. 

It is not the same address because of the local caching


#### 12


