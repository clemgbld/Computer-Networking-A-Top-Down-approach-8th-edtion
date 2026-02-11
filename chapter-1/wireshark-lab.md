# Wireshark Lab 1

The goal of this first lab was primarily to introduce you to Wireshark. The following
questions will demonstrate that you’ve been able to get Wireshark up and running, and
have explored some of its capabilities. Answer the following questions, based on your
Wireshark experimentation:

## 1

List 3 different protocols that appear in the protocol column in the unfiltered
packet-listing window in step 7 above.

- HTTP
- DNS
- TCP

## 2
How long did it take from when the HTTP GET message was sent until the HTTP
OK reply was received? (By default, the value of the Time column in the packet-
listing window is the amount of time, in seconds, since Wireshark tracing began.
To display the Time field in time-of-day format, select the Wireshark View pull
down menu, then select Time Display Format, then select Time-of-day.)

The get message arrived at 20:56:31.079978
the ok response arrived at 20:56:31.173656

So a bit less than 1ms.

## 3
What is the Internet address of the gaia.cs.umass.edu (also known as www-
net.cs.umass.edu)? What is the Internet address of your computer?

gaia.cs.umass.edu address: 128.119.245.12

My computer address: 192.168.1.56

## 4

[screen](./wirshark-lab-1-ex-4.PNG)
