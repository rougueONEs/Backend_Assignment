# Backend_Assignment


FIREBASE REALTIME DATABASE:
	Project Name: adarshassignmentpython
	URL: https://adarshassignmentpython.firebaseio.com/

FIREBASE REALTIME DATABASE STRUCTURE:
	/users:
		username: value
		user email: value
	/userInformation:
		username: value
		user email: value

			******NOTE*******
The given solution is based on the keys of the above database structure.
By Default one value was passed in both node: users and userInformation.

			******RECOMMENDATION******
It is recommended to use Python 2x Version for the given solution as python-firebase is not supported by Python3x


			******STEPS******
Install all the packages from requirements.txt using pip command
Required Packages: 1) requests
		   2) python-firebase
		   3) smtplib

	python -m pip install -r \path\to\requirements.txt



Open main.py present in directory BackendAssignment in your Python IDLE. Read the comments and replace the value accordingly.

	1)If you are using email account other than gmail, please replace 'smtp.gmail.com' with that email account domain handler at:
		mail = smtplib.SMTP('smtp.gmail.com',587) ...(near line 14)

	2)Replace 'email' and 'password' with your email account and password at:
		mail.login('email','password')            ...(near line 17)
		mail.sendmail('email',.......             ...(near line 18)

	DO NOT REPLACE ANYTHING ELSE IF YOU ARE USING GIVEN FIREBASE PROJECT

Now run Python Script main.py on Python IDLE or if you dont have IDLE then:

	1)ON WINDOWS: Make sure that path to your Python Interpreter is in your PATH VARIABLE.
				python.exe ..\path\to\main.py
		 Check out: https://www.pythoncentral.io/add-python-to-path-python-is-not-recognized-as-an-internal-or-external-command/ for errors (if any)
	
	2)ON LINUX: Make sure that path to your Python Interpreter is in your PATH VARIABLE.
				python ..\path\to\main.py
		Check out: https://www.pythoncentral.io/execute-python-script-file-shell/ for errors (if any)



Now open Firebase Project 'adarshassignmentpython'. Insert a new value in '/users' node as:
	/users:
		user2:
			username : 'Adarsh Agarwal'
			user email : 'kingallies97@gmail.com'

and see the result.

NOTE: This Python Script contains an infinite loop because there is no default httptrigger provided by firebase for Python. Therefore you have to manually terminate the script.

For any query or Error immediately contact me on:
email: kingallies97@gmail.com