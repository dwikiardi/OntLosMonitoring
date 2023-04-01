from time import sleep
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from win10toast import ToastNotifier

# make chrome log requests
options = Options()
options.add_argument('ignore-certificate-errors')
options.add_argument('--headless=new')
capabilities = DesiredCapabilities.CHROME
capabilities["loggingPrefs"] = {"performance": "ALL"}  # newer: goog:loggingPrefs
driver = webdriver.Chrome(
    desired_capabilities=capabilities, service=Service(ChromeDriverManager().install()),  options=options
)

# fetch a site that does xhr requests
driver.get("https://olt.itsnot.my.id/lol.php")
sleep(5)  # wait for the requests to take place

#notification
toast = ToastNotifier()

# try:
element = WebDriverWait(driver, 500).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/table/tbody/tr[1]"))
)
table = driver.find_element(By.XPATH, '//*[@id="uhu"]').text
data = table.split('\n')
totalData = len(data)

currenttotalData = totalData
print("Olt Monitor Running Bosku")
sleep(5)
while True:
    try:
        driver.get("https://olt.itsnot.my.id/lol.php")
        element = WebDriverWait(driver, 500).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/table/tbody/tr[1]"))
        )

        table = driver.find_element(By.XPATH, '//*[@id="uhu"]').text
        data = table.split('\n')
        totalData = len(data)
        currenttotalData = totalData

        sleep(120)

        driver.get("https://olt.itsnot.my.id/lol.php")
        element = WebDriverWait(driver, 500).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/table/tbody/tr[1]"))
        )

        table = driver.find_element(By.XPATH, '//*[@id="uhu"]').text
        data = table.split('\n')
        totalData = len(data)
        newtotalData= totalData

        # for datalos in range(10, 10):
        #     log = data[datalos]

        if currenttotalData == newtotalData:
            print('============================================')
            print('Belum Ada Los , OTW refresh')
            print('============================================')
            for datalos in range(currenttotalData - 1 , newtotalData):
                print('Data Los Terakhir :')
                print(data[datalos])
            print('============================================')
            continue

        elif currenttotalData < newtotalData :
            toast.show_toast(
                "Notification",
                "Ada yang los check bos",
                duration = 1200,
                icon_path = "icon.ico",
                threaded = True,
            )
            # notify
            print('============================================')
            print("Ada yang los check bos")
            print('============================================')
            for datalos in range(currenttotalData - 1 , newtotalData):
                print('Data Los Terbaru :')
                print(data[datalos])
            print('============================================')
            # again read the website
            driver.get("https://olt.itsnot.my.id/lol.php")
            element = WebDriverWait(driver, 500).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/table/tbody/tr[1]"))
            )                
            table = driver.find_element(By.XPATH, '//*[@id="uhu"]').text
            data = table.split('\n')
            totalData = len(data)
            currenttotalData = totalData
            sleep(120)
            continue
        else :
            toast.show_toast(
                "Notification",
                "Ada yang udah up check bos",
                duration = 1200,
                icon_path = "icon.ico",
                threaded = True,
            )
            # notify
            print("Ada yang udah up check bos")
            # again read the website
            driver.get("https://olt.itsnot.my.id/lol.php")
            element = WebDriverWait(driver, 500).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/table/tbody/tr[1]"))
            )                
            table = driver.find_element(By.XPATH, '//*[@id="uhu"]').text
            data = table.split('\n')
            totalData = len(data)
            currenttotalData = totalData
            sleep(120)
            continue

    except Exception as e:
        driver.quit()