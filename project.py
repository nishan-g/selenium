from bs4 import BeautifulSoup
import requests
import json

 


data = []
def read_and_write(html_content,selector):
    r =requests.get('https://webcache.googleusercontent.com/search?q=cache:https://webparanoid.com/en/scams-database')
    with open('test.html','w') as f:
        f.write(r.text)

    soup = BeautifulSoup(html_content,'html.parser')
    divs = soup.select(selector)

    for div in divs:
        condition = div.find('div').text
        name = div.find('a').text
        site_link = div.find('a')['href']
        description_tag = div.find('p')
        description = description_tag.text if description_tag else ''

        data.append({
            'Condition': condition,
            'Name': name,
            'Site_link': site_link,
            'Description' : description
        })
        with open('output.json','w') as f:
            json.dump(data,f,indent=0)


with open('test.html','r') as f:
    content = f.read()
read_and_write(content,'div.bg-blue-gray.p-6.mx-3.mb-6.rounded-xl')

def read_links(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)
    return [item['Site_link'] for item in data]


def fetch_reviews(links):
    good_reviews =[]
    bad_reviews = []
    for link in links:
        r = requests.get(f"https://webcache.googleusercontent.com/search?q=cache:https://webparanoid.com{link}")
        with open('temp.html', 'w') as f:
            f.write(r.text)
        
        with open('temp.html', 'r') as f:
            content = f.read()
        
    #     soup = BeautifulSoup(content, 'html.parser')
    #     divs = soup.select('div.bg-green-test-light.rounded-xl.py-4.px-6.-mx-px')

    #     good_reviews = [div.text for div in soup.select('selector_for_good_reviews')]
    #     bad_reviews = [div.text for div in soup.select('selector_for_bad_reviews')]
        
        
        
    # with open('output.json','w') as f:
    #     json.dump(data,f,indent=0)


links = read_links('output.json') 
print(len(links))
print(links)
# fetch_reviews(links)