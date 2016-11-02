Fuzzy.ai SDK for Python
=======================

A Python package for accessing the fuzzy.ai API.

  https://fuzzy.ai/

License
-------

Copyright 2015 9165584 Canada Corporation <legal@fuzzy.ai>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Installation
------------

You can get this library by forking it from our Github repository::

    git clone https://github.com/fuzzy-ai/fuzzy.ai-python.git

After that, you can just use regular setup.py stuff to set it up.

Testing
-------

Testing uses tox and supports py27, py33, py34, py35 and pypy.

To run for a single version:
  tox -e py27

Basic usage
-----------

When you use the fuzzyai module, you always have to provide your API key first.
Use the setup() function to do that::

  from fuzzyai.client import Client

  client = Client(YOUR_API_KEY)

To have a Fuzzy.ai agent make a decision for you, use the evaluate() function
of the fuzzyai module::

  agent_id = "AGENTIDHERE"

  inputs = {
    "height": 188
    "weight": 88.7
  }

  (outputs, evaluation_id) = client.evaluate(agent_id, inputs)

  # Real-world usage of the run_distance will return some performance
  # metric.

  client.feedback(evaluation_id, {"weight_loss": 0.25})

See also
--------

You can submit issues or make pull requests on Github.

    https://github.com/fuzzy-ai/fuzzy.ai-python

Thanks for using Fuzzy.ai.
