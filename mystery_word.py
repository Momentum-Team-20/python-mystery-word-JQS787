import random

def open_file(self):

        with open('words.txt', 'r') as file:
            data = file.read()
        self.random_word(data)
        return data

def random_word(self, data):

word_list = [word for word in data.split()]
random_word = random.choice(word_list)
word_length = len(random_word)
split_word = list(random_word)
hidden_word = ['_' * word_length]
guess_count = 8
guess_letters = []

if len(guess) > 1:
            print('Invalid entry: Only 1 letter at a time.')
        elif not guess.isalpha():
            print('Invalid entry: Letters only.')
        elif guess in guesses:
            print("You already guessed that!")

if __name__ == "__main__":
    play_game()


