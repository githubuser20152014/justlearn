# rock, paper, scissors

objects = ['rock', 'paper', 'scissors']

ask = input('Play Rock-Paper-Scissors (y/n)?: ').lower()

while(ask != "n"):
  p1 = input('Player 1 chooses: ').lower()
  p2 = input('Player 2 chooses: ').lower()
  # while p1 or p2 not in objects:
  #   print('choose from rock,paper,scissors')
  #   p1 = input('Player 1 chooses: ').lower()
  #   p2 = input('Player 2 chooses: ').lower()

  while (p2 == p1):
    p2 = input('Player 2, choose something else:').lower()



  if p1 == 'rock':
      if p2 == "scissors":
          print('Player 1 wins')
      elif p2 == "paper":
          print('Player 2 wins')
  elif p1 == "scissors":
      if p2 == "paper":
          print('Player 1 wins')
      elif p2 == "rock":
          print("Player 2 wins")
  else: 
    if p2 == "rock":
      print('Player 1 wins')
    elif p2 == "scissors":
      print('Player 2 wins')
    else:
      print('Player 2 wins')
      
  ask = input('Play again? (y/n): ').lower()    
