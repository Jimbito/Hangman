from random import *
from traitlets import Bool




class Hangman:
   
    def __init__(self, word_list, num_lives):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = word_list[randint(0,len(word_list) - 1)]
        self.list_letters = []
        self.word_guessed = ["_"] * len(self.word)
        print(f"The mystery word has {len(self.word)} characters")
        print(f"{self.word_guessed}")

    def check_letter(self, letter) -> None:
        if letter.lower() in self.word:
            indexes = [pos for pos, char in enumerate(self.word) if char == letter]
            replacements = [letter] * len(indexes)
            for (index, replacement) in zip(indexes, replacements):
                self.word_guessed[index] = replacement
            print(self.word_guessed)
        else: 
            self.num_lives = self.num_lives - 1
            print(f'The letter, {letter} is not in the word. You now have {self.num_lives} lives.')

    def ask_letter(self) -> None:
        letter = input("Please guess a letter: ")
        while letter in self.list_letters:
            letter = input(f"The letter, {letter}, has already been guessed. The letters you have guessed are:\n{self.list_letters}.\nPlease input a different one: ")
        while len(letter) != 1:
            letter = input("Please input just one letter: ")
        self.list_letters.append(letter)
        self.check_letter(letter)

    def play_game(self) -> Bool:
        while '_' in self.word_guessed:
            self.ask_letter()
            if self.num_lives == 0:
                message = f'GAME OVER, you ran out of lives. The word was {self.word}.'
                return False, message
        message = f"Well done, you guessed the word {self.word} correctly."
        return True, message

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    game=Hangman(word_list=word_list, num_lives=5)
    win, message = game.play_game()
    if win == True:
        print(message)
    else:
        print(message)


    