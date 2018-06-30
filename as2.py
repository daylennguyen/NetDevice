# from py 3.6 std library
# https://docs.python.org/3/library/socket.html#example
import socket
# https://docs.python.org/3/library/ipaddress.html
import ipaddress
import subprocess, re
import os

def get_mask():
	ipstr = '([0-9]{1,3}\.){3}[0-9]{1,3}'
	maskstr = '0x([0-9a-f]{8})'
	ipconfig = subprocess.Popen("ipconfig", stdout=subprocess.PIPE)
	output = ipconfig.stdout.read()
	mask_pattern = re.compile(r"Subnet Mask (\. )*: %s" % ipstr)
	pattern = re.compile(ipstr)
	masklist = []
	for maskaddr in mask_pattern.finditer(str(output)):
		mask = pattern.search(maskaddr.group())
		masklist.append(mask.group())
	return masklist
	
def is_ip4(address):
        ip4str='([0-9]{1,3}\.){3}[0-9]{1,3}'
        ip4_pattern=re.compile(ip4str)
        ip4_match=re.match(r'([0-9]{1,3}\.){3}[0-9]{1,3}',address,re.I)
        if ip4_match:
                return True
        else:
                return False

def is_ip6(address):
        ip6_match = re.match(r'(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}', address, re.I)
        if ip6_match:
                return True
        else:
                return False

def is_fqdn(fqdn):
        fqdn_match=re.match(r'([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}', fqdn, re.I)
        if fqdn_match:
                return True
        else:
                return False

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
		print("\t" + "6. test IPv4/IPv6 with IP address")
		print("\t" + "7. test IPv4/IPv6 with FQDN")
		ans = input("Please enter a command number: ")
		
		if ans == "0":
			print("Goodbye.")
			quit()
			
		elif ans == "1": 
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
			
		elif ans == "2":
			uFQDN = input("Enter a fully qualified domain name (FQDN): ")
			print("The FQDN you entered was ", uFQDN)
			print("the IP address of ", uFQDN,": ", socket.gethostbyname(uFQDN))
			
		elif ans == "3":
			ipAddr = input("Enter an IP address: ")
			FQDN = socket.getfqdn(ipAddr)
			print("The FQDN is: " + FQDN)
			
		elif ans == "4":
			ipAddr = input("Enter a hostname or IP address: ")
			print(os.system("ping " + ipAddr))
			
		elif ans == "5":
			print("TODO")
			
		elif ans == "6":
			ipAddress=input("Enter ip address:")
			if is_ip4(ipAddress):
                                print("ip address you enter is ip4")
                        elif is_ip6(ipAddress):
                                print("ip address you enter is ip6")
                        else:
                                print("invalid ip address.")
                        
		elif ans == "7":
			fqdn = input("Enter fqdn:")
			print(is_fqdn(fqdn))
			
		else:
			print("Invalid option.")
		
		
__main__()
