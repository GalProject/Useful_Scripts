from selenium import webdriver
import urllib
import time
#Link: http://olvreader.sefereshet.org.il/Olive/OTB/OpenU/?href=C20242/2008/01/02&usticket=eW9zaXNoMw==&ticket=db2e5dc329bcbe119c052a86d8f97e8c2ca62ca6_yosish3


driver = webdriver.Chrome("C:\\Users\\GalBenEvgi\\Desktop\\chromedriver.exe")



for x in range(1,229):
    temp = x.__str__()
    driver.maximize_window()
    driver.get("http://olvreader.sefereshet.org.il/Olive/OTB/OpenU/GetImage.ashx?kind=page&href=C20242%2F2008%2F01%2F02&page=" + temp)
    ele = driver.find_element_by_xpath("/html/body/img")
    src = ele.get_attribute('src')
    if (x % 2 != 0):
        time.sleep(1)
        urllib.urlretrieve(src, x.__str__() + ".jpg")
        time.sleep(1)
    else:
        continue
    #driver.save_screenshot(x + ".jpg")


