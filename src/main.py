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

game = input("Want to play games!  ").lower()
while True:
  if "yes" in game and "no" in game:
    game = input("i didn't understand yes or no?  ")
  if "no" in game and "yes" not in game:
   pass
  elif "yes" in game:
    print("I have games to play")
    print("spelling checker")
    print("Random number")
   
    while True:
      gam = input("which one you want to play(r for Random number and spt for other) ").lower()
      gam = gam.lower()
      if "r" not in gam and "spt" not in gam:
        print("type r or s to play")
      
       
       
      if gam == "r":
         print("so choose a number between 1 to 10 and if the number is the number that I am thinking than you will win")
         c_no =  random.randint(1,10)
         no = input("choose  ")
         no = int(no)
         if no == c_no:
           print("Wow you win!")
         if no != c_no:
           print(f"ohh... you lost better luck next time, well the no. is {c_no}")
      break
      if gam == "s":
         print("so in this i will give you two spellings and you have to which one is correct")
         cor = input(" break or braek tell,tell  ")
         if cor == "break":
            print("yayy! you win!")
         if cor == "braek":
            print("sorry'but better luck next time")
         break
  else:
    game = input("bro type something like yes or no.  ")
  
    
print("I hope you enjoyed but its time to say bye")

