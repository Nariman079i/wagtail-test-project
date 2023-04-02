from django.db.models import *
from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import *
class HomePage(Page):

    #Поля в БД
    subtitle = CharField(
        verbose_name="Подстрока",
        help_text="Введите подстроку",
        max_length=100,
        blank=True,
        null=True
    )
    doc_content = RichTextField(
        verbose_name="Контент",
        blank=True,
        null=True
    )

    bg_image = ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=SET_NULL,
        related_name="+"
    )
    #Поля в интерфейсе администратора
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('doc_content'),
        ImageChooserPanel('bg_image')
        ]
    
    


