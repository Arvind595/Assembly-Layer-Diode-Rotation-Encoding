# Rotational Kcodes 0,45,90,180,27 SC TP + BM

import re
print("Encoder is limited to 5 (angles) symbols so 26 chars z excluded")
print("No special Characters !")
print("===================================================")
n=input("Enter a list, example [5 hello]:")
n=n.split()

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
        txt = n[1]
    ## create a new list with just txt
        txt = [*txt]
    ## ignore the extra characters if more than k can represent
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
        data_odd=data
        data_even=data
        x=[]
        y=[]
        z=[]
        for i in range(0,len(data)):
            x.append(even_space(data[i]))
            y.append(odd_space(data[i]))
   
        for i in range(0,len(x)):
            z.append(y[i])
            z.append(x[i])
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



