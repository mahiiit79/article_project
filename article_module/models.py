from django.db import models

from account_module.models import User


class ArticleCategory(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان')
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان در url')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')

    def __str__(self):
        return f'( {self.title} - {self.url_title} )'

    class Meta:
        verbose_name = 'دسته بندی مقالات'
        verbose_name_plural = 'دسته بندی های مقالات'

class Article(models.Model):
    title_in_english = models.CharField(max_length=300,verbose_name='نام مقاله به انگلیسی')
    title_in_persian = models.CharField(max_length=300, verbose_name='نام مقاله به فارسی')
    category = models.ManyToManyField(ArticleCategory,related_name='article_categories',verbose_name='دسته بندی مقالات')
    image = models.ImageField(upload_to='images/articles',verbose_name='تصویر فایل')
    articles_file = models.FileField(upload_to='articles_files',verbose_name='قایل مقاله')
    publish_date = models.CharField(max_length=10,blank=True,null=True,verbose_name='تاریخ انتشار مقاله')
    count_pages = models.IntegerField(verbose_name='تعداد صفحات مقاله')
    journal = models.CharField(max_length=300,blank=True,null=True,verbose_name='مجله')
    university = models.CharField(max_length=300,blank=True,null=True,verbose_name='نام دانشگاه')
    free_or_buyable = models.BooleanField(verbose_name='رایگان/فروشی')
    price=models.CharField(max_length=20,null=True,blank=True,verbose_name='قیمت')
    abstract = models.TextField(verbose_name='چکیده')
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=200, unique=True,
                            verbose_name='عنوان در url')

    def __str__(self):
        return f"({self.title_in_english} - {self.title_in_persian})"

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'


class ArticleVisit(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name='مقاله')
    ip = models.CharField(max_length=30, verbose_name='آی پی کاربر')
    user = models.ForeignKey(User, null=True, blank=True, verbose_name='کاربر', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.article.title_in_english} - {self.article.title_in_persian} / {self.ip}'

    class Meta:
        verbose_name = 'بازدید محصول'
        verbose_name_plural = 'بازدیدهای محصول'
