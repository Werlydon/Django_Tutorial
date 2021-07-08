# Shareef Aliu, Avnoor Singh Sidhu, Daniel Le

def play_again():
    answer = input("Play again? (y/n)\n ").lower()
  
    if answer == "y":
        park()
        
    else:
        exit()

def game_over(reason):
  print("\n" + reason)
  print("Game Over!") 
  play_again()


def park():
  print("\nYou got lost in the amusement park. Find the exit as soon as possible.")
  print("You come to a crossroads. To your right is a path that leads to a delapitated ferry ride, and to your left is a path that leads to a merry-go-round.do you go right(1) or left(2)")
  print("1). Go down the path to the old ferry ride")
  print("2). Go down the path to the merry-go-round ")
  
  answer = input("1 or 2\n ")

  if answer == "1":
    print("As you move down the path to the ferry, you find a bright shiny key on the floor. You pick it up.")
    gate()
    
  elif answer == "2":
    game_over("you fell in a pothole and died lol")
  else:
    game_over("it was 1 or 2, why can't you just do that?")

def gate():
    print("\nYou continue moving forward and come to a gate.")
    print("You can go through the gate with the keys that you found (1), or you can move further down along on the path(2)")
    print("1). Unlock the gate and go through")
    print("2). Continue down the path")

    answer = input("1 or 2\n ")

    if answer == "1":
        print("You go through the gate and find a janitor that takes you to the exit and you find your family waiting for you.s")
    elif answer == "2":
        game_over("You continue down the path for all eternity, surviving off bugs and sidewalk mulch. You meet a few people along the way until you finally die of starvation. ")
    else:
        game_over("it was 1 or 2, how did you get this far without knowing that?")


park()