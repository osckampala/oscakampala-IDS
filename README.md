# OscaKampala IDS

OscaKampala IDS is a real-world Python-based Intrusion Detection System focused on modularity, ease of understanding, and contribution readiness.

## 📦 Features
- Packet capturing using Scapy
- Signature-based detection from YAML rules
- Logging of matched alerts to console and file
- Modular Python codebase
- Easy to extend with more protocols or machine learning later

## 🚀 Getting Started

```bash
git clone <your-repo-url>
cd OscaKampala_IDS
pip install -r requirements.txt
sudo python main.py
```

## 👷 Contributing

1. Fork the repo
2. Create a feature branch
3. Make your changes with proper comments
4. Submit a Pull Request

All code must follow PEP8 and include docstrings.

## 📂 Project Structure

```
OscaKampala_IDS/
├── main.py
├── core/
│   ├── capture.py
│   ├── parser.py
│   ├── rules.py
│   └── logger.py
├── config/
│   └── rules.yaml
├── logs/
├── requirements.txt
└── README.md
```

## 📜 License
MIT License
