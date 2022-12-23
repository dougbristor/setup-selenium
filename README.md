
I thought I would see what the new **ChatGPT** would say about installing selenium on a mac or pc.
You can skip down to **TLDR** at the bottom

## show me the instructions using python and selenium to scrape data from airbnb using a mac written in the style of a pirate


Ahoy matey! Are ye ready to set sail on the high seas of web scraping with Python and Selenium? Let's get started!

First, you'll need to install Python on your Mac. If you don't already have it installed, you can download it from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

Next, you'll need to install Selenium. You can do this by opening up a terminal window and typing the following command:

`pip install selenium` 

Now that you have Python and Selenium installed, let's start by importing the necessary libraries:

    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service

Next, you'll need to download the ChromeDriver executable and save it somewhere on your computer. You can download ChromeDriver from this link: [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)

Once you have ChromeDriver downloaded, you'll need to specify the path to the executable in your Python script:

`service = Service('/path/to/chromedriver')` 

You can then pass the `service` object and any desired `service_args` to the `webdriver.Chrome()` function like this:

`driver = webdriver.Chrome(service=service, service_args=['--verbose'])` 

This will start ChromeDriver as a service in the background, using the specified `service_args`. In this case, the `--verbose` flag will cause ChromeDriver to print log messages to the console.

Now that you have Selenium and ChromeDriver set up, you can use the `driver.get()` method to navigate to the Airbnb website:

`driver.get('https://www.airbnb.com')` 

From here, you can use Selenium's built-in functions to interact with the website and scrape the data you need. For example, you can use the `driver.find_element_by_css_selector()` method to locate specific elements on the page and extract their data.

For example, let's say you want to scrape the titles of all the listings on the Airbnb homepage. You could use the following code:

`titles = driver.find_elements_by_css_selector('._1b5j98h5')
for title in titles:
    print(title.text)` 

This will print out the titles of all the listings on the homepage.

I hope this helps set you on your way to a successful journey of web scraping with Python and Selenium! May the winds be at your back and the treasures be plentiful. Arrr!


## TLDR

You need to install python
https://www.python.org/downloads
and download ChromeDriver from this link: https://chromedriver.chromium.org/downloads

Next, you'll need to install Selenium. You can do this by opening up a terminal window and typing the following command:

`pip install selenium` 


Then create a file called scrape **[testairbnb.py](https://raw.githubusercontent.com/dougbristor/setup-selenium/main/testairbnb.py)**

```    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    
    service = Service('chromedriver')      # /path/to/chromedriver
    driver = webdriver.Chrome(service=service, service_args=['--verbose'])
    driver.get('https://www.airbnb.com')
    
    try:
        listings = WebDriverWait(driver, 10).until( EC.visibility_of_all_elements_located(
            (By.XPATH, '//div[contains(@aria-labelledby,"title") and @role="group"]')
            ))
    
        for listing in listings:	
           link = listing.find_element(By.CSS_SELECTOR,'a').get_attribute('href')
           text = listing.find_element(By.XPATH,'.//div[contains(@id,"title")]').text 
           print(f'{text}: {link.split("?")[0]}')
    
    finally:
        driver.quit()
```


open the terminal window in the same location as the file and typing the following command:

    python testairbnb.py

This should output something like this 


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
    
Done

