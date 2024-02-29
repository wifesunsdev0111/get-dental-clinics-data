from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from time import sleep


def get_linkedIn_link(search_index):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com/")

    url = ""

    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"QS5gu sy4vM\"]"))).click()
    except:
        pass
    
    try:
        search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[class=\"gLFyf\"]")))
        search_input.send_keys(search_index)
        search_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class=\"FPdoLc lJ9FBc\"]")))
        WebDriverWait(search_button, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[class=\"gNO89b\"]"))).click()

        search_result_lists = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[class=\"MjjYud\"]")))

        print(f'componet list = ', len(search_result_lists))

        
        for search_result in search_result_lists:
            url_dom_parent = WebDriverWait(search_result, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class=\"yuRUbf\"]")))
            title = search_result.find_element(By.CSS_SELECTOR, "span[class=\"VuuXrf\"]").text
            print(title)

            if "LinkedIn" in title:
                url_dom = url_dom_parent.find_element(By.TAG_NAME, "a")
                url = url_dom.get_attribute("href")
                break
            else:
                continue
        print(url)
    except:
        url = ""
        pass

    driver.quit()
    return url

# result = get_linkedIn_link("Mount Vernon Dental Smiles 8101 Hinson Farm Rd #216, Alexandria, VA 22306, Yhdysvallat, LinkedIn")

# print(f'link = ', result)
    
            