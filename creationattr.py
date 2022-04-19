import mage as m

class Domain:
    pass
class Stat(dict):
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
            expected.append((ea, self.__getattribute__(ea)))
        return expected

class Attribute(Stat):
    expectedattributes = ['name', 'description', 'basevalue', 'value']
    basevalue = 1

    def __init__(self, name, description, **kwargs):
        super(Attribute, self).__init__(name, description, **kwargs)
        self.value = self.basevalue



physical = {'name':'physical'}
strength = Attribute(name='strength', description='raw force power', affects='p')
dexterity = Attribute(name='dexterity', description='finesse and reaction', affects='p')
stamina = Attribute(name='stamina', description='withstand and endure', affects='p')
physical.__setitem__(strength.name, strength)
physical.__setattr__(dexterity.name, dexterity)
physical.__setattr__(stamina.name, stamina)

social = {'name':'social'}
charisma = Attribute(name='charisma', description='presence and impression', affects='s')
manipulation = Attribute(name='manipulation', description='convince and coerce', affects='s')
appearance = Attribute(name='appearance', description='poise and composure', affects='s')
social.__setattr__(charisma.name, charisma)
social.__setattr__(manipulation.name, manipulation)
social.__setattr__(appearance.name, appearance)

mental = {'name':'mental'}
perception = Attribute(name='perception', description='aware and attentive', affects='m')
intelligence = Attribute(name='intelligence', description='reliably recall', affects='m')
wits = Attribute(name='wits', description='serene in focus', affects='m')
mental.__setattr__(perception.name, perception)
mental.__setattr__(intelligence.name, intelligence)
mental.__setattr__(wits.name, wits)

attributes={'name':'attributes'}
attributes.__setattr__(physical['name'], physical)
attributes.__setattr__(mental['name'], mental)
attributes.__setattr__(social['name'], social)

character = {'name': 'character'}
character.__setattr__(attributes['name'], attributes)



if 'name' in character:
    print(character['name'])

def get_to_the_bottom():
    pass


def we_must_go_deeper():
    pass
    # there must be a way to recurse deeper into the file structure without depth awareness


M = m.Mage(name='tester')
