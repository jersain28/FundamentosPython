
#Diccionarios
#{"clave": "Valor"}

teacher={
    "name": "Jersain",
    "l_name": "Marin",
    "phone": "247123456",
    "groups": ["3BTIADSM", "3BTIADSM"]
}

print(type(teacher))
print(teacher)
print(teacher["name"])
print(teacher["groups"])
teacher["groups"].append("3CDSM")
teacher["phone"]="2471070544"
teacher["city"]="Huamantla"
print(teacher)