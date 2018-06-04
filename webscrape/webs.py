from bs4 import BeautifulSoup as bs
from urllib.error import HTTPError
from urllib.error import URLError
import urllib.request
import re


#  Override default user agent
class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"


urllib._urlopener = AppURLopener()


def main():
    try:
        open = AppURLopener()
        res = open.open("https://www.imovelweb.com.br/imoveis-sao-paulo-sp.html")
    except HTTPError as e:
        print(e)
    except URLError:
        print("Incorrect domain")
    else:
        page = bs(res, "html5lib")
        lis = page.findAll("li", {"class": "aviso-desktop"})
        # print(lis[1].find_all('input'))
        for i in range(len(lis)):
            inputs = lis[i].find_all('input')
            for j in range(len(inputs)):
                inp = inputs[j]
                print(inp)
                p = re.compile(r'\$(.+(\d))')
                # value = inp.findAll("input", {'class': 'avisoPrecio'})
                place_value = p.match(str(inp))
                if (place_value != None):
                    place_value = place_value.group(0)
                print(place_value)
            # child_input = li.children.name
            # if (child_input == 'input'):
            #     print(child_input)


main()
