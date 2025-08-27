from django.db import models
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.search import index
from wagtail.models import Page
from wagtail.fields import StreamField

from wagtail.api import APIField
from wagtail.fields import RichTextField
from mysite.serializers import RichTextSerializer


from wagtail.images.blocks import ImageBlock, ImageChooserBlock

from utils.models import StoryBlock, CaptionedImageBlock

from mysite.serializers import ArticleTopicSerializer

class HomePage(Page):
    introduction = RichTextField(blank=True)
    # hero_cta = StreamField(
    #     [("link", InternalLinkBlock())],
    #     blank=True,
    #     min_num=0,
    #     max_num=1,
    # )
    # body = StreamField(StoryBlock())
    featured_section_title = models.TextField(blank=True)

    search_fields = Page.search_fields + [index.SearchField("introduction")]

    content_panels = Page.content_panels + [
        FieldPanel("introduction"),
        # FieldPanel("hero_cta"),
        # FieldPanel("body"),
        # MultiFieldPanel(
        #     [
        #         FieldPanel("featured_section_title", heading="Title"),
        #         InlinePanel(
        #             "page_related_pages",
        #             label="Pages",
        #             max_num=12,
        #         ),
        #     ],
        #     heading="Featured section",
        # ),
    ]
    
    # Custom API fields
    api_fields=[
        APIField('introduction', serializer=RichTextSerializer),
        # APIField('hero_cta'),
        # APIField('body'),
        # APIField('featured_section_title'),
    ]
    
    # Create your models here.
class ArticlePage(Page):
    
    views = models.PositiveBigIntegerField(default=0, editable=False)
    
    author = models.ForeignKey(
        "utils.Author",
        blank=True,
        null=True,
        on_delete=models.deletion.PROTECT,
        related_name="article_pages", # Change from "+" to search for all articles from an author
    )
    
    publication_date = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Use this field to override the date that the "
        "news item appears to have been published.",
    )
    
    read_time = models.SmallIntegerField(default=1)
    
    description = models.TextField(blank=True)
    
    topic = models.ForeignKey(
        "utils.ArticleTopic",
        blank=True,
        null=True,
        on_delete=models.deletion.PROTECT,
        related_name="article_pages",
    )
    
    hero_image = StreamField(
        [("image", CaptionedImageBlock())],
        blank=True,
        max_num=1,
    )
    
    body = StreamField(StoryBlock())
    
    featured_section_title = models.TextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField("description"),
        index.FilterField("topic"),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("author"),
        FieldPanel("publication_date"),
        FieldPanel("read_time"),
        FieldPanel("topic"),
        FieldPanel("description"),
        FieldPanel("hero_image"),
        FieldPanel("body"),
        # MultiFieldPanel(
        #     [
        #         FieldPanel("featured_section_title", heading="Title"),
        #         InlinePanel(
        #             "page_related_pages",
        #             label="Pages",
        #             max_num=3,
        #         ),
        #     ],
        #     heading="Featured section",
        # ),
    ]
    
    # Custom API fields
    api_fields=[
        APIField('views'),
        APIField('author'),
        APIField('publication_date'),
        APIField('read_time'),
        APIField('topic', serializer=ArticleTopicSerializer()),
        APIField('description'),
        APIField('hero_image'),
        APIField('body'),
        APIField('featured_section_title'),
    ]    

