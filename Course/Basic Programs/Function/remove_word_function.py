def remove (string,word):
    new_string = string.replace(word, "")
    return new_string.strip()

a= 'Hussain is a not good boy.'

m = remove(a, "not ")
print (m)
