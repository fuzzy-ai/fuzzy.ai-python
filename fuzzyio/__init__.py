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

# XXX: delete this after fixing up the CLI test_has_class

from __future__ import print_function
import httplib2
import json

has_legs = False

class Agent:
    def __init__(self, server, id=None, name=None, inputs=None, outputs=None, rules=None):
        self.server = server
        self.id = id
        self.inputs = inputs
        self.outputs = outputs
        self.rules = rules
        self.name = name

    def save(self):
        if self.id:
            self.__update()
        else:
            self.__create()

    def get(self):
        results = self.server.request('GET', '/agent/%s' % self.id)
        self.__fromResults(results)

    def __update(self):
        payload = {
            'inputs': self.inputs,
            'outputs': self.outputs,
            'rules': self.rules
        }
        if self.name:
            payload['name'] = self.name
        results = self.server.request('PUT', '/agent/%s' % self.id, payload)
        self.__fromResults(results)

    def __create(self):
        payload = {
            'inputs': self.inputs,
            'outputs': self.outputs,
            'rules': self.rules
        }
        if self.name:
            payload['name'] = self.name
        results = self.server.request('POST', '/agent', payload)
        self.__fromResults(results)

    def __fromResults(self, results):
        self.id = results['id']
        self.inputs = results['inputs']
        self.outputs = results['outputs']
        self.rules = results['rules']
        self.updatedAt = results['updatedAt']
        self.createdAt = results['createdAt']
        self.latestVersion = results['latestVersion']

class Server:
    def __init__(self, api_key, root="https://api.fuzzy.io"):
        self.api_key = api_key
        self.root = root

    def request(self, method, url, payload=None):

        http = httplib2.Http()
        uri = "%s%s" % (self.root, url)
        headers = {
            "Authorization": "Bearer %s" % (self.api_key,)
        }

        if payload:
            headers["Content-Type"] = "application/json; charset=utf-8"
            body = json.dumps(payload)
        else:
            body = None

        (response, output) = http.request(uri, method, body, headers)

        results = None

        if 'content-type' in response:
            contentType = str.split(response['content-type'], ';', 1)
            if contentType[0] == "application/json":
                results = json.loads(output)

        if response.status != 200:
            if results:
                message = results["message"]
            else:
                message = output
            raise Exception("Bad status code %d: %s" % (response.status, message))

        return results

    def evaluate(self, agent_id, inputs):
        pass
