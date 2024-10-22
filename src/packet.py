class Packet:
    def __init__(self, src, dest, protocol, payload):
        self.header = {
            'src': src,
            'dest': dest,
            'type': protocol,
            'length': len(payload) + self.header_length(), #standard for ipv4
            'checksum': self.calculate_checksum(src,dest,payload)
        }
        self.payload = payload
    
    def calculate_checksum(self, src, dest, payload):
        # simple checksum calculation, in practice we use more complex algorithms (RC32, MD5)
        checksum = sum(ord(c) for c in src + dest + payload) % 256
        return checksum
    
    def header_length(self):
        return 20 #fix header