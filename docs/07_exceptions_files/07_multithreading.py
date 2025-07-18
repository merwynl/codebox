'''

Multi threading - Used to perform multiple takss concurrently (multitasking)
                - Good for I/O bound tasks like reading files and fetching data from API's
                - threading.Thread(target = my_function)

'''

import threading
import time

# Functions running on a single main thread
def walk_dog(name):
    time.sleep(8)
    print(f"You finished walking {name}.")

def take_out_trash():
    time.sleep(4)
    print("You took out the trash.")

def get_mail():
    time.sleep(2)
    print("You've got mail")

# Initializing multithreading on several functions
# Applying arguments to a multithreaded task. args, take in a tuple but must include a , if only one arg is given
chore1 = threading.Thread(target=walk_dog, args=("Rover",))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail())
chore3.start()

# Prevents any other code after multithreading to finish before the current tasks
chore1.join()
chore2.join()
chore3.join()

print("All chores are complete!")
