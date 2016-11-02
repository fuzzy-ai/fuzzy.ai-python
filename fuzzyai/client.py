# fuzzyio/client.py

# Copyright 2015 9165584 Canada Corporation <legal@fuzzy.ai>
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

import json
import requests

from version import VERSION


class Client:
    """ Client object for interacting with the Fuzzy.ai API
    """

    def __init__(self, key, root='https://api.fuzzy.ai'):
        self.key = key
        self.root = root
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % self.key,
            'User-Agent': 'fuzzy.ai-python/%s' % VERSION

        }

    def evaluate(self, agent_id, inputs, meta=False):
        """Make a fuzzy controller evaluation and return the results.

        Arguments:

        agent_id -- the Agent to call
        inputs -- dictionary of input values to send

        Returns a tuple of the results and the evaluation ID.
        """
        url = self._url('/agent/%s' % agent_id)
        params = {}
        if meta:
            params = {'meta': 'true'}
        data = json.dumps(inputs)
        r = requests.post(url, params=params, data=data, headers=self.headers)
        return (r.json(), r.headers.get('x-evaluation-id'))

    def feedback(self, evaluation_id, metrics):
        """Make feedback on an evaluation.

        Arguments:

        evaluation_id -- the Evaluation to provide feedback on
        metrics -- an object mapping metric names to numeric values

        Returns the results as a Feedback object.
        """
        url = self._url('/evaluation/%s/feedback' % evaluation_id)
        data = json.dumps(metrics)
        r = requests.post(url, data=data, headers=self.headers)
        return r.json()

    def _url(self, path):
        return self.root + path
