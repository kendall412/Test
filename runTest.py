import os
import json
import time
import argparse
import pygame 
from random import randint

class Test(object):

	def __init__(self,testType):
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

		backgroundmusic = pygame.mixer.music.load(os.path.join(self.musicPath,'upbeat.mp3'))
		pygame.mixer.music.play(-1)



	def takeTest(self):
		score = 0
		totalQuestion = 0

		rightLimit = len(os.listdir(self.rightPath))
		wrongLimit = len(os.listdir(self.wrongPath))


		for k,v in self.test.items():
			count = 1
			print(f"\n\n{count}. {v['question']}")
			print(f" a. {v['a']}")
			print(f" b. {v['b']}")
			print(f" c. {v['c']}")
			ans = input("Answer: ").lower()
			if ans == v['answer']:
				rightSound = f"self.right{randint(1,rightLimit)}.play()"
				exec(rightSound)

				print(f"\nCorrect! The answer is {ans}\n")
				score +=1; totalQuestion +=1; count +=1

			elif ans != v['answer']:
				wrongSound = f"self.wrong{randint(1,wrongLimit)}.play()"
				exec(wrongSound)

				print("\nWrong!\n")
				totalQuestion +=1; count +=1

		if score == totalQuestion:
			print("!!! PERFECT SCORE !!!")
		print(f"Total Score: {score} out of {totalQuestion}\n")
		time.sleep(2)


def setArgParseAttributes():
    parser = argparse.ArgumentParser(description="operates tests")
    parser.add_argument('-ci','--civicTest',action='store_true',help="will execute Civic test")
    parser.add_argument('-ko','--koreanTest',action='store_true',help="will execute Korean test")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
	args = setArgParseAttributes()

	if args.civicTest: testType="civic"
	elif args.koreanTest: testType="korean"

	x = Test(testType=testType)
	x.takeTest()