class Form:

    FormId = ""
    SenderId = ""
    FormTitle = ""
    FormDescription = ""
    Date = ""

    def __init__(self, formId, senderId, formTitle,formDescription, date):
        self.FormId = formId
        self.SenderId = senderId
        self.FormTitle = formTitle
        self.FormDescription = formDescription
        self.Date = date
