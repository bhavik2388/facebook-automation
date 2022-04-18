def scrapping():
    import praw
    import os
    import urllib
    import pandas as pd

    reddit =  praw.Reddit(client_id="KvOqIFkkksXsApJQNUrJdw",
                        client_secret="Z540CgcOCl6K60AdI2hc_XOg2x_52g",
                        user_agent="facebook automation")

    subreddit = reddit.subreddit('ProgrammerHumor')

    posts = subreddit.hot(limit=10)

    post_dict = {'Title':[], 'Score':[],'Comments':[], 'Post Url':[]}


    global count
    count = 0
    for post in posts:
        post_dict['Title'].append(post.title)
        post_dict['Score'].append(post.score)
        post_dict['Comments'].append(post.num_comments)
        post_dict['Post Url'].append(post.url)
        if post.url.endswith("jpg") or post.url.endswith("png") or post.url.endswith("jpeg"):
            count = count+1
            urllib.request.urlretrieve(post.url, f"image{count}.jpg")



    top_posts = pd.DataFrame(post_dict)
    top_posts.to_csv("Posts Data.csv",index=True)


from selenium import webdriver
from time import sleep

id = input("Enter your mail or mobile no. : ")
password = input("Enter ypur password: ")

def automation():
    driver = webdriver.Chrome(executable_path="C:/Users/bhavi/chromedriver/chromedriver")

    driver.get("http://facebook.com/")

    driver.implicitly_wait(5)
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input").send_keys(id)
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input").send_keys(password)
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button").click()

    driver.implicitly_wait(5)
    driver.find_element_by_xpath("html/body/div[1]/div/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/ul/li[1]/span/div/a").click()

    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div[2]").click()
    sleep(2)

    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/div/div/input").send_keys("E:/Facebook Automation/"+f"image{count}.jpg")
    sleep(1)
    btn = driver.find_element_by_xpath("//div[@aria-label='Post']")
    sleep(1)
    btn.click()
    sleep(3)

scrapping()

while count >= 0:
    automation()
    count = count - 1 
    sleep()