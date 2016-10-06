import random
import sys

students = ["Michelle", "James", "Blair", "Cait", "Karla", "Shan", "Roy", "Zach", "Tin", "Mel"]

# Groups
if len(sys.argv) > 1 and sys.argv[1] == 'groups':
    random.shuffle(students)
    print("Group 1 (Javascript Jedis)")
    for student in students[0:4]:
        print(student)

    print("\nGroup 2 (Carlton's Callbacks)")
    for student in students[4:8]:
       print(student)

    print("\nGroup 3 (Infinite Loop)")
    for student in students[8:12]:
        print(student)

    print("\nGroup 4 (Sublime Dimes)")
    for student in students[12:]:
        print(student)

# List
elif len(sys.argv) > 1 and sys.argv[1] == 'list':
    random.shuffle(students)
    for s in students:
        print(s)

# Pick Onne
else:
    print(students[random.randrange(len(students))])
