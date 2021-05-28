class AnswerDto:
    AnswerId = ""
    DocumentId = ""
    SenderId = ""
    UserImage = ""
    UserName = ""
    UserType = ""
    AnswerText = ""
    Date = ""

    def __init__(self, answerId, documentId, senderId, answerText, date, userImage, userName,userType ):
        self.AnswerId = answerId
        self.DocumentId = documentId
        self.SenderId = senderId
        self.UserImage = userImage
        self.UserName = userName
        self.AnswerText = answerText
        self.Date = date
        self.UserType = userType
