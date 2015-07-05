#!/usr/bin/env python3

# The MIT License (MIT)
#
# Copyright (c) 2014 Tanay PrabhuDesai
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from flask import Flask, render_template, request, redirect
import json
from question_asker import QuestionSet

app = Flask(__name__)

question_set = QuestionSet()
question_set.load_from_file('./res/questions.json')

f = open('./res/manifest.json','r')
d = json.load(f)

@app.route('/')
def welcome_screen():
	return render_template('welcome.html',info=d)

@app.route('/questions',methods=['POST','GET'])
def questions():
	if request.method == 'POST':
		q_no = int(request.form['q_no'])
		ans = request.form['ans']
		if question_set.check_answer(ans,q_no=q_no):
			q_no +=1
			m = ''
		else:
			m = 'You have entered a wrong answer, please try again'
		if question_set.get_question(q_no=q_no) == False:
			return redirect('/finish')
		return render_template('questions.html',msg=m,info=d,q_no=q_no,question=question_set.get_question(q_no=q_no))
	if request.method == 'GET':
		return render_template('questions.html',msg='',info=d,q_no=0,question=question_set.get_question(q_no=0))

@app.route('/finish',methods=['GET'])
def show_victory():
	return render_template('finish.html',info=d)

if __name__ == '__main__':
	app.run(host='127.0.0.1',debug=True)

