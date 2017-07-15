from sniper.tests import TestApp, TestCase, TestClient
from sniper.url import url

from sniper_jinja.controllers import JinjaController


class HelloCtrl(JinjaController):
    template_name = 'hello.html'


urls = [
    url(r'^/hello$', HelloCtrl),
]


class TestController(TestCase):
    def setUp(self):
        self.app = TestApp(
            urls=urls,
            config={
                'jinja_template_path': 'tests/templates'
            }
        )
        self.client = TestClient(self.app)

    async def test_hello(self):
        r = await self.client.get('/hello')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.body, '<h1>Hello world!</h1>')
