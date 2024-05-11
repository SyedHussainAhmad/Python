def readFile(filename):
    try:
        with open (filename,'r') as f:
            content = f.read()
            print(f'The content of {filename} is {content}.')
    except FileNotFoundError as e:
        print(f'The {filename} is not found.')

readFile('1.txt')
readFile('2.txt')
readFile('3.txt')