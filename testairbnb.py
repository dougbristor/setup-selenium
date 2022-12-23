from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

service = Service('chromedriver')      # /path/to/chromedriver
driver = webdriver.Chrome(service=service, service_args=['--verbose'])
driver.get('https://www.airbnb.com')

try:
    listings = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//div[contains(@aria-labelledby,"title") and @role="group"]')))

    for listing in listings:	
       link = listing.find_element(By.CSS_SELECTOR,'a').get_attribute('href')
       text = listing.find_element(By.XPATH,'.//div[contains(@id,"title")]').text 
       print(f'{text}: {link.split("?")[0]}')

finally:
    driver.quit()



"""
    De Panne, Belgium: https://www.airbnb.co.uk/rooms/47571956  
    Ratlinghope, UK: https://www.airbnb.co.uk/rooms/705067947839156864  
    Isle of Anglesey, UK: https://www.airbnb.co.uk/rooms/697038892914967872  
    Devon, UK: https://www.airbnb.co.uk/rooms/562204609423382348  
    Barber Booth, UK: https://www.airbnb.co.uk/rooms/654293014037001876  
    Gloucestershire, UK: https://www.airbnb.co.uk/rooms/593489329540194663  
    Settle, UK: https://www.airbnb.co.uk/rooms/5765014  
    Paris, France: https://www.airbnb.co.uk/rooms/35457466  
    Portishead, UK: https://www.airbnb.co.uk/rooms/17403841  
    Le Landin, France: https://www.airbnb.co.uk/rooms/15769894  
    Near Thorpeness, Suffolk, UK: https://www.airbnb.co.uk/rooms/43242377  
    Devon, UK: https://www.airbnb.co.uk/rooms/29893113  
    Devon, UK: https://www.airbnb.co.uk/rooms/24800857  
    Courgent, France: https://www.airbnb.co.uk/rooms/628761552757093228  
    Millbrook, UK: https://www.airbnb.co.uk/rooms/658577869997381425  
    Lancashire, UK: https://www.airbnb.co.uk/rooms/19099736  
    GB, UK: https://www.airbnb.co.uk/rooms/52023748  
    Millbrook, UK: https://www.airbnb.co.uk/rooms/574518750738307839  
    Selattyn, UK: https://www.airbnb.co.uk/rooms/45235966  
    Gwynedd, UK: https://www.airbnb.co.uk/rooms/634065622057904493

"""
