from providers.feodo_tracker import FeodoTracker
from providers.tor_exit_nodes import TorExitNodes


class MaliciousIpsHandler(object):
    providers = None

    def __init__(self):
        self.providers = [
            TorExitNodes(),
            FeodoTracker()
        ]

    def is_malicious(self, ip_address):
        for provider in self.providers:
            if ip_address in provider.get_malicious_ips_list():
                return True
        return False
