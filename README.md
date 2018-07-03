# NetDevice
This program is written for Python 3.X. It works on any Windows and Unix-based systems that have basic networking tools installed.
The program gives basic diagnostic information about the computer's network and runs some network tools.
To use it, start the program with "python as2.py", and then follow the menu prompts.

The program uses the socket library to retrieve the computer's IPv4 and IPv6 addresses. The socket library is also used to translate fully qualified domain names to IP addresses and vice versa. Using the socket library allows this part of the program to be operating-system-independent and takes few lines of code to implement.
Finding the computer's subnet mask, pinging a server, and doing a traceroute all require the use of calling the operating system's (usually built-in) utility programs. For example, it uses ipconfig for Windows and ifconfig for Unix-based OSs. By using the regular expression, the method will return the first mathched string in ipconfig/ifconfig process. This method doesn't gurantee the submask is the appropriate one for the ip address that returned from python socket package, but in most cases, they are the same thing.
The program will also automatically detect the type of address inputted, be it IPv4, IPv6, or a FQDN by using regular expressions, which increases usability.
