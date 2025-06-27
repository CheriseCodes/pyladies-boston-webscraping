from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    # Use Chrome to visit webpages
    driver = webdriver.Chrome()

    # Visit OpenAI webpage
    driver.get("https://en.wikipedia.org/wiki/OpenAI")

    # Find link (anchor) element that goes to Sam Altman's Wiki page using XPATH
    sam_altman_link_element = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[5]/td/div/ul/li[1]/a')

    # Visit Sam Altman's wiki page
    sam_altman_link_element.click()

    # Check what the current page is
    current_url = driver.current_url
    print(f"We are currently on: {current_url}")

    # Print content of current page (can be passed to Beautiful Soup HTML parser)
    print(f"{driver.page_source[0:1000]}...")

    # Close driver
    driver.close()

if __name__ == "__main__":
    main()