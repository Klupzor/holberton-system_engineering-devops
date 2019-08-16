# Load balancer

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/275/qfdked8.png)

Background Context
------------------

You have been given 2 additional servers:

-   gc-[STUDENT_ID]-web-02-XXXXXXXXXX
-   gc-[STUDENT_ID]-lb-01-XXXXXXXXXX

Let's improve our web stack so that there is [redundancy](https://intranet.hbtn.io/rltoken/QiOC_I-8BeV4aNExIucC9Q "redundancy") for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.

Resources
---------

**Read or watch**:

-   [Introduction to load-balancing and HAproxy](https://intranet.hbtn.io/rltoken/ngIXarEyu8jZwOL3Y30PLQ "Introduction to load-balancing and HAproxy")
-   [HTTP header](https://intranet.hbtn.io/rltoken/v32JmcDrSiOnFBfqzXvs_Q "HTTP header")
-   [Debian/Ubuntu HAProxy packages](https://intranet.hbtn.io/rltoken/BXGrW_6ocecWaOJb7OK_WA "Debian/Ubuntu HAProxy packages")

Requirements
------------

### General

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your files will be interpreted on Ubuntu 16.04 LTS
-   All your files should end with a new line
-   A `README.md` file, at the root of the folder of the project, is mandatory
-   All your Bash script files must be executable
-   Your Bash script must pass `Shellcheck` (version `0.3.7`) without any error
-   The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
-   The second line of all your Bash scripts should be a comment explaining what is the script doing


#### 0\. Double the number of webservers

In this first task you need to configure `web-02` to be identical to `web-01`. Fortunately, you built a Bash script during your [web server project](https://intranet.hbtn.io/rltoken/8oRonOh-zV4e2bmsZ3sxEw "web server project"), and they'll now come in handy to easily configure `web-02`. Remember, always try to automate your work!

Since we're placing our web servers behind a load balancer for this project, we want to add a custom Nginx response header. The goal here is to be able to track which web server is answering our HTTP requests, to understand and track the way a load balancer works. More in the coming tasks.

Requirements:

-   Configure Nginx so that its HTTP response contains a custom header (on `web-01` and `web-02`)
    -   The name of the custom HTTP header must be `X-Served-By`
    -   The value of the custom HTTP header must be the hostname of the server Nginx is running on
-   Write `0-custom_http_response-header` so that it configures a brand new Ubuntu machine to the requirements asked in this task
    -   [Ignore](https://intranet.hbtn.io/rltoken/3AOvROMUNUrzxEWhli4GTw "Ignore") [SC2154](https://intranet.hbtn.io/rltoken/i5f8DYX_rRYFz4hfbG_GJg "SC2154") for `shellcheck`

Example:

If your server's hostnames are not properly configured, follow this [tutorial](https://intranet.hbtn.io/rltoken/h3tE_15RKe2QYWzPsjqNDA "tutorial").

#### 1\. Install your load balancer

Install and configure HAproxy on your `lb-01` server.

Requirements:

-   Configure HAproxy with version equal or greater than 1.5 so that it send traffic to `web-01` and `web-02`
-   Distribute requests using a roundrobin algorithm
-   Make sure that HAproxy can be managed via an init script
-   Make sure that your servers are configured with the right hostnames: `[STUDENT_ID]-web-01` and `[STUDENT_ID]-web-02`. If not, follow this [tutorial](https://intranet.hbtn.io/rltoken/Tb9qeqRrtrO_b2uFpet9rw "tutorial").
-   For your answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements

