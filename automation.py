from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')
chrome_browser.maximize_window()
# Opening up the browser
chrome_browser.get(
    'https://www.seleniumeasy.com/test/basic-first-form-demo.html')

# Checking if element exists on page
assert 'Selenium Easy Demo' in chrome_browser.title
# Grabbing element by class name
show_message_button = chrome_browser.find_element_by_class_name("btn=default")

# print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

# Grabbing element by ID
user_message = chrome_browser.find_element_by_id('user-message')
# Grabbing element by CSS selector
user_button2 = chrome_browser.find_element_by_css_selector('#get-input > .btn')

# Ensuring the input is clear from previous user
user_message.clear()
# Simulating user typing
user_message.send_keys('I am learning this')
# Simulating button click
show_message_button.click()

output_message = chrome_browser.find_element_by_id('display')
assert 'I am learning this' in output_message.text

chrome_browser.close()
chrome_browser.quit()
