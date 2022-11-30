# Rotational Kcodes 0,45,90,180,27 SC TP + BM

import re
from getpass import getpass
ini_list = [105, 108, 121, 115, 109, 98, 105, 100, 107, 104, 116, 116, 121, 98, 105, 107, 121, 108, 115, 101] #predefined
pre_defined= ''.join(chr(val) for val in ini_list)
print("Encoder is limited to 5 (angles) symbols so 26 chars z excluded")
print("No special Characters !")
print("===================================================")
mode=input("Choose Mode : \n 0=open \n 1=hidden \n 2=predefined \n:")
frame=input("choose Frame type : \n 0=taproot \n 1=invtree \n:")
n=[]
if not mode=='2':

    if mode == '1':
        n=getpass("Enter a list, example [5 hello]:")
        n=n.split()
    
    else:
        n=input("Enter a list, example [5 hello]:")
        n=n.split()
else:
    n.append(40)
    n.append(pre_defined)


#Row Decode
def even_space(charr):
    if(bool(re.match('[aAfFkKpPuU]',charr))==True):
        return '0'
    elif(bool(re.match('[bBgGlLqQvV]',charr))==True):
        return '45'
    elif(bool(re.match('[cChHmMrRwW]',charr))==True):
        return '90'
    elif(bool(re.match('[dDiInNsSxX]',charr))==True):
        return '180'
    elif(bool(re.match('[eEjJoOtTyY]',charr))==True):
        return '270'
        
#column Decode
def odd_space(charrr):
    if(bool(re.match('[a-eA-E]',charrr))==True):
        return '0'
    elif(bool(re.match('[f-jF-J]',charrr))==True):
        return '45'
    elif(bool(re.match('[k-oK-O]',charrr))==True):
        return '90'
    elif(bool(re.match('[p-tP-T]',charrr))==True):
        return '180'
    elif(bool(re.match('[u-yU-Y]',charrr))==True):
        return '270'
        
#prilimenary Test
def check_input():
    number_of_char_to_enco=int(n[0])
    txt=[]
    unused=0
    if number_of_char_to_enco >= 2:
    ## half of the k's are used for block addressig, so only other half is left for data(char) encoding.
        number_of_char_to_enco=int(int(n[0])/2)
    ## second cell is the text string to encode
        if mode=='2':
            txt = pre_defined
            n[0]=40
        else:
            txt = n[1]
    ## create a new list with just txt
        txt = [*txt]
    ## ignore the extra characters if more than k can represent
        if mode == '0':
            print("char ignored : ",txt[number_of_char_to_enco:])
            txt = txt[0:number_of_char_to_enco]
            print("characters that will be encoded : ",txt)
    ## extra characters that can be accomodated
            extra = int(number_of_char_to_enco-len(txt))
            if extra >=1:
                print("Extra Char space:",extra)
                    
                if  (int(n[0])%2) != 0 or int(n[0])-(len(txt)*2):
                    unused=int(n[0])-(len(txt)*2)
                    print("Number of unused last odd D is: ",unused)
        #Frame Stuffing
        
        data=txt
        x=[]
        y=[]
        z=[]
        for i in range(0,len(data)):
            x.append(even_space(data[i]))
            y.append(odd_space(data[i]))
        if frame == '0':
            for i in range(0,len(x)):
                z.append(y[i])
                z.append(x[i])
                #print("Altium Angles: ",z)
        else :
            for i in range(0,len(x)):
                z.append(x[i])
                z.append(y[i])
                #print("Altium Angles: ",z)
        put_table(z,n[0],unused)
         
    else:
    #cannot encode with less k's
        print("not today! : below min range")
        
def put_table(codes,last,unused):
    z=codes
    print("                                ")
    print("================================")
    print("Altium Diode Codes For D%d to D%d" % (1,int(last)-int(unused)))
    print("================================")

    print(" Designator    |          Angle")

    j=0
    i=1
    while  j < len(z):
        print("--------------------------------")
        print(" D%d            |          %s" % (i,z[j]))
        i=i+1
        j=j+1
    for i in range(0,int(unused)):
        print("--------------------------------")
        print(" D%d            |           -" % (int(last)+i))
    print("--------------------------------")


## check for special characters - this encoder is limited to 5 (angles) symbols so 26 chars "z" excluded
dum=""
dum=dum.join(n[1])
special_characters = "!@#$%^&*()-+?_=,<>/0123456789zZ"

if any(c in special_characters for c in dum):
    print("Special Char/Z cannot Encode")
else:
    check_input()
