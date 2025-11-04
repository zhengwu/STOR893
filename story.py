import random
characters = ['Survivor', 'Ghost Hunter', 'Investigator', 'Medium']
settings = ['Mansion', 'Asylum', 'Graveyard', 'Forest']
actions = ['Investigate', 'Exorcise', 'Survive', 'Escape']
objects = ['Ouija Board', 'Camera', 'Flashlight', 'Crucifix']
character = random.choice(characters)
setting = random.choice(settings)
action = random.choice(actions)
object = random.choice(objects)
story = f"{character} is called to {action} a {setting} using a {object}, but soon realizes that they are not alone."
print(story)