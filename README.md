# instagram_xpbot
![Plateform](https://img.shields.io/badge/Platform-Linux%2FMacOS%2FWindows-red.svg) 
![Instagram XpBot](https://img.shields.io/badge/Instagram_XpBot-V.1.0.0-yellow.svg?logo=instagram&style=V.1.1.0)
![Python3.7](https://img.shields.io/badge/Python-V3.7.6-green.svg?)
![Selenium3.141.0](https://img.shields.io/badge/Selenium-V3.141.0-Blue.svg?)
## Getting Started
Goal of this project is to automate your instagram.  I’ve noticed a growing frustration within most people trying to build an audience on that platform. It goes something like this:
* “I’m doing everything the experts suggest to grow my Instagram — I post consistently and at the right times, I use the most relevant Instagram hashtags, I create engaging content, and I optimize for the ever-changing Instagram algorithm — and yet, my Instagram account STILL isn’t growing!”
* There is no ONE key to growing your Instagram. So I have bring you this project. It's a `selenium` based `python-script` it simply automate most of the instagram's functions.
## Built With
* `Python 3`
* `Selenium`
##  Functionalities of bot
* `Auto-like` and `auto-comment` on posts of various `ig-users`, `tagged-top-posts` and `hashtagged-top-posts`.
* `Follow/Unfollow` multiple users (takes user from a csv file saved in .data directory).
* `Scrape-ig-media` of any user account which can be accessed through your login account. You can get your download files locations and can fetch them from data/download_record.csv
* `Single or multiple posts` from diffrent ig accounts (access media files through download_record.csv and users from temp_users.csv)
* Scrape `ig user's followers and following's` list (access through data/followers and data/followings).
* `Auto-story-viewer`
## Installation
* Clone the repository `https://github.com/Chandresh24Singh/instagram_xpbot`.
* Install `Requirments.txt`.
* Download `web-driver` for your respective browser and os. I'm here using `chrome-web-driver` for `windows`.
* Locate the directory for your `web-driver`.
* Change directory location of `csv files` and `download media`.
* Change `your_username` and `your_password` to your login credentials.
