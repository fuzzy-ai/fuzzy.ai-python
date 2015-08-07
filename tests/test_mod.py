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

def test_evaluate_method():
    assert type(fuzzyio.evaluate) is FunctionType

def test_evaluate_method():
    assert type(fuzzyio.evaluate_with_id) is FunctionType

def test_agent_class():
    assert type(fuzzyio.Agent) is ClassType

def test_agent_constructor():
    a = fuzzyio.Agent(AGENT_ID)
    assert type(a) is InstanceType
    assert type(a.id) is StringType
    assert a.id == AGENT_ID

def test_agent_keyword_constructor():
    name = 'test_agent_keyword_constructor'
    (inputs, outputs, rules) = default_agent()
    a = fuzzyio.Agent(name=name, inputs=inputs, outputs=outputs, rules=rules)
    assert a.inputs == inputs
    assert a.outputs == outputs
    assert a.rules == rules

def test_save_method():
    a = fuzzyio.Agent(AGENT_ID)
    assert type(a.save) is MethodType

def test_save_new_agent():
    name = 'test_save_new_agent'
    (inputs, outputs, rules) = default_agent()
    fuzzyio.setup(API_KEY)
    a = fuzzyio.Agent(name=name, inputs=inputs, outputs=outputs, rules=rules)
    a.save()
    assert type(a.id) is UnicodeType

def test_get_agent():
    name = 'test_get_agent'
    (inputs, outputs, rules) = default_agent()
    fuzzyio.setup(API_KEY)
    a1 = fuzzyio.Agent(name=name, inputs=inputs, outputs=outputs, rules=rules)
    a1.save()
    a2 = fuzzyio.Agent(id=a1.id)
    a2.get()
    assert a2.inputs['input1']['low'][0] == a1.inputs['input1']['low'][0]

def test_get_nonexistent_agent():
    name = 'test_get_nonexistent_agent'
    (inputs, outputs, rules) = default_agent()
    fuzzyio.setup(API_KEY)
    a1 = fuzzyio.Agent(id='***NONEXISTENT***')
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
    fuzzyio.setup(API_KEY)
    a1 = fuzzyio.Agent(name=name, inputs=inputs, outputs=outputs, rules=rules)
    a1.save()
    a1.inputs['input2'] = {
        'low': [0, 1],
        'medium': [0, 1, 2],
        'high': [1, 2]
    }
    a1.save()

    a2 = fuzzyio.Agent(id=a1.id)
    a2.get()

    assert 'input2' in a2.inputs

def test_delete_agent():
    name = 'test_delete_agent'
    (inputs, outputs, rules) = default_agent()
    fuzzyio.setup(API_KEY)
    a1 = fuzzyio.Agent(name=name, inputs=inputs, outputs=outputs, rules=rules)
    a1.save()
    a1.delete()
    # We shouldn't be able to get a deleted agent
    try:
        a2 = fuzzyio.Agent(id=a1.id)
        a2.get()
        assert False
    except fuzzyio.DeletedAgentError:
        assert True
    except:
        assert False

def test_evaluate_agent():
    name = 'test_evaluate_agent'
    (inputs, outputs, rules) = default_agent()
    fuzzyio.setup(API_KEY)
    a = fuzzyio.Agent(name=name, inputs=inputs, outputs=outputs, rules=rules)
    a.save()
    results = a.evaluate({'input1': 1.5})
    assert type(results) is DictionaryType
    assert 'output1' in results
    assert type(results['output1']) is FloatType
    a.delete()

def test_agent_evaluate_with_id():
    name = 'test_agent_evaluate_with_id'
    (inputs, outputs, rules) = default_agent()
    fuzzyio.setup(API_KEY)
    a = fuzzyio.Agent(name=name, inputs=inputs, outputs=outputs, rules=rules)
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
    fuzzyio.setup(API_KEY)
    a = fuzzyio.Agent(name=name, inputs=inputs, outputs=outputs, rules=rules)
    a.save()
    results = fuzzyio.evaluate(a.id, {'input1': 0.5})
    assert type(results) is DictionaryType
    assert 'output1' in results
    assert type(results['output1']) is FloatType
    a.delete()

def test_server_evaluate_with_id():
    name = 'test_server_evaluate_with_id'
    (inputs, outputs, rules) = default_agent()
    fuzzyio.setup(API_KEY)
    a = fuzzyio.Agent(name=name, inputs=inputs, outputs=outputs, rules=rules)
    a.save()
    (results, evid) = fuzzyio.evaluate_with_id(a.id, {'input1': 0.5})
    assert type(results) is DictionaryType
    assert type(evid) is StringType
    assert 'output1' in results
    assert type(results['output1']) is FloatType
    a.delete()

def test_server_feedback():
    name = 'test_server_evaluate_with_id'
    (inputs, outputs, rules) = default_agent()
    fuzzyio.setup(API_KEY)
    a = fuzzyio.Agent(name=name, inputs=inputs, outputs=outputs, rules=rules)
    a.save()
    (results, evid) = fuzzyio.evaluate_with_id(a.id, {'input1': 0.5})
    fb = fuzzyio.feedback(evid, performance=8.1)
    assert type(fb.id) == UnicodeType
    assert type(fb.createdAt) == UnicodeType
    a.delete()

def test_evaluation():
    name = 'test_evaluation'
    (inputs, outputs, rules) = default_agent()
    fuzzyio.setup(API_KEY)
    a = fuzzyio.Agent(name=name, inputs=inputs, outputs=outputs, rules=rules)
    a.save()
    (results, evid) = fuzzyio.evaluate_with_id(a.id, {'input1': 0.5})
    e = fuzzyio.Evaluation(evid)
    assert e.id == evid
    a.delete()

def test_get_evaluation():
    name = 'test_get_evaluation'
    (inputs, outputs, rules) = default_agent()
    fuzzyio.setup(API_KEY)
    a = fuzzyio.Agent(name=name, inputs=inputs, outputs=outputs, rules=rules)
    a.save()
    (results, evid) = fuzzyio.evaluate_with_id(a.id, {'input1': 0.5})
    e = fuzzyio.Evaluation(evid)
    e.get()
    assert type(e.id) == StringType
    assert type(e.input) == DictionaryType
    assert type(e.fuzzified) == DictionaryType
    assert type(e.rules) == ListType
    assert type(e.inferred) == DictionaryType
    assert type(e.clipped) == DictionaryType
    assert type(e.combined) == DictionaryType
    assert type(e.centroid) == DictionaryType
    assert type(e.crisp) == DictionaryType
    assert type(e.createdAt) == UnicodeType
    a.delete()

def test_feedback():
    name = 'test_feedback'
    (inputs, outputs, rules) = default_agent()
    fuzzyio.setup(API_KEY)
    a = fuzzyio.Agent(name=name, inputs=inputs, outputs=outputs, rules=rules)
    a.save()
    (results, evid) = a.evaluate_with_id({'input1': 0.5})
    fb = fuzzyio.Feedback(evid, performance=8.1)
    assert fb.evid == evid
    assert fb.properties['performance'] == 8.1
    a.delete()

def test_save_feedback():
    name = 'test_save_feedback'
    (inputs, outputs, rules) = default_agent()
    fuzzyio.setup(API_KEY)
    a = fuzzyio.Agent(name=name, inputs=inputs, outputs=outputs, rules=rules)
    a.save()
    (results, evid) = a.evaluate_with_id({'input1': 0.5})
    fb = fuzzyio.Feedback(evid, performance=8.1)
    fb.save()
    assert type(fb.id) == UnicodeType
    assert type(fb.createdAt) == UnicodeType
    a.delete()

def test_get_feedback():
    name = 'test_get_feedback'
    (inputs, outputs, rules) = default_agent()
    fuzzyio.setup(API_KEY)
    a = fuzzyio.Agent(name=name, inputs=inputs, outputs=outputs, rules=rules)
    a.save()
    (results, evid) = a.evaluate_with_id({'input1': 0.5})
    fb = fuzzyio.Feedback(evid, performance=8.1)
    fb.save()
    e = fuzzyio.Evaluation(evid)
    fbs = e.feedback()
    assert type(fbs) == ListType
    assert len(fbs) == 1
    assert fbs[0]['id'] == fb.id
    a.delete()
