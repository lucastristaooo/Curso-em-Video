from datetime import date
x = int(input("Digite sua data de nascimento: "))
if (date.today().year - x) >= 18:
    print(f"Você tem {date.today().year-x} e seu alistamento deveria ter ocorrido a {(date.today().year-x)-18} ano(s)")
elif (date.today().year - x) == 18:
    print(f"Você tem {date.today().year-x} e já deve se alistar esse ano")
elif (date.today().year -x) < 18:
    print(f"Você tem {date.today().year-x} e seu alistamento deve ocorrer daqui {18-(date.today().year-x)} ano(s)")