# fuzzyio/agent.py
#
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

from errors import DeletedAgentError, NoSuchAgentError, HTTPError

class Agent:
    """A remote agent that can make evaluations"""
    def __init__(self, server, id=None, name=None, inputs=None, outputs=None, rules=None):
        """Initialize the agent.

        Arguments:

        server -- The Server instance to use for communication.

        Keyword arguments:

        id -- ID of the agent. Use this if the Agent is already created.
        name -- Name of a new Agent.
        inputs -- Input definition for a new agent. Dictionary mapping strings
            (input names) to dictionaries, each of which maps strings (set names)
            to arrays of floats. Each array can have 2 (slope up or down), 3
            (triangle), or 4 (trapezoid) numbers.
        outputs -- Output definition for a new agent. Dictionary mapping strings
            (output names) to dictionaries, each of which maps strings (set names)
            to arrays of floats. Each array can have 2 (slope up or down), 3
            (triangle), or 4 (trapezoid) numbers.
        rules -- Rules for a new agent. An array of strings, each of which is
            a rule like 'IF input1 IS low AND input2 IS high THEN output1 IS medium'.
        """

        self.server = server
        self.id = id
        self.inputs = inputs
        self.outputs = outputs
        self.rules = rules
        self.name = name

    def save(self):
        """Save a new or modified Agent."""
        if self.id:
            self.__update()
        else:
            self.__create()

    def get(self):
        """Get the full Agent information from the server."""
        try:
            (results, response) = self.server.request('GET', '/agent/%s' % self.id)
            self.__fromResults(results)
        except HTTPError as err:
            if err.status == 404:
                raise NoSuchAgentError(self.id)
            elif err.status == 410:
                raise DeletedAgentError(self.id)
            else:
                raise err

    def __update(self):
        payload = {
            'inputs': self.inputs,
            'outputs': self.outputs,
            'rules': self.rules
        }
        if self.name:
            payload['name'] = self.name
        (results, response) = self.server.request('PUT', '/agent/%s' % self.id, payload)
        self.__fromResults(results)

    def __create(self):
        payload = {
            'inputs': self.inputs,
            'outputs': self.outputs,
            'rules': self.rules
        }
        if self.name:
            payload['name'] = self.name
        (results, response) = self.server.request('POST', '/agent', payload)
        self.__fromResults(results)

    def __fromResults(self, results):
        self.id = results['id']
        self.inputs = results['inputs']
        self.outputs = results['outputs']
        self.rules = results['rules']
        self.updatedAt = results['updatedAt']
        self.createdAt = results['createdAt']
        self.latestVersion = results['latestVersion']

    def delete(self):
        """Delete an agent from the server."""
        self.server.request('DELETE', '/agent/%s' % self.id)

    def evaluate_with_id(self, inputs):
        """Make a fuzzy evaluation.

        Arguments:
        inputs -- a dictionary mapping string input names to float values.

        Returns a 2-tuple: a dictionary mapping string output names to float
        values, and a string for the evaluation ID.
        """
        (results, response) = self.server.request('POST', '/agent/%s' % self.id, inputs)
        return (results, response['x-evaluation-id'])

    def evaluate(self, inputs):
        """Make a fuzzy evaluation.

        Arguments:
        inputs -- a dictionary mapping string input names to float values.

        Returns a dictionary mapping string output names to float
        values. If you need the evaluation ID, use evaluate_with_id().
        """
        (results, evid) = self.evaluate_with_id(inputs)
        return results
