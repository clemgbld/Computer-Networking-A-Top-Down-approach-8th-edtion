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

