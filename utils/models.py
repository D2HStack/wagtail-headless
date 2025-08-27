from django.db import models

from wagtail.snippets.models import register_snippet
from wagtail import blocks
from wagtail.images.blocks import ImageBlock, ImageChooserBlock
from wagtail.fields import RichTextField
from wagtail.images import get_image_model
from wagtail.admin.panels import FieldPanel

# Create your models here.

############################ SNIPPET ############################

@register_snippet
class Author(models.Model):
    first_name = models.CharField(blank=False, max_length=255)
    last_name = models.CharField(blank=False, max_length=255)
    username = models.CharField(unique=True, max_length=255)
    
    role = models.CharField(blank=True, max_length=255)
    
    email = models.EmailField(unique=True)
    
    description = RichTextField(
        blank=True, 
        features=["bold", "italic", "link"],
    )

    image = models.ForeignKey(
        get_image_model(),
        on_delete=models.CASCADE,
        related_name="+"
    )
    
    panels = [
        FieldPanel("first_name"),
        FieldPanel("last_name"),
        FieldPanel("username"),
        FieldPanel("role"),
        FieldPanel("email"),
        FieldPanel("description"),
        FieldPanel("image"),
    ]
    
    # Define the human-readable name for this model in the Wagtail admin
    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"  # Plural form for lists

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
@register_snippet
class ArticleTopic(models.Model):
    title = models.CharField(blank=False, max_length=255)
    description = models.TextField(default="")
    slug = models.SlugField(blank=False, max_length=255)
    
    panels = [
        FieldPanel("title"),
        FieldPanel("description"),
        FieldPanel("slug"),
    ]
    
    # Define the human-readable name for this model in the Wagtail admin
    class Meta:
        verbose_name = "Article Topic"
        verbose_name_plural = "Article Topics"  # Plural form for lists

    def __str__(self):
        return self.title

############################ BLOCKS ############################

class CaptionedImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    image_alt_text = blocks.CharBlock(
        required=False,
        help_text="If left blank, the image's global alt text will be used.",
    )
    caption = blocks.CharBlock(required=False)

    class Meta:
        icon = "image"
        

class SectionBlocks(blocks.StreamBlock):
    paragraph = blocks.RichTextBlock(
        features=["bold", "italic", "link", "ol", "ul", "h3", "code", "blockquote", "hr"],
    )
    
    image = CaptionedImageBlock()

class SectionBlock(blocks.StructBlock):
    heading = blocks.CharBlock(
        form_classname="title",
        icon="title",
        required=False,
    )
    content = SectionBlocks()

    class Meta:
        icon = "doc-full"

class StoryBlock(blocks.StreamBlock):
    section = SectionBlock()