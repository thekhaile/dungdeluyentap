__author__ = 'khaile'
import requests


class Keywords(object):
    def __init__(self):
        self.url = 'aHR0cDovL2NvbnRlbnQuZ3VhcmRpYW5hcGlzLmNvbS9zZWFyY2g/dG8tZGF0ZT0yMDE2LTEyLTMx\nJnBhZ2Utc2l6ZT02MCZhcGkta2V5PWI2MDYzZTY4LTU4OWItNGVkYS05YTUwLTMzNGUyMTg3MTli\nNA==\n'

    def get_keywords(self):
        keywords = []
        r = requests.get(self.url.decode('base64','strict'))
        json = r.json()
        response = json['response']
        results = response['results']
        for result in results:
            keywords.append(result['webTitle'])

        return keywords



