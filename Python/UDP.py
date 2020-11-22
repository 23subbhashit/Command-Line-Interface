import sys
from struct import *
import socket, networking, textwrap

def main():
	#Creating raw socket to accept data packets from all ports
	s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
	
	while True:
		#Getting raw data and addr 
		raw_data, addr = s.recvfrom(65535)
		
		#Getting the Ethernet Header
		eth = eth_head(raw_data)
		print('Frame :-')
		print('Destination: {}, Source: {}, Protocol: {}'.format(eth[0], eth[1], eth[2]))
		
		#Checks for IPV4 packets
		if eth[2] == 8:
			ipv4 = ipv4_header(eth[3])
			print('\t - ' + 'IPV4 Packet: ')
			print('\t\t - ' + 'Version: {}, Header Length: {}, TTL: {}'.format(ipv4[0], ipv4[1], ipv4[2]))
			print('\t\t - ' + 'Protocol: {}, Source: {}, Target: {}'.format(ipv4[3], ipv4[4], ipv4[5]))
			
            #Displaying the UDP data
			if ipv4[3] == 17:
				udp = udp_head(ipv4[6])
				print('\t - ' + 'UDP Segment:')
				print('\t\t - ' + 'Source Port: {}, Destination Port: {}, Length: {}'.format(udp[0], udp[1], udp[2]))

#Function for getting ethernet Header by passing the raw data packet
def eth_head(raw_data):

	#unpacks ethernet header
	dest, src, prototype = unpack('! 6s 6s H', raw_data[:14])
	dest_mac = get_mac_addr(dest)
	src_mac = get_mac_addr(src)
	proto = socket.htons(prototype)
	data = raw_data[14:]
	
	return dest_mac, src_mac, proto, data

#Function for unpacking ip header
def ipv4_header(raw_data):
	#Unpacking the ipv4 header
	version_head_len = raw_data[0]
	version = version_head_len >> 4
	head_len = (version_head_len & 15) * 4
	ttl, proto, src, target = unpack('! 8x B B 2x 4s 4s', raw_data[:20])
	data = raw_data[head_len:]
	
	src = get_ip(src)
	target = get_ip(target)
	
	return version, head_len, ttl, proto, src, target, data

#Function for unpacking UDP header
def udp_head(raw_data):
	src_port, dest_port, size = unpack('! H H 2x H', raw_data[:8])
	data = raw_data[8:]
	
	return src_port, dest_port, size, data

#Returns mac address
def get_mac_addr(mac_raw):
    byte_str = map('{:02x}'.format, mac_raw)
    mac_addr = ':'.join(byte_str).upper()
    return mac_addr

#Returns a proper IP address
def get_ip(addr):
	return '.'.join(map(str,addr))

#Main function to run program
main()