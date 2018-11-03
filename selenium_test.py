from selenium import webdriver

def test_home():
    driver = webdriver.Chrome()
    driver.get('http://162.246.157.109:8000/')

    #test name
    elem = driver.find_element_by_id("name")
    assert elem is not None

    #test about
    elem = driver.find_element_by_id("about")
    assert elem is not None

    #test education
    elem = driver.find_element_by_id("education")
    assert elem is not None

    #test skills
    elem = driver.find_element_by_id("skills")
    assert elem is not None

    #test education
    elem = driver.find_element_by_id("work")
    assert elem is not None

    #test contact information
    elem = driver.find_element_by_id("contact")
    assert elem is not None

