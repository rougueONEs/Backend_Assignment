"""
**********PYTHON 2.7 SUPPORTED*************
**********PLEASE READ COMMENTS IN THE PROGRAM AND REPLACE THE VALUES ACCORDINGLY***********
"""



from firebase import firebase
import requests
import smtplib


def sendMail(name,email):
    mail = smtplib.SMTP('smtp.gmail.com', 587) #'smtp.gmail.com' will only work on gmail accounts. For rest domain, insert their smtp handler
    mail.ehlo()
    mail.starttls()
    mail.login('email', 'password') #REPLACE email with your email-id & password with your password
    mail.sendmail('email', email, "Dear "+name+", Welcome to our app") #REPLACE 'email' with your email-id
    mail.close()


if __name__ == '__main__':
    length = 0
    oldUsers=[]
    while True:

        fireb = firebase.FirebaseApplication('https://adarshassignmentpython.firebaseio.com', None)
        result = fireb.get(u'/users', None)

        resultlen = len(result)
        if resultlen>length:
            for x in result.keys():
                if x not in oldUsers:
                    newUser = result[x]
                    print (x,newUser)
                    length = resultlen
                    oldUsers.append(x)
                    fireb.put(u'/userInformation',x,newUser)
                    name = newUser[u'username'].encode('ascii','ignore')
                    email = newUser[u'user email'].encode('ascii','ignore')
                    sendMail(name,email)