from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver 
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


# form_url = "https://docs.google.com/forms/d/e/1FAIpQLScpsKQh4pjWJ4RBscCD6BHKgl4WclOCCxdFutTfmOdrAJMkxg/viewform"
form_url = "https://forms.gle/KEGSytxYFBKXgxEc9"
browser.get(form_url)

time.sleep(30)

while (True):
    try:
        # form_url = "https://docs.google.com/forms/d/e/1FAIpQLScpsKQh4pjWJ4RBscCD6BHKgl4WclOCCxdFutTfmOdrAJMkxg/viewform"
        browser.get(form_url)

        input_elements = list(browser.find_elements(By.TAG_NAME, "input"))
        answers = ["Edge of Tomorrow", "Food"]
        i = 0
        for input_element in input_elements:
            if (input_element.get_attribute("type") == 'text'):
                input_element.send_keys(answers[i])
                i+=1

        divs = list(browser.find_elements(By.TAG_NAME, "div"))
        # print(len(divs))
        submit_button = None
        for div in divs:
            # print(div.get_attribute("class"))
            if (div.get_attribute("class") == "uArJ5e UQuaGc Y5sE8d VkkpIf QvWxOd"):
                submit_button = div
                break 

        submit_button.click()

        time.sleep(2)
    except:
        continue

time.sleep(5)

# Close the browser
browser.quit()
