class Answer:

    AnswerId = ""
    SenderId = ""
    AnswerText = ""
    Date = ""

    def __init__(self, answerId, senderId, answerText, date):
        self.AnswerId = answerId
        self.SenderId = senderId
        self.AnswerText = answerText
        self.Date = date
