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

import json

class QuestionSet:
	def __init__(self):
		self.questions = []
		self.current_question = 0
		self.msg_winner = ''
		self.msg_looser = ''
	def load_from_file(self,filename):
		f = open(filename,'r')
		q_raw = json.load(f)
		self.questions = q_raw["questions"] #TODO add more stuff here
		for q in self.questions:
			for i,ans in enumerate(q['a']):
				ans = ans.split(' ')
				ans = ''.join(ans)
				ans = ans.lower()
				q['a'][i] = ans
		f.close()
	def check_answer(self,ans,q_no=None):
		ans = ans.split(' ')
		ans = ''.join(ans)
		ans = ans.lower()
		if q_no == None:
			a = self.questions[self.current_question]['a']
			self.current_question += 1
		else:
			if q_no >= len(self.questions):
				return False
			a = self.questions[q_no]['a']
		return ans in a
	def get_question(self,q_no=None):
		if q_no == None:
			if self.current_question >= len(self.questions):
				return False
			a = self.questions[self.current_question]['q']
		else:
			if q_no >= len(self.questions):
				return False
			a = self.questions[q_no]['q']
		return a
	def has_finished(self,q_no=None):
		if self.current_question >= len(self.questions):
			return True
		if q_no >= len(self.questions):
			return True
		return False
def main():
	print('Answer the following questions')

	question_set = QuestionSet()
	question_set.load_from_file('questions.json')

	while True:
		q = question_set.get_question()
		if not q:
			break
		print('\n'+q)
		inp = input()
		if question_set.check_answer(inp):
			print('Correct!')
		else:
			print('Wrong!')

if __name__ == '__main__':
	main()