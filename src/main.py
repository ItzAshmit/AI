import random

print("hello!")
print("My anme is timhsa")
name = input("and yours?  ")
print(f"really {name}! sounds like a name of a human")
print("I love cyan colour so i use them in all of my things")
colour = input("so what colour do you think the best  ") 
colour = colour.lower()
if colour == "cyan":
   print("I know that colour is amazing")
if colour != "cyan":
   print("hmm... I dont think that colour is good enough to be favourite")
  
while True:
  age = input("Can you tell me that ,How old are you?  ")
  try:
    age = int(age)
    break
  except ValueError:
    print("broo thats not a number")
print("well, I am 3 years old as i fully made in 2021")
if age > 3:
  print(f"so you are {age - 3} years older than me")
if age <3:
  print(f"Ohh... you are {3-age} younger than me")

while True:
  game =  input("Want to play games!  ").lower()
  if "yes" in game:
    print("I have games to play")
    print("stone paper scissors")
    print("Random number")
    
    while True:
       gam = input("which one you want to play(r for Random number and spt for other) ").lower()
       if "r" not in gam and "spt" not in gam:
         print("type r or spt to play")
       if "r" in game or "spt" in game:
         break
       
       
       if "r" in gam:
         while True:
       
            print("so choose a number between 1 to 10 and if the number is the number that I am thinking than you will win")
            c_no =  random.randint(1,10)
            while True:
              no = input("choose  ")
              try:
                no = int(no)
                break
              except ValueError:
                print("bro type a number")
            
            
            if no == c_no:
              print("Wow you win!")
            if no != c_no:
              print(f"ohh... you lost better luck next time, well the no. is {c_no}")
            retry = input("Want to play again?  ")
            if "no" in retry:
              break
            if "yes" in retry:
              continue
            if "yes" in retry and "no" in retry or "yes" not in retry and "no" not in retry:
              print("Bro try to type yes or no")
            
      
      
      
       if "spt" in gam:
       print("self explanatory stone paper scissors, the legendry game of choice in which Rock crushes scissors, scissors cuts paper, and paper covers rock. If both players make the same decision, it's a tie. ")
       while True:
         
          cor = input(" choice s for scissors, p for paper and st for stone  ")
          c_c = random.choice(["st","p","s"])
          if cor == c_c:
             print("it's a tie")
          if cor != c_c:
             print("sorry'but better luck next time")
          if cor != "st" or "p" or "s":
            print("bro type st for stone, p for paper and s for scissors")
          
            continue 
          
       break
       



  if "yes" in game and "no" in game:
      game = input("i didn't understand yes or no?  ")
  
  if "no" in game and "yes" not in game:
      break
  if "yes" not in game and "no" not in game:
      print("bro type something like yes or no.  ")
  
  
  

  
    
print("I hope you enjoyed but its time to say bye")

