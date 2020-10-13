import mage as m

"""this is to be the main program, which is why mage is being called here"""


def choose(selections, attempts=4):
    # first we print the options with the index to use as a selector
    # counter doin double duty
    i = 0
    while i < len(selections):
        print(str(i) + "-" + str(selections[i]))
        i += 1
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
                print('your choice is ' + str(choice) + " " + selections[choice])
                selection = selections[choice]
                return selection
        elif choice == 'QQ':
            print('-HIT the little red button!')
            from sys import exit as littleredbutton
            littleredbutton()
        elif attempt < attempts:
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


if __name__ == '__main__':
    m.test()
