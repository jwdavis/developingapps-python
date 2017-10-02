# Copyright 2017 Google Inc.
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

import os
import json
import logging

from google.cloud import pubsub_v1

"""Create publisher and subscriber clients using new v1 API
"""
publisher = pubsub_v1.PublisherClient()
sub_client = pubsub_v1.SubscriberClient()

"""Grab the project id from environment variable
"""
project_id = os.getenv('GCLOUD_PROJECT')

"""Construct paths to topic and subscription
"""
topic_path = publisher.topic_path(project_id, 'feedback')
sub_path = sub_client.subscription_path(project_id, 'worker-subscription')

"""publish_feedback

Publishes feedback info 
- jsonify feedback object
- encode as bytestring
- publish message
- return result
"""
def publish_feedback(feedback):
    payload = json.dumps(feedback, indent=2, sort_keys=True)
    data = payload.encode('utf-8')
    future = publisher.publish(topic_path, data=data)
    return future.result()

"""pull_feedback

Starts pulling messages from subscription
- receive callback function from calling module
- initiate the pull providing the callback function
"""
def pull_feedback(callback):
    sub_client.subscribe(sub_path, callback=callback)
