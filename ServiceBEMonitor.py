from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time, hashlib
from smtplib import SMTP as SMTP

driver = webdriver.Firefox(executable_path=r'C:\Users\Me\AppData\Local\Programs\Python\Python37\geckodriver.exe')  # Insert path of your Geckdriver.exe inside the quotes
driver.get("https://service.berlin.de/dienstleistung/120686/")  # Loads initial page

appointmentPageLink = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/div[3]/div[1]/div[2]/div[9]/div[1]/p[1]/a[1]")))
driver.execute_script("arguments[0].click();", appointmentPageLink)  # Clicks the link for appointments

while True:
        currentHash = hashlib.sha256(driver.page_source.encode('utf-8')).hexdigest()  # Get hash
        time.sleep(100) # Wait
        driver.refresh() # Refresh page
        newHash = hashlib.sha256(driver.page_source.encode('utf-8')).hexdigest()  # Get new hash to comapre(driver.page_source)

        if newHash == currentHash:  # Time to compare hashes!
            continue  # If the hashes are the same, continue
        else: # If the hashes are different, send email
            def send_email(message, status):
                fromaddr = 'ENTER SENDER EMAIL'  # Enter the email address to send from
                toaddrs = 'ENTER RECEIVER ADDRESS'  # Enter the receiving email address
                server = SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login('ENTER SENDER EMAIL', 'ENTER PASSWORD')  # Enter the sender email address, then the password for it in the next set of quotes.
                server.sendmail(fromaddr, toaddrs, 'Subject: %s\r\n%s' % (status, message))
                server.quit()

            send_email('New appointments available! https://service.berlin.de/dienstleistung/120686/', 'New update detected!')






