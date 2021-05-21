class User:
    Id=""
    firstName = ""
    lastName = ""
    email = ""
    password = ""

    def __init__(self,Id, firstName, lastName, email, password):
        self.Id = Id
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
