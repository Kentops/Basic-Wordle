import random
'''
Wordle...kinda
A coding practice to familiarize myself with Python
8/21/2024
'''


def main():
  file = open("words.txt", "r")
  words = []
  for line in file:
    words.append(line.strip())
  #words defined

  the_word = ""

  lives = 6
  play_again = True
  win = False

  #Startup
  print("Welcome to Wordle!")
  print()
  while(play_again):
    win = False
    lives = 6
    status = []
    for i in range(5):
      status.append("_")
    wrong_place = []
    wrong_letters = []
    the_word = words[random.randint(0, len(words) - 1)]
    while(lives > 0 and not win):
      print(f"Guesses left: {lives}")
      prompts(status,wrong_letters)
      #print(the_word)
      print()
      valid = False
      response = ""
      while not valid:
        response = input("Guess a word: ")
        response = response.lower()
        if(len(response) == 5):
          valid = True
        else:
          print("Response must be five letters long")
      lives -= 1
      wrong_place = []
      check_guess(the_word, response, status, wrong_place, wrong_letters)
      #Yellow
      print("Letters in wrong spots: ", end="")
      for let in wrong_place:
        print(let, end=" ")
      print()
      print()
      if(response.upper() == the_word.upper()):
        win = True
    #First while loop done
    if(win):
      print(f"Congratulations! You guessed the word in {6-lives} guesses!")
    else:
      print(f"Sorry, the word was {the_word}.")
    response = input("Would you like to play again? ")
    play_again = False
    if(response.lower() == "yes" or response.lower() == "y"):
      play_again = True
      print()


def prompts(status, wrong):
  '''Give information to the user'''
  #Grey
  print("Incorrect letters: ", end="")
  for let in wrong:
    print(let, end=" ")
  print()
  #Current Word
  print("Correct letters: ", end="")
  for let in status:
    print(let, end=" ")
  print()

def check_guess(word:str, guess:str, status, place, wrong):
  '''Check eacch letter of the guess against each letter of the word'''
  for i in range(5):
    #Green
    if(word[i] == guess[i]):
      status[i] = word[i].upper()
    #Yellow
    elif(guess[i] != word[i]):
      #Prevent duplicates
      guess_letter_count = 0
      real_letter_count = 0
      for j in range(5):
        if(guess[i] == word[j]):
          real_letter_count += 1
      if(real_letter_count == 0):
        #Grey
        temp = True
        for let in wrong:
          if guess[i].upper() == let:
            temp = False
        if(temp):
          wrong.append(guess[i].upper())
      else:
        #Letter in word, how many in guess?
        for j in range(i+1,5):
          if(guess[i] == guess[j]):
            guess_letter_count += 1
        #print(guess[i])
        #print(str(real_letter_count) + "" + str(guess_letter_count))
        if(real_letter_count - guess_letter_count >= 1):
          #wrong spot
          place.append(guess[i].upper())
        else:
          #Grey
          temp = True
          for let in wrong:
            if guess[i].upper() == let:
              temp = False
          if(temp):
            wrong.append(guess[i].upper())

main()
