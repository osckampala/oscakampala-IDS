import yaml

def load_rules(path='config/rules.yaml'):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def match_rules(packet, rules):
    payload = packet.get("payload", "").lower()
    for rule in rules:
        if rule["protocol"].lower() in payload and rule["signature"].lower() in payload:
            return rule["alert"]
    return None
