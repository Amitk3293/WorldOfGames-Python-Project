from selenium import webdriver
import os

def test_scores_archive():
    global scoreid
    driver = webdriver.Firefox()
    driver.get('http://127.0.0.1:5000')
    scoreid = driver.find_element_by_id("score").text
    if 0 < int(scoreid) < 1000:
        return True
    else:
        return False


def main_function():
    test_scores_archive()
    if scoreid == True:
        sys.exit(0)
    else:
        sys.exit(-1)


main_function()


