# fuzzyai/test/test_client.py

# Copyright 2016 9165584 Canada Corporation <legal@fuzzy.ai>
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
import unittest2
from mock import patch, Mock, ANY

from fuzzyai.client import Client

API_KEY = 'test-api-key'
AGENT_ID = 'test-agent-id'


class ClientTests(unittest2.TestCase):

    def test_client_constructor(self):
        c = Client(API_KEY)
        self.assertEqual(c.key, API_KEY)

    def test_client_constructor_with_root(self):
        c = Client(API_KEY, 'https://example.com')
        self.assertEqual(c.root, 'https://example.com')

    def test_client_url(self):
        c = Client(API_KEY)
        url = c._url('/test-path')
        self.assertEqual(url, 'https://api.fuzzy.ai/test-path')

    @patch('requests.post')
    def test_client_evaluate(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {}
        mock_response.headers.get.return_value = 'test-evaluation-id'
        mock_post.return_value = mock_response

        inputs = {'input1': 10}

        c = Client(API_KEY)
        (response, eval_id) = c.evaluate(AGENT_ID, inputs)
        mock_post.assert_called_with(
            c._url('/agent/%s' % AGENT_ID),
            data=json.dumps(inputs),
            headers=ANY,
            params=ANY
        )
        self.assertEqual(response, {})
        self.assertEqual(eval_id, 'test-evaluation-id')

    @patch('requests.post')
    def test_client_feedback(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {}
        mock_post.return_value = mock_response

        metrics = {'metric1': 5}

        c = Client(API_KEY)
        fb = c.feedback('test-evaluation-id', metrics)
        mock_post.assert_called_with(
            c._url('/evaluation/%s/feedback' % 'test-evaluation-id'),
            data=json.dumps(metrics),
            headers=ANY
        )
        self.assertEqual(fb, {})
