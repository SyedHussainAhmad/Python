mydictionary = {
'paratha':'bread',
'paani':'water',
'moqa':'chance',
'dobara':'again',
'kuch':'some',
'barish':'rain'
}

print('options are:',mydictionary.keys())
value = input ("Please Enter any value from above options:\n ")

print ('The meaning of your required value is:\n', mydictionary.get(value))
  