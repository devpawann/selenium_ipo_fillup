import os
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


from userData import userData
import os

os.environ['WDM_SSL_VERIFY'] = '0'
# binary_location = {
#     OSType.LINUX: "/usr/bin/brave-browser",
#     OSType.MAC: "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
#     OSType.WIN: f"{os.getenv('LOCALAPPDATA')}\\BraveSoftware\\Brave-Browser\\Application\\brave.exe",
# }[os_name()]
binary_location="/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
print("brave location is", binary_location)

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
options.binary_location = binary_location

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install())

driver.get('https://meroshare.cdsc.com.np/')
driver.implicitly_wait(10)

for user in userData:
    ########### LOGIN ################
    username = driver.find_element('xpath', '//*[@id="username"]')
    myBoid = user['userName']
    username.send_keys(myBoid.zfill(1))

    dp = driver.find_element('xpath',
                             '/html/body/app-login/div/div/div/div/div/div/div[1]/div/form/div/div[1]/div/div/select2/span/span[1]/span/span[1]')
    dp.click()

    ##### Enter DP Name here #########
    dpSearch = driver.find_element('class name', "select2-search__field")
    dpSearch.send_keys(user['dpName'] + '\n')
    driver.implicitly_wait(2)

    ##### Enter Password here #########
    password = driver.find_element('xpath', '//*[@id="password"]')
    password.send_keys(user['password'])
    driver.implicitly_wait(10)
    loginBtn = driver.find_element('xpath',
                                   '/html/body/app-login/div/div/div/div/div/div/div[1]/div/form/div/div[4]/div/button')
    loginBtn.click()
    driver.implicitly_wait(10)

    ########### FILLUP ASBA ################

    myAsba = driver.find_element('xpath', '//*[@id="sideBar"]/nav/ul/li[8]/a')
    myAsba.click()

    # TODO: Here can be different list so need to identify proper share/Mutual Fund

    applyIssue = driver.find_element('xpath',
                                     "/html/body/app-dashboard/div/main/div/app-asba/div/div[2]/app-applicable-issue/div/div/div/div/div[2]/div/div[2]/div/div[4]/button")

    applyIssue.click()

    # TODO: Confirm here too
    bankSelect = driver.find_element('id', "selectBank")
    selectedBank = Select(bankSelect)
    selectedBank.select_by_value("1:" + user['bankIndex'])

    kittNo = driver.find_element('id', "appliedKitta")
    kittNo.send_keys(user['kittaNo'])

    crn = driver.find_element('id', "crnNumber")
    crn.send_keys(user['CRN'])

    acceptCheckBox = driver.find_element('id', 'disclaimer')
    acceptCheckBox.click()

    proceedBtn = driver.find_element('xpath',
                                     '/html/body/app-dashboard/div/main/div/app-issue/div/wizard/div/wizard-step[1]/form/div[2]/div/div[5]/div[2]/div/button[1]')
    driver.implicitly_wait(10)
    proceedBtn.click()

    transPin = driver.find_element('id', 'transactionPIN')
    transPin.send_keys(user['PIN'])

    driver.implicitly_wait(10)

    applyBtn = driver.find_element('xpath',
                                   '//*[@id="main"]/div/app-issue/div/wizard/div/wizard-step[2]/div[2]/div/form/div[2]/div/div/div/button[1]')

    applyBtn.click()

    driver.implicitly_wait(10)


    driver.implicitly_wait(10)

    logout = driver.find_element('xpath',
                                 '/html/body/app-dashboard/header/div[2]/div/div/div/ul/li[1]')
    logout.click()

  `  print("Hurraayyyyyyyyy ", user["name"], " Applied Successfully")`

    driver.implicitly_wait(10)

