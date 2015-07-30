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

from __future__ import print_function
import fuzzyio
from types import *
import os

API_KEY = os.environ["FUZZY_IO_KEY"]
AGENT_ID = "ABABABAB"

def default_agent():
    inputs = {
        'input1': {
            'low': [0, 1],
            'medium': [0, 1, 2],
            'high': [1, 2]
        }
    }
    outputs = {
        'output1': {
            'low': [0, 1],
            'medium': [0, 1, 2],
            'high': [1, 2]
        }
    }
    rules = [
        "IF input1 IS low THEN output1 IS low",
        "IF input1 IS medium THEN output1 IS medium",
        "IF input1 IS high THEN output1 IS high"
    ]
    return (inputs, outputs, rules)

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

def test_agent_keyword_constructor():
    name = 'test_agent_keyword_constructor'
    (inputs, outputs, rules) = default_agent()
    f = fuzzyio.Server(API_KEY)
    a = fuzzyio.Agent(f, name=name, inputs=inputs, outputs=outputs, rules=rules)
    assert a.inputs == inputs
    assert a.outputs == outputs
    assert a.rules == rules

def test_save_method():
    f = fuzzyio.Server(API_KEY)
    a = fuzzyio.Agent(f, AGENT_ID)
    assert type(a.save) is MethodType

def test_save_new_agent():
    name = 'test_save_new_agent'
    (inputs, outputs, rules) = default_agent()
    f = fuzzyio.Server(API_KEY)
    a = fuzzyio.Agent(f, name=name, inputs=inputs, outputs=outputs, rules=rules)
    a.save()
    assert type(a.id) is UnicodeType

def test_get_agent():
    name = 'test_get_agent'
    (inputs, outputs, rules) = default_agent()
    f = fuzzyio.Server(API_KEY)
    a1 = fuzzyio.Agent(f, name=name, inputs=inputs, outputs=outputs, rules=rules)
    a1.save()
    a2 = fuzzyio.Agent(f, id=a1.id)
    a2.get()
    assert a2.inputs['input1']['low'][0] == a1.inputs['input1']['low'][0]

def test_get_nonexistent_agent():
    name = 'test_get_nonexistent_agent'
    (inputs, outputs, rules) = default_agent()
    f = fuzzyio.Server(API_KEY)
    a1 = fuzzyio.Agent(f, id='***NONEXISTENT***')
    try:
        a1.get()
        assert False
    except fuzzyio.NoSuchAgentError:
        assert True
    except:
        assert False

def test_update_agent():
    name = 'test_update_agent'
    (inputs, outputs, rules) = default_agent()
    f = fuzzyio.Server(API_KEY)
    a1 = fuzzyio.Agent(f, name=name, inputs=inputs, outputs=outputs, rules=rules)
    a1.save()
    a1.inputs['input2'] = {
        'low': [0, 1],
        'medium': [0, 1, 2],
        'high': [1, 2]
    }
    a1.save()

    a2 = fuzzyio.Agent(f, id=a1.id)
    a2.get()

    assert 'input2' in a2.inputs

def test_delete_agent():
    name = 'test_delete_agent'
    (inputs, outputs, rules) = default_agent()
    f = fuzzyio.Server(API_KEY)
    a1 = fuzzyio.Agent(f, name=name, inputs=inputs, outputs=outputs, rules=rules)
    a1.save()
    a1.delete()
    # We shouldn't be able to get a deleted agent
    try:
        a2 = fuzzyio.Agent(f, id=a1.id)
        a2.get()
        assert False
    except fuzzyio.DeletedAgentError:
        assert True
    except:
        assert False

def test_evaluate_agent():
    name = 'test_evaluate_agent'
    (inputs, outputs, rules) = default_agent()
    f = fuzzyio.Server(API_KEY)
    a = fuzzyio.Agent(f, name=name, inputs=inputs, outputs=outputs, rules=rules)
    a.save()
    results = a.evaluate({'input1': 1.5})
    assert type(results) is DictionaryType
    assert 'output1' in results
    assert type(results['output1']) is FloatType
    a.delete()

def test_agent_evaluate_with_id():
    name = 'test_evaluate_agent'
    (inputs, outputs, rules) = default_agent()
    f = fuzzyio.Server(API_KEY)
    a = fuzzyio.Agent(f, name=name, inputs=inputs, outputs=outputs, rules=rules)
    a.save()
    (results, evid) = a.evaluate_with_id({'input1': 1.5})
    assert type(evid) is StringType
    assert type(results) is DictionaryType
    assert 'output1' in results
    assert type(results['output1']) is FloatType
    a.delete()

def test_server_evaluate():
    name = 'test_evaluate_agent'
    (inputs, outputs, rules) = default_agent()
    f = fuzzyio.Server(API_KEY)
    a = fuzzyio.Agent(f, name=name, inputs=inputs, outputs=outputs, rules=rules)
    a.save()
    results = f.evaluate(a.id, {'input1': 0.5})
    assert type(results) is DictionaryType
    assert 'output1' in results
    assert type(results['output1']) is FloatType
    a.delete()

def test_server_evaluate_with_id():
    name = 'test_evaluate_agent'
    (inputs, outputs, rules) = default_agent()
    f = fuzzyio.Server(API_KEY)
    a = fuzzyio.Agent(f, name=name, inputs=inputs, outputs=outputs, rules=rules)
    a.save()
    (results, evid) = f.evaluate_with_id(a.id, {'input1': 0.5})
    assert type(results) is DictionaryType
    assert type(evid) is StringType
    assert 'output1' in results
    assert type(results['output1']) is FloatType
    a.delete()
