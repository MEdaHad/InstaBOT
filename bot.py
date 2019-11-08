from selenium import webdriver
import time

class InstaBot():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def close_browser(self):
        self.driver.close()

    def login(self):    
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(3)

        login_button = driver.find_element_by_xpath("/html/body/span/section/main/article/div[2]/div[2]/p/a")
        login_button.click()
        time.sleep(2)

        usr = driver.find_element_by_name("username")
        usr.send_keys(self.username)

        passw = driver.find_element_by_xpath("/html/body/span/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")
        passw.clear()
        passw.send_keys(self.password)

        logn = driver.find_element_by_xpath("/html/body/span/section/main/div/article/div/div[1]/div/form/div[4]")
        logn.click()


    def notnw(self):
        driver = self.driver
        time.sleep(3)

        notnw_btn = driver.find_element_by_css_selector("button.aOOlW:nth-child(2)")
        notnw_btn.click()
        time.sleep(2)



    def lik_pic(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/Ethiopia/")
        time.sleep(2)
        
        pic_hrefs = []
        pic_href = []
        href = []
        for i in range(0, 7 ):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)

                pic_hrefs = driver.find_element_by_tag_name('a')

                pic_href = [elem.get_attribute('hrefs') for elem  in pic_hrefs if '.com/p' in elem.get_attribute('hrefs') ]

                for i in pic_hrefs:
                    if i in pic_href:
                        href.append(j)

            except Exception as e:
                continue
        
        for i in href:
            driver.get(href)
            time.sleep(3)

            try:
                 like_button = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button/span")
                 like_button.click()
            except Exception:
                continue



ig = InstaBot("username", "password")
ig.login()
ig.notnw()
ig.lik_pic()
