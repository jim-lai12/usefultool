try:
    from cookielib import MozillaCookieJar
except ImportError:
    from http.cookiejar import MozillaCookieJar
try:
    from cookielib import Cookie
except ImportError:
    from http.cookiejar import MozillaCookieJar
import requests






class CookieWay:
    def __init__(self):
        self.cookiejar = MozillaCookieJar()
    def load(self,file="cookie.txt"):
        self.cookiejar.load(file,ignore_discard=True,ignore_expires=True)
    def save(self,file="cookie.txt"):
        self.cookiejar.save(file,ignore_discard=True,ignore_expires=True)
    def torequestscj(self,s):
        for item in self.cookiejar:
            cookiesobject = requests.cookies.create_cookie(domain=item.domain, name=item.name, value=item.value)
            s.cookies.set_cookie(cookiesobject)
    def toseleniumcj(self,driver):
        domains = []
        for item in self.cookiejar:
            if item.domain not in domains:
                domains.append(item.domain)
        for i in range(len(domains)):
            if domains[i][0:1] == ".":
                domains[i] = domains[i][1:]
        domains = list(set(domains))
        for item in domains:
            driver.get("https://"+item)
            for item2 in self.cookiejar:
                if item2.domain == item or item2.domain =="."+item:
                    cookie_dict = {'domain': item2.domain, 'name': item2.name, 'value': item2.value,
                                   'secure': item2.secure}
                    if item2.path_specified:
                        cookie_dict['path'] = item2.path
                    driver.add_cookie(cookie_dict)
    def sele2resq(self,driver,s):
        self.selcj_cj(driver)
        self.torequestscj(s)
    def resq2sele(self, s, driver):
        self.reqcj_cj(s)
        self.toseleniumcj(driver)
    def selcj_cj(self,driver):
        cookie = driver.get_cookies()
        for s_cookie in cookie:
            self.cookiejar.set_cookie(
                Cookie(version=0, name=s_cookie['name'], value=s_cookie['value'], port='80',
                                 port_specified=False,
                                 domain=s_cookie['domain'], domain_specified=True, domain_initial_dot=False,
                                 path=s_cookie['path'], path_specified=True, secure=s_cookie['secure'],
                                 expires="2069592763",  # s_cookie['expiry']
                                 discard=False, comment=None, comment_url=None, rest=None,
                                 rfc2109=False))
    def reqcj_cj(self,s):
        for s_cookie in s.cookies:
            self.cj.set_cookie(
                Cookie(version=0, name=s_cookie.name, value=s_cookie.value, port='80', port_specified=False,
                                 domain=s_cookie.domain, domain_specified=True, domain_initial_dot=False,
                                 path="/", path_specified=True, secure=True,
                                 expires="2069592763",  # s_cookie['expiry']
                                 discard=False, comment=None, comment_url=None, rest=None,
                                 rfc2109=False))


