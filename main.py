from core.capture import start_capture
from core.rules import load_rules, match_rules
from core.logger import log_alert

rules = load_rules("config/rules.yaml")

def handle_packet(packet):
    alert = match_rules(packet, rules)
    if alert:
        log_alert(alert, packet)

if __name__ == "__main__":
    print("[OscaKampala IDS] Starting packet capture on default interface...")
    print("Press Ctrl+C to stop.")
    start_capture(handle_packet)
