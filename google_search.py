# this program will go to google and query for a phrase, then check if the requested url is in the top 3
# core code is sampled from:
#   https://chromedriver.chromium.org/getting-started -> google search
#   https://www.w3schools.com/python/python_try_except.asp -> try catch
#   https://www.tutorialspoint.com/python/python_command_line_arguments.htm -> argument input

# i found the xpath variables using chrome inspector.  i right clicked on the element and did a copy xpath.  then i searched for that xpath in the inspector to make sure i got the 1 correct value.
# after that, i fine tuned the xpath to make sure it was stable  enough to find the element, but flexible enough to withstand website html changes

import time
from selenium import webdriver
import sys
from selenium.webdriver.common.by import By

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

# this function queries google and returns the top 3 results
def queryGoogle(driver, searchValue, urlToSearchFor):
    try:
        # open google.com
        # wait for input box to be visible.  you'll need to do a webdriver wait.
        driver.get('http://www.google.com/')
        time.sleep(1)  # use webdriver wait instead

        # google input.  had to use name as id was not available.
        #search_box = driver.findElement(By.xpath('input[@name="q"]'))
        #search_box.setAttribute("value", searchValue)
        #orvile: lower priorty -> use above 2 lines instead of below 2 lines
        # while i could query via name only, i chose to use xpath just in case the website changed
        # this is how i would've done that -> search_box = driver.find_element_by_name('q')
        # while i could've set the seach phrase via send keys, set value is more stable.
        # this is how i would've done that -> search_box.send_keys(searchValue)

        search_box = driver.find_element_by_name('q')
        search_box.send_keys(searchValue)

        search_box.submit()
        time.sleep(1)
        #orvile: query for top 3 entries adn return in object

        #links = driver.find_element(By.xpath('//*/a/div/cite'))
        links = driver.find_elements_by_xpath('//*/a/div/cite')

        isFound = False
        for searchLink in links:
            print(searchLink.text)
            if searchLink.text == urlToSearchFor:
                isFound = True
        return isFound

        #orville: return if foudn.
    except:
        print ('something went wrong in the search')
        print (sys.exc_info())
        return False
    finally:
    # find search results
        driver.quit()
    #Orville: return top 3 or emtpy object


searchValue = sys.argv[1]
urlToSearchFor = sys.argv[2]

driver = webdriver.Chrome('/Users/oantazo/Desktop/code/drivers/chromedriver77')  # Optional argument, if not specified will search path.

#orville: test failuers by changing driver location
isFound = queryGoogle(driver, searchValue, urlToSearchFor)

print ('Found: ', isFound)

#Need Assert
