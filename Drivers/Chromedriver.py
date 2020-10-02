from selenium import webdriver

chromedriver = 'C:/Selenium/chromedriver.exe'       # add path to your local chrome driver
edgedriver = 'C:/Selenium/msedgedriver.exe'         # add path to your local chrome driver
driver = webdriver.Edge(edgedriver)
driver.maximize_window()
