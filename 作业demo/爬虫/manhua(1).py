from bs4 import BeautifulSoup
#import csv
import json
import random
import requests
pa=0
def dealwithcontent(htmltext):
    final=[]
    bs = BeautifulSoup(htmltext, "html.parser")  # 创建BeautifulSoup对象
    body=bs.body;
    midcontainer=body.find("div",{id:'middleContainer'});
    comic=midcontainer.find("div",{id:'comic'})
    img=comic.find('img');
    src=imf['src']
    
    
    
    
    
    
    body=bs.body
    midcontain = body.find('div',{'id': 'middleContainer'})  # 找到id为7d的div
    comic = midcontain.find('div', {'id': 'comic'})  # 找到id为7d的div
    img = comic.find('img')
    src=img['src']
    imgelink=src
    #jdurl=jd['src']
    final.append(imgelink)
    return final

temp=[]
for i in range(3):
    page=i+2061




    url =f"https://xkcd.com/{page}"
    print(url)
    data= requests.get(url)
    final = []
    bs = BeautifulSoup(data.text, "html.parser")  # 创建BeautifulSoup对象
    body = bs.body
    midcontain = body.find('div', {'id': 'middleContainer'})  # 找到id为7d的div
    comic = midcontain.find('div', {'id': 'comic'})  # 找到id为7d的div
    img = comic.find('img')
    src = img['src']
    imgelink = 'http:'+src
    # jdurl=jd['src']
    final.append(imgelink)
    temp.append(final)
    print(final)
    mc=0

    for i in final:
        #重新访问得到图片
     
        
        
        
        
        
        
        image=requests.get(final[0]);

        src=f"D://image//image{pa}.png"
        with open(src,"wb") as f:
            f.write(image.content)
        pa=pa+1



#print(imgs)
print(temp)







    #data=requests.get(url)
    #links=BeautifulSoup(data).select("a")
    #urls=[]
    #for link in links:
       # url.append(link["href"])

#print(url)






