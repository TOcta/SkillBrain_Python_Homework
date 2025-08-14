# Tema 3

# Scrie un program care:

# Are deja salvate două informații: numele de utilizator și parola corectă.

# Cere utilizatorului să introducă numele de utilizator și parola de la tastatură.

# Verifică următoarele situații:

#     Dacă numele de utilizator introdus este corect și parola introdusă este corectă → afișează "Acces permis".

#     Dacă doar una dintre cele două este corectă (numele de utilizator sau parola) → afișează "User/Password incorect".

#     Dacă ambele sunt greșite → afișează "Acces respins".


    


usercor = "Octavian"
passwordcor = "1234"

user = input("Va rog sa introduceti numele de utilizator si parola\nUser: ")
password = input("Password: ")

# chiar daca scriu userul gresit imi ia mai intai in functie de cum este scris codul, trebuie avut grija la cum sunt pozitionate conditiile ptc este posibil
# sa se anuleze singura pana ajunge la conditia finala
if user != usercor and password !=passwordcor:
    print("Acces respins")
elif usercor != user or password !=passwordcor:
    print("ser/Password incorect")   
elif user ==usercor and password ==passwordcor:
    print("Acces permis")

# if usercor != user:
#     print("User incorect")   
# if password != passwordcor:
#     print("Password incorect")