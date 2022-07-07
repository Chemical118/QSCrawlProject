from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep

# Input
year = 2022
target_url = ['biological-sciences', 'computer-science-information-systems']
target_url = map(lambda t: t.lower().replace(' ', '-'), target_url)

# Selenium Setting
ua = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={ua.random}')
# options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
# options.add_argument("disable-gpu")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

basic_url = 'https://www.topuniversities.com/university-rankings/university-subject-rankings/' + str(year) + '/'

# Main
for target in target_url:
    driver.get(basic_url + target)
    sleep(3)

    driver.find_element(By.XPATH,
                        '//*[@id="block-tu-d8-content"]/div/article/div/div/div[3]/div/div[1]/div/div[3]/div[4]/div[1]/div[2]').click()
    sleep(0.5)

    driver.find_element(By.XPATH,
                        '//*[@id="block-tu-d8-content"]/div/article/div/div/div[3]/div/div[1]/div/div[3]/div[4]/div[1]/div[2]/div[2]/div[2]').click()
    sleep(3)

    driver.find_element(By.XPATH, '//*[@id="ranking-fillters"]/div[5]/div/div').click()
    driver.find_element(By.XPATH, '//*[@id="ranking-fillters"]/div[5]/div/div/input').send_keys('United States')
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="ranking-fillters"]/div[5]/div/div/div[2]/div[57]').click()

    input()

# driver.get(basic_url + 'computer-science-information-systems')
