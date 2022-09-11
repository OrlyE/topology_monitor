from unittest import TestCase

from malicious_ips_handler import MaliciousIpsHandler


class TestMaliciousIpsHandler(TestCase):

    def test_is_malicious(self):
        handler = MaliciousIpsHandler()
        handler.is_malicious(144)
        self.fail()
