import random
import sys

students = ["Carlos A.", "Noah", "Angie", "Arvin", "Victor", "Andrew", "Timmy", "Martin", "AJ", "Brigette", "Marcos", "Jonathan", "Jobeth", "Max", "Carlos B.", "Trevor", "Joseph", "Jeffrey"]

# Groups
if len(sys.argv) > 1 and sys.argv[1] == 'groups':
    random.shuffle(students)
    print("Group 1 (Javascript Jedis)")
    print(students[0:4])

    print("\nGroup 2 (Carlton's Callbacks)")
    print(students[4:8])

    print("\nGroup 3 (Infinite Loop)")
    print(students[8:13])

    print("\nGroup 4 (Beliebers)")
    print(students[13:])
    
else:
    print(students[random.randrange(len(students))])
