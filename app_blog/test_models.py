from django.test import TestCase
from django.utils import timezone
from .models import Category, Article


class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Set up non-modified objects used by all test"""
        Category.objects.create(category='Innovations', slug='innovations')

    def test_get_absolute_url(self):
        category = Category.objects.get(id=1)
        self.assertEqual(category.get_absolute_url(), '/articles/category/innovations')


class ArticleModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Set up non-modified objects used by all test"""
        category = Category.objects.create(category='Tech', slug='tech')
        Article.objects.create(
            title='Test Article',
            description='Test description',
            pub_date=timezone.datetime(2023, 5, 10, tzinfo=timezone.utc),
            slug='test-article',
            category=category
        )

    def test_get_absolute_url(self):
        article = Article.objects.get(id=1)
        self.assertEqual(article.get_absolute_url(), '/articles/2023/05/10/test-article')
