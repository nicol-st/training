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
        wrapper = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#listado-avisos .table')))
        phenomena_cell = wrapper.find_elements(By.TAG_NAME, 'td')
        headers = ['Phenomenon','Value','Warnig Level','Probability','Warning Zone','Beginning Time','Ending Time','Comment']
        cols = len(headers)
        all_cells = [cell.text for cell in phenomena_cell]
        tabledata = [all_cells[i:i+cols] for i in range(0, len(all_cells), cols)]
        print(tabulate(tabledata,headers,tablefmt="grid"))


bot = Bot()
bot.connect()

bot.browser.quit()