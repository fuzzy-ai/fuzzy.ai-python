# fuzzyio

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

from agent import Agent
from evaluation import Evaluation
from feedback import Feedback
from errors import DeletedAgentError, NoSuchAgentError, HTTPError
import server

"""fuzzy.io library

This module provides important classes for accessing the fuzzy.io API.
"""

def setup(api_key, root=None):
    server.api_key = api_key
    if root:
        server.root = root

def evaluate_with_id(agent_id, inputs):
    """Make a fuzzy controller evaluation and return the results.

    Arguments:

    agent_id -- the Agent to call
    inputs -- dictionary of input values to send

    Returns a tuple of the results and the evaluation ID, used for feedback.
    """
    agent = Agent(agent_id)
    return agent.evaluate_with_id(inputs)

def evaluate(agent_id, inputs):
    """Make a fuzzy controller evaluation and return the results.

    Arguments:

    agent_id -- the Agent to call
    inputs -- dictionary of input values to send

    Returns the results as a dictionary.
    """
    agent = Agent(agent_id)
    return agent.evaluate(inputs)
