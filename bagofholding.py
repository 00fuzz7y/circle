import datetime, pickle


class Bag:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.data = None
        self.fill()

    def fill(self):
        self.file = open(self.filename, 'r')
        self.users = {}

        for line in self.file:
            email, password, name, data, created, saved =line.strip().split(";")
            self.users[email] = (password, name, created, saved)

        self.file.close()

        for user in users:
            dataloc = users[user][3]
            datafile = open(dataloc, 'rb')
            for o in datafile:
                # each user will need an updatable dictionary that can be saved
                # these objects in the datafile then can be added as they need
            datafile.close()


    def get_user(self, email):
        if email in self.users:
            return self.users[email]
        else:
            return -1

    def get_data(self, user):
        pass

    def set_data(self, user, o):
        pass

    def add_user(self, email, password, name):
        if email.strip() not in self.users:
            self.users[email.strip()] = (password.strip(), name.strip(), Bag.get_date())
            self.save()
            return 1
        else:
            print("email in use")
            return -1

    def validate(self, email, password):
        if self.get_user(email) != -1:
            return self.users[email][0] == password
        else:
            return False

    def save(self):
        with open(self.filename, 'w') as f:
            for user in self.users:
                f.write(user + ";" + self.users[user][0] + ";" +
                self.users[user][1] + ";" + self.users[user][2] + ";"
                self.users[user][3] + "\n")



    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]

# def bagit(o, filename='bag'):
#     here = filename
#     heret = str(filename + '.txt')
#     with open(here, 'wb') as f:
#         with open(heret, 'w') as tf:
#             for e in meeji:
#                 for y, z in e.items():
#                     tf.write(y+ ';')
#                     pickle.dump(z,f)
#
# def bagitin(o):
#     fn = input("a name for your bag:")
#     bagit(o, fn)

if '__name__'== '__main__':
    fn = input("a name for your bag:")
