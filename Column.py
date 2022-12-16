import numpy as np

import pandas
from collections import Counter
import matplotlib.pyplot as plt

def showHistogram(Message, Encrypted):

    letter_counts_mess = Counter(Message.replace(' ', ''))
    df_mes = pandas.DataFrame.from_dict(letter_counts_mess, orient='index')

    letter_counts_enc = Counter(Encrypted)
    df_enc = pandas.DataFrame.from_dict(letter_counts_enc, orient='index')

    fig, axes = plt.subplots(nrows=1, ncols=2)
    df_mes.plot(ax=axes[0], kind='bar', title='Originalna poruka')
    df_enc.plot(ax=axes[1], kind='bar', title='Enkriptovana poruka ')
    plt.show()


def ColumnEncript(Message, num_row, num_col, key): #kljuc je redosled po kom se iscitavaju kolone
    New_message = Message.replace(' ', '')
    if(len(New_message)>(num_row*num_col)):
        print(f'Redovi*Kolone {num_row*num_col} moraju biti veci od ukupne duzine recenice{len(New_message)}!')

    if(len(New_message)<(num_row*num_col)):
        diff=num_row*num_col-len(New_message)



    list=[]
    for i in range(num_row*num_col-diff):
        list.append(New_message[i])

    for x in range(diff):
        list.append('*')
    #print(list)

    arr = np.array(list).reshape(num_row, num_col)
    print(arr)

    Encrypted = ''
    for i in range(len(key)):
        for j in range(len(key)):
            temp=i+1
            if (temp == key[j]):
                Encrypted += ''.join(arr[:, j])
                # print(j)
    #print(Encrypted)
    return Encrypted


def ColumnDecrypt(Message, num_rows, num_cols, key):
    Matrix = [["_" for cols in range(num_cols)] for rows in range(num_rows)]
    Decrypted=''
    i=0
    for col in key:
        col-=1
        for row in range(num_rows):
            #col=col-1
            Matrix[row][col]=Message[i]
            i+=1


    for row in range(num_rows):
        print(Matrix[row])
    for i in np.ravel(Matrix):
        Decrypted+=''.join(i)
    Decrypted_f=Decrypted.replace('*','')
    return Decrypted_f

Message='OVO JE SAMO JEDAN PRIMER'
print('Poruka: ', Message.replace(' ','').upper())
Enc=ColumnEncript(Message, 5,5 , [2,1,3,4,5])
print('Enrkiptovana poruka: ',Enc)
Dec=ColumnDecrypt(Enc,5,5,[2,1,3,4,5])
print('Dekriptovana ppruka: ',Dec)

showHistogram(Message,Dec)