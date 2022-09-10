from utils.logger import get_logger
from utils.ssh_connection import call_api
import json

logger = get_logger(stream=True)


class FeodoTracker(object):
    __malicious_ips = []

    def __init__(self):
        url = "https://feodotracker.abuse.ch/downloads/ipblocklist_recommended.json"

        response = call_api("get",url)
        logger.info("response  = {resp}".format(resp=response))
        if response.status_code != 200:
            raise Exception("Failed to get malicious ips data from {}. Status code return {}".format(url,
                                                                                                     str(
                                                                                                         response.status_code)))
        malicious_data = json.loads(response.content.decode("utf-8"))
        for data in malicious_data:
            self.__malicious_ips.append(data["ip_address"])

    def get_malicious_ips_list(self):
        return self.__malicious_ips
