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

def CaesarEncrypt(Message, length):

    New_message=Message.replace(' ','')
    Encrypted=''
    length%=26
    for i in range(len(New_message)):

        if(New_message[i].isupper()):
            Encrypted+=''.join(chr((ord(New_message[i])+length-65)%26+65)) #ascii lokacija 'A'
        else:
            Encrypted += ''.join(chr((ord(New_message[i]) + length - 97) % 26 + 97)) #ascii lokacija 'a'

    return  Encrypted, length

def CaesarDecrypt(Encrypted, length):
    Decrypted=''
    length %= 26
    for i in range(len(Encrypted)):
        if (Encrypted[i].isupper()):
            Decrypted += ''.join(chr((ord(Encrypted[i]) - length - 65) % 26 + 65))
        else:
            Decrypted += ''.join(chr((ord(Encrypted[i]) - length - 97) % 26 + 97))

    return Decrypted

def CaesarDecryptBF(Encrypted):
    for i in range(len(string.ascii_uppercase)):
        print('Pokusaj :', i, ' Tekst: ', CaesarDecrypt(Encrypted,i))

Message='Ovo je samo jedan primer'
Length=3
Enc, enc_len=CaesarEncrypt(Message, Length)
print('Ulazna poruka: ',Message.replace(' ',''))
print('Enkriptovano = ', Enc)
Dec=CaesarDecrypt(Enc,Length)
print('Dekriptovano = ',Dec)
CaesarDecryptBF(Enc)

showHistogram(Message,Enc)


