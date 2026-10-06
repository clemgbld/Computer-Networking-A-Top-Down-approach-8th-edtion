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
