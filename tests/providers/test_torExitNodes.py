from unittest import TestCase

from providers.tor_exit_nodes import TorExitNodes


def broken_function():
    raise Exception('This is broken')


class TestTorExitNodes(TestCase):
    def test_get_malicious_ips_list(self):
        provider = TorExitNodes()
        if len(provider.get_malicious_ips_list()) == 0:
            self.fail()

        self.assertRaises(Exception, provider.get_malicious_ips_list())

