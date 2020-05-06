from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request as urllib
import os 
import time
import logging as logger
import win32com.client as win32
import pandas as pd


class scrappy:
    def __init__(self,url=None,count=None):
        self.url = url # instagram open Account URL 
        self.savePhotosDir = r"C:\Users\Chandresh Singh\Documents\# Python Jupyter\Untitled Folder\Instagram bot\bots\main\temp" # photos saving DIR
        self.count = count # images count
        self.images = []
        self.videos = []
        self.scriptDir = os.path.dirname(os.path.realpath(__file__))  # current working Folder/Directory 
        self.postsUrls = []
        self.loadDriver()
    def loadDriver(self):
        try:
            # open chrome options pass --incognito add_argument 
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--incognito")
            self.driver = webdriver.Chrome(executable_path = r'./chromedriver.exe' , options=chrome_options)
            self.getUrl()
        except Exception as e:
            logger.error(str(e))
            
    def nav_user(self):
       self.driver.get('{}/{}/'.format("https://www.instagram.com",self.user)) #self.driver.get('htttps://instagram.com/user/')
       print ("navigating to... "+ self.user)        

    def getUrl(self):
        try:
            if self.driver is None:
                logger.error(" Please provide an url")
                return
            self.driver.get(self.url)
            # print(driver.get_log('driver')
        except Exception as e:
            logger.error( str(e))
        self.scollEnd()
    
    # Helps to scroll down
    def scollEnd(self):
        SCROLL_PAUSE_TIME = 2
         # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            if (len(self.postsUrls))>self.count:
                self.getPost()    
                return
            print("Scrolling..............")
            path = self.driver.find_elements_by_xpath("//*[@class='v1Nh3 kIKUG  _bz0w']//a")        
            self.getPostUrls(path)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Scroll down to bottom 
            time.sleep(SCROLL_PAUSE_TIME) # Wait to load page
            # Calculate new scroll height and compare with last scroll 
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            # print(last_height ,new_height )
            if new_height == last_height:
                self.getPost()    
                return 
            last_height = new_height 

    def getPostUrls(self,path):
        print("\nRetriving posts url .......")  
        for p in path:
            url = p.get_attribute("href")
            # print(url)
            if url not in self.postsUrls:
                self.postsUrls.append(url)

        print("Total posts found = " + str(len(self.postsUrls)))
        # print(self.postsUrls)
        

    def getPost(self):
        n=0
        for url in self.postsUrls:
           
            if n==self.count:
                self.saveImages()
            print(url+"\n")
            n=n+1
            self.driver.execute_script("window.open('"+url+"', '_self')")
            self.driver.implicitly_wait(2)
            imagesXpath = self.driver.find_elements_by_xpath("//*[@class='FFVAD']")
            for x in imagesXpath:
                img = x.get_attribute("srcset")
                # in @srcset there's about 3-4 resolution images url seperated by ,
                img = img.split(",")
                img = img[-1][:-6]
                print(img)
                if img not in self.images and img is not None :
                    # last one being highest res image -4 to escpae resoluton X*X in url
                    self.images.append(img)

            videosXpath = self.driver.find_elements_by_xpath("//*[@class='tWeCl']")
            for v in videosXpath:
                video = v.get_attribute("src")
                if video is not self.videos and video is not None:
                    self.videos.append(video)

        print("\nTotal Images found = "  + str(len(self.images)))
        print(self.images)
        print("\nTotal Videos found = " + str(len(self.videos)))
        print(self.videos)
        self.saveImages()
   
    def saveImages(self):
        # get the username to save phots name accordingly \
        temp=pd.read_csv('main/data/download_record.csv') 
        user=[]
        file=[]
        userName = self.url.split("/")
        userName = userName[-2]
        
        # saving into working folder as default 
        if self.savePhotosDir is None :      
            self.savePhotosDir = self.savePhotosDir = self.scriptDir + os.path.sep + 'Instagram'

        if not os.path.exists(self.savePhotosDir):
            os.makedirs(self.savePhotosDir)
        logger.info('\nFile saving into : ' + str(self.savePhotosDir))
    
        imgLen = len(self.images)
        print("Images found = "+str(imgLen))
        if self.count > imgLen or imgLen is None:
            self.count = imgLen

        try:
            for  i in range(self.count):
                fileName = self.savePhotosDir + os.sep + userName + str(i)+".jpeg"
                urllib.urlretrieve(self.images[i],fileName)
                print("\nSaving image = "+str(fileName))
                user.append(userName)
                file.append(fileName)
                

            if len(self.videos) >= 1:
                for i in range(len(self.videos)):
                    fileName = self.savePhotosDir + os.sep + userName + str(i)+".mp4"
                    urllib.urlretrieve(self.videos[i],fileName)
                    print("\nSaving video = "+str(fileName))
                    user.append(userName)
                    file.append(fileName)
                    
            data={"User":user,"File":file}
            df = pd.DataFrame(data)
            new=[temp,df]
            result = pd.concat(new)
            result.to_csv('main/data/download_record.csv',index=False)
            print('csv updating...')        
            
        except Exception as e:
            logger.error(str(e))

        print("Execution completed .....")
        time.sleep(10)
        self.driver.close()
        
 
        
class post:
    
    def __init__(self, username, password, path, caption):
        
        self.path = path
        self.caption = caption
        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'
        mobile_emulation = { "deviceName": "Nexus 5" }
        chrome_options = webdriver.ChromeOptions()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.driver = webdriver.Chrome('./chromedriver.exe',chrome_options=chrome_options)
        self.actionChain = webdriver.ActionChains(self.driver)
        self.login()
        
    def login(self):
        self.driver.implicitly_wait(2)
        self.driver.get('{}/accounts/login/'.format(self.base_url))
        time.sleep(3)
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_elements_by_xpath("//div[contains(text(),'Log In')]")[0].click()
        time.sleep(5)
        self.driver.find_elements_by_xpath("//button[contains(text(),'Not Now')]")[0].click()
        time.sleep(3)
       # self.driver.find_elements_by_xpath("//button[contains(text(),'Cancel')]")[0].click()
        self.newpost()
        
    def newpost(self):
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath('//div[@class="q02Nz _0TPg"]/*[name()="svg"][@aria-label="New Post"]').click()
        time.sleep(2)
        shell = win32.Dispatch("WScript.Shell")
        time.sleep(1)
        shell.Sendkeys(r"{}".format(self.path))
        shell.Sendkeys('{ENTER}')
        time.sleep(2)
        self.driver.find_elements_by_xpath("//button[contains(text(),'Next')]")[0].click()
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/div[2]/section[1]/div[1]/textarea").send_keys(r"{}".format(self.caption))
        self.driver.find_elements_by_xpath("//button[contains(text(),'Share')]")[0].click()
        time.sleep(20)
        #self.driver.find_elements_by_xpath("//button[contains(text(),'Not Now')]")[0].click()
        self.driver.close()
        
        
class auto_post:
    
    def __init__(self,n_logins,n_posts,fetch):
        data=self.fetch(fetch)
        login_id=pd.read_csv('main/data/temp_users.csv')
        x=0
        for n in login_id.iloc:
            x=x+1
            z=x-1
            if x > n_logins:
                break
            else:
                [username,password]=login_id.iloc[z] #z= no. of rows
                [Caption_id,path_id]=data
                y=0
                for i in Caption_id:
                    y=y+1
                    u=y-1
                    if y > n_posts:
                        break
                    path=path_id[u]
                    CaptionId=Caption_id[u]
                    caption='Have a look this amazing picture by:@{} #xperienceimagiantion #india #streetphotography #instalike #portraitphotography #likes #photos #foto #a #cute #followme #blackandwhite #lifestyle #sky #music #picture #followforfollowback #photographylovers #me #artist #d #l #makeup #instaphoto #instapic #insta #smile #travelgram'.format(CaptionId)
                    post(username, password, path, caption)
                time.sleep(1)
                
                
    def fetch(self,fetch):
        data=pd.read_csv('main/data/download_record.csv')
        x=[]
        y=[]
        username=data['User']
        z=0
        for i in username:
            [u,p]=data.iloc[z]
            z=z+1
            print(u)
            if u in fetch:
                x.append(u)
                y.append(p)
            else:
                continue
        data=[x,y]
        return(data)
            

        
#if __name__ == "__main__":
    
    
    #username="your_username"
    #password = "your_password"
    #path = r"C:\Users\Chandresh Singh\Documents\Scanned Documents\Welcome Scan.jpg"
   # caption="new post"
  #  ibot = post(username, password, path, caption)
''' 
    url = "https://www.instagram.com/bnw/"
    count = 3
    
    instagram = scrappy(
        user= user,
        count = count
        )
    
'''
    
















