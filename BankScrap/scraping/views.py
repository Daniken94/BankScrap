from django.shortcuts import render
from django.views import View

import requests
from bs4 import BeautifulSoup


class Index(View):
    def get(self, request):

        page = requests.get("http://www.bankier.pl/gielda/notowania/akcje")
        soup = BeautifulSoup(page.content, "html.parser")
        arr = soup.find_all('td', class_="colWalor textNowrap")
        arrkurs = soup.find_all('td', class_="colKurs")
        rows = soup.find_all('tr')

        u = 0
        kwalor = []
        for i in arr:
            arr2 = soup.find_all("td", class_="colWalor textNowrap")[u].get_text()
            kwalor.append(str.strip(arr2))
            u = u+1
        
        titler = []
        
        for titles in rows:
            nwalor = titles.find("a")
            if nwalor:
                wwalor = nwalor.get("title")
                titler.append(wwalor)


        # kurs = []

        # for kurse in rows:
        #     nwalor = kurse.find("td", class_="colKurs change up")

        #     kurs.append(nwalor)
        #         u = 0

        f = 0
        kurs = []
        for i in arrkurs:
            arr2 = soup.find_all("td", class_="colKurs")[f].get_text()
            kurs.append(str.strip(arr2))
            f = f+1


        return render(request, "index.html", {"arr": arr, "kwalor": kwalor, "titler": titler, "kurs": kurs})
