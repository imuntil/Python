class User():
    """user class"""

    def __init__(self, name):
        self.name = name


class Privileges():
    """privileges"""

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(self.privileges)


class Admin(User):
    """admin"""

    def __init__(self, name):
        super().__init__(name)
        self.privileges = Privileges()


admin = Admin('zhin')
admin.privileges.show_privileges()
