import yaml
import os

def load_rules(path):
    """
    Load detection rules from a YAML file.
    Returns a list of rule dictionaries.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Rules file not found: {path}")

    with open(path, "r") as f:
        try:
            rules = yaml.safe_load(f)
        except yaml.YAMLError as e:
            raise ValueError(f"Error parsing YAML file {path}: {e}")

    if not rules:
        raise ValueError(f"Rules file {path} is empty.")

    if not isinstance(rules, list):
        raise ValueError(f"Rules file {path} must contain a list of rule dictionaries.")

    # Optionally check that each rule is dict and has required keys
    for i, rule in enumerate(rules):
        if not isinstance(rule, dict):
            raise ValueError(f"Rule #{i+1} is not a dictionary.")
        for key in ("protocol", "signature", "alert"):
            if key not in rule:
                raise ValueError(f"Rule #{i+1} missing required key: '{key}'")

    return rules

def match_rules(packet, rules):
    """
    Match a captured packet against detection rules.

    Args:
      packet (dict): Must have keys 'protocol' and 'payload', both strings.
      rules (list): List of dicts loaded from YAML.

    Returns:
      dict: Alert info if matched, else None.
    """
    protocol = packet.get("protocol", "").lower()
    payload = packet.get("payload", "").lower()

    for rule in rules:
        if ("protocol" in rule and "signature" in rule and "alert" in rule):
            if rule["protocol"].lower() == protocol and rule["signature"].lower() in payload:
                return {
                    "alert": rule["alert"],
                    "signature": rule["signature"],
                    "protocol": rule["protocol"]
                }
    return None
