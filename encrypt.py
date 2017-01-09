

def alpha_reverse(ulist):
    f_name=input("File name with extension name(.txt) the message is to be saved : ")
    rlist=['#a1#\n']
    for i in ulist:
        if ord(i)>=97 and ord(i)<=122 :
            d=122-ord(i)
            rlist.append(chr(97+d))
        elif ord(i)>=0 and ord(i)<=31 :
            d=31-ord(i)
            rlist.append(chr(0+d))
        elif ord(i)>=32 and ord(i)<=64:
            d=64-ord(i)
            rlist.append(chr(32+d))
        elif ord(i)>=65 and ord(i)<=90:
            d=90-ord(i)
            rlist.append(chr(65+d))
        elif ord(i)>=91 and ord(i)<=96:
            d=96-ord(i)
            rlist.append(chr(91+d))
        elif ord(i)>=123 and ord(i)<=126 :
            d=126-ord(i)
            rlist.append(chr(123+d))
        elif ord(i)>=128 and ord(i)<=255 :
            d=255-ord(i)
            rlist.append(chr(128+d))


    rdl=len(rlist)
    k=open(f_name, 'a')
    i=0
    while i<rdl:
       k.write(str(rlist[i]))
       i=i+1
    k.close()


def morse_code(ulistm):
    f_name=input("File name with extension name(.txt) the message is to be saved: ")
    CODE = {'A': '.-','B': '-...','C': '-.-.','D': '-..','E': '.','F': '..-.','G': '--.','H': '....','I': '..','J': '.---','K': '-.-','L': '.-..','M': '--','N': '-.','O': '---','P': '.--.','Q': '--.-','R': '.-.','S': '...','T': '-','U': '..-','V': '...-','W': '.--','X': '-..-','Y': '-.--','Z': '--..','0': '-----','1': '.----','2': '..---','3': '...--','4': '....-','5': '.....','6': '-....','7': '--...','8': '---..','9': '----.',' ': '@'}
    mlist=['#m1#']
    for i in ulistm:
        #print (CODE[i.upper()])
        mlist.append(CODE[i.upper()])
        #print(mlist)
    rdl=len(mlist)
    k=open(f_name, 'a')
    i=0
    while i<rdl:
       k.write(str(mlist[i]))
       k.write('\n')
       i=i+1
    k.close()




if __name__=="__main__":

    ulist=[]
    ulistm=[]

    while 1:
        print(" a: Alpha reverse")
        print(' b: Morse Code')
        print(" x : Exit")
        ch = input("Enter Choice: ")


        if ch == 'a':
            udata=input("enter the message : ")
            ulist[1:0]=udata
            alpha_reverse(ulist)


        if ch=='b':
            udata=input("enter the message (Please use characters from A-Z or 0-9 and blank space. Special characters cannot be converted.):\n")
            ulistm[1:0]=udata
            morse_code(ulistm)

        if ch == 'x':
            print(ch)
            break

        elif ch!='a' and ch!='b' and ch!='x':
            print('invalid choice')


