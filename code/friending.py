likes = {}
all_contacts = [''] * 29
# ['', 'arty_s', 'at', ''  ]
# {1: [27, 22, 23], 2: [28, 27]}
# {1: [27], 2: 28, ...}
# likes:   {28: []}
with open("friends.txt", "r") as f:
    while True:
        line = f.readline()
        if line == '':
            break
        contacts = line.split(" ")
        number = int(contacts[0])
        name = contacts[1]
        all_contacts[number] = name
        likes[number] = []
        while True:
            like = f.readline()
            if like == '\n' or like == '':
                break
            likes[number].append(int(like))
print(all_contacts)
print(likes)
# ['', 'arty_s', 'at', ''  ]
# {1: [27, 22, 23], 2: [28, 27], ...., 27: [4, 5, 1]}

# (1, [27, 22, 23]), 27: [4, 5, 1]

for number, person_likes in likes.items():
    print('Matches for: ' + all_contacts[number])
    for like in person_likes:
        other_person_likes = likes[like]
        if number in other_person_likes:
            print(all_contacts[like])

