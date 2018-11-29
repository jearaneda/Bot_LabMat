import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config

url = "http://labmat.puc.cl"
username = config.username
password = config.password
cursos = ["MAT1610-1", "MAT1620-1","MAT1630-1","MAT1640-1", "MAT1203-1", "EYP1113-1", "MAT251I-1"]
driver = webdriver.Chrome()

if __name__ == "__main__":
   driver.get(url)

   uname = driver.find_element_by_name("usuario")
   uname.send_keys(username)

   passw = driver.find_element_by_name("clave")
   passw.send_keys(password)


   # Find the submit button using class name and click on it.
   submit_button = driver.find_element_by_class_name("btn-lg").click()




   WebDriverWait(driver, 50).until( lambda driver: driver.find_element_by_id('wrapper'))

   driver.get("https://www.labmat.puc.cl/dashboard#0.9239247194308471!/cursos/2018/22/Ingenieria/" + cursos[config.curso])

   WebDriverWait(driver, 100).until( lambda driver: driver.find_element_by_class_name('table-responsive'))


while True:
   c1 = driver.find_element_by_tag_name('tr').text
   time.sleep(100)
   driver.refresh()
   WebDriverWait(driver, 100).until( lambda driver: driver.find_element_by_class_name('table-responsive'))
   c2 = driver.find_element_by_tag_name('tr').text
   print(c1 ==  c2)
   if c1 != c2:
    fromaddr = "botcitolabmat@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = "Botcito Labmat"
    msg['Subject'] = "Nuevo mensaje LABMAT"
    msg["To"] = config.sendto
    body = c2
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, config.pass_bot)
    text = msg.as_string()
    server.sendmail(fromaddr, msg["To"].split(","), text)
    server.quit()
