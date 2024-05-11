def table():
    for n in range(2,21):
        with open (f'Multipliacation_table_of_{n}.txt','w') as f:
            for i in range (1,11):
                f.write(f"{n}x{i}={n*i}")
                if i!=10:
                    f.write('\n')
        

table()
