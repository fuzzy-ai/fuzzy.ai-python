# fuzzyio/errors/deleted_agent.py
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


class DeletedAgentError(Exception):
    """Error thrown when accessing an agent that was deleted"""
    def __init__(self, id):
        """Arguments:

        id -- ID of the agent
        """
        self.id = id

    def __str__(self):
        return "DeletedAgentError <%s>" % (self.id,)


class HTTPError(Exception):
    """An error that occurs during an HTTP request"""
    def __init__(self, status, message):
        """Arguments:

        status -- Numerical HTTP status
        message -- Message from the server
        """
        self.status = status
        self.message = message

    def __str__(self):
        return "HTTPError <%d>: '%s'" % (self.status, self.message)


class NoSuchAgentError(Exception):
    """Error thrown when accessing an agent that never existed"""
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return "NoSuchAgentError <%s>" % (self.id,)
