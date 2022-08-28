from operator import le


letter = '''Dear <|NAME|>,Greeting from a abc company that you are selected
You are selected!
have a great day ahead
Thanks and regard 
Date:<|DATE|>'''

name=input("Enter Your Name\n")
date=input("enter Date\n")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)