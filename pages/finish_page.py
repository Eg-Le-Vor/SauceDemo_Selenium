from base.base_class import Base


class Finish_page(Base):

    check = "Checkout: Complete!"
    check_link = "https://www.saucedemo.com/checkout-complete.html"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Методы"""

    def finish(self):
        self.get_current_url()
        self.check_url(self.check_link)
        self.get_screenshot()