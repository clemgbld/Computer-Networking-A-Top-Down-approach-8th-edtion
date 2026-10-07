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

