import random
 
subjects = [
  "film industries",
  "hollywod",
  "bollywod",
  "college",
  "vidhyapeeth",
  "south indus"
 ]

actions = [
 "virat kohli",
 "sonu sharma",
 "ritesh agrwal",
 "pm modi",
 "rohit sharma",
 "world cup"
]
places = [
 "bhart",
 "bihar",
 "asam",
 "utter pradesh",
 "karnatka",
 "delhi",
]

while True:
 
 subject = random.choice(subjects)
 action = random.choice(actions)
 place = random.choice(places)

 headline = f"BREAKING NEWS : {subject} {action} {place}"
 print("\n" + headline)
 
 user_input = input("\n Do you want another headline (yes/no)").strip().lower()
 if user_input == "no":
  break
 print("\n thanks for using the fake headlin generator.")