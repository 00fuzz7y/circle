"""this is the mage module, which contains the classes and associated transformations
    shown
"""


class Stat:
    expectedattributes = ['name', 'description']

    def __init__(self, name='default', description='uninteresting', **kwargs):
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
            expected.append(self.__getattribute__(ea))
        return expected


class Attribute(Stat):
    expectedattributes = ['name', 'description', 'basevalue', 'value']
    basevalue = 1

    def __init__(self, name, description, **kwargs):
        super(Attribute, self).__init__(name, description, **kwargs)
        self.value = self.basevalue


class Ability(Stat):
    expectedattributes = ['name', 'description', 'basevalue', 'value', 'specialties']
    basevalue = 0

    def __init__(self, name, description, **kwargs):
        super(Ability, self).__init__(name, description, **kwargs)
        self.value = self.basevalue
        self.specialties = []


class Skill(Ability):
    expectedattributes = ['name', 'description', 'basevalue', 'value']

    def __init__(self, name, description, **kwargs):
        super(Skill, self).__init__(name, description, **kwargs)


class Talent(Ability):
    expectedattributes = ['name', 'description', 'basevalue', 'value', 'specialties']

    def __init__(self, name, description, **kwargs):
        super(Talent, self).__init__(name, description, **kwargs)


class Knowledge(Ability):
    expectedattributes = ['name', 'description', 'basevalue', 'value', 'specialties']

    def __init__(self, name, description, **kwargs):
        super(Knowledge, self).__init__(name, description, **kwargs)


class Mage:

    def __init__(self, name, **kwargs):
        self.__setattr__('name', name)
        for k in kwargs.keys():
            self.__setattr__(k, kwargs[k])

    def set(self, attribute, value): self.__setattr__(attribute, value)
    def get(self, attribute): return self.__getattribute__(attribute)


def choose(selections, allowed=4):
    # first we print the options with the index to use as a selector
    # counter doin double duty
    i = 0
    while i < len(selections):
        try:
            print(str(i) + "-" + str(selections[i]))
            i += 1
        except KeyError:
            selections = list(selections)
            choice = choose(selections)
            return choice
    # now the loverly process of making decisions!
    chosen = False
    attempt = 0

    while not chosen:
        choice = input("from these, enter your choice's index(or 'QQ' to bail):")
        if choice.isdigit():
            choice = int(choice)
            if choice < 0:
                print('that choice is too small!')
                continue
            elif choice >= len(selections):
                print('that choice is too big!')
                continue
            else:
                print('your choice is ' + str(choice), end=" ")
                print(selections[choice])
                selection = selections[choice]
                return selection
        elif choice == 'QQ':
            print('-HIT the little red button!')
            from sys import exit as littleredbutton
            littleredbutton()
        elif attempt < allowed:
            print("you ain't even in the same book. try again.")
            attempt += 1
            continue
        else:
            print('come back when you can handle it, killer.')
            fact = "simple directions escape this one"
            return fact


def confirm(query):
    print(query)
    responses = ['no', 'yes']
    response = choose(responses)
    if response == 1:
        return True
    else:
        return False


def globalname(xx):
    for objname, oid in globals().items():
        if oid is xx:
            return objname


def test():
    """ a = (4, 1, 3, 5, 6, 7, 4, 2, 1)
    setgrouptotuple(attributes, a) """
    print('cool')
    thing = Skill(name='thing', description='does stuff', value=0, actions=['move', 'eat shit'])
    print(thing.name, thing.description, thing.basevalue, thing, thing.specialties, thing.expectedattributes)
    tempoGary = []

    strength = Attribute('strength', 'the power to move boulders around')
    tempoGary.append(strength)
    gary = Mage(name='gary', stats=tempoGary)
    print(gary.__getattribute__('name'))

    mage = create()
    for g in mage:
        for e in g.keys():
            i = g.__getitem__(e)
            print(i.__getattribute__('name'), end=':')
            print(i.__getattribute__('value'))


def setgrouptovalue(g, v):
    counter = 1
    for a in g:
        temp = g.__getitem__(a)
        temp.__setattr__('value', v)
        temp.__setattr__('ordinance', counter)
        counter = counter + 1


def setgrouptotuple(g, t):
    counter = 0
    for a in g:
        temp = g.__getitem__(a)
        temp.__setattr__('value', t[counter])
        counter = counter + 1


def getvaluesfor(g):
    pass


def allocate(points, group):
    print('now, we need to allocate the points among the attributes.')
    print("the first 'dot' is free, and you can't go above 4 at character creation.")
    points = points
    while points > 0:
        current = choose(group)
        current = group[current]
        print('how many points to ', current.name, 'out of ', points, end='')
        temp = input('?')
        if temp.isdigit():
            temp = int(temp)
# if we have the points to spend and we aren't going over 4,
            if temp <= points:
                current.__setattr__('value', temp)
                points = points - temp
    return group


def create():
    """this is to create a new mage, prompting the user for the statistics needed
    to create a mage, we need to get priority and point values from the user
    prioritise(attributes)
    btw. (physical, social, mental) which is (1, 2, 3)
    primary (set by user) can allocate 7 points between its three Attributes, secondary 5, etc.; (7, 5, 3) points
    allocate(attributes, priority)"""
    # statistic name, descriptions, affects
    # this is a stand in tuple-we want to replicate this using prioritise(); allocate() above
    print('in World of Darkness, Attributes three domains: physical, mental and social.')
    physical = {"strength": Attribute(name='strength', description='raw force power', affects='p')}
    physical.__setitem__("dexterity", Attribute(name='dexterity', description='finesse and reaction', affects='p'))
    physical.__setitem__('stamina', Attribute(name='stamina', description='withstand and endure', affects='p'))
    social = {'charisma': Attribute(name='charisma', description='presence and impression', affects='s')}
    social.__setitem__('manipulation', Attribute(name='manipulation', description='convince and coerce', affects='s'))
    social.__setitem__('appearance', Attribute(name='appearance', description='poise and composure', affects='s'))
    mental = {'perception': Attribute(name='perception', description='aware and attentive', affects='m')}
    mental.__setitem__('intelligence', Attribute(name='intelligence', description='reliably recall', affects='m'))
    mental.__setitem__('wits', Attribute(name='wits', description='serene in focus', affects='m'))

    print('to allocate points to them, we must choose a primary group to receive 7 points, ')
    primarydomain = 7
    secondarydomain = 5
    tertiarydomain = 3
    choices = [physical, social, mental]
    primary = choices.pop(choices.index(choose(choices)))
    print('then we must choose a secondary group to receive 5 points, and the third will get 3.')
    secondary = choices.pop(choices.index(choose(choices)))
    tertiary = choices.pop(0)
    print('primary(7): ', primary)
    primary = allocate(primarydomain, primary)
    print('secondary(5): ', secondary)
    secondary = allocate(secondarydomain, secondary)
    print('tertiary(3): ', tertiary)
    tertiary = allocate(tertiarydomain, tertiary)
    attributes = {}
    # add the groups to the main attributes
    attributes.update(primary)
    attributes.update(secondary)
    attributes.update(tertiary)

    """once the attributes are set, we need to do the same thing with our Abilities
    prioritise(Abilities) = (Talents, Skills, Knowledges)
    allocate() with (13, 9, 5) point totals to allocate
    """
    talents = {'alertness': Talent(name='alertness', description='attention to ones environment')}
    talents.__setitem__('athletics', Talent(name='athletics', description='traverse unsafe terrain '))
    talents.__setitem__('awareness', Talent(name='awareness', description='attention to spiritual disturbance'))
    talents.__setitem__('brawl', Talent(name='brawl', description='hand-to-hand combat'))
    talents.__setitem__('dodge', Talent(name='dodge', description='avoid a threat or move between cover'))
    talents.__setitem__('expression', Talent(name='expression', description='effectiveness of self-communication'))
    talents.__setitem__('instruction', Talent(name='instruction', description='pass on a skill you understand'))
    talents.__setitem__('intuition', Talent(name='intuition', description='your gut can save your butt'))
    talents.__setitem__('intimidation', Talent(name='intimidation', description='threaten to your own gain'))
    talents.__setitem__('streetwise', Talent(name='streetwise', description='you know how to run the streets'))
    talents.__setitem__('subterfuge', Talent(name='subterfuge', description='communicate covertly'))
    # this function was an early data storage test.

    skills = {'do': Skill(name='do', description='the way')}
    skills.__setitem__('drive', Skill(name='drive', description='operate a vehicle'))
    skills.__setitem__('etiquette', Skill(name='etiquette', description='social niceties'))
    skills.__setitem__('firearms', Skill(name='firearms', description='ballistic weaponry'))
    skills.__setitem__('leadership', Skill(name='leadership', description='inspire to action'))
    skills.__setitem__('meditation', Skill(name='meditation', description='cool under fire'))
    skills.__setitem__('melee', Skill(name='melee', description='HIT THE THING WITH THE THING'))
    skills.__setitem__('research', Skill(name='research', description='its somewhere in these stacks'))
    skills.__setitem__('stealth', Skill(name='stealth', description='avoid detection'))
    skills.__setitem__('survival', Skill(name='survival', description='find basic necessities'))
    skills.__setitem__('technology', Skill(name='technology', description='operate technology'))

    knowledges = {'computer': Knowledge(name='computer', description='information processing and code')}
    knowledges.__setitem__('cosmology', Knowledge(name='cosmology', description='the universe and its motions'))
    knowledges.__setitem__('culture', Knowledge(name='culture', description='both specific and the construct'))
    knowledges.__setitem__('enigmas', Knowledge(name='enigmas', description='separated and seemingly unrelated'))
    knowledges.__setitem__('investigation', Knowledge(name='investigation', description='find it out'))
    knowledges.__setitem__('law', Knowledge(name='law', description='intimacy with the law and its practice'))
    knowledges.__setitem__('linguistics', Knowledge(name='linguistics', description='languages'))
    knowledges.__setitem__('lore', Knowledge(name='lore', description='through story'))
    knowledges.__setitem__('medicine', Knowledge(name='medicine', description='bodily function and repair'))
    knowledges.__setitem__('occult', Knowledge(name='occult', description='traditional new-age black magick'))
    knowledges.__setitem__('science', Knowledge(name='science', description='known universe rules'))

    print('we must choose whether to prioritise talents, skills, or knowledges')
    primarydomain = 13
    secondarydomain = 9
    tertiarydomain = 5
    choices = [talents, skills, knowledges]
    primary = choices.pop(choices.index(choose(choices)))
    print('then we must choose a secondary group to receive 9 points, and the third will get 5.')
    secondary = choices.pop(choices.index(choose(choices)))
    tertiary = choices.pop(0)
    print('primary(13): ', primary)
    primary = allocate(primarydomain, primary)
    print('secondary(9): ', secondary)
    secondary = allocate(secondarydomain, secondary)
    print('tertiary(5): ', tertiary)
    tertiary = allocate(tertiarydomain, tertiary)

    abilities = {}
    abilities.update(talents)
    abilities.update(skills)
    abilities.update(knowledges)

    return attributes, abilities


if __name__ == '__main__':
    test()
    testattributes = (3, 4, 5, 1, 3, 1, 4, 3, 4)
    testabilities = (3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                     3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3)
    testbackgrounds = {'contacts': 3, 'library': 4}
    testspheres = {'matter': 4, 'mind': 2}
    tradition = 'sonsofaether'
    traditionsphere = 'matter'

    # now we need a way to turn these statistics into useful values-rolls
    moves =
    movement =
    velocity =
    acceleration =
    jumpheight =
    jumplength =
    jump = (jumpheight, jumplength)
