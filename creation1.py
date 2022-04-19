import mage as m

class Domain:
    pass

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

def get_attributes():
    # get physical, physical
    physical = {'name':'physical'}
    strength = Attribute(name='strength', description='raw force power', affects='p')
    dexterity = Attribute(name='dexterity', description='finesse and reaction', affects='p')
    stamina = Attribute(name='stamina', description='withstand and endure', affects='p')
    physical.__setitem__(strength.name, strength)
    physical.__setitem__(dexterity.name, dexterity)
    physical.__setitem__(stamina.name, stamina)

    # social
    social = {'name':'social'}
    charisma = Attribute(name='charisma', description='presence and impression', affects='s')
    manipulation = Attribute(name='manipulation', description='convince and coerce', affects='s')
    appearance = Attribute(name='appearance', description='poise and composure', affects='s')
    social.__setitem__(charisma.name, charisma)
    social.__setitem__(manipulation.name, manipulation)
    social.__setitem__(appearance.name, appearance)

    # I might be mental
    mental = {'name':'mental'}
    perception = Attribute(name='perception', description='aware and attentive', affects='m')
    intelligence = Attribute(name='intelligence', description='reliably recall', affects='m')
    wits = Attribute(name='wits', description='serene in focus', affects='m')
    mental.__setitem__(perception.name, perception)
    mental.__setitem__(intelligence.name, intelligence)
    mental.__setitem__(wits.name, wits)

    #become a whole person
    attributes={'name':'attributes'}
    attributes.__setitem__(physical['name'], physical)
    attributes.__setitem__(mental['name'], mental)
    attributes.__setitem__(social['name'], social)

    # get it out
    return attributes


def get_character(name='character'):
    character = {'name': name}
    attr = get_attributes()
    character.__setitem__(attr['name'], attr)


    if 'name' in character:
        print(character['name'])
    return character

def get_to_the_bottom():
    pass


def we_must_go_deeper():
    pass
# there must be a way to recurse deeper into data without depth awareness

# that, and get and set the value of an attribute without diving into the data

M = m.Mage(name='tester')
