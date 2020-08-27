from django.db import models
from wagtail.core.models import Page
from streams.blocks import TimelineItemBlock
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel

class TimelinePage(Page):
    body = StreamField(
        [
            ("timeline_item", TimelineItemBlock()),
        ],
        null=True,
        blank=True,
    )
    content_panels = Page.content_panels + [
        StreamFieldPanel("body", classname="full"),
    ]


