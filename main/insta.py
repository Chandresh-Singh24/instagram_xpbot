# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 03:42:59 2020

@author: Chandresh Singh
"""
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os
import csv
import time
import pandas as pd

class InstragramBot:

    def __init__(self, username, password):
        """
    	Initializes an instance of the InstagramBot class. 
    	Call the login function and log in.
        """
       
        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome('./chromedriver.exe', options=chrome_options)
        
        
        self.actionChain = webdriver.ActionChains(self.driver)
        self.login()

    def find_buttons(self, button_text):
        #find buttons
        buttons = self.driver.find_elements_by_xpath("//*[text()='{}']".format(button_text))
        return buttons
    
    def nav_url(self,url):
        self.driver.get('{}'.format(url))
        print("navigating to url..." + url)
        time.sleep(4)
        
    
    def infinite_scroll(self):
        """
        Scrolls to the bottom of a users page to load all of their media
        Returns:
        bool: True if the bottom of the page has been reached, else false
        """
        self.last_height = self.driver.execute_script("return document.body.scrollHeight")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.new_height = self.driver.execute_script("return document.body.scrollHeight")


        if self.new_height == self.last_height:
            return True

        self.last_height = self.new_height
        return False

    def login(self):
        
        self.driver.get('{}/accounts/login/'.format(self.base_url))
        time.sleep(4)
       # try:
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_elements_by_xpath("//div[contains(text(),'Log In')]")[0].click()
        time.sleep(6)
        self.driver.find_elements_by_xpath("//button[contains(text(),'Not Now')]")[0].click()
    #except NoSuchElementException:
         #   pass
        #except IndexError:
         #   pass

       
    def nav_user(self,user):
    	#navigates through user profile
        self.driver.get('{}/{}/'.format(self.base_url,user)) #self.driver.get('htttps://instagram.com/user/')
        print ("navigating to... "+ user)
    
      
        
    def follow_user(self, user):
    	self.nav_user(user)
    	follow_button = self.find_buttons('follow')
    	follow_button.click()
    
    def unfollow_user(self, user):
        self.nav_user(user)
        unfollow_button = self.find_buttons('following')
        if unfollow_button:
            for btn in unfollow_button:
                btn.click()
                unfollow_confirmation = self.find_buttons('Unfollow')[0]
                unfollow_confirmation.click()
            else:
                print('Already following'+ user)
                 
            
    
    def like_latest_posts(self, n_posts, like=True):
        """
        Likes a number of a users latest posts, specified by n_posts.
        Args:
            user:str: User whose posts to like or unlike
            n_posts:int: Number of most recent posts to like or unlike
            like:bool: If True, likes recent posts, else if False, unlikes recent posts
        TODO: Currently maxes out around 15.
        """
        action = 'Like' if like else 'Unlike'
        self.driver.find_elements_by_class_name('_9AhH0')[0].click()
        for img in range(n_posts):
            time.sleep(6) 
            try:
                self.driver.find_element_by_xpath("//*[@aria-label='{}']".format(action)).click()
            except Exception as e:
                print(e)
            time.sleep(2)
            #self.comment_post('have look on @xperience.imagination')
            self.driver.find_elements_by_class_name('_65Bje')[0].click()	
            print("Liked")

    def comment_latest_posts(self, n_posts, text, like=True):
        
        self.driver.find_elements_by_class_name('_9AhH0')[0].click()
        for img in range(n_posts):
            time.sleep(3) 
            self.comment_post(text)
            self.driver.find_elements_by_class_name('_65Bje')[0].click()

    def comment_post(self, text):
        """
        Comments on a post that is in modal form
        """
        time.sleep(3)
        for i in range(0, 22):  
            try:
                comment_input = self.driver.find_elements_by_class_name('Ypffh')[0]
                comment_input.click()
                comment_input.send_keys(text)
                self.find_buttons('Post')[0].click()
                time.sleep(30)
                print('Commentd.')
                break
            except StaleElementReferenceException as Exception:
                print("error retrying")


    def view_story(self,user):
        """
        to view someone's story directly
        """
        self.driver.get('{}/stories/{}/'.format(self.base_url,user)) #https://www.instagram.com/stories/lorenzoragazzi/
        #close
        for i in range(0, 2):
            try:    
                time.sleep(2)
                TapToPlay = self.find_buttons('Tap to play')[0]
                TapToPlay.click()
                time.sleep(4)
                close = self.find_buttons('Close')[0]
                close.click()
            except IndexError:
                pass
            continue
        
    def view_story_csv(self, csv_name,n_posts):
        with open("data/"+csv_name + ".csv") as f:
            reader = csv.reader(f)
            n=0
            for row in reader:
                n=n+1
                m=n-1
                print(n, " navigating to: " + row[0])
                #self.view_story(row[0])
                #time.sleep(20)
                #deleting user from csv
                data = pd.read_csv("data/"+csv_name+ ".csv")
                data.drop([m],implace = True)
                print ("deleting",n)
                
                if n==n_posts :
                    break
        
    def like_photo_hashtag(self, hashtag, n=40):
        
        self.driver.get('{}/explore/tags/{}/'.format(self.base_url,hashtag)) #self.driver.get('htttps://instagram.com/explore/tags/tag')
        time.sleep(2)
        self.like_latest_posts(n)
       
    def comment_photo_hashtag(self, hashtag, comment, n=10):
        self.driver.get('{}/explore/tags/{}/'.format(self.base_url,hashtag)) #self.driver.get('htttps://instagram.com/explore/tags/tag')
        time.sleep(4)
        self.comment_latest_posts(n, comment)
        time.sleep(20)
    
    def getUserFollowers(self,max,username):
        temp=pd.read_csv('main/data/followers.csv')
        self.nav_user("{}".format(username))
        followersLink = self.driver.find_element_by_css_selector('ul li a')
        followersLink.click()
        time.sleep(5)
        followersList = self.driver.find_element_by_css_selector('div[role=\'dialog\'] ul')
        numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
        
        followersList.click()
        
        while (numberOfFollowersInList < max):
            self.actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
            print(numberOfFollowersInList)
            time.sleep(2)
        
        followers = []
        for user in followersList.find_elements_by_css_selector('li'):
            userLink = user.find_element_by_css_selector('a').get_attribute('href')
            print(userLink)
            followers.append(userLink)
            if (len(followers) == max):
                break
        new=[temp,followers]
        new = pd.concat(new)
        new.to_csv('main/data/followers.csv',index=False)
        followers_new=pd.DataFrame(followers)
        followers_new.to_csv('main/data/updated_followers.csv',index=False)
        return followers 
        
     