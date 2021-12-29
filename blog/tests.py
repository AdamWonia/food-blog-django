import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url='http://127.0.0.1:8000')


# Test some web functionalities:
def web_test():
    # Log in and test after it:
    driver.get(url='http://127.0.0.1:8000/admin')
    driver.find_element_by_xpath('//*[@id="id_username"]').send_keys('login')
    driver.find_element_by_xpath('//*[@id="id_password"]').send_keys('password')
    driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
    time.sleep(1)

    # Go to main page:
    driver.find_element_by_xpath('//*[@id="user-tools"]/a[1]').click()
    time.sleep(1)

    # Click on post title:
    driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/p[1]/a').click()

    # Edit post author:
    driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/h2/a[1]').click()
    driver.find_element_by_xpath('//*[@id="id_name"]').send_keys('The best cook')
    driver.find_element_by_xpath('/html/body/div[4]/form/button').send_keys(webdriver.common.keys.Keys.SPACE)

    # Return to main page:
    driver.find_element_by_xpath('/html/body/div[1]/a/h1').click()
    time.sleep(1)

    # Add new post:
    driver.find_element_by_xpath('/html/body/div[2]/a/button').click()
    driver.find_element_by_xpath('//*[@id="id_name"]').send_keys('test name')
    driver.find_element_by_xpath('//*[@id="id_title"]').send_keys('test title')
    driver.find_element_by_xpath('//*[@id="id_text"]').send_keys('test text')
    driver.find_element_by_xpath('/html/body/div[4]/form/button').send_keys(webdriver.common.keys.Keys.SPACE)

    # Delete the post:
    driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/h2/a[2]').click()
    time.sleep(2)
    driver.find_elements_by_xpath('/html/body/div[4]/div/form/p/button')[0].click()


# Response test:
def response_test(width, file):
    height = 768
    driver.set_window_size(width, height)
    driver.save_screenshot(file)


if __name__ == "__main__":
    web_test()
    response_test(900, "../900_test.png")
    response_test(1200, "../1200_test.png")
    response_test(1800, "../1800_test.png")
    response_test(600, "../600_test.png")
