from selenium import webdriver

chrome_browser = webdriver.Chrome("./chromedriver")
chrome_browser.maximize_window()
chrome_browser.get("https://www.")

assert " " in chrome_browser.title

a = chrome_browser.find_element_by_class_name("")
a.get_attribute(" ")

assert "" in chrome_browser.page_source

b = chrome_browser.find_element_by_id("")
b = chrome_browser.find_element_by_css_selector("")
b.clear()
b.send_keys("")

a.click()

output_message = chrome_browser.find_element_by_id("")
assert "" in output_message.text

chrome_browser.close()
chrome_browser.close()

chrome_browser.quit()
