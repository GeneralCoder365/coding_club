import schedule
import time
import webbrowser
from time import sleep
from selenium import webdriver

def open_link(link):
    # webbrowser.open(link)
    # PATH TO CHROMEDRIVER
    browser = webdriver.Chrome(r"D:\Personal_Folders\Tocho\Programming\Coding_Club\coding_club\demos\zoom\chromedriver.exe")
    # OPENS TEMPORARY EMAIL SITE
    browser.execute_script("window.open('https://www.geeksforgeeks.org/', 'gforgtab');")

    # Switches to original blank tab and closes it
    browser.switch_to_window(browser.window_handles[0])
    browser.close()

    sleep(1)

    # Switches back to gforgtab
    browser.switch_to_window(browser.window_handles[0])

    sleep(3)

    # Finds the Sign In Button
    sign_in_path = "//a[contains(text(), 'Sign In')]"
    sign_in_button = browser.find_elements_by_xpath(sign_in_path)
    # Clicks the Sign In Button
    sign_in_button[0].click()

    sleep(3)

    # Choose Sign In with Google
    sign__in_with_google_path = "//a[id = 'glogin']"
    sign_in_google = browser.find_elements_by_xpath(sign__in_with_google_path)
    sign_in_google[0].click()

    # Switches back to the Temporary Email tab
    browser.switch_to_window(browser.window_handles[0])



    # OPENS INSTAGRAM 
    # browser.get('https://www.instagram.com/accounts/emailsignup/')
    # browser.execute_script("window.open('https://www.instagram.com/', 'instatab');")
    # browser.switch_to_window(browser.window_handles[1])
    # browser.get("https://www.google.com/")
    # sleep(5)
    browser.close()

open_link("")

def demo_meeting():
    open_link('MY ZOOM MEETING URL')

# schedule.every().friday.at("12:25").do(demo_meeting)

# while 1:
    # schedule.run_pending()
    # time.sleep(1)