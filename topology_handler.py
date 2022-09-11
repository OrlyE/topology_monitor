from typing import Iterable
from topologies_generation.topology_generator import create_topologies_datasource
from malicious_ips_handler import MaliciousIpsHandler
from utils.logger import Logger

logger = Logger.get_logger(__name__, log_level="INFO")


class TopologyHandler:
    def __init__(self, topologies_datasource: Iterable[dict]):
        self._topologies_datasource = topologies_datasource
        self._malicious_ips_handler = MaliciousIpsHandler()

    def _handle_topology(self, topology: dict):
        ip_address = topology["destination_ip"]

        if self._malicious_ips_handler.validate(ip_address):
            logger.warn("Found malicious ip: {}".format(ip_address))

    @staticmethod
    def _validate_topology(topology: dict) -> bool:
        return {"source_ip", "source_port", "destination_ip", "destination_port", "topology_timestamp"} \
            .issubset(topology.keys())

    def handle_topologies(self):
        filtered_topologies = (topology for topology in self._topologies_datasource if
                               self._validate_topology(topology))

        for topology in filtered_topologies:
            logger.info("Handling topology.")
            self._handle_topology(topology)
            logger.info("Done handling topology.")



def main():
    topologies_datasource = create_topologies_datasource()
    TopologyHandler(topologies_datasource).handle_topologies()


if __name__ == "__main__":
    main()
