
wizard = "Wizard"
wizard_hp = 70
wizard_dmg = 150

elf = "Elf"
elf_hp = 100
elf_dmg = 100

human = "Human"
human_hp = 150
human_dmg = 20

orc = "Orc"
orc_hp = 250
orc_dmg = 120

dragon = "Dragon"
dragon_hp = 300
dragon_dmg = 50

print("1)   Wizard")
print("2)   Elf")
print("3)   Human")
print("4)   Orc")
print("5) Exit The Game!")
character_select = input("Choose Your Character: ").lower()
if character_select == "1" or character_select == "wizard":
    character_select = wizard
    print("You have selected the Wizard!")
    print("Health:", wizard_hp)
    print("Damage:", wizard_dmg)
    my_hp = wizard_hp
    my_dmg = wizard_dmg
elif character_select == "2" or character_select == "elf":
    character_select = elf
    print("You have selected the Elf!")
    print("Health:", elf_hp)
    print("Damage:", elf_dmg)
    my_hp = elf_hp
    my_dmg = elf_dmg
elif character_select == "3" or character_select == "human":
    character_select = human
    print("You have selected the Human!")
    print("Health:", human_hp)
    print("Damage:", human_dmg)
    my_hp = human_hp
    my_dmg = human_dmg
elif character_select == "4" or character_select == "orc":
    character_select = orc
    print("You have selected the Orc!")
    print("Health:", orc_hp)
    print("Damage:", orc_dmg)
    my_hp = orc_hp
    my_dmg = orc_dmg
elif character_select == "5" or character_select == "exit":
    print("Thanks for playing!")
else:
    print("Unknown Character!")

while True and character_select != "5" and character_select != "exit":
    print(f"The {character_select} damaged the dragon")
    dragon_hp = dragon_hp - my_dmg
    print(f"The Dragon's hitpoints are now: {dragon_hp}")
    if dragon_hp <= 0:
        print("The Dragon has lost the battle!")
        break
    print(f"The dragon damaged the  {character_select}")
    my_hp = my_hp - dragon_dmg
    print(f"My hitpoints are now: {my_hp}")
    if my_hp <= 0:
        print(f"The {character_select} has lost the battle")
        break
