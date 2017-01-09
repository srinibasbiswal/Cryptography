
def alpha_reverse(list):
    f_output=input("Enter the file name with extension name(.txt) in which the decrypted code will be saved: ")
    coding=list[0]+list[1]+list[2]+list[3]
    a_list=list[5:]
    dlist=[]
    if coding=='#a1#':
        for i in a_list:
            if ord(i)>=97 and ord(i)<=122:
                d=122-ord(i)
                dlist.append(chr(97+d))
            elif ord(i)>=0 and ord(i)<=31 :
                d=31-ord(i)
                dlist.append(chr(0+d))
            elif ord(i)>=32 and ord(i)<=64:
                d=64-ord(i)
                dlist.append(chr(32+d))
            elif ord(i)>=65 and ord(i)<=90:
                d=90-ord(i)
                dlist.append(chr(65+d))
            elif ord(i)>=91 and ord(i)<=96:
                d=96-ord(i)
                dlist.append(chr(91+d))
            elif ord(i)>=123 and ord(i)<=126 :
                d=126-ord(i)
                dlist.append(chr(123+d))
            elif ord(i)>=128 and ord(i)<=255 :
                d=255-ord(i)
                dlist.append(chr(128+d))

        dll=len(dlist)
        k=open(f_output, 'a')
        i=0
        while i<dll:
            k.write(str(dlist[i]))
            i=i+1
        k.close()
        print("Decryption Completed!!")
    else:
        print('Cryptography code mismatch!!')

def morse_code(f_name):
    f_output=input("Enter the file name with extension name(.txt) in which the decrypted code will be saved: ")
    rlist=[]
    f=open(f_name, "r")
    array=f.readlines()
    m_array=array[1:]
    e_code=array[0]
    #print(e_code)

    CODE = {'.-\n':'A','-...\n':'B','-.-.\n':'C','-..\n':'D','.\n':'E','..-.\n':'F','--.\n':'G','....\n':'H','..\n':'I','.---\n':'J','-.-\n':'K','.-..\n':'L','--\n':'M','-.\n':'N','---\n':'O','.--.\n':'P','--.-\n':'Q','.-.\n':'R','...\n':'S','-\n':'T','..-\n':'U','...-\n':'V','.--\n':'W','-..-\n':'X','-.--\n':'Y','--..\n':'Z','-----\n':'0','.----\n':'1','..---\n':'2','...--\n':'3','....-\n':'4','.....\n':'5','-....\n':'6','--...\n':'7','---..\n':'8','----.\n':'9','@\n':' '}
    if e_code=='#m1#\n':
        for i in m_array:
            #print(CODE[i.upper()])
            rlist.append(CODE[i.upper()])
            #print(rlist)
        rdl=len(rlist)
        k=open(f_output,'a')
        i=0
        while i<rdl:
            k.write(str(rlist[i]))
            i=i+1
        k.close()
        print("Decryption Completed!!")
    else:
        print('Crytography code mismatch!! ')

if __name__=="__main__":

    while 1:
        menuch=input("Go to the menu: Y/N: ")
        if menuch=="y" or menuch=='Y':
            f_name=input("Enter the the file name (with extension name (.txt))in which the encrypted code is present: ")
            list=[]

            fp=open(f_name,'r')
            while 1:
                char=fp.read(1)
                if not char:
                    break
                list.append(char)
            print(list)
            print("\n\n")
            print(" a: Alpha reverse")
            print(' b: Morse Code')
            print(" x : Exit")
            ch = input("Enter in which format the code is: ")


            if ch == 'a':
                alpha_reverse(list)


            if ch=='b':
                morse_code(f_name)

            if ch == 'x':
                break

            elif ch!='a' and ch!='b' and ch!='x':
                print('invalid choice')

        else:
            break