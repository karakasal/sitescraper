import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://")
soup = BeautifulSoup(res.text,"html.parser")
res2 = requests.get("https://")
soup2 = BeautifulSoup(res2.text,"html.parser")

links = soup.select(".titleline")
subtext = soup.select(".subtext")
links2 = soup2.select(".titleline")
subtext2 = soup2.select(".subtext")

mega_links = links + links2
mega_subtext = subtext + subtext2

def sorted_dict(title_list):
    return sorted(title_list, key= lambda k:k["v"], reverse=True)

def get_titles(links,subtext):
    titles = []
    for index, item in enumerate(links):
        title = links[index].getText() 
        href = links[index].find('a')['href'] 
        vote = subtext[index].select(".score") 
        if len(vote):
            points = int(vote[0].getText().replace(" points","")) 
            if points > 99:
                titles.append({"t":title,"l":href,"v":points}) 
    return sorted_dict(titles)

pprint.pprint(get_titles(mega_links,mega_subtext))
