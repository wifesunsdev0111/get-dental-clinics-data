import requests
from bs4 import BeautifulSoup
import re
import spacy

def remove_duplicates(string_array):
    unique_strings = set(string_array)
    return list(unique_strings)

nlp = spacy.load("en_core_web_sm")

def extract_names(texts):
    names = []
    for text in texts:
        if "dr." in text.lower() and len(re.findall(r" ", text)) < 8:
            names.append(text)
        else:
            doc = nlp(text)
            for token in doc:
                if token.ent_type_ == "PERSON":
                    names.append(token.text)
    return names


def get_employee_names(url):
    # url = 'https://medicalwesthospital.org/doctor.php?cn=738'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    employee_names = []

    # Find potential name elements based on HTML tags and attributes
    potential_name_elements = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'p', 'span', 'strong'])


    # Define a regular expression pattern to match employee names
    name_pattern_2 = re.compile(r'^[A-Z][a-z]+ [A-Z][a-z]+$')
    name_pattern_1 = re.compile(r"Dr\. (\w+\s+\w+)")
    name_pattern_3 = re.compile(r'^[A-Z][a-z]+$')

    # Iterate over the potential name elements and extract the names
    for element in potential_name_elements:
        text = element.get_text().strip()

        # Check if the text matches the name pattern
        if name_pattern_1.match(text) or name_pattern_2.match(text) or name_pattern_3.match(text):
            employee_names.append(text)
    
    unique_names = remove_duplicates(employee_names)

    return extract_names(unique_names)


# get_employee_names()