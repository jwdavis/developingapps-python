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

from api import api

from flask import Flask
from flask import request, redirect, render_template, make_response
from flask import Response, send_from_directory, url_for

app = Flask(__name__, static_path='/public', static_url_path='')
app.config['DEBUG'] = True

@app.route('/api/quizzes/<quiz_name>', methods=['GET', 'POST'])
def api_quiz(quiz_name):
    if request.method == 'GET':
        questions = api.get_questions(quiz_name)
        response = Response(questions)
        response.headers['Content-Type'] = 'application/json'
        return response
    elif request.method == 'POST':
        answers = request.get_json()
        results = api.grade_quiz(quiz_name, answers)
        response = Response(results)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        return "The Quiz API only supports GET and POST requests"

@app.route('/api/quizzes/feedback/<quiz_name>', methods=['POST'])
def api_feedback(quiz_name):
    feedback = request.get_json()
    print feedback
    result = api.publish_feedback(feedback)
    response = Response(results)
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/client/')
def show_client_home():
    return send_from_directory('public/client', 'index.html')

@app.route('/client/<path:path>')
def serve_client(path):
    return send_from_directory('public/client', path)

@app.route('/')
def show_home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
