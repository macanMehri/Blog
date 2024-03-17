from django.db import models


class BaseModel(models.Model):

    is_active = models.BooleanField(
        default=False,
        verbose_name='Is Active'
    )

    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created Date'
    )

    updated_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated Date'
    )


    class Meta:
        abstract = True


    def __str__(self) -> str:
        raise NotImplementedError('You did not override the string method!')



class Category(BaseModel):

    title = models.CharField(
        max_length=255,
        blank=False,
        verbose_name='Title'
    )

    description = models.TextField(
        blank=False,
        verbose_name='Description'
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    

    def __str__(self) -> str:
        return self.title


    @staticmethod
    def get_actives() -> list:
        '''Returns a list of active objects'''
        return Category.objects.filter(is_active=True).order_by('pk')


class Post(BaseModel):

    title = models.CharField(
        max_length=255,
        blank=False,
        verbose_name='Title'
    )

    description = models.TextField(
        blank=False,
        verbose_name='Description'
    )

    category = models.ForeignKey(
        Category,
        null=False,
        on_delete=models.deletion.CASCADE,
        verbose_name='Category'
    )


    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


    def __str__(self) -> str:
        return f'{self.category} - {self.title} : {self.description}'


    @staticmethod
    def get_actives() -> list:
        '''Returns a list of active objects'''
        return Post.objects.filter(is_active=True).order_by('pk')
