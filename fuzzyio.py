# fuzzy.io.py
#
# Copyright 2015 fuzzy.io
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

import httplib2
import json

class FuzzyIOException:
    "An exception during a fuzzy.io request"

    def __init__(self, message, server=None):
        self.message = message
        self.server = server

class FuzzyAgent:
    "A remote fuzzy agent"

    def __init__(self, server, id):
        self.server = server
        self.id = id

    def evaluate(self, inputs):
        "Evaluate inputs using fuzzy logic. Return outputs."
        return self.server.request("POST", "/agent/%s" % self.id, inputs)

class FuzzyIO:
    "The fuzzy.io service"

    def __init__(self, apiKey, server="https://api.fuzzy.io"):
        self.apiKey = apiKey
        self.server = server
        self.http = httplib2.Http()

    def getAgent(self, agentID):
        return FuzzyAgent(self, agentID)

    def request(self, verb, relative, payload):

        uri = "%s%s" % (self.server, relative)
        body = json.dumps(payload)
        headers = {
            "Authorization": "Bearer %s" % (self.apiKey,),
            "Content-Type": "application/json; charset=utf-8"
        }

        (response, output) = self.http.request(uri, verb, body, headers)

        results = None

        if 'content-type' in response:
            contentType = str.split(response['content-type'], ';', 1)
            if contentType == "application/json":
                results = json.loads(output)

        if response.status != 200:
            if results:
                message = results.message
            else:
                message = output
            raise FuzzyIOException("Bad status code %d: %s" % (response.status, message))

        return results
