import bag
from pathlib import Path as P
import datetime as dt
import pickle as pi

class System():
    pass

class Mechanic():
    pass

class Stat(dict):
    expectedattributes = ['name', 'description']

    def __init__(self, name, description, **kwargs):
        self.name = name
        self.description = description
        for k in kwargs.keys():
            self.__setattr__(k, kwargs[k])

    def set(self, attribute, value): self.__setattr__(attribute, value)
    def get(self, attribute): return self.__getattribute__(attribute)
    def listattributes(self):
        expected = []
        for ea in self.expectedattributes:
            expected.append((ea, self.__getattribute__(ea)))
        return expected
    def repr(self):
        r = "="
        la = self.listattributes()
        na = []
        for a in la:
            na.append(str(a[1]))
        r = r.join(na)
        return r

class StatGroup(dict):
    expectedattributes = ['name']

    def __init__(self, name, **kwargs):
        self.name = name
        for k in kwargs.keys():
            self.__setattr__(k, kwargs[k])


    def set(self, attribute, value):self.__setattr__(attribute, value)
    def get(self, attribute): return self.__getattribute__(attribute)
    def listattributes(self):
        expected = []
        for ea in self.expectedattributes:
            if isinstance(self.get(ea), Stat) or isinstance(self.get(ea), StatGroup):
                temp = self.get(ea)
                expected.append((ea, temp.listattributes()))
            else:
                expected.append((ea, self.__getattribute__(ea)))
        return expected

    def repr(self):
        r = "="
        la = self.listattributes()
        r = str(la)
        return r

class Attribute(Stat):
    expectedattributes = ['name', 'description', 'value', 'basevalue']
    basevalue = 1

    def __init__(self, name, description, **kwargs):
        self.value = None
        super().__init__(name, description, **kwargs)
        if self.value is None:
            self.value = self.basevalue

class Domain(StatGroup):
    expectedattributes = ['name', 'description', 'priority']
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        self.priority = None

class Physical(Domain):
    expectedattributes = ['name', 'description', 'priority',
                            'Strength', 'Dexterity', 'Stamina']

    def __init__(self, name, descr, **kwargs):
        super().__init__(name, **kwargs)
        self.description = descr

class Mental(Domain):
    expectedattributes = ['name', 'description', 'priority',
                            'Perception', 'Intelligence', 'Wits']

    def __init__(self, name, descr, **kwargs):
        super().__init__(name, **kwargs)
        self.description = descr

class Social(Domain):
    expectedattributes = ['name', 'description', 'priority',
                            'Charisma', 'Manipulation', 'Appearance']

    def __init__(self, name, descr, **kwargs):
        super().__init__(name, **kwargs)
        self.description = descr

class Attributes(StatGroup):
    expectedattributes = ['name', 'description', 'Physical', 'Mental', 'Social']

    def __init__(self, name, descr, **kwargs):
        super().__init__(name, **kwargs)
        self.description = descr

class Ability(Stat):
    expectedattributes = ['name', 'description', 'value', 'basevalue',
                            'specialties', 'unskilled_modifier']
    basevalue = 0

    def __init__(self, name, description, **kwargs):
        self.value = None
        super().__init__(name, description, **kwargs)
        if self.value is None:
            self.value = self.basevalue
        self.specialties = []

class Skill(Ability):
    expectedattributes = ['name', 'description', 'value', 'basevalue' ,
                            'specialties', 'unskilled_modifier']
    unskilled_modifier = -1

    def __init__(self, name, description, **kwargs):
        super().__init__(name, description, **kwargs)

class Talent(Ability):
    expectedattributes = ['name', 'description', 'value', 'basevalue' ,
                            'specialties', 'unskilled_modifier']
    unskilled_modifier = -1

    def __init__(self, name, description, **kwargs):
        super().__init__(name, description, **kwargs)

class Knowledge(Ability):
    expectedattributes = ['name', 'description', 'value', 'basevalue' ,
                            'specialties', 'unskilled_modifier']
    unskilled_modifier = -3
    def __init__(self, name, description, **kwargs):
        super().__init__(name, description, **kwargs)

class Talents(Domain):
    expectedattributes = ['name', 'description', 'priority',
                'Athletics', 'Awareness', 'Brawl', 'Dodge',
                'Expression', 'Instruction', 'Intuition',
                'Intimidation', 'Streetwise', 'Subterfuge']

    def __init__(self, name, descr, **kwargs):
        super().__init__(name, **kwargs)
        self.description = descr

class Skills(Domain):
    expectedattributes = ['name', 'description', 'priority',
                'Do', 'Drive', 'Etiquette', 'Firearms',
                'Leadership', 'Meditation', 'Melee', 'Research',
                'Stealth', 'Survival', 'Technology']

    def __init__(self, name, descr, **kwargs):
        super().__init__(name, **kwargs)
        self.description = descr

class Knowledges(Domain):
    expectedattributes = ['name', 'description', 'priority',
                    'Computer', 'Cosmology', 'Culture',
                    'Enigmas', 'Investigation', 'Law', 'Linguistics',
                    'Lore', 'Medicine', 'Occult', 'Science']

    def __init__(self, name, descr, **kwargs):
        super().__init__(name, **kwargs)
        self.description = descr

class Abilities(StatGroup):
    expectedattributes = ['name', 'Talents', 'Skills', 'Knowledges']

    def __init__(self, name, descr, **kwargs):
        super().__init__(name, **kwargs)
        self.description = descr

class Character(StatGroup):
    expectedattributes = ['name', 'Attributes', 'Abilities']

    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        self.Attributes = get_attributes()
        self.Abilities = get_abilities()

    def mirror(self, attr, depth=0):
        # print character representation-should be recursive but can't sus it rn
        spaCHEH = "  "
        ea = attr.expectedattributes
        for each in ea:
            gap = spaCHEH * depth
            if isinstance(self.each, StatGroup):
                # we must go deeper
                depth += 1
                mirror(self.a, depth)

                # return from the depths
                depth -= 1
            elif isinstance(self.get(a), Stat):
                print("{}{}".format(gap, self.get(each).listattributes()))
                continue
            else:
                print(each, self.each)

# still need to get this ^ up into Character there
def get_attributes(TUP = None):
    # let's get physical, physical
    strength = Attribute('Strength', 'raw force power')
    dexterity = Attribute('Dexterity', 'finesse and reaction')
    stamina = Attribute('Stamina', 'withstand and endure')

    # I might be mental
    perception = Attribute(name='Perception', description='aware and attentive', affects='m')
    intelligence = Attribute(name='Intelligence', description='reliably recall', affects='m')
    wits = Attribute(name='Wits', description='serene in focus', affects='m')

    # social
    charisma = Attribute(name='Charisma', description='presence and impression', affects='s')
    manipulation = Attribute(name='Manipulation', description='convince and coerce', affects='s')
    appearance = Attribute(name='Appearance', description='poise and composure', affects='s')

    physical = Physical('Physical', descr='material influence')
    physical.Strength = strength
    physical.Dexterity = dexterity
    physical.Stamina = stamina


    mental = Mental('Mental', 'brainpower')
    mental.Perception = perception
    mental.Intelligence = intelligence
    mental.Wits = wits


    social = Social('Social', 'relationship with relationships')
    social.Charisma = charisma
    social.Manipulation = manipulation
    social.Appearance = appearance

    #become a whole person
    attributes=Attributes('Attributes','characteristics of the person')
    attributes.Physical = physical
    attributes.Mental = mental
    attributes.Social = social

    # get it out
    return attributes

def get_talents():

    # I'm just talented, I guess
    alertness = Talent('Alertness', "attention to one's environment")
    athletics = Talent('Athletics', 'traverse unsafe terrain')
    awareness = Talent('Awareness', 'attention to spiritual disurbance')
    brawl = Talent('Brawl', 'hand-to-hand combat')
    dodge = Talent('Dodge', 'avoid a threat or move between cover')
    expression = Talent('Expression', 'effectiveness of self-communication')
    instruction = Talent('Instruction', 'pass on a skill you understand')
    intuition = Talent('Intuition', 'your gut can save your butt')
    intimidation = Talent('Intimidation', 'threaten to your own benefit')
    streetwise = Talent('Streetwise', 'you know how to run the streets')
    subterfuge = Talent('Subterfuge', 'communicate covertly')

    # Steven Stills
    talents = Talents('Talents', 'Inherent Aptitude')
    talents.Alertness = alertness
    talents.Athletics = athletics
    talents.Awareness = awareness
    talents.Brawl = brawl
    talents.Dodge = dodge
    talents.Expression = expression
    talents.Instruction = instruction
    talents.Intuition = intuition
    talents.Intimidation = intimidation
    talents.Streetwise = streetwise
    talents.Subterfuge = subterfuge

    return talents

def get_skills():

    #KICKIT
    do = Skill('Do', 'the way')
    drive = Skill('Drive', 'operate a vehicle')
    etiquette = Skill('Etiquette', 'social niceties')
    firearms = Skill('Firearms', 'ballistic weaponry')
    leadership = Skill('Leadership', 'inspire to action')
    meditation = Skill('Meditation', 'cool under fire')
    melee = Skill('Melee', 'HIT THE THING WITH THE OTHER THING')
    research = Skill('Research', 'its somewhere in these stacks')
    stealth = Skill('Stealth', 'avoid detection')
    survival = Skill('Survival', 'find basic necessities')
    technology = Skill('Technology', 'operate technology')

    # SKEEEYULZ
    skills = Skills('Skills', 'Practiced in Preparation')
    skills.Do = do
    skills.Drive = drive
    skills.Etiquette = etiquette
    skills.Firearms = firearms
    skills.Leadership = leadership
    skills.Meditation = meditation
    skills.Melee = melee
    skills.Research = research
    skills.Stealth = stealth
    skills.Survival = survival
    skills.Technology = technology

    #THANKYOU
    return skills

def get_knowledges():
    computer = Knowledge('Computer', 'information processing and code')
    cosmology = Knowledge('Cosmology', 'the universe and its motions')
    culture = Knowledge('Culture', 'both specific and the construct')
    enigmas = Knowledge('Enigmas', 'separated and seemingly unrelated')
    investigation = Knowledge('Investigation', 'find it out')
    law = Knowledge('Law', 'intimacy with and the practice of')
    linguistics = Knowledge('Linguistics', 'languages')
    lore = Knowledge('Lore', 'through story')
    medicine = Knowledge('Medicine', 'bodily functions and their repair')
    occult = Knowledge('Occult', 'traditional new-age black magicks')
    science = Knowledge('Science', 'theories of the known universe')


    knowledges = Knowledges('Knowledges', 'Studied Information')
    knowledges.Computer = computer
    knowledges.Cosmology = cosmology
    knowledges.Culture = culture
    knowledges.Enigmas = enigmas
    knowledges.Investigation = investigation
    knowledges.Law = law
    knowledges.Linguistics = linguistics
    knowledges.Lore = lore
    knowledges.Medicine = medicine
    knowledges.Occult = occult
    knowledges.Science = science

    return knowledges

def get_abilities():

    talents = get_talents()
    skills = get_skills()
    knowledges = get_knowledges()

    abilities = Abilities('Abilities', 'Proficient Action')
    abilities.Talents = talents
    abilities.Skills = skills
    abilities.Knowledges = knowledges

    return abilities

def get_character(name='character'):
    character = Character(name)

    attr = get_attributes()
    character.Attributes = attr
    abilities = get_abilities()
    character.Abilities = abilities

    if 'name' in character:
        print(character['name'])
    return character

def conception(character_name=None):

    if character_name is None:
        character_name = input("{}?: {} ".format(choices[0][0], choices[0][1]))
    char = get_character(character_name)
    att_priority = [None, None, None]
    att_points_available = [7, 5, 3]
    abi_priority= [None, None, None]
    abi_points_available = [13, 9, 5]

    p = [att_priority, att_points_available, abi_priority, abi_points_available]

    refine_character(char, p)

    # return allocated character
    return char

name =     "What is this character's name"                              #0
done =     "Are you done"                                               #1
aspect =   "Which aspect of your character would you like to define"    #2
priority = "What priority should this be"                               #3
domain =   "Which domain would you like to put points into"             #4
physical = "Which physical Attribute is getting points"                 #5
mental =   "Which mental Attribute is getting points"                   #6
social =   "Which social Attribute is getting points"                   #7
abilities= "Which set of Abilities would you like to put points into?"  #8
talent =   "Which Talent is getting points"                             #9
skill  =   "Which Skill is getting points"                              #10
knowledge= "Which Knowledge is getting points"                          #11

choices = [ [name, "any sequence of characters will do for a name"],
            [done, ["yes", "no"]],
            [aspect, ['Attributes', 'Abilities', 'Backgrounds']],
            [priority, ["primary", "secondary", "tertiary"]],
            [domain, ['Physical', 'Mental', 'Social']],
            [physical, ['Strength', 'Dexterity', 'Stamina']],
            [mental, ['Perception', 'Intelligence', 'Wits']],
            [social, ['Charisma', 'Manipulation', 'Appearance']],
            [abilities, ['Talents', 'Skills', 'Knowledges']],
            [talent, ['Athletics', 'Awareness', 'Brawl', 'Dodge',
                        'Expression', 'Instruction', 'Intuition',
                        'Intimidation', 'Streetwise', 'Subterfuge']],
            [skill, ['Do', 'Drive', 'Etiquette', 'Firearms',
                        'Leadership', 'Meditation', 'Melee', 'Research',
                        'Stealth', 'Survival', 'Technology']],
            [knowledge, ['Computer', 'Cosmology', 'Culture',
                            'Enigmas', 'Investigation', 'Law', 'Linguistics',
                            'Lore', 'Medicine', 'Occult', 'Science']]]

def refine_character(char, points):
    done = False
    points_to_allocate = [points[1], points[3]]
    while done is False:
        sum_attribute=0
        sum_ability = 0
        sum_points_to_spend=0
        for t in points_to_allocate[0]:
            sum_attribute+=t
        for b in points_to_allocate[1]:
            sum_ability += b
        # no more points to allocate
        for x in points:
            for y in x:
                print('{}'.format(y), end=' ')
        sum_points_to_spend = sum_ability + sum_attribute
        print("{} {} {}".format(sum_attribute, sum_ability, sum_points_to_spend))

        if sum_points_to_spend == 0:
            done = True
            break
        # choose between attributes, abilities, and backgrounds
        choiceIndex = 2
        group = choose(choices[choiceIndex][0], choices[choiceIndex][1])
        print("aspect: {}".format(group))

        if group == 'Attributes':  # points to attributes
            choiceIndex = 4
        elif group == 'Abilities':  # points to abilities
            choiceIndex = 8

        # subgroup to allocate points to
        subgroup = choose(choices[choiceIndex][0], choices[choiceIndex][1])
        # attempt to allocate
        # priority of the section to allocate (determines points to allocate)
        choiceIndex = 3

        priority = choose(choices[choiceIndex][0], choices[choiceIndex][1])
        index = 0
        # index = choices.index(p, choices[choiceIndex][1])
        counter = 0
        for i in choices[choiceIndex][1]:
            if i == priority:
                index = counter
            else:
                counter += 1
                continue
        # we need to see if that priority was used
        # if it hasn't, set it and return the points
        if group == 'Attributes':
            pri_index = 0
            ava_index = 1

            if subgroup in points[pri_index]:
                if points[pri_index][index] == subgroup:
                    to_allocate = points[ava_index][index]
                else:
                    print('that is not the priority you put last time')
                    # implement a range-checking means to swap priority
                    continue
            elif points[pri_index][index] is None:
                points[pri_index][index] = subgroup
                to_allocate = points[ava_index][index]
            else:
                print('no points here')

            limits_at_creation = (1, 4)
            if subgroup == 'Physical':
                choiceIndex = 5
            elif subgroup == 'Mental':
                choiceIndex = 6
            elif subgroup == 'Social':
                choiceIndex = 7
        elif group == 'Abilities':
            pri_index = 2
            ava_index = 3
            if subgroup in points[pri_index]:
                if points[pri_index][index] == subgroup:
                    to_allocate = points[ava_index][index]
                else:
                    print('that is not the priority you put last time')
                    # implement a range-checking means to swap priority
                    continue
            elif points[pri_index][index] is None:
                points[pri_index][index] = subgroup
                to_allocate = points[ava_index][index]
            else:
                print('no points here')

            limits_at_creation = (0, 3)
            if subgroup == 'Talents':
                choiceIndex = 9
            elif subgroup == 'Skills':
                choiceIndex = 10
            elif subgroup == 'Knowledges':
                choiceIndex = 11
        else:
            print('what are me doing?')
        print("Points available = {}".format(to_allocate))
        for st in choices[choiceIndex][1]:
            c_s = get_at_depth(char, st)
            print("{}:{}".format(st, c_s), end=' ')
        s = choose(choices[choiceIndex][0], choices[choiceIndex][1])
        curr_s = get_at_depth(char, s)
        if curr_s >= limits_at_creation[0] and curr_s <= limits_at_creation[1]:
            stat_choices = []
            for x in range(limits_at_creation[0], limits_at_creation[1] + 1):
                stat_choices.append(x)
            pointed_question="set {} to".format(s)
            points_to_set = choose(pointed_question, stat_choices)
            if points_to_set == curr_s:
                print('what was the point, pun totally intended?')
            elif points_to_set < curr_s:
                diff = curr_s - points_to_set
            elif points_to_set > curr_s:
                diff = -(points_to_set - curr_s)
            set_at_depth(char, s, points_to_set)
            points[ava_index][index]= to_allocate + diff

        else:
            print("shouldn't be out of range, but it is, so try again.")

        # print('made it to the end')
        # done allocating to this group?
        # choiceIndex = 1
        # dun = choose(choices[choiceIndex][0], choices[choiceIndex][1])
        # if dun == 'no':
        #     continue
        # else:
        #     done = True

    refined_character = char
    return refined_character

def choose(query, choices, attempts=0, attempts_allowed=4):
    while attempts < attempts_allowed:
        print("{}?: 'QQ' or 'qq' to quit".format(query))
        counter = 1
        for c in choices:
            print("{}: {}".format(counter, c))
            counter += 1
        i = "What would you like?: "
        i = input(i)
        if i == 'QQ' or i == 'qq':
            exit(0)
        elif i.isdigit():
            i = int(i)
            #print(len(choices))
            if 0 < i <= len(choices):
                #print("i:", i)
                choice = choices[i-1]
                print("you chose:", choice)
                #print("Counter:", counter)
                return choice
            else:
                attempts += 1
                attempts_left = attempts_allowed - attempts
                if attempts == 4:
                    print(i," is an invalid choice. You have no attempts left, quitting...")
                else:
                    print("{} is an invalid choice. You have {} attempts left.".format(i, attempts_left))
                choose(choices, attempts, attempts_allowed)
                continue
        else:
            attempts += 1
            attempts_left = attempts_allowed - attempts
            if attempts == 4:
                print(i, " is an invalid choice. You have no attempts left, quitting...")
            else:
                print("{} is an invalid choice. You have {} attempts left.".format(i, attempts_left))
            choose(choices, attempts, attempts_allowed)
            continue

def get_depth(attr, stat, current_depth=None, stat_at=None):
    OPEN_B = '['
    CLOS_B = ']'

    for a in attr:
        if stat_at is not None:
            return stat_at
        elif 'name' in attr[a]:
            # desired not found and not at max_depth, go deeper
            current_depth = current_depth + OPEN_B
            # print(current_depth)
            s=stat
            c_d = current_depth
            stat_at = get_depth(attr[a], stat=s, current_depth=c_d)

            #not in there
            current_depth = current_depth[:-1]
        elif a == 'name':
            # set current_depth
            if current_depth == None:
                current_depth = str(attr[a])
            else:
                current_depth = current_depth + "'{}']".format(attr[a])
                # print(current_depth)
        else:
            # at max_depth, possibly set value?
            if attr[a].name == stat:
                # print("{} found @ {}".format(stat, current_depth))
                bracketify = "['{}']".format(stat)
                st_at = current_depth + bracketify
                return st_at
            else:
                #print("{}".format(attr[a].repr()))
                continue
    # print('stat not found')
    return stat_at
    # then can set c_n[abilities][knowledges][computer].value

def get_at_depth(char, stat):
    c = char
    depth = get_depth(char, stat)
    statement_to_evaluate = depth + ".value"
    # print("s_2_E: {}".format(statement_to_evaluate))

    lp = {char['name']: char}
    temp = eval(statement_to_evaluate, {}, lp)
    return temp

def set_at_depth(character, stat, to):
    depth = get_depth(character, stat)
    statement_to_execute = "{}.value = {}".format(depth, to)
    lp = {character['name']: character}
    exec(statement_to_execute, {}, lp)
    # print(get_at_depth(character, stat))

def get():
    G = None
    loc = {'G': G}
    G = eval("conception('G')")
    return G

def load(name):
    temp = None
    p = P.cwd()
    p = p / name
    with open(p, 'rb') as f:
        temp = pi.load(f)
    name = temp
    return name

def save(name):
    temp = None
    p = P.cwd()
    p = p / name
    with open(p, 'wb') as f:
        pi.dump(name, f)
    name = temp
    return name


if __name__ == '__main__':
    G = conception('G')
    mirror(G)
