from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment

class BlogTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post = Post.objects.create(title='Test Post', content='Content here', author=self.user)
        self.comment = Comment.objects.create(post=self.post, author=self.user, text='Nice post')

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')

    def test_comment_creation(self):
        self.assertEqual(self.comment.text, 'Nice post')
