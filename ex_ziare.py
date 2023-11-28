import requests
from bs4 import BeautifulSoup
import openpyxl
def extragere_informatii_produse(url, limita = 5):
    raspuns = requests.get(url)


    if raspuns.status_code == 200:
        soup = BeautifulSoup(raspuns.text, "html.parser")
        elemente_nume = soup.find_all("a", class_="font-bold d-block mt-md-2 mb-1")
        elemente_pret = soup.find_all("div", class_="real-price font-bold")    
        informatii_produse = []
       
        index = 0
       
        for nume_element, pret_element in zip(elemente_nume, elemente_pret):
            nume = nume_element.get_text(strip=True)
            pret = pret_element.find("span").get_text(strip=True)
            informatii_produse.append({"nume": nume, "pret": pret})

            index <= 1

            if index >= limita:
                return informatii_produse
            
        return informatii_produse  
    else:
        print("Cererea HTML a esuat.Cod de stare", Raspuns_stare_code)   
        return None 
    
url = "https://adevarul.ro/stiri-locale/bacau/"

informatii_produse = extragere_informatii_produse(url, limita=5)

if informatii_produse:
    for i in informatii_produse:
        nume_produs = i["nume"]
        pret = format(round(float(i["pret"])*1000))
        print("Nume produs:", nume_produs)
        print("Pret:", pret)
        print()