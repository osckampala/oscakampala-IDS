from scapy.all import sniff
from core.parser import parse_packet

def start_capture(callback, iface=None):
    sniff(iface=iface, prn=lambda pkt: callback(parse_packet(pkt)), store=0)
