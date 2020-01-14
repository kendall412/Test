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

		file = f"{self.testType}.json"

		with open(file,"r") as f:
			self.test = json.load(f)

		pygame.mixer.init()
		self.burp = pygame.mixer.Sound(os.path.join('sound','burp.wav'))
		self.yougotit = pygame.mixer.Sound(os.path.join('sound','you got it.wav'))
		# music = pygame.mixer.music.load('music.mp3')
		# pygame.mixer.music.play(-1)


	def takeTest(self):
		

		score = 0
		totalQuestion = 0

		for k,v in self.test.items():

			print(v['question'])
			print(f"A. {v['a']}")
			print(f"B. {v['b']}")
			print(f"C. {v['c']}")
			ans = input("Answer: ").lower()

			if ans == v['answer']:
				self.yougotit.play()
				print(f"\nCorrect! The answer is {ans}\n")
				score +=1
				totalQuestion +=1
			elif ans != v['answer']:
				self.burp.play()
				print("\nWrong!\n")

				totalQuestion +=1

		if score == totalQuestion:
			print("!!! PERFECT SCORE !!!")
		print(f"Total Score: {score} out of {totalQuestion}\n")
		time.sleep(2)


def setArgParseAttributes():
    parser = argparse.ArgumentParser(
        description="operates tests")
    parser.add_argument('-c','--civicTest',action='store_true',help="will execute Civic test")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = setArgParseAttributes()
    if args.civicTest:
    	x = Test(testType="civic")
    	x.takeTest()