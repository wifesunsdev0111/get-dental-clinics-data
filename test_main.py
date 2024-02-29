from selenium import webdriver
# from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from time import sleep
import time
import getAllCities
import getEmail
import re
import quickstart
import quickstart_select_cities
import getLInkedIn

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://huggingface.co/chat/ ")


# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"w-full justify-center rounded-full border-2 border-gray-300 bg-black px-5 py-2 text-lg font-semibold text-gray-100 transition-colors hover:bg-gray-900 bg-white text-gray-800 hover:bg-slate-100\"]"))).click()

# def get_search_result(query):
#     search_textarea_dom = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[placeholder=\"Ask anything\"]")))
#     sleep(5)
#     search_textarea_dom.send_keys(query)
#     sleep(2)
#     search_button_dom = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"btn mx-1 my-1 h-[2.4rem] self-end rounded-lg bg-transparent p-1 px-[0.7rem] text-gray-400 disabled:opacity-60 enabled:hover:text-gray-700 dark:disabled:opacity-40 enabled:dark:hover:text-gray-100\"]")))
#     search_button_dom.click()

#     result_doms = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[class=\"group relative -mb-6 flex items-start justify-start gap-4 pb-4 leading-relaxed\"]")))
#     result_dom_position = len(result_doms) - 1
#     result_dom = result_doms[result_dom_position]
#     sleep(20)
#     result_lists = result_dom.find_elements(By.TAG_NAME, "li")
    
#     results = []
#     for result in result_lists:
#         result_text = result.text
#         results.append(result_text)
    
#     print(len(result_lists), results)
#     return results

# states = get_search_result("List all the state of USA")

# print(f'All States = ', states)

# all_cities = []
# for state in states:
#     search_string = "What are the all the cities in " + state + " State"
#     all_cities = all_cities + get_search_result(search_string)

# print(f"All cities = ", all_cities)

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/maps/")

try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[jsname=\"b3VHJd\"]"))).click()
except:
    pass



# PROXY_USERNAME = "root"
# PROXY_PASSWORD = "future123"

# seleniumwire_options = {
#     'proxy': {
#         'http': f'http://{PROXY_USERNAME}:{PROXY_PASSWORD}@35.94.102.9:3128',
#         'verify_ssl': False,
#     },
# }

# driver = webdriver.Chrome(
#     seleniumwire_options=seleniumwire_options
# )

# driver.maximize_window()
# driver.get("https://www.google.com/maps/")

sleep(5)

all_clinics_data = []

def count_down(seconds):
    start_time = time.time()
    end_time = start_time + seconds

    while time.time() < end_time:
        remaining_seconds = int(end_time - time.time())
        print("Time remaining: {} seconds".format(remaining_seconds))
        time.sleep(1)

    print("Time's up!")
    return "Time end"

quickstart_select_cities.main()

all_cities = quickstart_select_cities.get_select_cities()

print(all_cities)

print(f'All cities length = ', len(all_cities))

for index, city in enumerate(all_cities):
    
    state = getAllCities.get_state_from_city(city)
    search_input = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[class=\"searchboxinput xiQnY\"]")))

    search_string = "Dental Clinics in " + city + ", " + state + ", U.S"
    print(f'Search String = ', search_string)
    search_input.clear()
    search_input.send_keys(search_string)
    sleep(2)
    search_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[class=\"google-symbols\"]")))
    search_button.click()
    sleep(5)

    time_limit = 60
    # Get the initial page height
    try:
        start_time = time.time()
        scroll_div = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"m6QErb DxyBCb kA9KIf dS8AEf ecceSd\"]")))
        page_height = driver.execute_script("return arguments[0].scrollHeight;", scroll_div)

        start_time = time.time()
        end_time = start_time + 60

        while True:
            # Scroll to the bottom of the page
            driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", scroll_div)
            clinic_lists = driver.find_elements(By.CSS_SELECTOR, "div[class=\"Nv2PK tH5CWc THOPZb \"]")
            sleep(5)

            try:
                end_contet = driver.find_element(By.CSS_SELECTOR, "span[class=\"HlvSq\"]")
                if end_contet:
                    print(f"Scroll End", end_contet.text)
                    break
            except:
                continue
    except:
        clinic_lists = driver.find_elements(By.CSS_SELECTOR, "div[class=\"Nv2PK tH5CWc THOPZb \"]")
        pass

    # try:
    #     clinic_lists = driver.find_elements(By.CSS_SELECTOR, "div[class=\"Nv2PK tH5CWc THOPZb \"]")
    # except:
    #     pass
        
   
    sleep(2)

    for index, clinic in enumerate(clinic_lists):

        try:
            driver.execute_script("arguments[0].scrollIntoView(false); window.scrollBy(0, 0);", clinic)
        except:
            pass
        print(f'Total Clinic Count = ', len(clinic_lists), index)
                    
        try:
            location_click = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(clinic)).click()
        except:
            pass

        sleep(2)
        email = ""
        names = []
        clinic_name = ""
        website= ""
        linkedin = ""
        phone_number = ""
        location_name = ""
        plus_codes = ""


        try:
            clinic_name = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1[class=\"DUwDvf lfPIob\"]"))).text
        except:
            pass

        print(f'clinic_name = ', clinic_name)

        

        
        try:
            website_button = driver.find_element(By.CSS_SELECTOR, 'img.Liguzb[src="//www.gstatic.com/images/icons/material/system_gm/1x/public_gm_blue_24dp.png"]').find_element(By.XPATH, 'ancestor::div[4]')
            website = website_button.find_element(By.CSS_SELECTOR, "div[class=\"Io6YTe fontBodyMedium kR99db \"]").text
        except:
            pass

        print(f'website = ',website)
        
        try:
            phone_button = driver.find_element(By.CSS_SELECTOR, 'img.Liguzb[src="//www.gstatic.com/images/icons/material/system_gm/1x/phone_gm_blue_24dp.png"]').find_element(By.XPATH, 'ancestor::div[4]')
            phone_number = phone_button.find_element(By.CSS_SELECTOR, "div[class=\"Io6YTe fontBodyMedium kR99db \"]").text
        except:
            pass

        print(f'phone_number = ', str(phone_number))
        
        try:
            location_button = driver.find_element(By.CSS_SELECTOR, 'img.Liguzb[src="//www.gstatic.com/images/icons/material/system_gm/1x/place_gm_blue_24dp.png"]').find_element(By.XPATH, 'ancestor::div[3]')
            location_name = location_button.find_element(By.CSS_SELECTOR, "div[class=\"Io6YTe fontBodyMedium kR99db \"]").text
        except:
            pass
        
        print(f'location_name', location_name)


        try:
            plus_codes_button = driver.find_element(By.CSS_SELECTOR, 'img.Liguzb[src="//maps.gstatic.com/mapfiles/maps_lite/images/2x/ic_plus_code.png"]').find_element(By.XPATH, 'ancestor::div[4]')
            plus_codes = plus_codes_button.find_element(By.CSS_SELECTOR, "div[class=\"Io6YTe fontBodyMedium kR99db \"]").text
        except:
            pass
        
        print(f'plus_code = ', plus_codes)
        url = "https://" + website
        
        try:
            email, names = getEmail.extract_company_contact_info(url)
        except:
            pass
        
        print(f'email = ', email)
        print(f'all name = ', names)
        try:
            search_index = clinic_name + " " + location_name + ", " + "LinkedIn"
            linkedin = getLInkedIn.get_linkedIn_link(search_index)
        except:
            pass

        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"VfPpkd-icon-LgbsSe yHy1rc eT1oJ mN1ivc\"]"))).click()
        except:
            pass

        quickstart.main()
        columnCount = quickstart.getColumnCount()
        
        
        print(f'columnCount = ',columnCount)

       
        cleaned_number = re.sub(r'[+\s]', '', phone_number)
        email_string = " ".join(email)
        results = []
        results.append(str(columnCount + 1))
        results.append(clinic_name)
        results.append(website)
        results.append(cleaned_number)
        results.append(city)
        results.append(state)
        results.append(email_string)
        results.append(location_name)
        results.append(plus_codes)
        results.append(linkedin)

        for index, name in enumerate(names):
            if index > 23:
                break
            else:
                results.append(name)
        print(results)

        if len(results) < 34:
            # Calculate the number of empty strings needed
            num_empty_strings = 34 - len(results)

            # Append empty strings to the results array
            results += [""] * num_empty_strings
           
        RANGE_DATA = f'dental_clinics_data!A{columnCount + 2}:AH'
        quickstart.insert_data(RANGE_DATA, results)
        
        sleep(2)

