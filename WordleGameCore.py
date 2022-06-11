import random
from WordleRes import WORDLE_WORDS
from enum import Enum

class WordKeyStatus(Enum):
    NE = 0
    Exist = 1
    Match = 2

class WordleGameCore:
    def __init__(self):
        self.__targetWord = self.__getRandomWord()

    def __getRandomWord(self):
        wordResLength = len(WORDLE_WORDS)
        randomIndex = random.randint(0, wordResLength - 1)
        targetWord = WORDLE_WORDS[randomIndex]
        return targetWord

    def getTargetWord(self):
        return self.__targetWord

    def check(self, word):
        if len(word) == 5:
            ret = []
            Succeed = True
            for index in range(5):
                pos = self.__targetWord.find(word[index])
                if pos < 0:
                    ret.append(WordKeyStatus.NE)
                    Succeed = False
                elif self.__targetWord[index] ==  word[index]:
                    ret.append(WordKeyStatus.Match)
                else:
                    ret.append(WordKeyStatus.Exist)
                    Succeed = False
            return [Succeed, ret]
        else:
            return [False, []]

