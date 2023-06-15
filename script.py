# importing selenium webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# username and password
username = ""
password = ""

count = 0
# maximum numbers of users you want to scrape
max_count = 3

# create a webdriver object and set the chromedriver.exe path
driver = webdriver.Chrome()

# get the Instagram login page
driver.get("https://www.instagram.com/")

# creating a set to store the users
data = set()

# implicit wait for 10 seconds
driver.implicitly_wait(10)

# search fields
with open("names.txt","r") as f:
    letters = f.read().split(",")

# username field input
insta_username = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
insta_username.send_keys(username)

# password field output
insta_password = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
insta_password.send_keys(password)

# login button click
login_button = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button")
login_button.click()

# clicking on search field
search_field = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[1]/div/div[2]/div[2]/span/div/a/div")
search_field.click()

# scraping the user names
def searcher(element):
    search_input = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input")
    search_input.send_keys(element)
    time.sleep(5)
    search_results = driver.find_elements(By.XPATH, "//div[@role='none']")

    for result in search_results:
        if result.text[0] != "#":
            data.add(result.text.split("\n")[0])
    search_input.clear()

# running the searcher function on all the letters
for letter in letters:
    searcher(letter)

# scraping the page source and saving it in a file in files folder
for i in data:
    driver.get(f"https://www.instagram.com/{i}/reels")
    time.sleep(5)
    page_source = driver.page_source
    if "_abpm" in driver.page_source:
        with open(f"files/{i}.txt","w") as f:
            f.write(page_source)
        count += 1
    if count == max_count:
        break

# closing the driver
driver.quit()
