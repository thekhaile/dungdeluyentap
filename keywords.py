__author__ = 'khaile'
import requests


class Keywords(object):
    def __init__(self):
        self.url1 = 'aHR0cDovL2NvbnRlbnQuZ3VhcmRpYW5hcGlzLmNvbS9zZWFyY2g/dG8tZGF0ZT0yMDE2LTEyLTMx\nJnBhZ2Utc2l6ZT02MCZhcGkta2V5PWI2MDYzZTY4LTU4OWItNGVkYS05YTUwLTMzNGUyMTg3MTli\nNA==\n'
        self.url2 = 'aHR0cDovL2NvbnRlbnQuZ3VhcmRpYW5hcGlzLmNvbS9zZWFyY2g/dG8tZGF0ZT0yMDE2LTEyLTMx\nJnNob3ctZmllbGRzPWVjb25vbXkmcGFnZS1zaXplPTYwJmFwaS1rZXk9YjYwNjNlNjgtNTg5Yi00\nZWRhLTlhNTAtMzM0ZTIxODcxOWI0\n'

    def get_keywords(self, option=1):
        keywords = []
        if option == 1:
            r = requests.get(self.url1.decode('base64','strict'))
        else:
            r = requests.get(self.url1.decode('base64','strict'))
        json = r.json()
        response = json['response']
        results = response['results']
        for result in results:
            keywords.append(result['webTitle'])

        return keywords



