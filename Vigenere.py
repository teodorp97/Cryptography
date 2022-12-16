import numpy as np
import string

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


alphabet=string.ascii_letters

def check_key(Message, Key):


    if(len(Message)==len(Key)):
        return Key
    else:
        index=len(Message)//len(Key)
        Key=Key*(index+1) #govori koliko puta je sifra duza od kljuca
    #print(len(Message), len(Key))
    return Key[:len(Message)]

def VigenereEncrypt(Message, Key, len_alphabet):
    New_message = Message.replace(' ', '')
    New_key=check_key(New_message,Key)
    Encrypted=[]
    for i in range(len(New_message)):
        char=(ord(New_message[i])+ord(New_key[i]))%len_alphabet #len_alphabet = 26 u slucaju alfabeta
        char+=ord('A')
        #print(char, chr(char))
        Encrypted.append(chr(char))
    return ''.join(Encrypted), New_key

def VigenereDecrypt(Message, Key, len_alphabet):

    New_message = Message.replace(' ', '')

    Decrypted=[]
    for i in range(len(New_message)):
        char=((ord(New_message[i])-ord(Key[i]))+len_alphabet)%len_alphabet
        char+=ord('A')
        Decrypted.append(chr(char))
    return ''.join(Decrypted)




Message='POTREBNA POMOC NOVAC I LOVA'
key='KRIPTO'


Enc, Enc_key =VigenereEncrypt(Message,key,26)
Dec=VigenereDecrypt(Enc,Enc_key,26)
print('Poruka = ', Message)
print('Enkriptovana poruka = ',Enc)
print('Kljuc = ',Enc_key)
print('Dekriptovana poruka = ',Dec)
showHistogram(Message,Enc)