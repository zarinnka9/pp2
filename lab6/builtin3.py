def is_palindrome(s):
    return s.lower() == s.lower()[::-1]  

string = "Madam"
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
