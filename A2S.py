##ASCII
test_list = input("Acii Valid Char :")
res = [ord(ele) for sub in test_list for ele in sub]
print("The ascii list is : " + str(res))
