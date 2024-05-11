def game():
    return 44

hiscore = game()
with open ('history.txt') as f:
    b= f.read()

if b=="":
    with open ('history.txt','w') as f:
        f.write(str(hiscore))

elif int(b)<hiscore:
    with open ('history.txt','w') as f:
        f.write(str(hiscore))