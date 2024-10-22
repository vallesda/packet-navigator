import pytest
from src.packet import Packet

class TestPacket:
    def setup_method(self):
        self.src = "192.168.1.10"
        self.dest = "192.168.1.20"
        self.protocol = "TCP"
        self.payload = "Hello World!"
        self.packet = Packet(self.src, self.dest, self.protocol, self.payload)

    def test_packet_initialization(self):
        assert self.packet.header["src"] == self.src
        assert self.packet.header["dest"] == self.dest
        assert self.packet.header["type"] == self.protocol
        assert self.packet.header["length"] == len(self.payload) + self.packet.header_length()
        assert self.packet.header["checksum"] is not None
        assert self.packet.payload == self.payload

    def test_header_length(self):
        assert self.packet.header_length() == 20  # Assuming a fixed header length of 20 bytes

    def test_calculate_checksum(self):
        # Test checksum calculation
        expected_checksum = sum(ord(c) for c in self.src + self.dest + self.payload) % 256
        assert self.packet.calculate_checksum(self.src, self.dest, self.payload) == expected_checksum

    def test_checksum_integrity(self):
        payload1 = "Payload 1"
        payload2 = "Payload 2"
        
        packet1 = Packet(self.src, self.dest, "TCP", payload1)
        packet2 = Packet(self.src, self.dest, "TCP", payload2)
        
        assert packet1.calculate_checksum(self.src, self.dest, payload1) != packet2.calculate_checksum(self.src, self.dest, payload2)

if __name__ == "__main__":
    pytest.main()