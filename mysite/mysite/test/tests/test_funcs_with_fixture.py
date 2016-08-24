from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


class MySiteTest(StaticLiveServerTestCase):
    fixtures = ['auth.user.json']

    def setUp(self):
        self.profile = webdriver.FirefoxProfile()
        self.profile.set_preference("intl.accept_languages", "en-us")

        self.browser = webdriver.Firefox(firefox_profile=self.profile)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_login_ad(self):
        self.browser.get(self.live_server_url + '/admin/login/')

        self.browser.find_element_by_id('id_username').send_keys("ad01")
        self.browser.find_element_by_id("id_password").send_keys('p@ssw0rd')
        self.browser.find_element_by_css_selector(
            'form input[type="submit"]').click()

        self.assertEquals(u'Site administration | Django site admin',
                          self.browser.title)

        self.browser.get(self.live_server_url)
        self.assertEquals(u'mysite', self.browser.title)

    def test_login_sa(self):
        self.browser.get(self.live_server_url + '/admin/login/')

        self.browser.find_element_by_id('id_username').send_keys("sa01")
        self.browser.find_element_by_id("id_password").send_keys('p@ssw0rd')
        self.browser.find_element_by_css_selector(
            'form input[type="submit"]').click()

        self.assertEquals(u'Site administration | Django site admin',
                          self.browser.title)

        self.browser.get(self.live_server_url)
        self.assertEquals(u'mysite', self.browser.title)

    def test_login_pa(self):
        self.browser.get(self.live_server_url + '/admin/login/')

        self.browser.find_element_by_id('id_username').send_keys("pa01")
        self.browser.find_element_by_id("id_password").send_keys('p@ssw0rd')
        self.browser.find_element_by_css_selector(
            'form input[type="submit"]').click()

        self.assertEquals(u'Site administration | Django site admin',
                          self.browser.title)

        self.browser.get(self.live_server_url)
        self.assertEquals(u'mysite', self.browser.title)

    def test_login_pu(self):
        self.browser.get(self.live_server_url + '/admin/login/')

        self.browser.find_element_by_id('id_username').send_keys("pu01")
        self.browser.find_element_by_id("id_password").send_keys('p@ssw0rd')
        self.browser.find_element_by_css_selector(
            'form input[type="submit"]').click()

        self.assertEquals(u'Site administration | Django site admin',
                          self.browser.title)

        self.browser.get(self.live_server_url)
        self.assertEquals(u'mysite', self.browser.title)

    def test_login_au(self):
        self.browser.get(self.live_server_url + '/admin/login/')

        self.browser.find_element_by_id('id_username').send_keys("au01")
        self.browser.find_element_by_id("id_password").send_keys('p@ssw0rd')
        self.browser.find_element_by_css_selector(
            'form input[type="submit"]').click()

        self.assertEquals(u'Site administration | Django site admin',
                          self.browser.title)

        self.browser.get(self.live_server_url)
        self.assertEquals(u'mysite', self.browser.title)
