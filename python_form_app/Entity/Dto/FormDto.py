class FormDto:
    FormId = ""
    DocumentId = ""
    SenderId = ""
    UserImage = ""
    UserName = ""
    UserType = ""
    FormTitle = ""
    FormDescription = ""
    Date = ""

    def __init__(self, formId, documentId, senderId, formTitle, formDescription, date, userImage, userName, userType):
        self.FormId = formId
        self.DocumentId = documentId
        self.SenderId = senderId
        self.UserImage = userImage
        self.UserName = userName
        self.FormTitle = formTitle
        self.FormDescription = formDescription
        self.Date = date
        self.UserType = userType
