from unittest import TestCase

from providers.feodo_tracker import FeodoTracker


class TestFeodoTracker(TestCase):
    def test_get_malicious_ips_list(self):
        provider = FeodoTracker()
        if len(provider.get_malicious_ips_list()) == 0:
            self.fail()

        self.assertRaises(Exception, provider.get_malicious_ips_list())
