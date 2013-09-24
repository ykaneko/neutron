# Copyright 2013 Isaku Yamahata <yamahata at private email ne jp>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from neutron.tests.unit.openvswitch import test_agent_scheduler
from neutron.tests.unit.ryu import fake_ryu
from neutron.tests.unit.ryu import test_ryu_plugin


class FakeRyu(object):
    def setUp(self):
        self.fake_ryu = fake_ryu.patch_fake_ryu_client().start()
        super(FakeRyu, self).setUp()


class RyuAgentSchedulerTestCase(
    FakeRyu, test_agent_scheduler.OvsAgentSchedulerTestCase):
    plugin_str = test_ryu_plugin.PLUGIN_NAME


class RyuDhcpAgentNotifierTestCase(
    FakeRyu, test_agent_scheduler.OvsDhcpAgentNotifierTestCase):
    plugin_str = test_ryu_plugin.PLUGIN_NAME


class RyuL3AgentNotifierTestCase(
    FakeRyu, test_agent_scheduler.OvsL3AgentNotifierTestCase):
    plugin_str = test_ryu_plugin.PLUGIN_NAME
