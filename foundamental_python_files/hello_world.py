import random

user_noun = input("Enter a noun: ")
user_verb = input("Enter a verb: ")
random_sentence = random.randrange(0,2)

def story_1():
    print("The",user_noun,"carefully", user_verb,"the gourmet meal!")

def story_2():
    print("The",user_noun,"fearfully", user_verb,"up the hill!")
print(random_sentence)

if random_sentence == 0:
    story_1()
else:
    story_2()
