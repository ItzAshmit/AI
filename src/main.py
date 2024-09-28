print("hello!")
print("My anme is timhsa")
name = input("and yours?  ")
print(f"really {name}! sounds like a name of a human")
print("I love cyan colour so i use them in all of my things")
colour = input("so what colour do you think the best  ") 
if colour == "cyan":
   print("I know that colour is amazing")
if colour != "cyan":
   print("hmm... I dont think that colour is good enough to be favourite")
age = input("Can you tell me that ,How old are you?  ")
age = int(age)
print("well, I am 3 years old as i fully made in 2021")
if age > 3:
   print(f"so you are {age - 3} years older than me")
if age <3:
   print(f"Ohh... you are {3-age} years smaller than me")
game = input("Want to play games!  ")
if "no" == game:
   print("I think thats enough for today so bye")
if "yes" == game:
   print("I have a game to play")
   print("spelling checker")
   print("Random number")
   gam = input("which one you want to play  ")
   if gam == "Random number":
      print("so choose a number between 1 to 10 and if the number is the number that I am thinking than you will win")
      no = input("choose  ")
      no = int(no)
      if no == 6:
         print("Wow you win!")
      if no != 6:
         print("ohh... you lost better luck next time, well the no. is 6")
   if gam == "spelling checker":
      print("so in this i will give you two spellings and you have to which one is correct")
      cor = input(" break or braek tell,tell  ")
      if cor == "break":
         print("yayy! you win!")
      if cor == "braek":
         print("sorry'but better luck next time")
print("I hope you enjoyed but its time to say bye")

