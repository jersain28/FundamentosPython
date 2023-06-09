# funtion input -> retorno string
name=input('Como te llamas? ')
age=int(input('Cuantos años tienes \n'))
future=int(input('cuantos años mas? \n'))
             
print("Hola " + name)
print("En "+ str(future) + "años tendras " + str(age+future))

#Format Strings
"""
Hola Jersain, en 3 años tendras 
"""
text_complete="Hola {}, en {} años tendras {} años"
print(text_complete.format(name, future, age + future))

print("Hola {name}, en {future} años tendras {age+future} años")