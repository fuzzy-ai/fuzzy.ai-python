# test_mod.py

# Copyright 2015 9165584 Canada Corporation <legal@fuzzy.io>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import fuzzyio
from types import *

API_KEY = "BABABABA"
AGENT_ID = "ABABABAB"

def test_server_class():
    assert type(fuzzyio.Server) is ClassType

def test_server_constructor():
    f = fuzzyio.Server(API_KEY)
    assert type(f) is InstanceType

def test_evaluate_method():
    f = fuzzyio.Server(API_KEY)
    assert type(f.evaluate) is MethodType

def test_agent_class():
    assert type(fuzzyio.Agent) is ClassType

def test_agent_constructor():
    f = fuzzyio.Server(API_KEY)
    a = fuzzyio.Agent(f, AGENT_ID)
    assert type(a) is InstanceType
    assert type(a.id) is StringType
    assert a.id == AGENT_ID
