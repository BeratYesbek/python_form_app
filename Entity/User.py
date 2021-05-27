class User:
    Id = ""
    firstName = ""
    lastName = ""
    email = ""
    password = ""
    userImage = ""
    userType = ""

    def __init__(self, Id, firstName, lastName, email, userImage, userType, password):
        self.Id = Id
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.userImage = userImage
        self.password = password
        self.userType = userType
