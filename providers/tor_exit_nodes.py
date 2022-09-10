from utils.ssh_connection import call_api
from utils.logger import get_logger
logger = get_logger(stream=True)
import json

class TorExitNodes(object):
    __malicious_ips = None

    def __init__(self):
        url = "https://check.torproject.org/torbulkexitlist"

        response = call_api("get",url)
        logger.info("response  = {resp}".format(resp=response))
        if response.status_code != 200:
            raise Exception("Failed to get malicious ips data from {}. Status code return {}".format(url,
                str(response.status_code)))

        self.__malicious_ips = ((response.content.decode("utf-8")).splitlines())

    def get_malicious_ips_list(self):
        return self.__malicious_ips
