# Networking basics #1

Resources
---------

**Read or watch**:

-   [What is localhost](https://intranet.hbtn.io/rltoken/7SedZ8ILSQulYf7xzSbraQ "What is localhost")
-   [What is 0.0.0.0](https://intranet.hbtn.io/rltoken/n5IFAt_OWGJtGW33t7Jfag "What is 0.0.0.0")
-   [What is the hosts file](https://intranet.hbtn.io/rltoken/21l3Uqizr3LpA1ZGrYPg3g "What is the hosts file")
-   [Netcat examples](https://intranet.hbtn.io/rltoken/uMleIIzkRoR2w8EkwItSEg "Netcat examples")

**For reference:**

-   [TCP/IP Illustrated](https://intranet.hbtn.io/rltoken/2jv8NCJl_aAA_W2F9l21EA "TCP/IP Illustrated")

**man or help**:

-   `ifconfig`
-   `telnet`
-   `nc`
-   `cut`

#### 0\. Localhost

What is `localhost`?

1.  A hostname that means *this IP*
2.  A hostname that means *this computer*
3.  An IP attached to a computer


#### 1\. All IPs

What is `0.0.0.0`?

1.  All IPv4 addresses on the local machine
2.  All the IPs
3.  It means null in networking

#### 2\. Change your home IP

Write a Bash script that configures an Ubuntu server with the below requirements.

Requirements:

-   `localhost` resolves to `127.0.0.2`
-   `facebook.com` resolves to `8.8.8.8`.
-   The checker is running on Docker, so make sure to read [this](https://intranet.hbtn.io/rltoken/8PP1z09aHTqgTjyvET6-hg "this")

#### 3\. Show attached IPs

Write a Bash script that displays all active IPv4 IPs on the machine it's executed on.

#### 4\. Port listening on localhost

Write a Bash script that listens on port `98` on `localhost`.

