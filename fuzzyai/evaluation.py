# fuzzyio/evaluation.py
#
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

from server import request

class Evaluation:
    """Introspection data on a single evaluation"""
    def __init__(self, evid):
        """Specifies the evaluation we're interested in."""
        self.id = evid
    def get(self):
        (results, headers) = request("GET", "/evaluation/%s" % (self.id,))
        self.__fromResults(results)
    def __fromResults(self, results):
        self.input = results['input']
        self.fuzzified = results['fuzzified']
        self.rules = results['rules']
        self.inferred = results['inferred']
        self.clipped = results['clipped']
        self.combined = results['combined']
        self.centroid = results['centroid']
        self.crisp = results['crisp']
        self.createdAt = results['createdAt']
    def feedback(self):
        (results, headers) = request("GET", "/evaluation/%s/feedback" % (self.id,))
        return results
