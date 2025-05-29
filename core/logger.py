import logging
from datetime import datetime

# Setup logging
log_file = "logs/alerts.log"
logging.basicConfig(
    filename=log_file,
    filemode="a",
    format="%(asctime)s | %(levelname)s | %(message)s",
    level=logging.INFO
)

def log_alert(rule, packet):
    """
    Logs an alert with detailed rule and packet metadata.
    """
    alert_msg = (
        f"[ALERT 🚨] Rule ID: {rule.get('id', 'N/A')} | "
        f"Name: {rule.get('name')} | "
        f"Protocol: {rule.get('protocol')} | "
        f"Alert: {rule.get('alert')} | "
        f"Packet Summary: {packet.summary()}"
    )
    logging.info(alert_msg)
    print(alert_msg)
