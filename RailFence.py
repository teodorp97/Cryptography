import numpy as np

#za crtanje histograma
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


def cipher_encryption(Message, rails_num): #message = string, num=broj redova
    New_message=Message.replace(" ", "").upper()

    Matrix = [["_" for cols in range(len(New_message))] for rows in range(rails_num)]
    row = 0
    check = 0
    for i in range(len(New_message)):
        if check==0:

            Matrix[row][i]=New_message[i]

            row=row+1
            if row == rails_num:
                check=1
                row-=1
        elif check == 1:
            row-=1
            Matrix[row][i]=New_message[i]
            if row==0:
                check=0
                row=1
    for row in range(rails_num):
        print(Matrix[row])

    Encrypted=''

    arr=np.ravel(Matrix)
    Encrypted=''
    for i in range(len(arr)):
        if(arr[i]!="_"):
            Encrypted+=''.join(arr[i])
    return Encrypted

def cipher_decryption(Encrypted, rails_num):

    Matrix = [["_" for cols in range(len(Encrypted))] for rows in range(rails_num)]
    for row in range(rails_num):
        print(Matrix[row])

    print('\n')
    dir_down = False
    row, col = 0, 0

    for i in range(len(Encrypted)):
        if (row == 0) or (row == rails_num - 1):
            dir_down = not dir_down
        Matrix[row][col] = '*'
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1



    for row in range(rails_num):
        print(Matrix[row])

    i = 0

    for row in range(rails_num):
        for col in range(len(Encrypted)):
            if(Matrix[row][col]=='*'):
                Matrix[row][col]=Encrypted[i]
                i+=1
    print('\n')

    for row in range(rails_num):
        print(Matrix[row])

    Decrypted = ''

    for col in range(len(Encrypted)):
        for row in range(rails_num):
            if(Matrix[row][col]!='_'):
                Decrypted+=''.join(Matrix[row][col])

    return Matrix, Decrypted

Rails_number=8
Message='Ovo je samo jedan primer'
print('Poruka: ', Message.replace(' ','').upper())
Enc=cipher_encryption(Message,Rails_number)
print('Enrkiptovana poruka: ', Enc)

print('Dekripcija')
print('\n')
Matrix, Dec =cipher_decryption(Enc, Rails_number)
print('\n')
print('Dekriptovana poruka: ',Dec)

showHistogram(Message,Enc)
