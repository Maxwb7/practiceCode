#deck of many things

import random




sun = "Sun: You gain 50,000 XP, and a wondrous item (which the DM determines randomly) appears in your hands."
moon = "Moon: You are granted the ability to cast the wish spell 1d3 times."
star = "Star: Increase one of your Ability Scores by 2. The score can exceed 20 but can't exceed 24."
throne = "Throne: You gain proficiency in the Persuasion skill, and you double your Proficiency Bonus on checks made with that skill. In addition, you gain rightful ownership of a small keep somewhere in the world. However, the keep is currently in the hands of Monsters, which you must clear out before you can claim the keep as. yours."
key = "Key: A rare or rarer Magic Weapon with which you are proficient appears in your hands. The DM chooses the weapon."
knight = "Knight: You gain the service of a 4th-level Fighter who appears in a space you choose within 30 feet of you. The Fighter is of the same race as you and serves you loyally until death, believing the fates have drawn him or her to you. You control this character."
void = "The Void: This black card Spells Disaster. Your soul is drawn from your body and contained in an object in a place of the DM's choice. One or more powerful beings guard the place. While your soul is trapped in this way, your body is Incapacitated. A wish spell can't restore your soul, but the spell reveals the location of the object that holds it. You draw no more cards."
flames ="Flames: A powerful devil becomes your enemy. The devil seeks your ruin and plagues your life, savoring your suffering before attempting to slay you. This enmity lasts until either you or the devil dies."
skull = "Skull: You summon an avatar of death-a ghostly humanoid Skeleton clad in a tattered black robe and carrying a spectral scythe. It appears in a space of the DM's choice within 10 feet of you and attacks you, warning all others that you must win the battle alone. The avatar fights until you die or it drops to 0 Hit Points, whereupon it disappears. If anyone tries to help you, the helper summons its own Avatar of Death. A creature slain by an Avatar of Death can't be restored to life."
ruin = "Ruin: All forms of Wealth that you carry or own, other than Magic Items, are lost to you. Portable property vanishes. Businesses, buildings, and land you own are lost in a way that alters reality the least. Any documentation that proves you should own something lost to this card also disappears."
eurayle = "Euryale: The card's medusa-like visage curses you. You take a -2 penalty on Saving Throws while Cursed in this way. Only a god or the magic of The Fates card can end this curse."
rogue = "Rogue: A nonplayer character of the DM's choice becomes Hostile toward you. The identity of your new enemy isn't known until the NPC or someone else reveals it. Nothing less than a wish spell or Divine Intervention can end the NPC's hostility toward you."
jester ="Jester: You gain 10,000 XP, or you can draw two additional cards beyond your declared draws."

vizier = "Vizier: At any time you choose within one year of drawing this card, you can ask a question in meditation and mentally receive a truthful answer to that question. Besides information, the answer helps you solve a puzzling problem or other dilemma. In other words, the knowledge comes with Wisdom on how to apply it."
comet = "Comet: If you single-handedly defeat the next Hostile monster or group of Monsters you encounter, you gain Experience Points enough to gain one level. Otherwise, this card has no effect."
fates = "The Fates: Reality's fabric unravels and spins anew, allowing you to avoid or erase one event as if it never happened. You can use the card's magic as soon as you draw the card or at any other time before you die."
gem = "Gem: Twenty-five pieces of jewelry worth 2,000 gp each or fifty gems worth 1,000 gp each appear at your feet."
talons = "Talons: Every magic item you wear or carry disintegrates. Artifacts in your possession aren't destroyed but do Vanish."
idiot = "Idiot: Permanently reduce your Intelligence by 1d4 + 1 (to a minimum score of 1). You can draw one additional card beyond your declared draws."
donjon = "Donjon: You disappear and become entombed in a state of suspended animation in an extradimensional Sphere. Everything you were wearing and carrying stays behind in the space you occupied when you disappeared. You remain imprisoned until you are found and removed from the Sphere. You can't be located by any Divination magic, but a wish spell can reveal the location of your prison. You draw no more cards."
balance = "Balance: Your mind suffers a wrenching alteration, causing your Alignment to change. Lawful becomes chaotic, good becomes evil, and vice versa. If you are true neutral or unaligned, this card has no effect on you."
fool = "Fool: You lose 10,000 XP, discard this card, and draw from the deck again, counting both draws as one of your declared draws. If losing that much XP would cause you to lose a level, you instead lose an amount that leaves you with just enough XP to keep your level."


card13 = [sun,moon,star,throne,key,knight,void,flames,skull,ruin,eurayle,rogue,jester]
card22 = [vizier,comet,fates,gem,idiot,donjon,balance,fool]

inp = ""
while inp != "13" and inp != "22":
    inp = input("Enter 13 or 22: ")
    if inp != "13" and inp != "22":
        print("You must type 13 or 22")

if inp == "13":
    card13 = card13
if inp == "22":
    card13 = card13 + card22 #ok this works but now I have to update the code to choose.



#but if 22 is selected we can just add card2 to card and run the program like normal, another function i suppose. 
#Unless the card is the Fool or the Jester, the card reappears in the deck, making it possible to draw the same card twice.
#well shit, another programing hurdle, but not a huge deal. if card drawn is Jester add it back in or something like that.


while True:
    try:
        playerInput = int(input(("enter a whole number between 1 - 13/22: ")))
    except ValueError:
        print()
        print("Sorry, I didn't understand that.")
        print()
        continue

    if playerInput < 1:
        print()
        print("Sorry, your response must not be negative or 0.")
        print()
        continue
    if playerInput > 22:
        print()
        print("sorry, your response must be between 1-22")
        print()
        continue
    else:
        break

for draw in range(playerInput):
    cardDrawn = random.choice(card13)
    print(cardDrawn)
    print()
    card13.remove(cardDrawn)
    
    if cardDrawn == void:
        print("Your soul is sucked from your body. Draw no more cards")
        break
       
        
    elif cardDrawn == skull:
        print("Refer to the DMG to see the Specter of Death's stats")
        print()
        
    elif cardDrawn == (fool):
        print("the card magically shuffles back into the deck.")
        print()
        card13.append(cardDrawn)
        
    elif cardDrawn == (jester):
        print("the card magically shuffles back into the deck.")
        print()
        card13.append(cardDrawn)

#Done - my list auto shrinks. Done - my list auto stops if void is drawn.   ok this is my main project. I am more of a project based learner. next I am gonna figure out how to get it to choose between
# 13-22 card decks.



    
