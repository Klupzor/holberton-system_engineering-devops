# regular_expressions
*For this project, students are expected to look at this concept:*

-   *[Regular Expression](https://intranet.hbtn.io/concepts/29)*

Background Context
------------------

For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the `//`:

Resources
---------

**Read or watch**:

-   [Regular expressions - basics](https://intranet.hbtn.io/rltoken/SJ2eQ7V2iQlCgLc-L96zWg "Regular expressions - basics")
-   [Regular expressions - advanced](https://intranet.hbtn.io/rltoken/qyjWL-J1_qUaZGR690gH1Q "Regular expressions - advanced")
-   [Rubular is your best friend](https://intranet.hbtn.io/rltoken/WCjn8NgohbQ5NGXEObWZvQ "Rubular is your best friend")
-   [Use a regular expression against a problem: now you have 2 problems](https://intranet.hbtn.io/rltoken/Zfvv_ydOCvJ_YaBB6eDqVw "Use a regular expression against a problem: now you have 2 problems")
-   [Learn Regular Expressions with simple, interactive exercises](https://intranet.hbtn.io/rltoken/Y-OVGcJ5cskdXWIBowiE_A "Learn Regular Expressions with simple, interactive exercises")

Requirements
------------

### General

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your files will be interpreted on Ubuntu 14.04 LTS
-   All your files should end with a new line
-   A `README.md` file, at the root of the folder of the project, is mandatory
-   All your Bash script files must be executable
-   The first line of all your Bash scripts should be exactly `#!/usr/bin/env ruby`
-   All your regex must be built for the Oniguruma library

* * * * *

Quiz questions
--------------

Show

* * * * *

Tasks
-----

 Done?\
Help

#### 0\. Simply matching Holberton mandatory

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/78/just-match-Holberton.png)

Requirements:

-   The regular expression must match `Holberton`
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

Example:

**Repo:**

-   GitHub repository: `holberton-system_engineering-devops`
-   Directory: `0x06-regular_expressions`
-   File: `0-simply_match_holberton.rb`

Get a container

 Done?\
Help

#### 1\. Repetition Token #0 mandatory

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/78/repetition-token-0.png)

Requirements:

-   Find the regular expression that will match the above cases
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

**Repo:**

-   GitHub repository: `holberton-system_engineering-devops`
-   Directory: `0x06-regular_expressions`
-   File: `1-repetition_token_0.rb`

Get a container

 Done?\
Help

#### 2\. Repetition Token #1 mandatory

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/78/repetition-token-1.png)

Requirements:

-   Find the regular expression that will match the above cases
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

**Repo:**

-   GitHub repository: `holberton-system_engineering-devops`
-   Directory: `0x06-regular_expressions`
-   File: `2-repetition_token_1.rb`

Get a container

 Done?\
Help

#### 3\. Repetition Token #2 mandatory

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/78/repetition-token-2.png)

Requirements:

-   Find the regular expression that will match the above cases
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

**Repo:**

-   GitHub repository: `holberton-system_engineering-devops`
-   Directory: `0x06-regular_expressions`
-   File: `3-repetition_token_2.rb`

Get a container

 Done?\
Help

#### 4\. Repetition Token #3 mandatory

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/78/repetition-token-3.png)

Requirements:

-   Find the regular expression that will match the above cases
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

**Repo:**

-   GitHub repository: `holberton-system_engineering-devops`
-   Directory: `0x06-regular_expressions`
-   File: `4-repetition_token_3.rb`

Get a container

 Done?\
Help

#### 5\. Not quite HBTN yet mandatory

Requirements:

-   The regular expression must be exactly matching a string that starts with `h` ends with `n` and can have any single character in between
-   Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

Example:

**Repo:**

-   GitHub repository: `holberton-system_engineering-devops`
-   Directory: `0x06-regular_expressions`
-   File: `5-beginning_and_end.rb`

Get a container

 Done?\
Help

#### 6\. Call me maybe mandatory

This task is brought to you by Holberton mentor [Neha Jain](https://intranet.hbtn.io/rltoken/V4rEpseJEPRMMnfaZPbkgw "Neha Jain"), Senior Software Engineer at LinkedIn.

Requirement:

-   The regular expression must match a 10 digit phone number

Example:

**Repo:**

-   GitHub repository: `holberton-system_engineering-devops`
-   Directory: `0x06-regular_expressions`
-   File: `6-phone_number.rb`

Get a container

 Done?\
Help

#### 7\. OMG WHY ARE YOU SHOUTING? mandatory

![](https://intranet.hbtn.io/images/contents/sysadmin/projects/78/shouting.jpg)

Requirement:

-   The regular expression must be only matching: capital letters

Example:

**Repo:**

-   GitHub repository: `holberton-system_engineering-devops`
-   Directory: `0x06-regular_expressions`
-   File: `7-OMG_WHY_ARE_YOU_SHOUTING.rb`

Get a container

 Done?\
Help

#### 8\. Textme #advanced

This exercise was prepared for you by [Guillaume Plessis](https://intranet.hbtn.io/rltoken/LrcPduX-OTu5lWqTvZg31w "Guillaume Plessis"), VP of Infrastructure at TextMe. It is something he uses daily. You can thank Guillaume for his project [on Twitter](https://intranet.hbtn.io/rltoken/FuFAuWPWMeiCgyQkh3SwZA "on Twitter").

For this task, you'll be taking over Guillaume's responsibilities: one afternoon, a TextMe VoIP Engineer comes to you and explains she wants to run some statistics on the TextMe app text messages transactions.

Requirements:

-   Your script should output: `[SENDER],[RECEIVER],[FLAGS]`
    -   The sender phone number or name (including country code if present)
    -   The receiver phone number or name (including country code if present)
    -   The flags that were used

You can find a [log file here](http://intranet-projects-files.s3.amazonaws.com/holbertonschool-sysadmin_devops/78/text_messages.log "log file here").

Example:

**Repo:**

-   GitHub repository: `holberton-system_engineering-devops`
-   Directory: `0x06-regular_expressions`
-   File: `100-textme.rb`

Get a container

 Done?\
Help

#### 9\. Pass LinkedIn technical interview level0 #advanced

One way to get started in getting a Software Engineering job at LinkedIn is to solve their regex puzzle.

Requirements:

-   Solve LinkedIn regex puzzle: [https://engineering.linkedin.com/puzzle](https://intranet.hbtn.io/rltoken/u2xzwrPyylRY7dpGJJ9P-Q "https://engineering.linkedin.com/puzzle")
-   Provide as an answer file a screenshot containing your contact information, including your Holberton email address

Example:

![](https://s3.amazonaws.com/holbertonintranet/files/correction_system/78/sylvain-kalache-regex-linkedin.png)

Well, I guess I can get into LinkedIn hiring process:

![](https://s3.amazonaws.com/holbertonintranet/files/correction_system/78/passed-linkedin-regex-challenge.gif)

**Repo:**

-   GitHub repository: `holberton-system_engineering-devops`
-   Directory: `0x06-regular_expressions`
-   File: `101-passed_linkedin_regex_challenge.jpg`

Get a container
