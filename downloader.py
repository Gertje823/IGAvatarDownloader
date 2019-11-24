import requests
import urllib.request
from datetime import date
import sys
from dateutil.parser import parse as parsedate
import datetime
from urllib.parse import urlparse
import os, sys
import time
with open('users.txt', 'r', encoding='utf-8') as list_of_users:
            users = list_of_users.readlines()
today = date.today()
date = today.strftime("%d-%m-%Y")
i = 1
sessionid ="YOUR_SESSIONID_HERE"

for user in users:
        try:
                if i < 50:
                        i+=1
                        r=requests.get(f"https://www.instagram.com/web/search/topsearch/?context=blended&query={user}&rank_token=0.3953592318270893&count=1")
                        data = r.json()
                        users = data['users']
                        for u in users:
                            userid = u['user']['pk']
                            
                        r=requests.get(f"https://i.instagram.com/api/v1/users/{userid}/info/", headers={"Cookie":f"sessionid={sessionid};", "User-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 Instagram 12.0.0.16.90 (iPhone9,4; iOS 10_3_3; en_US; en-US; scale=2.61; gamut=wide; 1080x1920)"})
                        data = r.json()
                        username = data['user']['username']
                        ava = data['user']['hd_profile_pic_url_info']['url']
                        follower = data['user']['follower_count']
                        following = data['user']['following_count']
                        full_name = data['user']['full_name']
                        isPrivate = data['user']['is_private']
                        isVerified = data['user']['is_verified']
                        bio = data['user']['biography']
                        print(ava)
                        print("Username:", username)
                        print('Private:', isPrivate)
                        a = urlparse(ava)
                        name = os.path.basename(a.path)
                        
                        filename = f"{username} - {name}"
                        if not os.path.isfile(filename):
                            with open(filename, 'wb') as f:
                                urllib.request.urlretrieve(ava, f"{username} - {name}")
                                print(f"Image saved to {username} - {name}")
                        else:
                                print('File already exists, skipped.')
                                print(i)
                else:
                        i=0
                        print("Rate limit please wait")
                        time.sleep(180)
        except:
            pass
