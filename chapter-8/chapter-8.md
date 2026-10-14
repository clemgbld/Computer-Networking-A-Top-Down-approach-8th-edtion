# CHAPTER 8: Security in computer networks

## Review questions

### section 8.1

#### 1

What are the differences between message confidentiality and message integ-
rity? 

Message confidentiality means that the message is not visible to everyone.

Message integrity means that the message has not be altered.


Can you have confidentiality without integrity? 

Yes you can totally encrypt a message but not send a MAC code with it to prove it has not been altered.

Can you have integrity without confidentiality? Justify your answer.

Yes you can totally send a message in clear text and send a MAC code wit it to prove it has not been altered.

#### 2

Internet entities (routers, switches, DNS servers, Web servers, user end
systems, and so on) often need to communicate securely. Give three
specific example pairs of Internet entities that may want secure
communication.

- user end systems and Web servers
- routers and routers
- switches and routers

### section 8.2

#### 3

From a service perspective, what is an important difference between a
symmetric-key system and a public-key system?

The difference is that in a symmetric-key system there is only one shared key and in a public-key system there is 2 keys a private and a public-key

#### 4

Suppose that an intruder has an encrypted message as well as the decrypted
version of that message. Can the intruder mount a ciphertext-only attack, a
known-plaintext attack, or a chosen-plaintext attack?

Known-plaintext attack

#### 5

Consider an 8-bit block cipher. How many possible input blocks does
this cipher have? 

2 ^ 8 = 256

How many possible mappings are there? 

(2 ^ 8)! = (256)!

If we view
each mapping as a key, then how many possible keys does this
cipher have?

It has (256)! possible keys.

#### 6

Suppose N people want to communicate with each of N- 1 other peo-
ple using symmetric key encryption. All communication between any two
people, i and j, is visible to all other people in this group of N, and no other
person in this group should be able to decode their communication. How
many keys are required in the system as a whole? 

You need N (N - 1) / 2 keys.

Now suppose that public
key encryption is used. How many keys are required in this case?

You need 2 N keys.

#### 7

Suppose n = 10,000, a = 10,023, and b = 10,004. Use an identity of modu-
lar arithmetic to calculate in your head (a # b) mod n.

[(a mod n) * (b mod n)] mod n

the result is 92


#### 8

Suppose you want to encrypt the message 10101111 by encrypting the
decimal number that corresponds to the message. What is the decimal
number?

175

### section 8.3 - 8.4

#### 9

In what way does a hash provide a better
message integrity check than a checksum
(such as the Internet checksum)?

Internet checksum are two easy to brut force compared to hash and hash 2 ^16 possibility for internet checksum , 2 ^ 256 for sha256 for example.

#### 10

Can you “decrypt” a hash of a message to get
the original message? Explain your answer.

No you cannot decrypt a hash, hashing is one way only (there is no secret key, and information loss happens due to compression).

#### 11

Consider a variation of the MAC algorithm
(Figure 8.9) where the sender sends
(m, H(m) + s), where H(m) + s is the concatenation of H(m) and s.
Is this variation flawed ?

Yes it is deeply flawed.

Why or why not ?

Because with this approach the shared secret is in clear text concatenated to the H(m) which is a rather obvious security flaw.

#### 12

What does it mean for a signed document to
be verifiable and nonforgeable?

It means encrypting the document with your private key (or a hash of the document because encryption is expensive) to create a signature.
Another person who owns the public key paired with the private key can then decrypt the document with the public key to show that a person signed a message or a document.
It is like a real signature but nonforgeable and verifiable.

#### 13

In what way does the public-key encrypted
message hash provide a better digital signa-
ture than the public-key encrypted message?

Since the hash is smaller it will be less expensive to encrypt.

#### 14

Suppose certifier.com creates a certificate for
foo.com. Typically, the entire certificate would
be encrypted with certifier.com’s public key.
True or false?
False certificate are not encrypted since they are public document thus they are in plain-text.

#### 15

Suppose Alice has a message that she is ready
to send to anyone who asks. Thousands of
people want to obtain Alice’s message, but
each wants to be sure of the integrity of the
message. In this context, do you think a MAC-
based or a digital-signature-based integrity
scheme is more suitable? 

A digital-signature based integrity scheme is more suitable.

Why?

Because since digital-signature-based integrity rely on pk infrastructure Alice could distribute 1 public key to everyone which is much either than created thousands of key which would be require if a MAC-based integrity scheme would have been used.

#### 16

What is the purpose of a nonce in an end-
point authentication protocol?

To be protected from a playback attack.

#### 17

What does it mean to say that a nonce is a
once-in-a-lifetime value? 

Since nonce is based on time there cannot be two same nonce since a point in time let's say Timestamp 1791351660 happens only once is a lifetime.

In whose lifetime?

In our case it is during the Authentication lifetime.

#### 18

ls the message integrity scheme based on
HMAC susceptible to playback attacks? 

Yes it is.

If so,how can a nonce be incorporated into the
scheme to remove this susceptibility?

The person that is expcting a message + HMAC

Needs to provide a nonce.
Then when providing a mac we will append the nonce to the message before hashing to prove that we are live.

### section 8.5 - 8.8

#### 19

Suppose that Bob receives a PGP message
from Alice. How does Bob know for sure that
Alice created the message (rather than, say,
Trudy)? Does PGP use a MAC for message
integrity?

Bob can know for sure that is Alice that created the message thanks to the digital signature.

PGP use MAC only for hybrid architecture.

#### 20

In the TLS record, there is a field for TLS
sequence numbers. True or false?

False

#### 21

What is the purpose of the random nonces in
the TLS handshake?

To prevent a connection replay attack.

#### 22

Suppose an TLS session employs a block
cipher with CBC. True or false: The server
sends to the client the IV in the clear.

True

#### 23

Suppose Bob initiates a TCP connection to
Trudy who is pretending to be Alice. During
the handshake, Trudy sends Bob Alice’s cer-
tificate. In what step of the TLS handshake
algorithm will Bob discover that he is not
communicating with Alice?

Master key derivation, because Trudy cannot decrypt a message encrypted with the PMS since she doesn't have the correct private key to do it.

#### 24

Consider sending a stream of packets from
Host A to Host B using IPsec. Typically, a new
SA will be established for each packet sent in
the stream. True or false?

False

#### 25

Suppose that TCP is being run over IPsec
between headquarters and the branch office
in Figure 8.28. If TCP retransmits the same
packet, then the two corresponding packets
sent by R1 packets will have the same
sequence number in the ESP header. True or
false?

False

#### 26

An IKE SA and an IPsec SA are the same
thing. True or false?

False

#### 27

Consider WEP for 802.11. Suppose that the
data is 10101100 and the keystream is
1111000. What is the resulting ciphertext?

It is a XOR between the data and the keystream:

10101100
01111000
--------
11010100

the cyphertext is 11010100.

### section 8.9

#### 28

Stateful packet filters maintain two data struc-
tures. Name them and briefly describe what
they do.

- Connection table:

A table keep tracks of the ongoing TCP connection.

- Access control list:

It is identical to the acces list of traditional packet filters but also state which connection should be checked.

#### 29

Consider a traditional (stateless) packet filter.
This packet filter may filter packets based on
TCP flag bits as well as other header fields.
True or false?

True.

#### 30

In a traditional packet filter, each interface can
have its own access control list. True or false?

True

#### 31

Why must an application gateway work in
conjunction with a router filter to be effective?

To have a finer grained level of security.

Router filter base on IP/TCP/UDP/ICMP header and application gateway perform additional application layer verification.

#### 32

Signature-based IDSs and IPSs inspect into
the payloads of TCP and UDP segments. True
or false?

True

## Problems

#### 1

Using the monoalphabetic cipher in Figure 8.3, encode the message
“This is an easy problem.” Decode the message “rmij’u uamu xyj.”

This is an easy problem -> Uasi si mj cmiw lokngch

rmij'u uamu xyj -> wasn't that fun

#### 2

Show that Trudy’s known-plaintext attack, in which she knows the
(ciphertext, plaintext) translation pairs for seven letters, reduces
the number of possible substitutions to be checked in the example in
­ Section 8.2.1 by approximately 10^9.

26! = 4.0329 * 10^26

26 - 7 =  19

19! = 1.021 * 10^17

10^26 - 17 = 10^9

3.3 * 10^9

#### 3

Consider the polyalphabetic system shown in Figure 8.4. Will a chosen-
plaintext attack that is able to get the plaintext encoding of the message
“The quick brown fox jumps over the lazy dog.” be sufficient to decode
all messages? Why or why not?

Yes because since we have C1 we can deduce when C2 is used and therefore decode every message.

#### 4

Consider the block cipher in Figure 8.5. Suppose that each block cipher
Ti simply reverses the order of the eight input bits (so that, for example,
11110000 becomes 00001111). Further suppose that the 64-bit scrambler
does not modify any bits (so that the output value of the mth bit is equal
to the input value of the mth bit). (a) With =
n 3 and the original 64-bit
input equal to 10100000 repeated eight times, what is the value of the
output? 

00000101 00000101 00000101 00000101 00000101 00000101 00000101 00000101

(b) Repeat part (a) but now change the last bit of the original
64-bit input from a 0 to a 1. 

N 1: 10100000 -> 00000100

N2 : 00000100 -> 00100001

N3: 00100001 -> 10000101

00000101 00000101 00000101 00000101 00000101 00000101 00000101 10000101

(c) Repeat parts (a) and (b) but now suppose
that the 64-bit scrambler inverses the order of the 64 bits.


N 1: 10100000 -> 00000100


00000100 00000101 00000101 00000101 00000101 00000101 00000101 00000101


N 2: 10100000 -> 00000100


00000100 00000101 00000101 00000101 00000101 00000101 00000101 00000100


N3: 00000100 -> 00100001


00100001 00000101 00000101 00000101 00000101 00000101 00000101 00000100




#### 5

Consider the block cipher in Figure 8.5. For a given “key” Alice and Bob
would need to keep eight tables, each 8 bits by 8 bits. For Alice (or Bob)
to store all eight tables, how many bits of storage are necessary? 

number of row in one table 2 ^ 8 = 256

There are 8 tables so 256 * 8 = 2048

2046 * 8 = 16384 

How does this number compare with the number of bits required for a full-
table 64-bit block cipher?

it is much smaller

2^64 * 8 = 1,4 * 10^20

#### 6

Consider the 3-bit block cipher in Table 8.1. Suppose the plaintext is
100100100. (a) Initially assume that CBC is not used. What is the result-
ing ciphertext? 

011011011

(b) Suppose Trudy sniffs the ciphertext. Assuming she
knows that a 3-bit block cipher without CBC is being employed (but
doesn’t know the specific cipher), what can she surmise? 

That the complexity to decode the message is 2^3! since every block is the same.


(c) Now sup-
pose that CBC is used with =
IV 111. What is the resulting ciphertext

IV = 111

First block:

100
111
---
011

011 -> 100

Second block:

100
100
---
000

000 -> 110

Third block:

100
110
---
010

010 -> 101

The answer is 100110101

#### 7

(a) Using RSA, choose =
p 3 and =
q 11, and encode the word “dog” by
encrypting each letter separately. Apply the decryption algorithm to the
encrypted version to recover the original plaintext message. 
n = 33
z = 20
e = 17
d = 13

choosing number that are compatible with private and public key for the words.

d = 4
o = 5
g = 7

After encryption 

d = 16
o = 14
g = 28

After decryption

d = 4
o = 5
g = 7

(b) Repeat
part (a) but now encrypt “dog” as one message m.

let's take dog as 2

After encryption

dog = 29

After decryption

dog = 2

#### 8

Consider RSA with  p = 5 q = 11

a ) What are n and z?

n = 55

z = 40

b) Let e be 3. Why is this an acceptable choice for e?

Yes because it doesn't share any factor with 40

c) Find d such that = de 1 (mod z) and < d 160.

using the function i wrote [here](./rsa_d.py).

27

e) Encrypt the message  m = 8 using the key (n, e).
Let c denote the corresponding ciphertext.

c = 8 ^ 3 mod 55 = 17

#### 9

In this problem, we explore the Diffie-Hellman (DH) public-key encryption algorithm, that we studied in Section 8.2.2

a) With p = 11 and g = 2, suppose Alice and Bob choose private keys

Sa = 5 and Sb = 12, respectively. Calculate Alice's and Bob's public-keys Ta and Tb.

Show all the work.

Ta = g^ Sa mod p

Ta = 2 ^ 5 mod 11

Ta = 10

Tb = g^ Sa mod p

Tb = 2 ^ 12 mod 11

Tb = 4


b) Following up on part (b), now calculate S as the shared symmetric key.
Show all work.

Ssa = (Tb) ^ Sa mod p
Ssa = 4 ^5 mod 11
Ssa = 1

Ssb = (Ta) ^Sb mod p
Ssb = 10 ^12 mod 11
Ssb = 1


c) Provide a timing diagram that shows how Diffie-Hellman can be
attacked by a man-in-the-middle. The timing diagram should have three
vertical lines, one for Alice, one for Bob, and one for the attacker Trudy.

I won't draw the diagram but a man in the middle attack is possible if Trudy makes Alice believe that she is Bob and Bob believe that she is Alice.

#### 10

Suppose Alice wants to communicate with Bob using symmetric key
cryptography using a session key KS. In Section 8.2, we learned how
public-key cryptography can be used to distribute the session key from
Alice to Bob. In this problem, we explore how the session key can be
­distributed—without public key cryptography—using a key distribution
center (KDC). The KDC is a server that shares a unique secret symmetric
key with each registered user. For Alice and Bob, denote these keys by
K A KDC and KB KDC. Design a scheme that uses the KDC to distribute KS
to Alice and Bob. Your scheme should use three messages to distribute
the session key: a message from Alice to the KDC; a message from the
KDC to Alice; and finally a message from Alice to Bob. The first message
is KA - KDC(A, B). using the notation KA - KDC' KB - KDC', S, A and B answer the following questions.

a) What is the second message.

KA-KDC(KS, KB-KDC(KS, KA))

b) What is the third message.

KB-KDC(KS, KA)

#### 11

Compute a third message, different from the two messages in Figure 8.8,
that has the same checksum as the messages in Figure 8.8.

IOU1
00.B
9BO9


#### 12

Suppose Alice and Bob share two secret keys: an authentication key S1
and a symmetric encryption key S2. Augment Figure 8.9 so that both
integrity and confidentiality are provided.

It is the same diagram except that we encrypt the message with the symetric key and send (K(m), H(m + s))

#### 13

In the BitTorrent P2P file distribution protocol (see Chapter 2), the seed
breaks the file into blocks, and the peers redistribute the blocks to each
other. Without any protection, an attacker can easily wreak havoc in a tor-
rent by masquerading as a benevolent peer and sending bogus blocks to a
small subset of peers in the torrent. These unsuspecting peers then redis-
tribute the bogus blocks to other peers, which in turn redistribute the
bogus blocks to even more peers. Thus, it is critical for BitTorrent to have
a mechanism that allows a peer to verify the integrity of a block, so that it
doesn’t redistribute bogus blocks. Assume that when a peer joins a tor-
rent, it initially gets a .torrent file from a fully trusted source. Describe
a simple scheme that allows peers to verify the integrity of blocks.

In the torrent file we have the hash of each block so each peer when it receive block needs to hash it and verify that it is the correct hash that is in the torrent file.

#### 14

The OSPF routing protocol uses a MAC rather than digital signatures to
provide message integrity. Why do you think a MAC was chosen over
digital signatures?

Because it is faster (no encryption only hashing) and you just need one symetric key for all the router has opposed to a pki infrastructure where you would have to manage a lot of key and also we want to only achieve integrity and not prove that one router specific router has sent a packet.

#### 15

Consider our authentication protocol in Figure 8.18 in which Alice authen-
ticates herself to Bob, which we saw works well (i.e., we found no flaws in
it). Now suppose that while Alice is authenticating herself to Bob, Bob
must authenticate himself to Alice. Give a scenario by which Trudy, pre-
tending to be Alice, can now authenticate herself to Bob as Alice. (Hint:
Consider that the sequence of operations of the protocol, one with Trudy
initiating and one with Bob initiating, can be arbitrarily interleaved. Pay
particular attention to the fact that both Bob and Alice will use a nonce,
and that if care is not taken, the same nonce can be used maliciously.)

Trudy can use a reflection attack.

#### 16

A natural question is whether we can use a nonce and public key cryp-
tography to solve the end-point authentication problem in Section 8.4.
Consider the following natural protocol: 

1) Alice sends the message “I am Alice” to Bob.

2) Bob chooses a nonce, R, and sends it to Alice.

3) Alice uses her private key to encrypt the nonce and sends the resulting
value to Bob. 

4) Bob applies Alice’s public key to the received message.
Thus, Bob computes R and authenticates Alice.

a) Diagram this protocol, using the notation for public and private keys
employed in the textbook.

[diagram](./problem-16.png)

b) Suppose that certificates are not used. Describe how Trudy can become
a “woman-in-the-middle” by intercepting Alice’s messages and then
pretending to be Alice to Bob.

When Bob Alice would give her public key to bob in clear trudy would just have to replace it hers and then intercept the nonce and reply to bob with the nonce encrypted with her public key and if Alice manages to do then Bob will mistake her for Alice.

#### 17

Figure 8.21 shows the operations that Alice must perform with PGP to pro-
vide confidentiality, authentication, and integrity. Diagram the correspond-
ing operations that Bob must perform on the package received from Alice.

[diagram](./problem-17.png)

#### 18

Suppose Alice wants to send an e-mail to Bob. Bob has a public-private key pair (Kb+, Kb-) and Alice has Bob certificate.
But Alice does not
have a public, private key pair. Alice and Bob (and the entire world) share the same Hash function H(.)

a) In this situation, is it possible to design a scheme so that Bob can verify
that Alice created the message? If so, show how with a block diagram
for Alice and Bob.

Not it is not possible without a digital signature but and Alice doesn't have public/private keys pair.

b) Is it possible to design a scheme that provides confidentiality for send-
ing the message from Alice to Bob? If so, show how with a block dia-
gram for Alice and Bob.

 yes Alice just needs to encrypt the message with Bob public key and Bob can then decrypt the message.

Alice ->[Kb+(m)] -> (Internet) -> [Kb-(m)] -> Bob

#### 19

Consider the Wireshark output below for a portion of an SSL session.

a) Is Wireshark packet 112 sent by the client or server?

Packet 112 is sent by the client.

b) What is the server’s IP address and port number?

address = 216.75.194.220 , port = 443

c) Assuming no loss and no retransmissions, what will be the sequence
number of the next TCP segment sent by the client?

283

d) How many SSL records does Wireshark packet 112 contain?

3, Handshake Protocol: client key exchange, change cipher spec protocol: change cipher spec and Handshake protocol: Encrypted Handshake message

e) Does packet 112 contain a Master Secret or an Encrypted Master Secret
or neither?

An  Encrypted Master Secret.

f) Assuming that the handshake type field is 1 byte and each length field
is 3 bytes, what are the values of the first and last bytes of the Master
Secret (or Encrypted Master Secret)?

the encrypted master key start at byte 5 and end at byte 133.

g) The client encrypted handshake message takes into account how
many SSL records?

4

h) The server encrypted handshake message takes into account how
many SSL records?

5

#### 20

In Section 8.6.1, it is shown that without sequence numbers, Trudy
(a woman-in-the middle) can wreak havoc in a TLS session by interchang-
ing TCP segments. Can Trudy do something similar by deleting a TCP
segment? What does she need to do to succeed at the deletion attack?
What effect will it have?

Deleting TCP segments alone won't work in isolation she would need to also increment the sequence number correctly of every next TCP segments.
The effect is that the receiver will receive an incomplete message.

#### 21

Suppose Alice and Bob are communicating over a TLS session. Suppose
an attacker, who does not have any of the shared keys, inserts a bogus
TCP segment into a packet stream with correct TCP checksum and
sequence numbers (and correct IP addresses and port numbers). Will
TLS at the receiving side accept the bogus packet and pass the payload
to the receiving application? Why or why not?

Not it wouldn't work because a key is hashed with the record for integrity.

#### 22

The following true/false questions pertain to Figure 8.28.

a) When a host in 172.16.1 24 sends a datagram to an Amazon.com
server, the router R1 will encrypt the datagram using IPsec.

False no in the diagram only the datagrams sent between the Headquarters and the Branch office will be encrypted using Ipsec.

b) When a host in 172.16.1 24 sends a datagram to a host in 172.16.2 24,
the router R1 will change the source and destination address of the IP
datagram.

False the Ip datagram is left intact and wrapped in an IpSec datagram with the source IP as the IP of R1 and with the destination IP as the one of R2.

c) Suppose a host in 172.16.1 24 initiates a TCP connection to a Web
server in 172.16.2 24. As part of this connection, all datagrams sent
by R1 will have protocol number 50 in the left-most IPv4 header field.

True.

d) Consider sending a TCP segment from a host in 172.16.1 24 to a host
in 172.16.2 24. Suppose the acknowledgment for this segment gets
lost, so that TCP resends the segment. Because IPsec uses sequence
numbers, R1 will not resend the TCP segment.

False R1 will resend the segment.

#### 23

Consider the example in Figure 8.28. Suppose Trudy is a woman-in-the-
middle, who can insert datagrams into the stream of datagrams going
from R1 and R2. As part of a replay attack, Trudy sends a duplicate copy
of one of the datagrams sent from R1 to R2. Will R2 decrypt the duplicate
datagram and forward it into the branch-office network? If not, describe
in detail how R2 detects the duplicate datagram.

No a replay attack won't work because the security association keeps track of which datagram has been sent thanks to the seq # field in the ESP header in the Enchilada.

#### 24

Provide a filter table and a connection table for a stateful firewall that is
as restrictive as possible but accomplishes the following:

a) Allows all internal users to establish Telnet sessions with external
hosts.

b) Allows external users to surf the company Web site at 222.22.0.12.

c) But otherwise blocks all inbound and outbound traffic.

The internal network is 222.22/16. In your solution, suppose that the
connection table is currently caching three connections, all from inside to
outside. You’ll need to invent appropriate IP addresses and port
numbers.

Filters table:

action    source address          dest address           protocol      source port     dest port    flag bit   check connection

allow     222.22/16               outside of 222.22/16    TCP           > 1023           23          any             
allow     outside of 222.22/16    222.22/16               TCP           23               > 1023      ACK             X
allow     outside of 222.22/16    222.22.0.12             TCP           > 1023           80          any
allow     222.22.0.12             outside of 222.22/16               TCP           80               > 1023      ACK             x
deny      all                     all                     all           all              all         all

Stateful filters table:

source address     dest address     source port       dest port

122.22.1.7         222.22.0.12      12699             80
122.22.93.2        222.22.0.12      37654             80
222.22.65.143      203.77.240.43    48712             23

#### 25

Suppose Alice wants to visit the Web site activist.com using a TOR-like
service. This service uses two non-colluding proxy servers, Proxy1 and
Proxy2. Alice first obtains the certificates (each containing a public key)
for Proxy1 and Proxy2 from some central server.

Denote K1+(), K2+(), K1-(), K2-() for the encryption / decryption with public and private RSA keys.

a) Using a timing diagram, provide a protocol (as simple as possible)
that enables Alice to establish a shared session key S1 with Proxy1.
Denote ( ) S m 1 for encryption/decryption of data m with the shared
key S1.

[diagram](./problem-25-a.png)

b) Using a timing diagram, provide a protocol (as simple as possible)
that allows Alice to establish a shared session key S2 with Proxy2 with-
out revealing her IP address to Proxy2.


[diagram](./problem-25-b.png)

c) Assume now that shared keys S1 and S2 are now established. Using
a timing diagram, provide a protocol (as simple as possible and not
using public-key cryptography) that allows Alice to request an html page
from activist.comwithout revealing her IP address to Proxy2 and without
revealing to Proxy1 which site she is visiting. Your diagram should end
with an HTTP request arriving at activist.com.


[diagram](./problem-25-c.png)

## Wireshark Lab: TLS

### 2 a first look at the captured trace

#### 1

What is the packet number in your trace that contains the initial TCP SYN
message? (By “packet number,” we meant the number in the “No.” column at the
left of the Wireshark display, not the sequence number in the TCP segment itself).

Number 579 in my own trace.

#### 2

Is the TCP connection set up before or after the first TLS message is sent from
client to server?

Yes it is.

### 3 The TLS Handshake: client hello

#### 3

What is the packet number in your trace that contains the TLS Client Hello
message? 

In my own trace it is the packet number 636.

#### 4

 What version of TLS is your client running, as declared in the Client Hello
message?

TLS 1.0

#### 5

How many cipher suites are supported by your client, as declared in the Client
Hello message? A cipher suite is a set of related cryptographic algorithms that
determine how session keys will be derived, and how data will be encrypted and
be digitally signed via a HMAC algorithm

[Cypher suites](./wireshark-client-cypher-suites.png)

#### 6

Your client generates and sends a string of “random bytes” to the server in the
Client Hello message. What are the first two hexadecimal digits in the random
bytes field of the Client Hello message? 
Enter the two hexadecimal digits
(without spaces between the hex digits and without any leading '0x' , using
lowercase letters where needed). Hint: be careful to fully dig into the Random
field to find the Random Bytes subfield (do not consider the GMT UNIX
Time subfield of Random)

c9

#### 7

What is the purpose(s) of the “random bytes” field in the Client Hello message?
Note: you’ll have do some searching and reading to get the answer to this
question; see section 8.6 and in RFC 5246.

The random bytes act as a nonce.

### The TLS Handshake: Server hello message

#### 8

What is the packet number in your trace that contains the TLS Server Hello
message? 

In my own trace the packet number is 657.

#### 9

Which cipher suite has been chosen by the server from among those offered in the
earlier Client Hello message?

Cipher Suite: TLS_AES_256_GCM_SHA384 (0x1302)

#### 10

Does the Server Hello message contain random bytes, similar to how the Client
Hello message contained random bytes? And if so, what is/are their purpose(s)?

Yes, same purpose than the one in the client it act as a nonce to verify that the client is live and to prevent the server against a replay attack of an impersonator.

#### 11

What is the packet number in your trace for the TLS message part that contains
the public key certificate for the www.cics.umass.edu server (actually the
www.cs.umass.edu server)?

In my own trace it is in packet 658.

#### 12

A server may return more than one certificate. If more than one certificate is
returned, are all of these certificates for www.cs.umass.edu? 

No.

If not all are for
www.cs.umass.edu, then who are these other certificates for? 

They are for the other domain name that are pointing to the same server than www.cs.umass.edu.

You can determine
who the certificate is for by checking the id-at-commonName field in the
retuned certificate.


www.cics.umass.edu

#### 13

What is the name of the certification authority that issued the certificate for idat-commonName=www.cs.umass.edu?

ESET, spol. s r. o.

#### 14

What digital signature algorithm is used by the CA to sign this certificate? Hint:
this information can be found in signature subfield of the
SignedCertificate field of the certificate for www.cs.umass.edu.

PKCS #1 SHA-256 With RSA Encryption

#### 15

Let's take a look at what a real public key looks like! What are the first four
hexadecimal digits of the modulus of the public key being used by
www.cics.umass.edu? Enter the four hexadecimal digits (without spaces between
the hex digits and without any leading '0x' , using lowercase letters where needed,
and including any leading 0s after '0x'). Hint: this information can be found in
subjectPublicKeyInfo subfield of the SignedCertificate field of
the certificate for www.cs.umass.edu.

EB 06 FA 60

#### 16

Look in your trace to find messages between the client and a CA to get the CA’s
public key information, so that the client can verify that the CA-signed certificate
sent by the server is indeed valid and has not been forged or altered. Do you see
such message in your trace? If so, what is the number in the trace of the first
packet sent from your client to the CA? If not, explain why the client did not
contact the CA.

There is no such message because the client already has the information of trusted certificates preinstalled to verify that the certificate has no been forged (it has the public key to verify the signature).

#### 17

What is the packet number in your trace for the TLS message part that contains
the Server Hello Done TLS record?

Iti is in the same packet than in the Server hallo packet.

### The TLS Handshake: wrapping up the handshake

#### 18

What is the packet number in your trace for the TLS message that contains the
public key information, Change Cipher Spec, and Encrypted Handshake message,
being sent from client to server?

In my own trace 695.


#### 19

Does the client provide its own CA-signed public key certificate back to the
server? If so, what is the packet number in your trace containing your client’s
certificate?

The client doesn't provide any certificate to the server.


###  5 Application data

#### 20

What symmetric key cryptography algorithm is being used by the client and
server to encrypt application data (in this case, HTTP messages)?

Cipher Suite: TLS_AES_256_GCM_SHA384 (0x1302)

#### 21

In which of the TLS messages is this symmetric key cryptography algorithm
finally decided and declared?

In the server hello, after receiving the client hello, with all the algorithm that the cleint supports.

#### 22

What is the packet number in your trace for the first encrypted message carrying
application data from client to server?

In my own trace this is packet number 695.

#### 23

What do you think the content of this encrypted application-data is, given that this
trace was generated by fetching the homepage of www.cics.umass.edu?

The first encrypted info is the master symetric key and the second encrypted info is the html page itself i guess.

#### 24

What packet number contains the client-to-server TLS message that shuts down
the TLS connection? Because TLS messages are encrypted in our Wireshark
traces, we can’t actually look inside a TLS message and so we’ll have to make an
educated guess here.

This is just the last packet exchange between client and server.
