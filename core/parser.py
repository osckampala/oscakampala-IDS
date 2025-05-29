def parse_packet(pkt):
    try:
        return {
            "src": pkt[0][1].src if hasattr(pkt[0][1], 'src') else 'N/A',
            "dst": pkt[0][1].dst if hasattr(pkt[0][1], 'dst') else 'N/A',
            "payload": str(bytes(pkt))
        }
    except Exception as e:
        return {"payload": "", "error": str(e)}
