class HomePage:
    def __init__(self, page):
        self.page = page
        self.title = page.locator('//head//title')
        self.menuButton = page.locator('div > nav > a')