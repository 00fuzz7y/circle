import bag
from pathlib import Path as P
import datetime as dt
import pickle as pi

class User(dict):
    pass

class Stat(dict):
    expectedattributes = ['name', 'description']

    def __init__(self, name='something', description='basic', **kwargs):
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
        r = ":"
        la = self.listattributes()
        na = []
        for a in la:
            na.append(str(a[1]))
        r = r.join(na)
        return r

class Attribute(Stat):
    expectedattributes = ['name', 'description', 'value', 'basevalue']
    basevalue = 1

    def __init__(self, name, description, **kwargs):
        super(Attribute, self).__init__(name, description, **kwargs)
        self.value = self.basevalue

class Ability(Stat):
    expectedattributes = ['name', 'description', 'value', 'basevalue' ,
                            'specialties', 'unskilled_modifier']
    basevalue = 0

    def __init__(self, name, description, **kwargs):
        super(Ability, self).__init__(name, description, **kwargs)
        self.value = self.basevalue
        self.specialties = []

class Skill(Ability):
    expectedattributes = ['name', 'description', 'value', 'basevalue' ,
                            'specialties', 'unskilled_modifier']
    unskilled_modifier = -1

    def __init__(self, name, description, **kwargs):
        super(Skill, self).__init__(name, description, **kwargs)

class Talent(Ability):
    expectedattributes = ['name', 'description', 'value', 'basevalue' ,
                            'specialties', 'unskilled_modifier']
    unskilled_modifier = -1

    def __init__(self, name, description, **kwargs):
        super(Talent, self).__init__(name, description, **kwargs)

class Knowledge(Ability):
    expectedattributes = ['name', 'description', 'value', 'basevalue' ,
                            'specialties', 'unskilled_modifier']
    unskilled_modifier = -3
    def __init__(self, name, description, **kwargs):
        super(Knowledge, self).__init__(name, description, **kwargs)

# this should probably be contained in a class extension
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

    physical={'name':'physical'}
    physical.__setitem__(strength.name, strength)
    physical.__setitem__(dexterity.name, dexterity)
    physical.__setitem__(stamina.name, stamina)

    mental = {'name': 'mental'}
    mental.__setitem__(perception.name, perception)
    mental.__setitem__(intelligence.name, intelligence)
    mental.__setitem__(wits.name, wits)


    social = {'name': 'social'}
    social.__setitem__(charisma.name, charisma)
    social.__setitem__(manipulation.name, manipulation)
    social.__setitem__(appearance.name, appearance)

    #become a whole person
    attributes={'name':'attributes'}
    attributes.__setitem__(physical['name'], physical)
    attributes.__setitem__(mental['name'], mental)
    attributes.__setitem__(social['name'], social)

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
            [aspect, ['attributes', 'abilities', 'backgrounds']],
            [priority, ["primary", "secondary", "tertiary"]],
            [domain, ['physical', 'mental', 'social']],
            [physical, ['strength', 'dexterity', 'stamina']],
            [mental, ['perception', 'intelligence', 'wits']],
            [social, ['charisma', 'manipulation', 'appearance']],
            [abilities, ['talents', 'skills', 'knowledges']],
            [talent, ['athletics', 'awareness', 'brawl', 'dodge',
                        'expression', 'instruction', 'intuition',
                        'intimidation', 'streetwise', 'subterfuge']],
            [skill, ['do', 'drive', 'etiquette', 'firearms',
                        'leadership', 'meditation', 'melee', 'research',
                        'stealth', 'survival', 'technology']],
            [knowledge, ['computer', 'cosmology', 'culture',
                            'enigmas', 'investigation', 'law', 'linguistics',
                            'lore', 'medicine', 'occult', 'science']]]

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

        if group == 'attributes':  # points to attributes
            choiceIndex = 4
        elif group == 'abilities':  # points to abilities
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
        if group == 'attributes':
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
            if subgroup == 'physical':
                choiceIndex = 5
            elif subgroup == 'mental':
                choiceIndex = 6
            elif subgroup == 'social':
                choiceIndex = 7
        elif group == 'abilities':
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
            if subgroup == 'talents':
                choiceIndex = 9
            elif subgroup == 'skills':
                choiceIndex = 10
            elif subgroup == 'knowledges':
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

def jar(o, file):
    # we need to take the important data from the character
    pass

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

def mirror(attr, depth=0):
    # print character representation-should be recursive but can't sus it rn
    spaCHEH = "  "
    for a in attr:
        gap = spaCHEH * depth
        if 'name' in attr[a]:
            # we must go deeper
            depth += 1
            mirror(attr[a], depth)

            # return from the depths
            depth -= 1
        elif a == 'name':
            depth += 1
            print("{}{}:".format(gap, attr[a]))
        else:
            print("{}{}".format(gap,attr[a].repr()))
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
