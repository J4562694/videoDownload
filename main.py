from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import os
import time

# 存储视频的位置
local_path = 'videos'
if not os.path.exists(local_path):
    os.makedirs(local_path)

# 爬取页面网址
url = 'https://www.istockphoto.com/search/search-by-asset?affiliateredirect=true&assetid=1285651124&assettype=film&utm_campaign=srp_videos_10&utm_content=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fvideos%2F%25E6%2588%25B4%25E5%25B7%25A5%25E5%259C%25B0%25E5%25AE%2589%25E5%2585%25A8%25E5%25B8%25BD%2F&utm_medium=affiliate&utm_source=pexels&utm_term=%E6%88%B4%E5%B7%A5%E5%9C%B0%E5%AE%89%E5%85%A8%E5%B8%BD'

# 启动Chrome浏览器
chrome_options = webdriver.ChromeOptions()
chromeDriver = r'C:\Users\JingzeSystem\Desktop\picturesDownload\chromedriver.exe'
driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()
driver.get(url)
time.sleep(300)  # 给页面加载留出足够时间

videoItems = 87

# 使用XPath找到所有视频元素
videos = driver.find_elements(By.XPATH, '//video')

for i, video in enumerate(videos, start=1):
    if i > videoItems:
        break
    video_url = video.get_attribute('src')
    if video_url :
        try:
            response = requests.get(video_url)
            filename = f'{i}.mp4'
            if response.status_code == 200:
                with open(os.path.join(local_path, filename), 'wb') as f:
                    f.write(response.content)
                print(f"Video {i} downloaded.")
        except Exception as e:
            print(f"Error downloading video {i}: {e}")

driver.close()
