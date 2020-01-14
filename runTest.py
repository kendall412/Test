import os
import json
import time
import argparse
import pygame 
# for sound effects
# https://www.zapsplat.com/sound-effect-category/fart/
# https://www.pacdv.com/sounds/people_sounds.html

class Test(object):

	def __init__(self,testType):
		self.testType = testType
		testfile = f"{self.testType}.json"

		with open(testfile,"r") as f:
			self.test = json.load(f)

		pygame.mixer.init()
		self.burp = pygame.mixer.Sound(os.path.join('sound','burp.wav'))
		self.yougotit = pygame.mixer.Sound(os.path.join('sound','you got it.wav'))
		backgroundmusic = pygame.mixer.music.load(os.path.join('sound','upbeat.mp3'))
		pygame.mixer.music.play(-1)


	def takeTest(self):
		score = 0
		totalQuestion = 0

		for k,v in self.test.items():
			count = 1
			print(f"\n\n{count}. {v['question']}")
			print(f" a. {v['a']}")
			print(f" b. {v['b']}")
			print(f" c. {v['c']}")
			ans = input("Answer: ").lower()
			if ans == v['answer']:
				self.yougotit.play()
				print(f"\nCorrect! The answer is {ans}\n")
				score +=1
				totalQuestion +=1
				count +=1
			elif ans != v['answer']:
				self.burp.play()
				print("\nWrong!\n")
				totalQuestion +=1
				count +=1

		if score == totalQuestion:
			print("!!! PERFECT SCORE !!!")
		print(f"Total Score: {score} out of {totalQuestion}\n")
		time.sleep(2)


def setArgParseAttributes():
    parser = argparse.ArgumentParser(
        description="operates tests")
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