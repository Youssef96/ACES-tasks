word = raw_input("Enter a Word : ")

if word[::-1] == word:
    print "Palindrome."
else:
    print "Not Palindrome."
