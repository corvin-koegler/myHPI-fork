from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from wagtail_localize.fields import SynchronizedField
from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel, PublishingPanel
from django import forms
from wagtail.search import index
from wagtail.models import Page
from .models import BasePage, InformationPage, MinutesList, MinutesLabel, TaggedMinutes

# --- Page Admins --- #
class BasePageAdmin(SnippetViewSet):
    model = BasePage
    menu_label = "Base Page"
    menu_icon = "doc-full"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False

    override_translatable_fields = [
        SynchronizedField("visible_for"),
    ]
    settings_panels = [
        PublishingPanel(),
        FieldPanel("is_public", widget=forms.CheckboxInput),
        FieldPanel("visible_for", widget=forms.CheckboxSelectMultiple),
    ]
    # FilterFields required for restricting search results
    search_fields = Page.search_fields + [
        index.FilterField("group_id"),
        index.FilterField("is_public"),
    ]

class InformationPageAdmin(SnippetViewSet):
    model = InformationPage
    menu_label = "Information Page"
    menu_icon = "doc-full"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False

    override_translatable_fields = [
        SynchronizedField("visible_for"),
    ]
    settings_panels = [
        PublishingPanel(),
        FieldPanel("is_public", widget=forms.CheckboxInput),
        FieldPanel("visible_for", widget=forms.CheckboxSelectMultiple),
    ]
    # FilterFields required for restricting search results
    search_fields = Page.search_fields + [
        index.FilterField("group_id"),
        index.FilterField("is_public"),
    ]

# --- Minutes Admins --- #

class MinutesListAdmin(SnippetViewSet):
    model = MinutesList
    menu_label = "List"
    menu_icon = "tasks"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False

    content_panels = Page.content_panels + [
        FieldPanel("group", widget=forms.Select),
    ]
    parent_page_types = [
        "FirstLevelMenuItem",
        "SecondLevelMenuItem",
        "InformationPage",
        "RootPage",
    ]
    subpage_types = ["Minutes"]

class MinutesLabelAdmin(SnippetViewSet):
    model = MinutesLabel
    menu_label = "Labels"
    menu_icon = "title"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False

class MinutesTagsAdmin(SnippetViewSet):
    model = TaggedMinutes
    menu_label = "Tags"
    menu_icon = "tag"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False

@register_snippet
class MinutesGroup(SnippetViewSetGroup):
    items = (
        MinutesListAdmin,
        MinutesLabelAdmin,
        MinutesTagsAdmin,
    )
    menu_icon = "doc-full-inverse"
    menu_label = "Minutes"
    menu_name = "minutes"

    add_to_settings_menu = True
