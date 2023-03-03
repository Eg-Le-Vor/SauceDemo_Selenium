from base.base_class import Base


class Finish_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Методы"""

    def finish(self):
        self.check_u = "https://www.saucedemo.com/checkout-complete.html"
        
        self.get_current_url()
        self.check_url(self.check_u)
        self.get_screenshot()