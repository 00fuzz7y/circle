"""
designed to ease the experience of GMing
        campaigns
        sessions
        characters
        scenes
    -handling the aforementioned through template interface Element functions;
      create()
      read()
      update()
      delete()

Mage the Ascension

Name: Aodh
Player: Genie
Chronicle: Recumbent
Essence:Dynamic/Pattern/Primordial/Questing
Mature:
Demeanor:
Tradition:Sons of Aether
Mentor:
Cabal:

Attributes:[7/5/3] Base 1
Physical(Strength, Dexterity, Stamina)
Social(Charisma, Manipulation, Appearance)
Mental(Perception, Intelligence, Wits)

Abilities:[13/9/5] Base 0
Talents(Alertness, Athletics, Awareness, Brawl, Dodge, Expression, Instruction, Intuition, Intimidation, Streetwise, Subterfuge)
Skills(Do, Drive, Etiquette, Firearms, Leadership, Meditation, Melee, Research, Stealth, Survival, Technology)
Knowledges(Computer, Cosmology, Culture, Enigmas, Investigation, Law, Linguistics, Lore, Medicine, Occult, Science)

Backgrounds[7](Allies, Arcane, Avatar, Chantry, Destiny, Dream, Familiar, Influence, Library, Mentor, Node, Resources, Sanctum, Talisman)
Spheres[5+Tradition](Prime, Spirit, Mind, Matter, Life, Forces, Space, Time, Entropy)

Speed=Strength+Dexterity+5
Initiative=Dexterity+Wits
Willpower:5
Arete:1
Quintessence/Paradox:

#at character creation once base points are spent, then FP may be
FP:[15] 5FP/Attributes 2FP/Abilities FP/Backgrounds 4FP/Arete FP/Willpower 7FP/Spheres 4Quintessence/FP

Health=Bruised[]Hurt[]Injured[]Wounded[]Mauled[]Crippled[]Incapacitated[]

#XP=experience points CR=CurrentRating
XP:3/NewAbility 10/NewSphere
    Willpower/Knowledges=CR
    Talents/Abilities=2CR
    Attributes=4CR
    TraditionSphere=7CR
    Sphere/Arete=8CR

"""
#imports
import math

def confirm(query):
    s = input(query)
    if s==(y,Y):return True

class Character:

    System:World_of_Darkness

class Mage:

    System:Mage_the_Ascension

    def __init__(self, name):
        self.name= name

    def introduce(self):
        print("this one's name is "+name)

if __name__== '__main__':

    confirm('create new Mage?')
    custom_name = input("custom_name?(leave empty for default<curr=datetime>")
    if len(custom_name)<1:custom_name == #if empty, set as current datetime
