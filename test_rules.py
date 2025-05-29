import sys
import os

# Fix module import path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from core.rules import load_rules, match_rules

def test_rule_matching():
    try:
        rules = load_rules("config/rules.yaml")
    except Exception as e:
        print(f"Failed to load rules: {e}")
        return

    test_packets = [
        {"protocol": "TCP", "payload": "GET /admin HTTP/1.1"},
        {"protocol": "UDP", "payload": "This looks like dns tunneling activity"},
        {"protocol": "TCP", "payload": "SSH connection attempt"},
        {"protocol": "TCP", "payload": "Normal web traffic"},
        {"protocol": "ICMP", "payload": "ping request"},
    ]

    for i, pkt in enumerate(test_packets, 1):
        alert = match_rules(pkt, rules)
        if alert:
            print(f"Packet {i} ALERT: {alert['alert']} (Signature: {alert['signature']}, Protocol: {alert['protocol']})")
        else:
            print(f"Packet {i} No alert.")

if __name__ == "__main__":
    test_rule_matching()
