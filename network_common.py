import requests

class downloader:
    """

    """
    def __init__(self):
        self.session = requests.session() # Create a requests session
        self.login_url = ""
        self.loginCnt = 0

    def set_login_url(self, url):
        self.login_url = url


    def login(self):
        pass

    def dlWebpage(self, url, payload={}, abort_on_error=False):
        results = self.session.get(url, params=payload)
        return results

    def dlWebPageBinary(self, url, payload={}, abort_on_error=False):
        r = self.dlWebpage(url, payload, abort_on_error=False)
        return r
        #return r.text   # Returns only the contents of the url given (eg html, graphic, etc)

    def dlWebpageData(self, url, payload={}, abort_on_error=False):
        r = self.dlWebpage(url, payload, abort_on_error=False)
        return r.text   # Returns only the contents of the url given (eg html, graphic, etc)

