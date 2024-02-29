from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from time import sleep
import getContactUrl
from bs4 import BeautifulSoup
import re
import clearEmail
import getNames
import requests

def extract_company_contact_info(url):

    def remove_duplicates(string_array):
        unique_strings = set(string_array)
        return list(unique_strings)
    
    def extract_contact_info(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', soup.get_text())

        email_links = soup.find_all(href=re.compile(r'mailto:'))
        href_email = [re.sub(r'mailto:', '', link.get('href')) for link in email_links]

        email_addresses.extend(href_email)
        
        email_addresses = remove_duplicates(email_addresses)
        return email_addresses

    def remove_email_duplicates(array):
        unique_strings = set()

        # Iterate over the array
        for email in array:
            # Convert the email to lowercase
            lowercase_email = email.lower()

            # Check if the lowercase email is already in the set
            if lowercase_email not in unique_strings:
                # Add the lowercase email to the set
                unique_strings.add(lowercase_email)

        # Convert the set back to a list
        unique_array = list(unique_strings)

        return unique_array

    emailAddresses = []
    names = []

    available_urls = getContactUrl.available_urls(url, "contact")
    for u in available_urls:
        try:
            email_addresses = extract_contact_info(u)
            emailAddresses.extend(email_addresses)
        except:
            pass
    emailAddresses = remove_duplicates(emailAddresses)
  

    available_urls = getContactUrl.available_urls(url, "name")
    for u in available_urls:
        try:
            names = getNames.get_employee_names(u)
            names.extend(names)
        except:
            pass
    
    emailAddresses = clearEmail.clear_emails(emailAddresses)
    emailAddresses = remove_email_duplicates(emailAddresses)
    names = remove_duplicates(names)

    if len(emailAddresses) == 0:
        print("No email address")
    if len(emailAddresses) != 0:
        print("Email Addresses:", emailAddresses)
        # data_save(f"Email Addresses: {emailAddresses}")
    if len(names) != 0:
        print(f"names = ", names)

    return emailAddresses, names

# url = "https://www.zynex.com/"
# print(extract_company_contact_info(url))


# def check_phone_number(phone_number):
#         try:
#             parsed_number = phonenumbers.parse(phone_number)
#             return phonenumbers.is_valid_number(parsed_number)
#         except phonenumbers.phonenumberutil.NumberParseException:
#             return False
# print(check_phone_number("+49345674890"))

