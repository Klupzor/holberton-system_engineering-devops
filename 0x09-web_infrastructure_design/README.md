# Web infrastructure design

Resources
---------


[![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2019/6/1fac233a1f792d74b75a.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUXW7JF5MT%2F20190723%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20190723T155751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=acdb1a37e56f17b79ac31487d40cbc4f56deab88845b0a2faf0237c0ee48d05a)](https://youtu.be/lQNEW76KdYg)

-   [Network basics](https://intranet.hbtn.io/rltoken/Sn9ZSSHjyEW5aRfKvNiZCg "Network basics")
-   [Server](https://intranet.hbtn.io/rltoken/83joH7-HzuV9gBNe16iTrA "Server")
-   [Web server](https://intranet.hbtn.io/rltoken/7moqhXcFOXP6zNMWdsjWjQ "Web server")
-   [DNS](https://intranet.hbtn.io/rltoken/G0a1v98rwb2RHA8VHxo36A "DNS")
-   [Load balancer](https://intranet.hbtn.io/rltoken/H6TVgGaqt13JhXKzJ2rVAA "Load balancer")
-   [Monitoring](https://intranet.hbtn.io/rltoken/JY6524JCvX9dREoNgnQUFw "Monitoring")
-   [Julien's talk #0](https://intranet.hbtn.io/rltoken/f6s2Z0D2ZsNK9_mVyQBpIQ "Julien's talk #0") (The audio quality is a bit rough. We recommend using the subtitles as an aid but don't rely too much on them. You may need to raise the volume a bit.)
-   [Julien's talk #1](https://intranet.hbtn.io/rltoken/95jSTDllW6svkme0HTqjxQ "Julien's talk #1") (The audio quality is a bit rough. We recommend using the subtitles as an aid but don't rely too much on them. You may need to raise the volume a bit.)
-   [What is a database](https://intranet.hbtn.io/rltoken/XLIOfzfuaxPQu39VQ0TLtw "What is a database")
-   [What's the difference between a web server and an app server?](https://intranet.hbtn.io/rltoken/Nb8B47Y2D8SLqQMOKVoQyQ "What's the difference between a web server and an app server?")
-   [DNS record types](https://intranet.hbtn.io/rltoken/pSGVxlKznxONwGEHIXLSwA "DNS record types")
-   [Single point of failure](https://intranet.hbtn.io/rltoken/wYpewVpIp9PSqqL27RPafg "Single point of failure")
-   [How to avoid downtime when deploying new code](https://intranet.hbtn.io/rltoken/Mlvynt0OgLQXrxjrC5Wlnw "How to avoid downtime when deploying new code")
-   [High availability cluster (active-active/active-passive)](https://intranet.hbtn.io/rltoken/POX3jE0S6TChQHSYQraYeQ "High availability cluster (active-active/active-passive)")
-   [What is HTTPS](https://intranet.hbtn.io/rltoken/vfKbtcsS_aON8mi_y759LQ "What is HTTPS")
-   [What is a firewall](https://intranet.hbtn.io/rltoken/HrYI70d_nxUPZeufjUYzIw "What is a firewall")

Tasks
-----

#### 0\. Simple web stack

A lot of websites are powered by simple web infrastructure, a lot of time it is composed of a single server with a [LAMP stack](https://intranet.hbtn.io/rltoken/lBFrw_pTU3_sMuYFptFFsw "LAMP stack").

On a whiteboard, design a one server web infrastructure that hosts the website that is reachable via `www.foobar.com`. Start your explanation by having a user wanting to access your website.

Requirements:

-   You must use:
    -   1 server
    -   1 web server (Nginx)
    -   1 application server
    -   1 application files (your code base)
    -   1 database (MySQL)
    -   1 domain name `foobar.com` configured with a `www` record that points to your server IP `8.8.8.8`
-   You must be able to explain some specifics about this infrastructure:
    -   What is a server
    -   What is the role of the domain name
    -   What type of DNS record `www` is in `www.foobar.com`
    -   What is the role of the web server
    -   What is the role of the application server
    -   What is the role of the database
    -   What is the server using to communicate with the computer of the user requesting the website
-   You must be able to explain what the issues are with this infrastructure:
    -   SPOF
    -   Downtime when maintenance needed (like deploying new code web server needs to be restarted)
    -   Cannot scale if too much incoming traffic

#### 1\. Distributed web infrastructure

On a whiteboard, design a three server web infrastructure that hosts the website `www.foobar.com`.

Requirements:

-   You must add:
    -   2 servers
    -   1 web server (Nginx)
    -   1 application server
    -   1 load-balancer (HAproxy)
    -   1 set of application files (your code base)
    -   1 database (MySQL)
-   You must be able to explain some specifics about this infrastructure:
    -   For every additional element, why you are adding it
    -   What distribution algorithm your load balancer is configured with and how it works
    -   Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both
    -   How a database Primary-Replica (Master-Slave) cluster works
    -   What is the difference between the Primary node and the Replica node in regard to the application
-   You must be able to explain what the issues are with this infrastructure:
    -   Where are SPOF
    -   Security issues (no firewall, no HTTPS)
    -   No monitoring

#### 2\. Secured and monitored web infrastructure

On a whiteboard, design a three server web infrastructure that hosts the website `www.foobar.com`, it must be secured, serve encrypted traffic, and be monitored.

Requirements:

-   You must add:
    -   3 firewalls 
    -   1 SSL certificate to serve `www.foobar.com` over HTTPS
    -   3 monitoring clients (data collector for Sumologic or other monitoring services)
-   You must be able to explain some specifics about this infrastructure:
    -   For every additional element, why you are adding it
    -   What are firewalls for
    -   Why is the traffic served over HTTPS
    -   What monitoring is used for
    -   How the monitoring tool is collecting data
    -   Explain what to do if you want to monitor your web server QPS
-   You must be able to explain what the issues are with this infrastructure:
    -   Why terminating SSL at the load balancer level is an issue
    -   Why having only one MySQL server capable of accepting writes is an issue
    -   Why having servers with all the same components (database, web server and application server) might be a problem

#### 3\. Scale up

Readme

-   [Application server vs web server](https://intranet.hbtn.io/rltoken/XuhRS6VTEMuBHiZU5vo-sQ "Application server vs web server")

Requirements:

-   You must add:
    -   1 server
    -   1 load-balancer (HAproxy) configured as cluster with the other one
    -   Split components (web server, application server, database) with their own server
-   You must be able to explain some specifics about this infrastructure:
    -   For every additional element, why you are adding it
