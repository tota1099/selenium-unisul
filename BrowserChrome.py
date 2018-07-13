from selenium import webdriver

def get():
    chrome_options = webdriver.ChromeOptions()
    prefs = {'profile.managed_default_content_settings.images': 2, 'disk-cache-size': 4096}
    chrome_options.add_experimental_option("prefs", prefs)
    return webdriver.Chrome(chrome_options=chrome_options)
