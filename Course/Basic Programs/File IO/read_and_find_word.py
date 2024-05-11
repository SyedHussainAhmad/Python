from gettext import find


with open ('texts.txt','r') as f:
    a=f.read()
    print(a)

    if 'twinkle' in a:
        print('twinkle is present')    
    else:
        print('twinkle is not present')
    
 