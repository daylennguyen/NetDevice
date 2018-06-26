# from py 3.6 std library

# https://docs.python.org/3/library/socket.html#example
import socket

# https://docs.python.org/3/library/ipaddress.html
import ipaddress


test = "Welcome User!"
print(test)

host_name = socket.gethostname()
host_ipv4 = socket.gethostbyname(host_name)

print("Your Hostname is: ", host_name)
print("From this we've determined your IP address!")
print("Your IP Address (ipv4): ", host_ipv4)
print("\nWe will filter through addr_data_list: ")
print(socket.getaddrinfo(host_name, 0, socket.AF_INET6))

# dump ipv6 data into a list
addr_data_list = socket.getaddrinfo(host_name, 80, socket.AF_INET6)
print("\nYour IP Addresses (ipv6): ")

for addr_data in addr_data_list:
    print(addr_data[4][0])

print("Still need retrieve the subnet information\n")

uFQDN = input("Enter a fully qualified domain name (FQDN): ")

print("The FQDN you entered was ", uFQDN)
print("the IP address of ", uFQDN,": ", socket.gethostbyname(uFQDN))
