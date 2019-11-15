from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import requests
import os
import time
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="flimapia"
)

link=[]
error=[]
mycursor = mydb.cursor()

brower = webdriver.Chrome(executable_path="E:\ChromeDriver\chromedriver.exe")
  
website_URL ="http://www.filmapia.com/where-is-it-shot/films/?language=All"
brower.get(website_URL)
brower.implicitly_wait(2)

brower.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
brower.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

scroll=0
print("Wait Until all movies Are loading......")
while(scroll!=1):
    try:
        brower.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        load=brower.find_element_by_class_name('load-more')
        load.click()
        time.sleep(2)
    except:
        scroll=1
        print("Loading complete!")
        
def information_downloader(s):
    brower.get(s)
    cast=""
    director=""
    production=""
    scenes=""
    scenes_des=""
    location=""
    location_link=""
    time.sleep(3)
    image1=brower.find_element_by_class_name('fm-movie-description')
    filmName = image1.find_element_by_id('film-name')
    film_name=filmName.text
    image3=brower.find_element_by_id('cast-container')
    cast_list=(image3.text.split('\n'))
    image4=brower.find_element_by_id('director-container')
    director_list=(image4.text.split('\n'))
    image5=brower.find_element_by_id('production-container')
    production_list=(image5.text.split('\n'))
    image6=brower.find_element_by_id('film-year-lang')
    year_list=image6.text.split('|')
    image7=brower.find_element_by_id('movie-desc')
    des=image7.text
    image8=brower.find_elements_by_class_name('fm-scenes-details')
    i=0
    for info in image8:
        i=i+1
        try:
            image9=info.find_element_by_tag_name('h3')
            if(scenes==""):
                scenes=image9.text
            else:
                scenes=scenes+","+image9.text
        except:
            error.append("scenes_name_"+str(i))
            
        try:
            image10=info.find_element_by_tag_name('p')
            if(scenes_des==""):
                scenes_des=image10.text
            else:
                scenes_des=scenes_des+","+image10.text
        except:
            error.append("scenes_des_"+str(i))
            
        try:
            image11=info.find_element_by_class_name('breadcrumb-loction')
            if(location==""):
                location=image11.get_attribute('title')
            else:
                location=location+","+image11.get_attribute('title')
        except:
            error.append("location_"+str(i))
            
        try:
            image12=image11.find_element_by_tag_name('a')
            brower.implicitly_wait(10)
            if(location_link==""):
                location_link=image12.get_attribute('href')
            else:
                location_link=location_link+","+image12.get_attribute('href')
        except:
            error.append("location_link_"+str(i))
            
    
    for i in cast_list:
        if(cast==""):
            cast=i
        else:
            cast=cast+","+i
    for j in director_list:
        if(director==""):
            director=j
        else:
            director=direstor+","+j
    for p in production_list:
        if(production==""):
            production=p
        else:
            production=production+","+p

    t=time.asctime(time.localtime(time.time()))
    sql = "INSERT INTO flim_info (time_stamp,film_name, cast, director, production, year, language, descpriton, location, location_link,scenes,scenes_descripton) VALUES (%s ,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (str(t),str(film_name),cast,director,production,str(year_list[1]),str(year_list[2]),str(des),location,location_link,scenes,scenes_des)
    mycursor.execute(sql, val)
    mydb.commit()
    
images=brower.find_elements_by_class_name('fm-movies')

for ima in images:
    i=ima.find_element_by_tag_name('a')
    link.append(i.get_attribute('href'))

for j in link:
    time.sleep(2)
    information_downloader(j)
    print("information collected")