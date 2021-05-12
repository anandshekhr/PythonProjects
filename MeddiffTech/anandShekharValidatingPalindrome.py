#to get validating a word as palindrome

def sol(word):
    for i in range(len(word)):
        for p in ('@@#$!@#%@^%!#'):
            word = word.replace(p," ")
        t = word[:i] + word[i+1:]
        if t ==t[::-1]:
            return True
    return word==word[::-1]

print(sol('anand#'))
print(sol('#shekahr'))
print(sol('nutun#'))

