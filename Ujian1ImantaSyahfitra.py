
# IMANTA SYAHFITRA MZ
# NO 1 

def Hashtag(string):
    s = string.split()
    # print(s)
    z = '#'

    if len(s) > 0:
        for i in s:
            z += i.capitalize()

        if len(z) > 140:
            z = 'False'
    else:
        z = 'False'

    return print(z)

Hashtag("Hello there how are you doing")
Hashtag(" Hello  World ")
Hashtag("")
Hashtag("adklaksdjasdadsakdjksasjadsadasdasdasdsadasdsadsadasdasdasdasdsadasdasdsadsadadasdadasdsadsadmsdmsamdmsadsmkdkskdmskmdmskdmmsdmsmdmskdmskmdksmdmsk")
print('==========================================================================')
#NO 2
# 2. Create_Phone_Number
def create_phone_number(number):
    angka = number
    hasil = ''
    tipe = []
    stng = 0

    for j in angka:
        tipe.append(type(j))
       
    for k in tipe:
        if k == str:
            stng += 1

    if len(angka) != 10 or stng > 0:
        hasil = 'list must contain 10 integer'
    
    else :
        part1 = ''
        part2 = ''
        part3 = ''
        for i in range(len(angka)) :
            if i < 3:
                part1 += str(angka[i])
            elif i > 2 and i < 6:
                part2 += str(angka[i])
            elif i > 5:
                part3 += str(angka[i])
            
        hasil = f'({part1}) {part2}-{part3}'
    return print(hasil)

create_phone_number([1,2,3,4,5,6,7,8,9,0])
create_phone_number([0,2,1,4,2,2,0,2,2,9])
print('ada string')
create_phone_number([1,'2',3,4,5,6,7,8,9])
print('kalo list lebih dari 10')
create_phone_number([1,2,3,4,5,6,7,8,9,0,1])
print('==========================================================================')

# NO3

def sort_odd_even(num):
    z=num
    genap=[]
    ganjil=[]
    if len(z)>0:
        for i in z:
            if i%2==0:
                genap.append(i)
            else:
                ganjil.append(i)
        # print(genap)
        # print(ganjil)
        list=genap
        for i in range(len(list)-1):
            for i in range(len(list)-1):
                if list[i]<list[i+1]:
                    list[i],list[i+1]=list[i+1],list[i]
        # print(list)
        list1=ganjil
        for i in range(len(list1)-1):
            for i in range(len(list1)-1):
                if list1[i]>list1[i+1]:
                    list1[i],list1[i+1]=list1[i+1],list1[i]
        # print(list1)
        m=[ganjil[0],ganjil[1],genap[0],genap[1],ganjil[2],genap[2]]
        print(m)
    else:
        print('masukan angka')

sort_odd_even([5,3,2,8,1,4])
sort_odd_even([7,1,8,9,2,10])
print('Kalo list kosong')
sort_odd_even([])
print('==========================================================================')

# 4. hallowTriangle
def hollowTriangle(height):
    z= ''
    a = height
    for i in range (a):
        for j in range (a*2+1):
            if j >= a-i and j <= a+i:
                if (j == a - i or j == a + i) or i == a - 1:
                    z += '#'
                else :
                    z += '_'
            elif j == (a*2+1)-1 or j == 0:
                z += ''
            else:
                z += '_'  
        z += '\n'
    print (z) 

hollowTriangle(1)
hollowTriangle(2)
hollowTriangle(3)
hollowTriangle(4)
hollowTriangle(5)
hollowTriangle(6)









