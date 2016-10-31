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
from types import StringType

api_key = None
root = "https://api.fuzzy.ai"

http = httplib2.Http()

def request(method, url, payload=None):

    if type(api_key) != StringType:
        raise Exception("API key '%s' is not a string" % (api_key,))

    uri = "%s%s" % (root, url)

    headers = {
        "Authorization": "Bearer %s" % (api_key,)
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
