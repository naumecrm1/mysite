from django.test import TestCase
from django.urls import reverse, resolve
from django.utils import timezone
from .views import HomePageView, ArticleCategoryList, ArticleList, ArticleDetail
from .models import Article, Category


class URLTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Set up data for tests"""
        category = Category.objects.create(category='Tech', slug='tech')
        cls.article = Article.objects.create(
            title='Sample Article',
            description='Sample description',
            pub_date=timezone.datetime(2023, 5, 10, tzinfo=timezone.utc),
            slug='sample-article',
            category=category
        )

    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEqual(view.func.view_class, HomePageView)

    def test_article_list_view_status_code(self):
        url = reverse('articles-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_article_category_list_view_status_code(self):
        url = reverse('articles-category-list', args=('tech',))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_article_category_list_url_resolves_article_category_list_view(self):
        view = resolve('/articles/category/tech')
        self.assertEqual(view.func.view_class, ArticleCategoryList)

    def test_article_detail_view_status_code(self):
        url = reverse('news-detail', kwargs={
            'year': self.article.pub_date.strftime('%Y'),
            'month': self.article.pub_date.strftime('%m'),
            'day': self.article.pub_date.strftime('%d'),
            'slug': self.article.slug
        })
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_article_detail_url_resolves_article_detail_view(self):
        view = resolve(f"/articles/{self.article.pub_date.strftime('%Y')}/{self.article.pub_date.strftime('%m')}/{self.article.pub_date.strftime('%d')}/{self.article.slug}")
        self.assertEqual(view.func.view_class, ArticleDetail)
