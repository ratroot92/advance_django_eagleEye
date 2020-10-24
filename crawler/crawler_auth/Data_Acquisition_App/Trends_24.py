from bs4 import BeautifulSoup
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


class Twitter_Trends():
        
    def World_Top_Trends(self):
        url='https://trends24.in/';
        topTrends={};
        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)

        try:
            page = session.get(url);
        except Exception as e:
            print(e)
            print("World_Top_Trends -- Failed ")
            return topTrends
        status_code=page.status_code;
        
        hashtag_name=[];
        hashtag_href=[];
        hashtag_count=[];
        if(status_code==200):
            data=BeautifulSoup(page.text,'lxml')
            new=data.find('ol',class_="trend-card__list");
            li=data.find_all('li')
            for i in li:
                hashtag_name.append(i.a.text)
                hashtag_href.append(i.a.attrs['href'])
                if(i.find('span')):
                    hashtag_count.append(i.span.text)
                else:
                    hashtag_count.append("count unavalible")
            
            
                
        topTrends = []
        for item in zip(hashtag_name, hashtag_count, hashtag_href):
        
            topTrends.append({
                'name':item[0],
                'count':item[1],
                'href':item[2]})
            
        return topTrends
        
        


              
    def Pakistan_Top_Trends(self):
        url='https://trends24.in/pakistan/';
        topTrends={};
        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        try:
             page = session.get(url);
        except Exception as e:
            print(e)
            print("Pakistan_Top_Trends -- Failed ")
            return topTrends
        status_code=page.status_code;
       
        hashtag_name=[];
        hashtag_href=[];
        hashtag_count=[];
        if(status_code==200):
            data=BeautifulSoup(page.text,'lxml')
            new=data.find('ol',class_="trend-card__list");
            li=data.find_all('li')
            for i in li:
                hashtag_name.append(i.a.text)
                hashtag_href.append(i.a.attrs['href'])
                if(i.find('span')):
                    hashtag_count.append(i.span.text)
                else:
                    hashtag_count.append("count unavalible")
            
            
                
        topTrends = []
        for item in zip(hashtag_name, hashtag_count, hashtag_href):
        
            topTrends.append({
                'name':item[0],
                'count':item[1],
                'href':item[2]})
            
        return topTrends