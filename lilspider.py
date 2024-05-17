"""
I know this script is awful :)
But because it solved my problem, I put it on GitHub
Unfortunately, it is not my priority, but I will try to improve it next year
"""

import concurrent.futures
import requests
import os
import time
from bs4 import BeautifulSoup

# ///////////////// Extract href links /////////////////
def get_links():
    for i in range(7251):
        print('-------------[ Page '+str(i)+']-------------')
        os.system('curl -s "https://www.enamad.ir/DomainListForMIMT/Index/'+str(i)+'" -e "https://www.enamad.ir/" -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/314.0.0.0 Safari/537.36" | grep ?id= >> orginal_urls.txt')
        time.sleep(1)
    print('create clean link file...')
    os.system("""cat orginal_urls.txt | cut -d '"' -f 2 > enamad-URLS.txt""")
    print('Start to Extarct informations:')
    


# ///////////////// Erxtract Data link by link /////////////////
def fetch_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/314.0.0.0 Safari/537.36','Referer': 'https://www.enamad.ir/',} 
    try:
        global a, file1, file2, totalReq
        file1 = open("enamad-data.txt", "a")
        totalReq = open("total_request.txt", "a")
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        a_elements = soup.find_all('a', class_='domainlink')
        div_elements = soup.find_all('div', class_='col-sm-12 col-md-8 contentinformation licontent mobiledes')
        div_elements2= soup.find_all('div', class_='col-sm-12 col-md-6 contentinformation licontent mobiledes')
        td_elements= soup.find_all('div', class_='cls_td')
        for a in a_elements:
            file1.write("\n"+a.text.strip())
        for div in div_elements:
            file1.write("\t"+div.text.strip())
        for div2 in div_elements2:
            file1.write("\t"+div2.text.strip())
        for td1 in td_elements:
            file1.write("\t"+td1.text.strip())
        totalReq.write(url+"\n")

        print(f"Processed: {url}")
    except requests.RequestException as e:
        print(f"Error fetching data in request ")
        file2 = open("enamad-data.txt", "a")
        file2.write("\n"+a.text.strip()+"\tERROR_314")
        file2.close()


# ///////////////// threads nummber (Default: 20) /////////////////
def main():
    with open('enamad-URLS.txt', 'r') as file:
        urls = file.read().splitlines()
    batch_size = 20
    with concurrent.futures.ThreadPoolExecutor(max_workers=batch_size) as executor:
        for i in range(0, len(urls), batch_size):
            batch_urls = urls[i:i + batch_size]
            results = list(executor.map(fetch_url, batch_urls))
# ///////////////// for fix ratelimit issue /////////////////
            #time.sleep(5)

    for url, result in zip(urls, results):
        print(f"URL: {url} - Result: {result}")

if __name__ == "__main__":
    get_links()
    main()
    file1.close()
