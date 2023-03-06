from base.base_class import Base
from utils.logger import Logger


class Finish_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Методы"""

    def finish(self):
        self.check_u = "https://www.saucedemo.com/checkout-complete.html"
        
        Logger.add_start_step(method='finish')
        self.get_current_url()
        self.check_url(self.check_u)
        self.get_screenshot()
        Logger.add_end_step(url=self.driver.current_url, method='finish')