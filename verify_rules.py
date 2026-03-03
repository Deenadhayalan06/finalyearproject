import unittest
from app import app
import warnings
warnings.filterwarnings('ignore')

class TestURLSafety(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_https_safe(self):
        # https should be safe (xx=1.0)
        response = self.app.post('/', data={'url': 'https://google.com'})
        # In index.html, xx >= 0.5 is safe. xx=1.0 is safe.
        # "Website is 100% safe to use..."
        # We look for "1.0" in the rendered template variable or the text.
        # The template has 'let x = "{{ xx }}";'
        # So we expect 'let x = "1.0";'
        content = response.data.decode('utf-8')
        if 'let x = "1.0"' in content:
            print("\nHTTPS test passed: Found 'let x = \"1.0\"'")
        else:
            print("\nHTTPS test failed. Content snippet:", content[:500])
            self.fail("Did not find 'let x = \"1.0\"' for HTTPS URL")

    def test_http_unsafe(self):
        # http should be unsafe (xx=0.0)
        response = self.app.post('/', data={'url': 'http://google.com'})
        content = response.data.decode('utf-8')
        if 'let x = "0.0"' in content:
             print("\nHTTP test passed: Found 'let x = \"0.0\"'")
        else:
             print("\nHTTP test failed. Content snippet:", content[:500])
             self.fail("Did not find 'let x = \"0.0\"' for HTTP URL")

    def test_www_unsafe(self):
        # www should be unsafe (xx=0.0)
        response = self.app.post('/', data={'url': 'www.google.com'})
        content = response.data.decode('utf-8')
        if 'let x = "0.0"' in content:
             print("\nWWW test passed: Found 'let x = \"0.0\"'")
        else:
            print("\nWWW test failed. Content snippet:", content[:500])
            self.fail("Did not find 'let x = \"0.0\"' for WWW URL")

if __name__ == '__main__':
    unittest.main()
