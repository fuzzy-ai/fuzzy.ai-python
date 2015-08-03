# fuzzyio/server.py

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

import httplib2
import json

from errors import HTTPError

class Server:
    """The Fuzzy.io server"""
    def __init__(self, api_key, root="https://api.fuzzy.io"):
        """Arguments:

        api_key -- User's API key. Keep this secret!
        root -- The root of the API. Use this if you test with mocks
        """
        self.api_key = api_key
        self.root = root

    def evaluate_with_id(self, agent_id, inputs):
        """Make a fuzzy controller evaluation and return the results.

        Arguments:

        agent_id -- the Agent to call
        inputs -- dictionary of input values to send

        Returns a tuple of the results and the evaluation ID, used for feedback.
        """
        (results, response) = self.request('POST', '/agent/%s' % agent_id, inputs)
        return (results, response['x-evaluation-id'])

    def evaluate(self, agent_id, inputs):
        """Make a fuzzy controller evaluation and return the results.

        Arguments:

        agent_id -- the Agent to call
        inputs -- dictionary of input values to send

        Returns the results as a dictionary.
        """
        (results, evid) = self.evaluate_with_id(agent_id, inputs)
        return results

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
            raise HTTPError(response.status, message)

        return (results, response)
