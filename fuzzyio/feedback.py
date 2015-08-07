# fuzzyio/feedback.py

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

from server import request

class Feedback:
    """Feedback on an evaluation"""
    def __init__(self, evid=None, id=None, **kwargs):
        self.evid = evid
        self.id = id
        self.properties = kwargs
    def save(self):
        if self.id:
            raise Exception("Feedback is immutable")
        (results, response) = request('POST', '/evaluation/%s/feedback' % (self.evid), self.properties)
        self.id = results['id']
        self.createdAt = results['createdAt']
