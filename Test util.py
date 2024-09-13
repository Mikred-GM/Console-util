import unittest
from io import StringIO
from scapy.layers.inet import IP
from scapy.all import Ether, sendp

class TestPcapMatcher(unittest.TestCase):
    def setUp(self):
        self.pcap1 = StringIO("""
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
Ether / IP / UDP / Raw
