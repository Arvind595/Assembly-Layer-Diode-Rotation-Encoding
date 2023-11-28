# Rotational Kcodes 0,45,90,180,27 SC TP + BM
#Skadoosh.Legacy.V0.5
#https://www.onlinegdb.com/online_python_compiler

#revision : dora glitch fixed --removed even check "len(y)%2==0"

import re
from getpass import getpass

def decode(y):
    flag=0
    for i in y:
        if ((bool(re.match('[a-zA-Z!@#$%^&*()-+?_=,<>/]',i))))==True:
            flag=flag+1
            
    if len(y) > 1 and  flag == 0 :
        if (selftest==False):
            y=y.split()
        alpha=[
                 ['a', 'b', 'c', 'd', 'e'], 
                 ['f', 'g', 'h', 'i', 'j'], 
                 ['k', 'l', 'm', 'n', 'o'],
                 ['p', 'q', 'r', 's', 't'],
                 ['u', 'v', 'w', 'x', 'y'],]

        beta=['0','45','90','180','270']
        even=[]
        odd=[]
        frame1=[]
        frame2=[]
        j=0
        k=0
        for i in range(0, len(y)):
            if i%2 == 0:
                even.append(y[i])
                j=j+1
            else:
                odd.append(y[i])
                k=k+1
        #print(even)
        #print(odd)
        for i in range (0, len(even)):
            
            frame1.append(alpha [beta.index(even[i])] [beta.index(odd[i])] )
            frame2.append(alpha [beta.index(odd[i])] [beta.index(even[i])] )
        frame1=''.join(frame1)
        frame2=''.join(frame2)
        
        
        print("\n   Decryption Sucessfull !!")
        print("=================================================")
        print("Frame 1 Message: ",frame1)   
        print("Frame 2 Message: ",frame2)   
        print("=================================================")
     
        
    else:
        print("----ERROR : uneven data lenght/invalid characters ----")
        

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
    number_of_char_to_enco=int(n[0]) #first cell is diode count
    txt=[]
    unused=0
    if number_of_char_to_enco > 1: #cannot encode with less k's
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
            print("\nchar ignored : ",txt[number_of_char_to_enco:])
            txt = txt[0:number_of_char_to_enco]
            print("\ncharacters that will be encoded : ",txt)
    ## extra characters that can be accomodated
            extra = int(number_of_char_to_enco-len(txt))
            if extra >=1:
                print("\nExtra Char space:",extra)
                    
                if  (int(n[0])%2) != 0 or int(n[0])-(len(txt)*2):
                    unused=int(n[0])-(len(txt)*2)
                    print("\nNumber of unused last odd D is: ",unused)
        #Frame Stuffing
        
        data=txt
        x=[] #to store block address
        y=[] #to store cell address
        z=[] #final angles
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
        if(selftest):
            decode(z)
        print("\n==============================END=================================\n")
        #print(x)
        #print(y)
        #print(z)
        
    else :
    #cannot encode with less k's
        print("not today! : below min range")
        
def put_table(codes,last,unused):
    z=codes
    print("                                ")
    print("\nEncryption Results : ")
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

#######################################################################################################

ini_list = [105, 108, 121, 115, 109, 98, 105, 100, 107, 104, 116, 116, 121, 98, 105, 107, 121, 108, 115, 101] #predefined
pre_defined= ''.join(chr(val) for val in ini_list)
n=[]
selftest = False

print("\n===================================================")
print("\n \t\t Rotational Kcodes \n \t\t Skadoosh.Legacy.V0.5 \n")
print("===================================================\n")

start=input("\nChoose Function  \n 1.ENCODE \n 2.DECODE (default) : ")


if  start == '1':
    
    print("\n")    
    print("===================================================")
    print("Encoder is limited to 5 (angles) symbols so 26 chars z excluded \n")
    print("No special Characters !")
    print("===================================================\n")

    mode=input("Choose Mode : \n 0 = open \n 1 = hidden (default) \n 2 = predefined : ")
    frame=input("\nChoose Frame type : \n 0 = taproot \n 1 = invtree (default) : ")
    selftest=int(input("\nEnable SelfTest ? \n 0 = Disable \n 1 = Enable : "))

  
    
    if mode == '0': #open mode
         n=input("\nEnter a list, example like [10 hello]: ") 
         n=n.split()
                   
    elif mode =='2':  #predefined
        n.append(40)
        n.append(pre_defined) #predefined asci append
        
    else :
        #Prompt the user for a password without echoing.
        n=getpass("\nEnter data to encrypt: ") #hidden mode
        n=n.split() #split into cells
       
    ## check for special characters - this encoder is limited to 5 (angles) symbols so 26 chars "z" excluded
    dum=""
    dum=dum.join(n[1]) #copy only the 1st cell string
    special_characters = "!@#$%^&*()-+?_=,<>/0123456789zZ"
    
    if ((bool(re.match('[a-zA-Z!@#$%^&*()-+?_=,<>/]',str(n[0])))==True)):
        print("nSpecial Char/Z cannot Encode")
    
    elif any(c in special_characters for c in dum): #string check
        print("\nSpecial Char/Z cannot Encode")
        
    else:
        check_input()
       
else : 
      decode(input(("\nEnter a list to decode: ")))

## need to add self test feature
## need to add default inputs and flow , change to bool variables
