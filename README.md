# Instagram Scraper
Use this instagram scraper

# setup in linux
#### 1.clone the repo
#### 2.Create a new virtual environment using the venv module.
#### `python3 -m venv env`
#### 3.Activate the virtual environment.
#### `source env/bin/activate`
#### 4.install all the required modules
#### `pip install -r requirements.txt`
#### 5.To exit the virtual environment and return to your system's global Python environment, use the following command
#### `deactivate`

# Files To Download
#### 1.The project repo contains the chromedriver for linux if you are using another os install the chromedrive according to your os and replace the existing one with your driver

# Files Usage
#### 1.`script.py` is used to scrape the instagram in the files you have to provide your login credentials as the scraper uses your credentials to login in to your account and then scrape the data it stores all the scraped files in the files folder
#### 2. `cleanser.py` this files writes the account names with the likes and comments greater than the values specified in list.txt
#### 3. `list.txt` write the values like `200,100` where 200 is number of likes and 100 is number of comments.The cleanser.py uses this files as reference and writes the names of the accounts who reels have minimum number of likes and comments as specified in the list.txt
#### 4. `names.txt` this file contains the fields the scraper inputs in the instagram search field so if you want any specific words or names you can input it here or else just write random `a,b,c,d,e,f` etc.. letters.
#### 5. `output.txt` this file contains the account names written by cleanser.py
#### 6. `requirements.txt` this file contains all the modules used in the program install all the modules before running any script

## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://rajeshportfolio.me/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rajesh-kanugu-aba8a3254/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/exploringengin1)

## Tech Stack

- Python
- Selenium
  
## Authors

- [@kanugurajesh](https://github.com/kanugurajesh)

## Support

For support, you can buy me a coffee

<a href="https://www.buymeacoffee.com/kanugurajen" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/kanugurajesh/Image-Classification/blob/main/LICENSE.txt)
