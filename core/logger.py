import logging
from datetime import datetime
import os

if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(filename='logs/alerts.log', level=logging.INFO, format='%(asctime)s %(message)s')

def log_alert(alert, packet):
    msg = f"ALERT: {alert} | SRC: {packet.get('src')} | DST: {packet.get('dst')}"
    logging.info(msg)
    print(msg)
