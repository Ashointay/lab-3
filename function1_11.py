def is_palindrome(word):
    word = word.lower().replace(" ", "") 
    return word == word[::-1]

word = input()
print(is_palindrome(word)) 
