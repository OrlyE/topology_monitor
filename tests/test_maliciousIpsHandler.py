from unittest import TestCase

from malicious_ips_handler import MaliciousIpsHandler


class TestMaliciousIpsHandler(TestCase):

    def test_is_malicious(self):
        handler = MaliciousIpsHandler()
        is_malicious = handler.validate(144)
        if is_malicious:
            self.fail()
