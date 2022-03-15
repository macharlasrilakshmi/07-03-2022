mystr = input("enter a string:")
mystr = mystr.casefold()
revstr = reversed(mystr)
if list(mystr) == list(revstr):
   print("The string is  palindrome.")
else:
   print("The string is not  palindrome.")
