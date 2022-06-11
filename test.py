from operator import length_hint
from unittest import result
from zoneinfo import available_timezones
from WordleGameCore import WordleGameCore
from WordleGameCore import WordKeyStatus
from WordleGameHelper import WordleGameHelper
from WordleRes import WORDLE_WORDS
import random

def showStatus(status):
    for item in status:
        if item == WordKeyStatus.Match:
            print("2 ")
        if item == WordKeyStatus.Exist:
            print("1 ")
        if item ==  WordKeyStatus.NE:
            print("0 ")


if __name__ == '__main__':
    game = WordleGameCore()
    helper = WordleGameHelper()
    
    print("Target:", game.getTargetWord())

    times = 0
    availableWords = WORDLE_WORDS
    while True:
        times = times + 1
        length = len(availableWords)
        randomIndex = random.randint(0, length - 1)
        testWord = availableWords[randomIndex]

        [succeed, status] = game.check(testWord)
        if succeed:
            print("Succeed! target word is ", testWord, " times ", times)
            break

        intResult = [value.value for value in status]
        helper.updateConditions(testWord, status)
        availableWords = helper.getaAvailableWords()
        print("times:", times, " word:", testWord, " result:", intResult, "lastNum:", len(availableWords))
