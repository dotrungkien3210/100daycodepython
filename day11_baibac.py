import random
card_input = [1,2,3,4,5,6,7,8,9,10,10,10,10]
your_card = []
enemy_card = []
for i in range(2):
    your_card.append(random.choice(card_input))
    enemy_card.append(random.choice(card_input))
print(your_card)
print(enemy_card)
while(True):
    choose = input("Do you want to draw more y/n")
    if(choose == "y"):
        your_card.append(random.choice(card_input))
        if(sum(your_card)>21):
            print("you lose")
            break
        else:
            print(f"sum of your card is {sum(your_card)} with {your_card}")
    else:
        break
print(f"sum of your card is {sum(enemy_card)} with {enemy_card}")
print(f"sum of your card is {sum(your_card)} with {your_card}")
if(sum(your_card)>sum(enemy_card)):
    print("you win")
else:
    print("you lose")