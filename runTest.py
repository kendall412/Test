import os
import json
import time
import argparse
import pygame 
import random
from random import randint

class Test(object):

	def __init__(self,testType,bgMusic):

		self.bgMusic = bgMusic
		self.testType = testType
		testfile = f"{self.testType}.json"

		with open(testfile,"r") as f:
			self.test = json.load(f)

		self.setupSound()


	def setupSound(self):
		pygame.mixer.init()

		self.wrongPath = os.path.join('sound','wrong')
		self.rightPath = os.path.join('sound','right')
		self.musicPath = os.path.join('sound','music')

		rightCount = 1
		for soundFile in os.listdir(self.rightPath):
			string = f"self.right{rightCount} = pygame.mixer.Sound(os.path.join(self.rightPath,'{soundFile}'))"
			exec(string)
			rightCount +=1

		wrongCount = 1
		for soundFile in os.listdir(self.wrongPath):
			string = f"self.wrong{wrongCount} = pygame.mixer.Sound(os.path.join(self.wrongPath,'{soundFile}'))"
			exec(string)
			wrongCount +=1

		if self.bgMusic:
			backgroundmusic = pygame.mixer.music.load(os.path.join(self.musicPath,'upbeat.mp3'))
			pygame.mixer.music.play(-1)
		else:
			pass


	# def takeTest(self):
	# 	score = 0
	# 	totalQuestion = 0
	# 	questionCount = 1

	# 	rightLimit = len(os.listdir(self.rightPath))
	# 	wrongLimit = len(os.listdir(self.wrongPath))


	# 	for k,v in self.test.items():
			
	# 		print(f"\n\n{questionCount}. {v['question']}")
	# 		print(f" a. {v['a']}")
	# 		print(f" b. {v['b']}")
	# 		print(f" c. {v['c']}")
	# 		ans = input("Answer: ").lower()
	# 		if ans == v['answer']:
	# 			rightSound = f"self.right{randint(1,rightLimit)}.play()"
	# 			exec(rightSound)

	# 			print(f"\nCorrect! The answer is {ans}\n")
	# 			score +=1; totalQuestion +=1; questionCount +=1

	# 		elif ans != v['answer']:
	# 			wrongSound = f"self.wrong{randint(1,wrongLimit)}.play()"
	# 			exec(wrongSound)

	# 			print("\nWrong!\n")
	# 			totalQuestion +=1; questionCount +=1

	# 	if score == totalQuestion:
	# 		print("!!! PERFECT SCORE !!!")
	# 	print(f"Total Score: {score} out of {totalQuestion}\n")
	# 	time.sleep(2)


	def takeTest(self):
		score = 0
		totalQuestion = 0
		questionCount = 1

		rightLimit = len(os.listdir(self.rightPath))
		wrongLimit = len(os.listdir(self.wrongPath))
		testLimit = len(self.test)
		tests = list(range(1,testLimit+1))
		random.shuffle(tests)

		for i in tests:
			testElement = f"q{i}"

			print(f"\n\n{questionCount}.{self.test[testElement]['question']}")
			print(f" a.{self.test[testElement]['a']}")
			print(f" b.{self.test[testElement]['b']}")
			print(f" c.{self.test[testElement]['c']}")
			
			ans = input("Answer: ").lower()
			
			if ans == self.test[testElement]['answer']:
				rightSound = f"self.right{randint(1,rightLimit)}.play()"
				exec(rightSound)

				print(f"\nCorrect!\n")
				score +=1; totalQuestion +=1; questionCount +=1			

			elif ans != self.test[testElement]['answer']:
				wrongSound = f"self.wrong{randint(1,wrongLimit)}.play()"
				exec(wrongSound)

				print("\nWrong!\n")
				totalQuestion +=1; questionCount +=1

		if score == totalQuestion:
			print("!!! PERFECT SCORE !!!")
		print(f"Total Score: {score} out of {totalQuestion} ({(score/totalQuestion)*100:.2f})\n")
		time.sleep(2)


def setArgParseAttributes():
    parser = argparse.ArgumentParser(description="operates tests")
    parser.add_argument('-mu','--music',action='store_true',help="will turn on background music")
    parser.add_argument('-ci','--civicTest',action='store_true',help="will execute Civic test")
    parser.add_argument('-ko','--koreanTest',action='store_true',help="will execute Korean test")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
	args = setArgParseAttributes()

	if args.civicTest: testType="civic"
	elif args.koreanTest: testType="korean"

	if args.music:
		x = Test(testType=testType,bgMusic=True)
	else:
		x = Test(testType=testType,bgMusic=False)

	x.takeTest()