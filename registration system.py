class Applicant:
    def __init__(self , name , number , mail):
        self.name = name
        self.number = number
        self.mail = mail


    def info(self):
        print "Name : %s " %self.name
        print "Phone-number : %s " %self.number
        print "E-Mail : %s " %self.mail
        print "***************************** \n"

while True:
    q=raw_input("Press Enter for next applicant , (P) For printing all existing Applicants \n  ")
    if len(q)==0 :
        sign_up= Applicant(raw_input("Name:") , raw_input("Phone-number: ") , raw_input("E-mail: "))
    elif q=="p" or q=="P":
        sign_up.info()
