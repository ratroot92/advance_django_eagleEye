from bs4 import BeautifulSoup
import requests

class Twitter_Trends():
        
    def World_Top_Trends(self):
        url='https://trends24.in/';
        page = requests.get(url);
        status_code=page.status_code;
        dic={};
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
            
            
                
        dic = []
        for item in zip(hashtag_name, hashtag_count, hashtag_href):
        
            dic.append({
                'name':item[0],
                'count':item[1],
                'href':item[2]})
            
        return dic


              
    def Pakistan_Top_Trends(self):
        url='https://trends24.in/pakistan/';
        page = requests.get(url);
        status_code=page.status_code;
        dic={};
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
            
            
                
        dic = []
        for item in zip(hashtag_name, hashtag_count, hashtag_href):
        
            dic.append({
                'name':item[0],
                'count':item[1],
                'href':item[2]})
            
        return dic