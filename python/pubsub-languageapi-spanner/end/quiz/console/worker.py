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

import logging
import sys
import time
import json

from quiz.gcp import pubsub, languageapi, spanner

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
log = logging.getLogger()

def pubsub_callback(message):
    message.ack()
    log.info('Message received')
    log.info(message)
    data = json.loads(message.data)
    score = languageapi.analyze(str(data['feedback']))
    data['score'] = score
    log.info('Score: {}'.format(score))
    spanner.save_feedback(data)
    log.info('Feedback saved')    

def main():
    log.info('Worker starting...')
    pubsub.pull_feedback(pubsub_callback)
    while True:
        time.sleep(60)

if __name__ == '__main__':
    main()
