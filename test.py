def choose(query, choices, attempts=0, attempts_allowed=4):
    while attempts < attempts_allowed:
        print("{}?: 'QQ' or 'qq' to quit".format(query))
        counter = 1
        for c in choices:
            print("{}: {}".format(counter, c))
            counter += 1
        i = "Select your choice: "
        i = input(i)
        if i == 'QQ' or i == 'qq':
            exit(0)
        elif i.isdigit():
            i = int(i)
            #print(len(choices))
            if 0 < i <= len(choices):
                #print("i:", i)
                choice = choices[i-1]
                print("Selected choice:", choice)
                #print("Counter:", counter)
                return choice
            else:
                attempts += 1
                attempts_left = attempts_allowed - attempts
                if attempts == 4:
                    print(i," invalid choice. You have no attempts left, quitting...")
                else:
                    print("{} invalid choice. You have {} attempts left.".format(i, attempts_left))
                choose(choices, attempts, attempts_allowed)
                continue
        else:
            attempts += 1
            attempts_left = attempts_allowed - attempts
            if attempts == 4:
                print(i, " invalid choice. You have no attempts left, quitting...")
            else:
                print("{} invalid choice. You have {} attempts left.".format(i, attempts_left))
            choose(choices, attempts, attempts_allowed)
            continue