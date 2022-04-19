import mage as m

name =     "What is this character's name"
done =     "Are you done"
aspect =   "Which aspect of your character would you like to define"
domain =   "Which domain would you like to put points into"
priority = "What priority should this be"
physical = "Which physical Attribute is getting points"
mental =   "Which mental Attribute is getting points"
social =   "Which social Attribute is getting points"
talent =   "Which Telent is getting points"
skill  =   "Which Skill is getting points"
knowledge= "Which Knowledge is getting points"

choices = [ [name, "any sequence of characters will do for a name"],
            [done, ["yes", "no"]],
            [aspect, ['attributes', 'abilities', 'backgrounds']],
            [priority, ["primary", "secondary", "tertiary"]],
            [domain, ['physical', 'mental', 'social']],
            [physical, ['strength', 'dexterity', 'stamina']],
            [mental, ['perception', 'intelligence', 'wits']],
            [social, ['charisma', 'manipulation', 'appearance']],
            [talent, ['athletics', 'awareness', 'brawl', 'dodge',
                        'expression', 'instruction', 'intuition',
                        'intimidation', 'streetwise', 'subterfuge']],
            [skill, ['do', 'drive', 'etiquette', 'firearms',
                    'leadership', 'meditation', 'melee', 'research',
                    'stealth', 'survival', 'technology']],
            [knowledge, ['computer', 'cosmology', 'culture',
                    'enigmas', 'investigation', 'law', 'linguistics',
                    'lore', 'medicine', 'occult', 'science']]]


class Stat(dict):
    expectedattributes = ['name', 'description']

    def __init__(self, name='something', description='basic', **kwargs):
        self.name = name
        self.description = description
        self.unset = True
        for k in kwargs.keys():
            self.__setattr__(k, kwargs[k])

    def set(self, attribute, value): self.__setattr__(attribute, value)
    def get(self, attribute): return self.__getattribute__(attribute)
    def listattributes(self):
        expected = []
        for ea in self.expectedattributes:
            expected.append((ea, self.__getattribute__(ea)))
        return expected

class Attribute(Stat):
    expectedattributes = ['name', 'description', 'basevalue', 'value']
    basevalue = 1

    def __init__(self, name, description, **kwargs):
        super(Attribute, self).__init__(name, description, **kwargs)
        self.value = self.basevalue

class Ability(Stat):
    expectedattributes = ['name', 'description', 'basevalue', 'value',
                            'specialties', 'unskilled modifier']
    basevalue = 0

    def __init__(self, name, description, **kwargs):
        super(Ability, self).__init__(name, description, **kwargs)
        self.value = self.basevalue
        self.specialties = []

class Skill(Ability):
    expectedattributes = ['name', 'description', 'basevalue', 'value',
                            'specialities', 'unskilled modifier']
    unskilled_modifier = -1

    def __init__(self, name, description, **kwargs):
        super(Skill, self).__init__(name, description, **kwargs)

class Talent(Ability):
    expectedattributes = ['name', 'description', 'basevalue', 'value',
                            'specialties', 'unskilled modifier']
    unskilled_modifier = -1

    def __init__(self, name, description, **kwargs):
        super(Talent, self).__init__(name, description, **kwargs)

class Knowledge(Ability):
    expectedattributes = ['name', 'description', 'basevalue', 'value',
                            'specialties', 'unskilled modifier']
    unskilled_modifier = -3
    def __init__(self, name, description, **kwargs):
        super(Knowledge, self).__init__(name, description, **kwargs)

def get_attributes():
    # let's get physical, physical
    strength = Attribute(name='strength', description='raw force power', affects='p')
    dexterity = Attribute(name='dexterity', description='finesse and reaction', affects='p')
    stamina = Attribute(name='stamina', description='withstand and endure', affects='p')

    # I might be mental
    perception = Attribute(name='perception', description='aware and attentive', affects='m')
    intelligence = Attribute(name='intelligence', description='reliably recall', affects='m')
    wits = Attribute(name='wits', description='serene in focus', affects='m')

    # social
    charisma = Attribute(name='charisma', description='presence and impression', affects='s')
    manipulation = Attribute(name='manipulation', description='convince and coerce', affects='s')
    appearance = Attribute(name='appearance', description='poise and composure', affects='s')

    #become a whole person
    attributes={'name':'attributes'}
    attributes.__setitem__(strength.name, strength)
    attributes.__setitem__(dexterity.name, dexterity)
    attributes.__setitem__(stamina.name, stamina)
    attributes.__setitem__(perception.name, perception)
    attributes.__setitem__(intelligence.name, intelligence)
    attributes.__setitem__(wits.name, wits)
    attributes.__setitem__(charisma.name, charisma)
    attributes.__setitem__(manipulation.name, manipulation)
    attributes.__setitem__(appearance.name, appearance)

    # get it out
    return attributes

def get_talents():

    # I'm just talented, I guess
    alertness = Talent(name='alertness', description="attention to one's environment")
    athletics = Talent(name='athletics', description='traverse unsafe terrain')
    awareness = Talent(name='awareness', description='attention to spiritual disurbance')
    brawl = Talent(name='brawl', description='hand-to-hand combat')
    dodge = Talent(name='dodge', description='avoid a threat or move between cover')
    expression = Talent(name='expression', description='effectiveness of self-communication')
    instruction = Talent(name='instruction', description='pass on a skill you understand')
    intuition = Talent(name='intuition', description='your gut can save your butt')
    intimidation = Talent(name='intimidation', description='threaten to your own benefit')
    streetwise = Talent(name='streetwise', description='you know how to run the streets')
    subterfuge = Talent(name='subterfuge', description='communicate covertly')

    # Steven Stills
    talents = {'name': 'talents'}
    talents.__setitem__(alertness.name, alertness)
    talents.__setitem__(athletics.name, athletics)
    talents.__setitem__(awareness.name, awareness)
    talents.__setitem__(brawl.name, brawl)
    talents.__setitem__(dodge.name, dodge)
    talents.__setitem__(expression.name, expression)
    talents.__setitem__(instruction.name, instruction)
    talents.__setitem__(intuition.name, intuition)
    talents.__setitem__(intimidation.name, intimidation)
    talents.__setitem__(streetwise.name, streetwise)
    talents.__setitem__(subterfuge.name, subterfuge)

    return talents

def get_skills():

    #KICKIT
    do = Skill(name='do', description='the way')
    drive = Skill(name='drive', description='operate a vehicle')
    etiquette = Skill(name='etiquette', description='social niceties')
    firearms = Skill(name='firearms', description='ballistic weaponry')
    leadership = Skill(name='leadership', description='inspire to action')
    meditation = Skill(name='meditation', description='cool under fire')
    melee = Skill(name='melee', description='HIT THE THING WITH THE OTHER THING')
    research = Skill(name='research', description='its somewhere in these stacks')
    stealth = Skill(name='stealth', description='avoid detection')
    survival = Skill(name='survival', description='find basic necessities')
    technology = Skill(name='technology', description='operate technology')

    # SKEEEYULZ
    skills = {'name': 'skills'}
    skills.__setitem__(do.name, do)
    skills.__setitem__(drive.name, drive)
    skills.__setitem__(etiquette.name, etiquette)
    skills.__setitem__(firearms.name, firearms)
    skills.__setitem__(leadership.name, leadership)
    skills.__setitem__(meditation.name, meditation)
    skills.__setitem__(melee.name, melee)
    skills.__setitem__(research.name, research)
    skills.__setitem__(stealth.name, stealth)
    skills.__setitem__(survival.name, survival)
    skills.__setitem__(technology.name, technology)

    #THANKYOU
    return skills

def get_knowledges():
    computer = Knowledge(name='computer', description='information processing and code')
    cosmology = Knowledge(name='cosmology', description='the universe and its motions')
    culture = Knowledge(name='culture', description='both specific and the construct')
    enigmas = Knowledge(name='enigmas', description='separated and seemingly unrelated')
    investigation = Knowledge(name='investigation', description='find it out')
    law = Knowledge(name='law', description='intimacy with and the practice of')
    linguistics = Knowledge(name='linguistics', description='languages')
    lore = Knowledge(name='lore', description='through story')
    medicine = Knowledge(name='medicine', description='bodily functions and their repair')
    occult = Knowledge(name='occult', description='traditional new-age black magicks')
    science = Knowledge(name='science', description='theories of the known universe')


    knowledges = {'name': 'knowledges'}
    knowledges.__setitem__(computer.name, computer)
    knowledges.__setitem__(cosmology.name, cosmology)
    knowledges.__setitem__(culture.name, culture)
    knowledges.__setitem__(enigmas.name, enigmas)
    knowledges.__setitem__(investigation.name, investigation)
    knowledges.__setitem__(law.name, law)
    knowledges.__setitem__(linguistics.name, linguistics)
    knowledges.__setitem__(lore.name, lore)
    knowledges.__setitem__(medicine.name, medicine)
    knowledges.__setitem__(occult.name, occult)
    knowledges.__setitem__(science.name, science)

    return knowledges

def get_abilities():

    talents = get_talents()
    skills = get_skills()
    knowledges = get_knowledges()

    abilities = {'name': 'abilities'}
    abilities.__setitem__(talents['name'], talents)
    abilities.__setitem__(skills['name'], skills)
    abilities.__setitem__(knowledges['name'], knowledges)

    return abilities

def get_character(name='character'):
    character = {'name': name}

    attr = get_attributes()
    character.__setitem__(attr['name'], attr)
    abilities = get_abilities()
    character.__setitem__(abilities['name'], abilities)

    if 'name' in character:
        print(character['name'])
    return character

def done():
    pass
    # get out of the program

def can_allocate(points, to):
    pass

def allocate(how_many_points, to, limit=None):
    pass
def allocate_character(character):
    attribute_points = (7, 5, 3)
    ability_points = (13, 9 , 5)
    domain_priority = (None, None, None)
    ability_priority= (None, None, None)
    to_allocate = (attribute_points, ability_points)

    att_sum = 0
    abi_sum = 0
    for t in attribute_points:
        att_sum += t

    for b in ability_points:
        abi_sum += b

    c = choose(choices[2][0], choices[2][1])    #btw attribute, ability, and backgrouds
    print(c)
    if c == 1:  # wants to allocate attribute points
        if att_sum > 0:
            choose(choices[4][0], [4][1])
        else:
            print('cannot allocate attribute points')

    return character

def choose(query, choices, attempts=0, attempts_allowed=4):
    while attempts < attempts_allowed:
        print("{}?: 'QQ' to quit".format(query))
        counter = 1
        for c in choices:
            print("{}: {}".format(counter, c))
            counter += 1
        i = "your choice is: "
        i = input(i)
        if i.isdigit():
            i = int(i) - 1
            if i > -1 and i < counter:
                choice = choices[i]
                return choice
            else:
                continue

        if i == 'QQ':
            if choose(choices[1][0], choices[1][1]) == 0:
                done()
        else:
            attempts_left = attempts_allowed - attempts
            attempts += 1
            print("{} is not a choice. You have {} attempts left.".format(i, attempts_left))
            choose(choices, attempts, attempts_allowed)

def character_creation():

    character_name = input("{}?: {} ".format(choices[0][0], choices[0][1]))
    character = get_character(character_name)

    allocate_character(character)

    # return allocated character
    return character

def get_to_the_bottom():
    pass


def we_must_go_deeper():
    pass
# there must be a way to recurse deeper into data without depth awareness

# that, and get and set the value of an attribute without diving into the data

M = m.Mage(name='tester')
