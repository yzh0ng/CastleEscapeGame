class Door():
  "making door objects that contain the room items"
  def __init__(self, door_name, room_items): #every door has a name and a list of things
      self.door_name = door_name
      self.room_items = room_items       # we will pass in a dictionary of items:phrase that is specific to each item




#initializing all three doors and a dictionary that holds all the items and their phrases or password
Movie = Door("Movie", {"Corpse Bride": "Hopscotch!", "Beetlejuice": "It’s showtime!", "Coraline": "You know, you could stay forever…"})
Documents = Door("Documents", {"Butterfly Sculpture": "A delicately sculpted wooden butterfly is placed on the shelf.", "A Handbook": "The cover of the handbook says “The Handbook for the Recently Deceased.” Your name is listed on the last page.", "A Doll": "The doll has blue short hair with buttoned eyes."})
Study = Door("Study", {"Fountain Pen": "A fountain pen is placed on the desk.", "Paper": "A piece of paper is placed on the desk."})




def tragicEnding():
 print("The mansion's puzzle was too challenging for you.")
 print("You failed, and was miserably left in the haunted mansion.")
 print("And you died from starvation and dehydration.")
 print("THE END")




#beginning intros + start of game
print("Hello unfortunate soul, you are now trapped in this mansion, find your way out of here")
while True:
  choice = input("Will you now go through the Movie door, Documents door or Study door >>> ").lower()
  print()




  #this while loop will allow user to go between study and documents room
  while choice == "study": #when you go into study without going into movie room
      print()
          # Add any interactive elements here
      action = input("Enter 'examine' to look at the items or 'exit' to go back to the foyer: ").lower()
      print()
   
      if action == "examine":
          print("You take a closer look at the items on the tables.")
          print("Inside the Study, you notice some interesting items:")
          print("\t- A table with pen and paper.")
          print("\t- Another table with a pen, calculator, and ledger.")
          print()
      elif action == "exit":
          print("You left the Study room and went back to the Foyer.")
          print()
          break
      else:
          print("That's not an option. You remain in the Study.")
          print()




  while choice == "documents": #gives hints to right movie and sends back to foyer
      print("You've entered the Documents room. In front of you, there are some hints:")
      print()
      for item, description in Documents.room_items.items():
          print(f"\t- {item}: {description}")
      print()
      go_back = input("You must return to the Foyer. Do you want to go back? (y/n): ").lower()
      print()
      if go_back == "y":
          print("You leave the Documents room.")
          print()
          break
      elif go_back == "n":
          print("You remained in the Documents room.")
          print()
      else:
          print("That is not a choice. Please try again!")
          print()




#here once movie door starts, it continues with rest of storyline
  if choice == "movie": #this path is when movie is chosen first time, so no hints, room is locked and movie must be chosen
      print("You've entered the Movie room.")
      print("As you step inside, the door behind you gets shut. You are locked!")
      print("In front of you, there is a black dest and on top, three are movie CDs.\n")


      while True:
       movieChoice = input("Enter the number of the movie you would like to watch: 1) Corpse bride, 2) Beetlejuice, 3) Coraline >>> ").lower()
       print()
       if movieChoice in ("1", "corpse bride"):
           print("You have inserted the [Corpse Bride] in the CD player. \nAs soon as you take a seat, the movie starts to play...")
           print("\t\"Hopscotch!\"")
           print("...And the movie ends.")
           break
       elif movieChoice in ("2", "beetlejuice"):
           print("You have inserted the [Beetlejuice] in the CD player. \nAs soon as you take a seat, the movie starts to play...")
           print("\t\"It's showtime!\"")
           print("...And the movie ends.")
           break
       elif movieChoice in ("3", "coraline"):
           print("You have inserted the [Coraline] in the CD player. \nAs soon as you take a seat, the movie starts to play...")
           print("\t\"You know, you could stay forever... if you want to.\"")
           print("...And the movie ends.")
           break
       else:
           print("Please enter the VALID NUMBER of the movie you would like to watch.\n")
     
      print("\nAs the movie screen turns off, a secret passage opens up.\n")
     
      anotherRoom = input("Would you like to go into the passage? (y/n) ")
      print()
      if anotherRoom == "y":
           print("You crawled into the secret passage...")
           print("You enter the Study, but as you step inside, you hear a click behind you. The door to the Foyer is now locked!")


           action = input("Enter 'examine' to look at the items or 'door' to go towards the study room door: ").lower()
           print()
   
           if action == "examine":
                print("You take a closer look at the items on the tables.")
                print("Inside the Study, you notice some interesting items:")
                print("\t- A table with pen and paper.")
                print("\t- Another table with a pen, calculator, and ledger.\n")
                print("You finished examining the items on the table.")
                escape_answer = input("Now... do you want to escape? (y/n)")
                if escape_answer == "n":
                    print()
                    print("You are really close... why don't you try taking a guess.")

                print()
           elif action == "door":
                print("You walk towards the study room door and you realize it is locked.\n")
                break
           else:
                print("That's not an option. You remain in the Study.")
                print()
                print("\nTo escape, you must type the phrase that the movie told you.\n")
           
           escape_phrase = input("What is the magic phrase to escape? ")
           print()
             
           if escape_phrase.lower() in ["hopscotch","hopscotch!"]:
               print("The door unlocks with a satisfying click! You are free to return to the Foyer!")
               print("As you step outside the mansion and feel the wind, you are relieved to have escaped the puzzle")
               print(".....but did you? \n")
           # Here, you could reset the game state or allow them to choose again
           elif escape_phrase.lower() in ["it's showtime", "you know, you could stay forever"]:
               print("The door remains locked. You've lost your chance to escape!.")
               tragicEnding()
           # Optionally, you could end the game or take them back to a safe state
           else:
               print("That's not the correct phrase. You remain trapped in the Study.")
               tragicEnding()
           break
      elif anotherRoom == "n":
          tragicEnding()
          break
      else:
          print("That is not a valid choice. Try again!")
