name ="İzel"
print(name)
print(type(name))
#name string bir veri tipi
age=25
print(age)
print(type(age))
#age integer veri tipi

job=False
print(job)
print(type(job))
#job boolean bir veri tipi 

height=1.63
print(height)
print(type(height))
#height bir float veri tipi 

if job==1:
    print("Kişi bir işte çalışıyor")
else:
    print("Kişi işsiz")


if height<1.5:
    print("Kişi kısadır")
elif 1.5< height <=1.7:
    print("Kişi orta boyludur")
else:
    print("Kişi uzundur")