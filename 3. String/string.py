a ='Sakshad' # Single quoted string

b = "Sakshad" # Double quoted string

c = '''Sakshad''' # Triple quoted string

nameshort = a[0:3] #prints from 0 to 2 excluding 3
character1 = b[1]
negetive_slicing = c[-7:-3]

print(nameshort)
print(character1)
print(negetive_slicing)

#Skip Value
word = "0123456789"
print(word[1: 6: 2])
