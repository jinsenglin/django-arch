from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


class MySiteTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_root_title(self):
        self.browser.get(self.live_server_url)
        self.assertEquals(u'mysite', self.browser.title)
