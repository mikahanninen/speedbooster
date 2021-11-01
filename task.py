from RPA.Browser.Selenium import Selenium
from RPA.HTTP import HTTP
import re
from time import sleep

analyzer_site = "https://analyze.speedboostr.com/"
site_to_analyze = "https://ggbexhaust.com/"

browser = Selenium()
http = HTTP()

def wait_while_analyzing():
    browser.wait_until_element_is_visible('//p[@class="analysis-animation"]')
    while True:
        visible = browser.is_element_visible('//p[@class="analysis-animation"]')
        if not visible:
            return
        sleep(0.5)

def get_oversize_images_and_download():
    elements = browser.get_webelements('//div[@class="offenders"]//a')
    for element in elements:
        href = element.get_attribute("href")
        match = re.match(".*files\/(.*\..*)\?.*", href)
        http.download(href, match.group(1))

def minimal_task():
    browser.open_available_browser(analyzer_site, headless=True)
    browser.input_text_when_element_is_visible('//input[@type="text"]', site_to_analyze)
    browser.click_element('//button[@type="submit"]')
    wait_while_analyzing()
    browser.execute_javascript("window.scrollBy(0,400);")
    browser.click_element_when_visible('//td[text()="Oversized images"]')
    get_oversize_images_and_download()
    print("Done.")


if __name__ == "__main__":
    minimal_task()
