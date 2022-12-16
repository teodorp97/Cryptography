import numpy
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


def InverseMatrix(K):
    coffactor=np.linalg.inv(K)*np.linalg.det(K) #coffactor matrix
    det=int(np.linalg.det(K))
    inv=pow(det,-1,26) #pronalazenje inverznog broja po modulu
    return (int(coffactor*inv)%26)


def createMatrix(key): #pravljenje kljuca u obliku matrice 3x3 (bitno je da kljuc bude duzine 9
    Matrix=[[0] * 3 for i in range(3)]
    k=0

    for i in range(3):
        for j in range(3):
            Matrix[i][j] = np.int(ord(key[k]) % 65)
            i+=1
    return Matrix

def createKeyArr(key):

    arr=np.zeros((3,3))
    k=0
    for i in range(3):
        for j in range(3):
            arr[i][j]=ord(key[k])%65
            k+=1
    return arr.astype(int)

def createMessageArr(Message):

    arr=np.zeros(3)
    k=0

    for i in range(3):
        arr[i]=ord(Message[i])%65
    return arr.astype(int)

def HillEncrypt(Message, Key_as_Arr):
    New_message=Message.replace(' ','').upper()

    Encrypted=''
    Decrypted=''
    diff=len(New_message)%3
    if(diff!=0):
        New_message=New_message+(3-diff)*'*' #dopuna karakterima kako bi poruka mogla da se izdeli u celine od po 3 komada


    cofactor=np.linalg.inv(Key_as_Arr)*np.linalg.det(Key_as_Arr) #kofaktorska matrica
    det=int(np.linalg.det(Key_as_Arr)) #determinanta matrice kljuca
    InvKey=cofactor*pow(det,-1,26) #inverzija po modulu


    for i in range(0,len(New_message),3):

        mess=createMessageArr(New_message[i:i+3])

        print('Delovi poruke: ',mess,'\n')

        enc=np.dot(Key_as_Arr,mess)%26
        dec=np.round(np.dot(InvKey,enc)%26).astype(int)
        for j in range(len(enc)):

            Encrypted+=''.join(chr(enc[j]%26+65))
            Decrypted+=''.join(chr(dec[j]%26+65))

    if(diff==0):
        return Encrypted, Decrypted
    else:
        return Encrypted, Decrypted[:-(3-diff)]
    #return Encrypted, Decrypted[:-(3-diff)] #odsecanje dodatih slova



#Key='GYBNQKURP'
Key='ABCDEFKGH'
Message='OVO JE SAMO JEDAN PRIMER'
print('Poruka: ', Message.replace(' ','').upper())

KeyAsArr=createKeyArr(Key)

Enc,Dec=HillEncrypt(Message,KeyAsArr)
#mess=createMessageArr('ACT')
print('Kljuc u obliku matrice: ')
print(KeyAsArr)
print('Enkriptovana poruka: ',Enc)
print('Dekriptovana poruka: ', Dec)

showHistogram(Message,Enc)
