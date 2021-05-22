names = ['DIVYA SRIVASTAVA','AYUSHI VERMA','RIDHI MISHRA']

names_containing_e = [names for nmae in names if 'e' in names]

names_capitalized = [name.title() for name in names]

names_ending_with_a = [name for name in names if name.endswith('a')]

print (names)
print(names_containing_e)
print(names_capitalized)
print(names_ending_with_a)