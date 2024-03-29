from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from titleList import generate_random_title, store_title
from get_book_titles import get_titles_from_file
import random

class wishlist():

    def __init__(self, driver):
        self.driver = driver

    def wishlist_with_acc(self):

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "html-body")))
        time.sleep(2)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "html-body")))
        time.sleep(2)
         
        random_title = generate_random_title()
        
        # Locate the search field and send the random title
        search_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "search-field")))
        search_field.send_keys(random_title)
        print("Insert a title")
        
        # Submit the search by pressing ENTER
        search_field.send_keys(Keys.ENTER)
        print("Entered a Title")

        # Wait for the first item to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div[2]/main/section/div/div[2]/div/ul/div[1]/a/div[2]/p")))
        time.sleep(2)
        
        #clicks a random title within the search perimeter
        p_elements = WebDriverWait(self.driver, 10).until(
            (EC.presence_of_all_elements_located((By.CLASS_NAME, "ProductCard-Name"))))
        elements_p = random.choice(p_elements)
        elements_p.click()
        print("Clicked a Random Title")
        time.sleep(2)

        add_wishlist = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div[2]/main/section[1]/div/article/div[6]/div[1]/button/div"))
        )
        add_wishlist.click()
        print("Added to Wishlist")
        time.sleep(3)

        click_wishlist = self.driver.find_element(By.XPATH, "//*[@id='root']/div/section[1]/header/nav/div[3]/a")
        click_wishlist.click()
        time.sleep(3)
        print("End of Wishlist")

    # def wishlist_no_acc(self):

    #     random_title = generate_random_title()
        
    #     # Locate the search field and send the random title
    #     search_field = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.ID, "search-field")))
    #     search_field.send_keys(random_title)
    #     print("Insert a title")
        
    #     # Submit the search by pressing ENTER
    #     search_field.send_keys(Keys.ENTER)
    #     print("Entered a Title")

    #     # Wait for the first item to load
    #     WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div[2]/main/section/div/div[2]/div/ul/div[1]/a/div[2]/p")))
    #     time.sleep(2)
        
    #     #clicks a random title within the search perimeter
    #     p_elements = WebDriverWait(self.driver, 10).until(
    #         (EC.presence_of_all_elements_located((By.CLASS_NAME, "ProductCard-Name"))))
    #     elements_p = random.choice(p_elements)
    #     elements_p.click()
    #     print("Clicked a Random Title")
    #     time.sleep(2)

    #     add_wishlist = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div[2]/main/section[1]/div/article/div[6]/div[1]/button/div")))
    #     add_wishlist.click()
    #     time.sleep(5)

if __name__ == "__main__":    
    wishlist_instance = wishlist()
    wishlist_instance.wishlist_with_acc()

