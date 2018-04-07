import numpy as np



if 0:
    number = [1, 2, 3]
    print(number)
    number.append(9)
    print(number)
    number.append("hhh")
    print(number)
    number.extend([5, 3, 6, 8])
    print(number)
    number.insert(0, "StartsHere")
    print(number)
    number.remove(3)
    print(number)
    number.remove(3)
    print(number)
    del number[2]
    print(number)
    a = number.pop()
    print(a)
    b = number.pop(2)
    print(b)
    c = number.pop(2)
    print(c)
if(0):
    num=[5,"bulshit",4,3,7,9,6,0,"fuckyall"]
    a=num.pop()
    b=num.pop()
    c=num.pop()
    print(a)
    print(b)
    print(c)
    d=num.pop(1)
    print(d)



#The next block is the demon of list slicing
if(0):
    yo=[1,2,3,"you are so nice",5,"love you!"]
    q=yo[:2]
    print(q)
    p=yo[0:2]
    print(p)
    print(yo[1:2])  #"start and print from here and stop before the next No."
    print(yo[2:])   # Ah, actually, this method is "start and print from here until the last"
    # Now I am going to add the third parameter: step distnce--bu chang in Chinese
    print(yo[1:5:3])
    print(yo[1:5:2])  # start at [1] and stop before [5], two "steps" as a step. If the "window" is out of the list, there will be no output at that step
    # Duang, there's a special method: reverse the list
    print(yo[::-1])


if(0):
    # fen pian copy
    list1=[1,2,9,3,7]
    list2=list1[:] # copy and preserve
    list3=list1
    list1.sort()
    print(list1)
    print(list2)
    print(list3)

# tuple
if(0):
    temp=(1)
    print(type(temp))
    temp=(1,)
    type(temp)
    print(type(temp))
    # the key of tuple is ","
    temp=("jj","yy","ee")
    temp=temp[:2]+("mua",)+temp[2:]
    print(temp)
    temp=temp[:2]+temp[3:]
    print(temp)
    # add and delet
    #del temp
    #print(temp)
    str1="I love you my daring"
    str1=str1[:10]
    print(str1)
    print(str1[5])
    str2="I love you my daring"
    str2=str2.replace("daring","girl")
    print(str2)

if(0):
    list4=[1,3,5,6,4,8,7]#"a","Bioinformatics","paper","APS","CityU","Accept"
    temp = list4[0]
    for each in list4:
        if each>temp:
            temp=each
    print(temp)

if(0):
    def multi(a,b,c,d):
        """This function can do the formulation a+b*c-d"""
        print(a+b*c-d)
    multi(12,34,56,78)
    print(multi.__doc__) # doc for the function

    #key word parameter and mo ren parameter
    def nutri(name="protein",word="good"):
        print(name+" "+word)
    print(nutri())
    print(nutri("sugar","less"))

    def changeAble(*params):
        print("have %d parameters" % len(params))
        print("the second param is:", params[1]) # be care of here. if params are int, don't use '+', use ','
    print(changeAble("I",'love','you','babe'))

    # release package
    a=[1,2,3,4,5]
    print(changeAble(*a))

if(0):
    def discount(price,rate):
        final_price = price * rate
        return final_price
    original_price = float(input('please enter the ori price:'))
    rate = float(input('please enter discount:'))/100
    newprice = discount(original_price,rate)
    print('After discount is:', newprice)

if (0):
    def Total_price(numOfGoods):
        original_price = float(input('Please enter the original price:'))
        disccount = float(input('Enter discount:')) / 10
        def single_price(origin_Single_price,rate):
            final_price = origin_Single_price*rate
            return final_price
        total_price = single_price(original_price, disccount) * numOfGoods
        return total_price

    numOfGoods=float(input('Enter number of goods:'))
    total=Total_price(numOfGoods)
    print(total)

if (0):
    student=['zoushangjie','xiaopengyou']
    programme=['Genomics and bioinformatics in CUHK','666']
    print(programme.index('Genomics and bioinformatics in CUHK'))
    print("zoushangjie:", programme[student.index('zoushangjie')])
    dict_master={'zoushangjie':'Genomics and bioinformatics in CUHK',"lin":'PKU'}
    print(dict_master['zoushangjie'])
    dict_master[1]='TSU'
    print(dict_master)
    dict_master['Lin']='TSU'
    print(dict_master)
    dict_master.update(Lin='PKU Medical') # No '' on key !!??
    print(dict_master)

if (0):
    list1=[1,1,2,4,5,77,8,77]
    print(list1)
    list1=list(set(list1))  # set can remove repeated values
    print(list1)