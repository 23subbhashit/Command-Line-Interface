import sys
from struct import *
import socket, networking, textwrap

#For Data representation
TAB_1 = '\t - '
TAB_2 = '\t\t - '
TAB_3 = '\t\t\t - '
TAB_4 = '\t\t\t\t - '

DATA_TAB_1 = '\t   '
DATA_TAB_2 = '\t\t   '
DATA_TAB_3 = '\t\t\t   '
DATA_TAB_4 = '\t\t\t\t   '

#Formatting multi line data
def format_multi_line(prefix, string, size=80):
    size -= len(prefix)
    if isinstance(string, bytes):
        string = ''.join(r'\x{:02x}'.format(byte) for byte in string)
        if size % 2:
            size -= 1
    return '\n'.join([prefix + line for line in textwrap.wrap(string, size)])


#Function for getting ethernet Header by passing the raw data packet
def eth_head(raw_data):

	#unpacks ethernet header
	dest, src, prototype = unpack('! 6s 6s H', raw_data[:14])
	dest_mac = get_mac_addr(dest)
	src_mac = get_mac_addr(src)
	proto = socket.htons(prototype)
	data = raw_data[14:]
	
	return dest_mac, src_mac, proto, data
	
	
# Driver function
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
			
			#print('\t\t - ' + 'Data: {}'.format(ipv4[6]))
		
			if ipv4[3] == 6:
				#Printing TCP Header data
				tcp = tcp_head(ipv4[6])
				print(TAB_1 + 'TCP Segment:')
				print(TAB_2 + 'Source Port: {}, Destination Port: {}'.format(tcp[0], tcp[1]))
				print(TAB_2 + 'Sequence: {}, Acknowledgment: {}'.format(tcp[2], tcp[3]))
				print(TAB_2 + 'Flags:')
				print(TAB_3 + 'URG: {}, ACK: {}, PSH:{}'.format(tcp[4], tcp[5], tcp[6]))
				print(TAB_3 + 'RST: {}, SYN: {}, FIN:{}'.format(tcp[7], tcp[8], tcp[9]))
				
				if len(tcp[10]) > 0:
					#Unpacking HTTP Data if there else prints the TCP data
					if tcp[0] == 80 or tcp[1] == 80:
						print(TAB_2 + 'HTTP Data: ')
						try:
							http = networking.HTTP(tcp[10])
							http_info = str(http[10]).split('\n')
							for line in http_info:
								print(DATA_TAB_3 + str(line))
						except:
							print(format_multi_line(DATA_TAB_3, tcp[10]))
					else:
						print(TAB_2 + 'TCP Data:')
						print(format_multi_line(DATA_TAB_3, tcp[10]))
			
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
	
#Function for unpacking TCP Header
def tcp_head(raw_data):

	#Unpacks the header for getting initial information
	(src_port, dest_port, SEQ, ACK, offset_reserved_flag) =  unpack('! H H L L H', raw_data[:14])
	
	#Getting the flag bits
	offset = (offset_reserved_flag >> 12) * 4
	flag_urg = (offset_reserved_flag & 32) >> 5
	flag_ack = (offset_reserved_flag & 16) >> 4
	flag_psh = (offset_reserved_flag & 8) >> 3
	flag_rst = (offset_reserved_flag & 4) >> 2
	flag_syn = (offset_reserved_flag & 2) >> 1
	flag_fin = offset_reserved_flag & 1
	
	#Getting the main packet data after cleaing the packet
	data = raw_data[offset:]
	
	#Returning the important packet information
	return src_port, dest_port, SEQ, ACK, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin, data
	

#Returns a proper IP address
def get_ip(addr):
	return '.'.join(map(str,addr))


#Returns mac address
def get_mac_addr(mac_raw):
    byte_str = map('{:02x}'.format, mac_raw)
    mac_addr = ':'.join(byte_str).upper()
    return mac_addr

#Formats multi-line data
def format_multi_line(prefix, string, size=80):
    size -= len(prefix)
    if isinstance(string, bytes):
        string = ''.join(r'\x{:02x}'.format(byte) for byte in string)
        if size % 2:
            size -= 1
    return '\n'.join([prefix + line for line in textwrap.wrap(string, size)])
    
#Function for ICMP Header
def icmp_head(raw_data):
	icmp_type, code, checksum = unpack('! B B H', raw_data[:4])
	data = raw_data[4:]
        
	return icmp_type, code, checksum, data

#Function for unpacking UDP header
def upd_head(raw_data):
	src_port, dest_port, size = unpack('! H H 2x H', raw_data[:8])
	data = raw_data[8:]
	
	return src_port, dest_port, size, data

#Main function to rum program
main()