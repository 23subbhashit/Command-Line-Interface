import sys
import socket
# import dpkt, pcap
def TCP():
    print(sys.argv[1])
print("Output from TCP")
TCP()


# pc = pcap.pcap()     # construct pcap object
# pc.setfilter('icmp') # filter out unwanted packets
# for timestamp, packet in pc:
#     print(dpkt.ethernet.Ethernet(packet))