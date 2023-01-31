desired_cap = {
 'os_version': '10',
 'resolution': '1920x1080',
 'browser': 'Chrome',
 'browser_version': 'latest',
 'os': 'Windows',
 'name': 'BStack-[Python] Sample Test', # test name
 'build': 'BStack Build Number 1' # CI/CD job or build name
}
import selenium
from selenium import webdriver   # for webdriver
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



class Lyrics_Scraping:
    def __init__(self,song,artist):

        self.lyric=[]
        self.url = 'https://www.google.com'
        self.option = Options()
        self.option.add_argument('--headless')
        self.driver = webdriver.Remote(command_executor='https://name:key@hub-cloud.browserstack.com/wd/hub',
                                       desired_capabilities=desired_cap)

        self.driver.get(self.url)
        self.search = self.driver.find_element(By.CLASS_NAME, 'gLFyf')
        self.search.click()
        self.search.send_keys(f'{artist} {song} lyrics')
        self.search.send_keys(Keys.ENTER)

        self.lyrics = self.driver.find_elements(By.CSS_SELECTOR, "span[jsname='YS01Ge']")

        for l in self.lyrics:
            self.lyric.append(l.text)
        self.driver.quit()

    def get_lyrics(self):

      return self.lyric




