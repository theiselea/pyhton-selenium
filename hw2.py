import os
print("Öğrenci Kayıt Sistemine Hoşgeldin!")
studentList = ["Armağan Aksu", "Ali Demir", "İrem Kayacı"]

#öğrenci isim kaydetme
def register():
    newRegister = input("Kayıt olmak için isim ve soyisminizi girin: ")
    studentList.append(newRegister)
    print("Mevcut Liste\n",studentList)

#öğrenci isim silme
def deletion():
    delete = str(input("Silmek istediğiniz Öğrencinin isim soyismini giriniz: "))
    studentList.remove(delete)
    print("Mevcut Liste\n", studentList)

#birden fazla öğrenci ekleme
def multipleAdding():
    studentList.extend(["Tekmil Temir" , "İbrahim Güneş"]) 
    print(studentList)

#öğrenci no öğrenme
def detNumbers():
    no = int(input("Yazdırmak istediğiniz öğrencinin numarasını girin:  "))
    print(studentList[no])

#birden fazla öğrenci silme
def multipleDiscard():
    response =int(input("Öğrenci silmek için 1'e bas: "))
    while response==0:
        if response==1:
            multiple=input("Silmek istediğiniz ismi girin: ")
            studentList.remove(multiple)
            print("Mevcut liste\n", studentList)
        else:
            break

#liste
def listing():
    i = 0
    for i in range(len(studentList)):
        print(studentList[i])
        i+=1

def selectOperation():
    operator = int(input("""Lütfen İşlem Seçiniz\n
    1.Kayıt Olma
    2.İsim Çıkarma
    3.Birden Fazla İsim Ekleme
    4.Numara ile Öğrenci Yazdırma
    5.Birden Fazla İsim Çıkarma 
    6.Listeleme
    7.Çıkış
    """))
    if operator == 1:
        register()
    elif operator == 2:
        deletion()
    elif operator == 3:
        multipleAdding()
    elif operator == 4:
        detNumbers()
    elif operator == 5:
        multipleDiscard()
    elif operator == 6:
        listing()
    elif operator == 7:
        exit()        
    else :
        print("Listede olmayan bir seçim yaptınız!")
    while True:
        selectOperation()
        
selectOperation()


