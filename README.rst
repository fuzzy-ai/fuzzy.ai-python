fuzzyio
=======

A Python package for accessing the fuzzy.io API.

  https://fuzzy.io/

License
-------

Copyright 2015 9165584 Canada Corporation <legal@fuzzy.io>

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

    git clone https://github.com/fuzzy-io/python.git

After that, you can just use regular setup.py stuff to set it up.

Testing
-------

It uses pytest. However, you need to have a Fuzzy.io API key to make it work.
You can get one by going to::

  https://fuzzy.io/signup

The test script (not the SDK itself!) looks for the API key in the FUZZY_IO_KEY
environment variable. So you can run the test something like this::

  FUZZY_IO_KEY=<yourkeyhere> python -m pytest

Basic usage
-----------

When you use the fuzzyio module, you always have to provide your API key first.
Use the setup() function to do that::

  import fuzzyio

  fuzzyio.setup(YOUR_API_KEY)

To have a Fuzzy.io agent make a decision for you, use the evaluate() function
of the fuzzyio module::

  from __future__ import print_function

  agent_id = "AGENTIDHERE"

  inputs = {
    "height": 188
    "weight": 88.7
  }

  outputs = fuzzyio.evaluate(agent_id, inputs)

  print outputs["run_distance"]

If you need to provide feedback on the evaluation, use the evaluate_with_id()
function to get an ID for the evaluation, and then provide that to the
feedback() function::

  agent_id = "AGENTIDHERE"

  inputs = {
    "height": 188
    "weight": 88.7
  }

  (outputs, evaluation_id) = fuzzyio.evaluate_with_id(agent_id, inputs)

  # Real-world usage of the run_distance will return some performance
  # metric.

  fuzzyio.feedback(evaluation_id, {"weight_loss": 0.25})

Advanced usage
--------------

All of the Fuzzy.io API is available through this SDK.

The Agent class represents a single agent. It includes evaluate() and
evaluate_with_id() methods as well as save() and delete() to change the agent
on the server. Use that last part carefully!

The Evaluation class represents a single evaluation. It includes a get() method
to fetch details about the evaluation and the feedback() method to fetch
feedback on the evaluation.

 The Feedback class represents a single feedback data point. It has a save()
 method to generate feedback for an evaluation.

See also
--------

You can submit issues or make pull requests on Github.

  https://github.com/fuzzy-io/python

Thanks for using Fuzzy.io.
