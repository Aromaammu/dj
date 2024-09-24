import requests
from bs4 import BeautifulSoup
website_url="https://infopark.in/companies/job-search"
res = requests.get(website_url, verify=False)
keywords=["python","php"]
output_file=open("jobs.txt",'w')
soup=BeautifulSoup(res.text,'lxml')
soup.find_all("div",{"class:row company-list,joblist"})
jobs=soup.find_all("div",{"class":"row company-list joblist"})
for job in jobs:
    title_element=job.find("a")
    title=title_element.text
    link=title_element["href"]
    company_name=job.find("div",{"class":"jobs-comp-name"}).text
    last_date=job.find("div",{"class":"jobs-comp-name"}).text
    if any(word.lower()in title.lower() for word in keywords):
        output_file.write(title+""+company_name)
