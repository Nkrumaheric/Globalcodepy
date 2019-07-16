#num = [1,56,234,87,4,76,24,69,90,135]

#def is_even(z): return z % 2 ==0
#print(list(filter(is_even, num)))

#num = [1,56,234,87,4,76,24,69,90,135]

#def is_odd(z): return z % 2 ==1
#print(list(filter(is_odd, num)))

#Li = list(map( lambda x : x % 2 == 0,num))
#print(Li)


#Li = list(filter( lambda x : x % 2 == 0,num))
#print(Li)

'''numbers = [12, 54, 33, 67, 24, 89, 11, 24, 47]
def even (b) : return b % 2 == 0

print(list(filter(even, numbers)))
print(list(filter(lambda even: even%2==1, numbers)))'''

'''List1 = range (1,51)
print([a for a in List1 if a%2==1])'''



words = ["hello", "my", "name", "is", "Sam"]
length = [len(word) for word in words]
word = [word.upper() for word in words]
tupple=(word,length)
print(tupple)