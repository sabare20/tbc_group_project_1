friendships = {}
while True:
    command = input("შეიყვანეთ ინფორმაცია ან დაწერეთ FINISH: ")
    if command == "FINISH":
        break
    if " - " in command:
        person1, person2 = command.split(" - ")
        if person1 not in friendships:
            friendships[person1] = set()
        if person2 not in friendships:
            friendships[person2] = set()
        friendships[person1].add(person2)
        friendships[person2].add(person1)
for person, friends in friendships.items():
    print(f"{person} - {', '.join(sorted(friends))}")