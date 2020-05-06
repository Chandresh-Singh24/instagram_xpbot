from main import scrap_post
from main import insta
import time
import os
import csv

 

"""
Here is your working bot
.
.
.
Change to your credentials
"""


if __name__ == '__main__':
    

    #--------------------to scrap media-------------------------#
    '''
    url = "https://www.instagram.com/thevedats/"
    count = 10
    scrap = scrap_post.scrappy( 
        url = url, 
        count = count
        )
    
    scrap.loadDriver()
    '''   
    ###############################################################
    
    

    #----------------instagram bot in new instance----------------#

    ibot = insta.InstragramBot('your_username','your_password')
        
    
    #ibot.getUserFollowers('xperience.imagination', 20)
    
    #ibot.nav_user('xperience.imagination/tagged')
    
    
    
    time.sleep(10)
   # ibot.comment_latest_posts(13, "great concept! Really love your profile")
    ##print()
    #("done")
    
   # time.sleep(500)

    #ibot.nav_user('xperience.imagination/tagged')
    #time.sleep(10)
    #ibot.comment_latest_posts(10, "great pic! ")
    #print("done")
    #print()
    
    #time.sleep(500)

    #ibot.nav_user('xperience.imagination/tagged')
    #time.sleep(10)
    #ibot.like_latest_posts(20)
    #print("done")
    #print()

    #time.sleep(1000)
    

    #time.sleep(10)
   # ibot.nav_user('xperience.imagination/tagged')
    #time.sleep(10)
    #ibot.comment_latest_posts(20, "Amazing content! Really love your profile")
    #print()
   # print("done")
    
    #ibot.like_photo_hashtag('paris')
    #time.sleep(3500)
    
    #ibot.nav_user('xperience.imagination/tagged')
    #time.sleep(3)
    #ibot.comment_latest_posts(10, "Amazing concept!")
    
    #time.sleep(4)
    #ibot.view_story('xperience.imagination')
    #ibot.get_user_followers("xperience.imagination")
    
#    ibot.view_story_csv("users",1)
            
   # ibot.driver.close()      

    
    
    
    

