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

from google.cloud import pubsub_v1

pub_client = pubsub_v1.PublisherClient()
sub_client = pubsub_v1.SubscriberClient()

project_id = os.getenv('GCLOUD_PROJECT')
topic_path = pub_client.topic_path(project_id, 'feedback')
sub_path = sub_client.subscription_path(project_id, 'worker-subscription')

def pull_from_feedback():

    def callback(message):
        message.ack()

    sub_client.subscribe(sub_path, callback=callback)
    print message
