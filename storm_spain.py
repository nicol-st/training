from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from tabulate import tabulate

class Bot():
    def __init__(self):
        self.browser = WebDriver()
        self.wait = WebDriverWait(self.browser,10)
        self.wait_longer = WebDriverWait(self.browser, 30)
        self.tabledata = []
        
    def connect(self):
        self.browser.get('https://www.aemet.es/en/eltiempo/prediccion/avisos')
        phenomena_table = self.wait.until(EC.presence_of_element_located((By.ID, 'listado-avisos')))
        phenomena_cells = phenomena_table.find_element(By.CLASS_NAME, 'table')
        phenomena_rows = phenomena_cells.find_elements(By.TAG_NAME, 'td')
        for cell in phenomena_rows:
            phenomena_rows = cell.text
            print(phenomena_rows)
            phenomena_rows = phenomena_rows.splitlines()
            headers = ['Phenomenon','Value','Warnig Level','Probability','Warning Zone','Beginning Time','Ending Time','Comment']
            cols = len(headers)
            #print(phenomena_rows)
            tabledata = [phenomena_rows[i:i + cols] for i in range(0, len(phenomena_rows), cols)]
            print(tabledata)
    

bot = Bot()
bot.connect()

bot.browser.quit()