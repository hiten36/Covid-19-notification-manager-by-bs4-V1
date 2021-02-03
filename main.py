import requests
from bs4 import BeautifulSoup
from plyer import notification

def noti(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon="/home/hiten/PycharmProjects/covid-19 notification manager/covid19 notification manager/icon.png",
        timeout=6
    )
def request(url):
    p=requests.get(url)
    return p.text
if __name__ == '__main__':
    url=request('https://www.deccanherald.com/national/coronavirus-india-karnataka-maharashtra-delhi-tamil-nadu-west-bengal-update-state-wise-total-number-of-confirmed-cases-deaths-on-october-28-908058.html')
    soup=BeautifulSoup(url,'html.parser')
    states_list=[]
    for td in soup.find_all('td')[3:]:
        states_list.append(td.get_text())
    states_to_show=['rajasthan','delhi','mumbai','bihar']
    for index,states in enumerate(states_list):
        if states.lower() in states_to_show:
            ntitle=states_list[index]
            nmessage=f'Total cases: {states_list[index+1]}\nTotal deaths: {states_list[index+2]}'
            noti(ntitle,nmessage)