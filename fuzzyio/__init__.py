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
from server import Server
from evaluation import Evaluation

from errors import DeletedAgentError, NoSuchAgentError, HTTPError

"""fuzzy.io library

This module provides important classes for accessing the fuzzy.io API.
"""

# XXX: delete this after fixing up the CLI test_has_class

has_legs = False
