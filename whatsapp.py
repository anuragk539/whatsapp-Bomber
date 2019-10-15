from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('F:\Chrome Downloads\chromedriver.exe')  #download chromedriver.exe for your default chrome version and set the path
print("Scan the QR code")
driver.get("https://web.whatsapp.com/")           #opening your whatsapp

def Sendmsg():
    name = input("Enter the name  jisko pareshan karna hai : ")
    msg = input("Kya send karna hai likho yaha : ")
    count = int(input("Kitni bar vejna hai ???: "))

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))    #searching for your element
    user.click()

    msg_box = driver.find_element_by_class_name("_3u328")     #Your message box input

    for i in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name("_3M-N-")
        button.click()


print("Press 1 for sending multiple messages \nPress 2 to exit")
n = int(input())
if (n == 1):
    Sendmsg()

elif(n==2):
    quit()
