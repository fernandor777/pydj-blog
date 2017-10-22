from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):
    def test_no_init_pubdate(self):
        post1 = Post()
        self.assertIsNone(post1.fecha_publicacion)
