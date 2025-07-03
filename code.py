# import the random module
import random

# create subjects
subjects = [
    "shahrukh khan",
    "Virat kohli",
    "Nirmala sitaraman",
    "Mumbai cat",
    "Group of monkeys",
    "prime ministernn modi",
    "auto rickshaw driver from delhi"
    ]

# create actions
actions = [
    "launches",
    "cancels ",
    "dances with",
    "eats",
    "declares war on ",
    "orders",
    "celebrates"
]


# create places
places = [
    "at Red fort",
    "in mumbai local train ",
    "inside parliament",
    "at ganga ghat",
    "during ipl match",
    "in India Gate"
]

# start the headline generatiuon loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    places = random.choice(places)

    headline = f"Breaking News: {subject} {action} {places}"
    print("\n"+headline)

    user_input = input("\nDo you want another headline? (yes/no)").strip().lower()
    if user_input == "no":
        break

#print goodbye message
print("\n Thanks for using the Fake news headline generator. Have a fun day")
