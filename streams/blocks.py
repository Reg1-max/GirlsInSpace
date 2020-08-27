from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class TimelineItemBlock(blocks.StructBlock):
    timeline_item = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('date', blocks.DateBlock(required=True, help_text="enter the date that the event happened on")),
                ('title', blocks.CharBlock(required=True, help_text="name the event here")),
                ('image', ImageChooserBlock(required=False, help_text="insert an image to go with your event (optional)")),
                ('text', blocks.TextBlock(required=True, help_text="describe the event here")),
            ]
        )
    )
    
    class Meta: # noqa
        template = "streams/timeline_item_block.html"
        icon = "edit"
        label = "Timeline Item"

class CardBlock(blocks.StructBlock):
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
               ('image', ImageChooserBlock(required=True)),
               ('title', blocks.CharBlock(required=True, max_length=40)),
               ('text', blocks.TextBlock(required=True, max_length=200)),
               ('button_page', blocks.PageChooserBlock(required=False)),
               ('button_url', blocks.URLBlock(required=False, help_text="use if you want to go to external links")),
               ('button_title', blocks.CharBlock(required=False, max_length=40, help_text="Give your button a title")),
            ]
        )
    )

    class Meta: # noqa
        template = "streams/card_block.html"
        icon = "placeholder"
        label = "Cards"