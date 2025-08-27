# from django.db import models
from django.db import models
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.search import index
from wagtail.models import Page
from wagtail.fields import StreamField
# from mysite.utils.blocks import StoryBlock, InternalLinkBlock
# from mysite.utils.models import BasePage

from wagtail.api import APIField
from wagtail.fields import RichTextField
from mysite.serializers import RichTextSerializer

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

