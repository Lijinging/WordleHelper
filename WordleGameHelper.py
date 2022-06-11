from WordleRes import WORDLE_WORDS
from WordleGameCore import WordKeyStatus
from enum import Enum

class WordleGameHelper:

    class LetterPositionInfo:
        def __init__(self):
            self.determinedPosition = set([])
            self.excludePosition = set([])

    def __init__(self):
        self.__availableWords = WORDLE_WORDS
        self.__excludeLetters = set([]) # [char1, char2, ...]
        self.__includeLetters = {} # {char: LetterPositionInfo, ...}

    def __isAvailable(self, word) -> bool:
        for letter in self.__excludeLetters:
            if letter in word:
                return False
        for letter in self.__includeLetters:
            if letter not in word:
                return False
            for pos in self.__includeLetters[letter].determinedPosition:
                if word[pos] != letter:
                    return False
            for pos in self.__includeLetters[letter].excludePosition:
                if word[pos] == letter:
                    return False
        return True                

    def updateConditions(self, word, status):
        for index in range(5):
            if status[index] == WordKeyStatus.Match:
                if word[index] not in self.__includeLetters:
                    self.__includeLetters[word[index]] = self.LetterPositionInfo()
                self.__includeLetters[word[index]].determinedPosition.add(index)
            elif status[index] == WordKeyStatus.Exist:
                if word[index] not in self.__includeLetters:
                    self.__includeLetters[word[index]] = self.LetterPositionInfo()
                self.__includeLetters[word[index]].excludePosition.add(index)
            else:
                self.__excludeLetters.add(word[index])

    def getaAvailableWords(self):
        newAvailableWords = [word for word in self.__availableWords if self.__isAvailable(word)]
        self.__availableWords = newAvailableWords
        return newAvailableWords.copy()




