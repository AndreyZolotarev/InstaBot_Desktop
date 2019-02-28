from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import datetime

username = input('Type your username: ')
password= input('Type your password: ')
# username = 'my username'
# password= 'my password'

hashtag = 'dogsofinstagram'
like_limit = random.randint(48,55)


chrome_path ='chromedriver.exe'

driver = webdriver.Chrome(chrome_path)

def IB_login():
    driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    time.sleep(random.randint(2,4))

    username_elem = driver.find_element_by_xpath("//input[@name='username']")
    username_elem.clear()
    username_elem.send_keys(username)
    time.sleep(random.randint(2,4))

    password_elem = driver.find_element_by_xpath("//input[@name='password']")
    password_elem.clear()
    password_elem.send_keys(password)
    password_elem.send_keys(Keys.ENTER)
    time.sleep(random.randint(2,4))

def closebrowser():
    driver.close()

def liking_photos():
    print('IB is working...')
    driver.get('https://www.instagram.com/explore/tags/'+ hashtag + '/')
    time.sleep(random.randint(2,4))

    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(random.randint(5,7))

    hrefs = driver.find_elements_by_tag_name('a')
    time.sleep(random.randint(4,5))
    hrefs[10].click()
    time.sleep(random.randint(4,5))
    hrefs.clear()

    for i in range(like_limit):
        try:
            like_button = driver.find_element_by_class_name('coreSpriteHeartOpen')
            like_button.click()
            time.sleep(random.randint(4,5))

            next_photo = driver.find_element_by_class_name('coreSpriteRightPaginationArrow')
            next_photo.click()
            time.sleep(random.randint(4,5))
            print('IB liked %d/%d' % ((i+1),like_limit))
        except:
            print('An error occured. IB skipped this photo')
            next_photo = driver.find_element_by_class_name('coreSpriteRightPaginationArrow')
            next_photo.click()
            time.sleep(random.randint(4,5))
            try:
                like_button = driver.find_element_by_class_name('coreSpriteHeartOpen')
                like_button.click()
                time.sleep(random.randint(4,5))
            except:
                print('Double exception, skipped two pics')
                next_photo = driver.find_element_by_class_name('coreSpriteRightPaginationArrow')
                next_photo.click()
                time.sleep(random.randint(4,5))

    print('Finished successfully. IB liked %d photos' % like_limit)

def timer(time_limit):
    while time_limit > 0:
        print('Wait for %d minutes...' % time_limit)
        time_limit -= 1
        time.sleep(60)
    print('Finished')


if __name__ == '__main__':
    IB_login()
    for x in range(12):
        liking_photos()
        print('Finished round %d/12' % (x+1))
        if (x+1) < 12:
            #timer(random.randint(55,63))
            timer(random.randint(20,30))
        else:
            print('Done')
