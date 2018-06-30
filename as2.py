# from py 3.6 std library
# https://docs.python.org/3/library/socket.html#example
import socket
# https://docs.python.org/3/library/ipaddress.html
import ipaddress
import subprocess, re
import os

def isIPv4(str):
	pattern = r'([0-9]{1,3}\.){3}[0-9]{1,3}'
	return re.match(pattern, str)

def isIPv6(str):
	pattern = r'(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}'
	return re.match(pattern, str)

def isFQDN(str):
	pattern = r'([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}'
	return re.match(pattern, str)

# todo: make to work with Linux
def get_mask():
	ipstr = '([0-9]{1,3}\.){3}[0-9]{1,3}'
	#maskstr = '0x([0-9a-f]{8})'
	ipconfig = subprocess.Popen("ipconfig", stdout=subprocess.PIPE)
	output = ipconfig.stdout.read()
	mask_pattern = re.compile(r"Subnet Mask (\. )*: %s" % ipstr)
	pattern = re.compile(ipstr)
	masklist = []
	for maskaddr in mask_pattern.finditer(str(output)):
		mask = pattern.search(maskaddr.group())
		masklist.append(mask.group())
	return masklist
	
def showInfo():
	host_name = socket.gethostname()
	print("Your Hostname is: ", host_name)
	host_ipv4 = socket.gethostbyname(host_name)
	print("Your IP Address (ipv4): ", host_ipv4)
	addr_data_list = socket.getaddrinfo(host_name, 80, socket.AF_INET6)
	print("Your IP Addresses (ipv6): ", end="")
	for addr_data in addr_data_list:
		print(addr_data[4][0], end="")
	print("")
	mask = get_mask()[0]
	print("The mask is ", mask)
	
def fqdnToIp():
	uFQDN = input("Enter a fully qualified domain name (FQDN): ")
	if not isFQDN(uFQDN):
		print("Not a FQDN!")
		return
	print("The FQDN you entered was ", uFQDN)
	print("the IP address of ", uFQDN,": ", socket.gethostbyname(uFQDN))
	
def ipToFqdn():
	ipAddr = input("Enter an IP address: ")
	if isIPv4(ipAddr):
		print("You entered an Ipv4 address.")
	elif isIPv6(ipAddr):
		print("You entered an Ipv6 address.")
	else:
		print("Not an IP address!")
		return
	FQDN = socket.getfqdn(ipAddr)
	print("The FQDN is: " + FQDN)
	
def doPing():
	name = input("Enter a hostname or IP address: ")
	if isIPv4(name):
		print("You entered an Ipv4 address.")
	elif isIPv6(name):
		print("You entered an Ipv6 address.")
	elif isFQDN(name):
		print("You entered a FQDN.")
	else:
		print("Invalid ping target!")
		return
	
	# should work for all systems
	print(os.system("ping " + name))
	
def doTraceRoute():
	name = input("Enter a hostname or IP address: ")
	if isIPv4(name):
		print("You entered an Ipv4 address.")
	elif isIPv6(name):
		print("You entered an Ipv6 address.")
	elif isFQDN(name):
		print("You entered a FQDN.")
	else:
		print("Invalid traceroute target!")
		return
	
	if os.name == 'nt': # windows system
		print(os.system("tracert " + name))
	else:
		print(os.system("traceroute " + name))
	
	
def __main__():
	# needed?
	#host_name = socket.gethostname()
	#print(socket.getaddrinfo(host_name, 0, socket.AF_INET6))

	while True:
		print("\n\t" + "0. Exit")
		print("\t" + "1. Show machine's IPv4, IPv6, and subnet information.")
		print("\t" + "2. Get an IP from a FQDN")
		print("\t" + "3. Get a FQDN from an IP")
		print("\t" + "4. Ping a server")
		print("\t" + "5. trace route to target")
		num = input("Please enter a command number: ")
		
		if num == "0":
			print("Goodbye.")
			quit()
		elif num == "1": 
			showInfo()
		elif num == "2":
			fqdnToIp()
		elif num == "3":
			ipToFqdn()
		elif num == "4":
			doPing()
		elif num == "5":
			doTraceRoute()
		else:
			print("Invalid option.")
		
__main__()