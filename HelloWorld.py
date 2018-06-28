# from py 3.6 std library

# https://docs.python.org/3/library/socket.html#example
import socket

# https://docs.python.org/3/library/ipaddress.html
import ipaddress
import subprocess, re

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
#mask = get_mask()[0]
#print("The mask is ",mask)

uFQDN = input("Enter a fully qualified domain name (FQDN) or IP addres: ")
def IP_fqdn_converter(instr):
    ip4str=re.compile('([0-9]{1,3}\.){3}[0-9]{1,3}')
    ip6str=re.compile('(.*:){7}(.*)')
    fqdnstr=re.compile('(.*\.){2}(.*)')
    matchip4 = re.match(ip4str,instr,re.I|re.M)
    matchip6 = re.match(ip6str.instr,re.I|re.M)
    matchfqdn = re.match(fqdnstr.instr,re.I|re.M)
    if matchip4:
        print("you enter is ipv4: ",instr);
    elif matchip6:
        print("you enter is ipv6: ",instr);
    elif matchfqdn:
        print("you enter is fqdn: ",instr);
    else:
        print("Please enter valid ip or fqdn");
IP_fqdn_converter(uFQDN)

# print("The FQDN you entered was ", uFQDN)
# print("the IP address of ", uFQDN,": ", socket.gethostbyname(uFQDN))
