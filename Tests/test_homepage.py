from environments import *
from models.homepage import HomePage
def test_homepage(page):
    page.goto(docker_url)
    homepage = HomePage(page)
    assert homepage.title.inner_text() =='Home'
    page.close()