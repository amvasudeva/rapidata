#! /usr/bin/python

import time
import ConfigParser 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.common.exceptions import NoSuchElementException

config = ConfigParser.ConfigParser()
config.read('/root/pet_input')

ff = webdriver.Firefox()
ff.get(config.get('DEFAULT','url'))
try:

    time.sleep(5)
    ee = ff.find_element_by_xpath("//html/body/div/ul/li[1]/a")
    ee.click()

    ee = ff.find_element_by_xpath("//html/body/div/a")
    ee.click()

    fname = ff.find_element_by_id("firstName")
    fname.send_keys(config.get('DEFAULT','first_name'))

    lname = ff.find_element_by_id("lastName")
    lname.send_keys(config.get('DEFAULT','last_name'))

    address = ff.find_element_by_id("address")
    address.send_keys(config.get('DEFAULT','address'))

    city = ff.find_element_by_id("city")
    city.send_keys(config.get('DEFAULT','city'))

    telephone = ff.find_element_by_id("telephone")
    telephone.send_keys(config.get('DEFAULT','telephone'))

    time.sleep(5)

    ee = ff.find_element_by_xpath("//html/body/div/form/table/tbody/tr[6]/td/p/input")
    ee.click()


    time.sleep(5)


    ee = ff.find_element_by_xpath("//html/body/div/table[3]/tbody/tr/td[1]/a")
    ee.click()

    time.sleep(5)
    ee = ff.find_element_by_xpath("//html/body/div/ul/li[1]/a")
    ee.click()

    lname = ff.find_element_by_id("lastName")
    lname.send_keys(config.get('DEFAULT','last_name'))

    time.sleep(5)
    ee = ff.find_element_by_xpath("//html/body/div/form/table/tbody/tr[2]/td/p/input")
    ee.click()

    element = WebDriverWait(ff, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))

except NoSuchElementException as e:
        print "=========================================================================================" 
        print "=========================================================================================" 
        print e
        print "=========================================================================================" 
        print "=========================================================================================" 
#        raise

ff.close()
