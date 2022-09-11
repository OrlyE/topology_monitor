from unittest import TestCase

from topologies_generation.topology_generator import create_topologies_datasource
from topology_handler import TopologyHandler

topologies_datasource = create_topologies_datasource()
handler = TopologyHandler(topologies_datasource)


class TestTopologyHandler(TestCase):

    def test__handle_topology(self):
        if self.assertRaises(Exception, handler.handle_topologies()):
            self.fail()

    def test__validate_topology(self):
        self.fail()

    def test_handle_topologies(self):
        self.fail()
