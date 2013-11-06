# coding : utf -8
#from flask.ext.htmlbuilder import html
#from flask.ext.admin.babel import lazy_gettext
from quokka import admin
from quokka.modules.posts.admin import PostAdmin
from quokka.core.admin.models import ModelAdmin
from quokka.core.admin import _, _l
from .models import Cart, Processor


class ProductAdmin(PostAdmin):
    column_list = ('title', 'slug', 'channel',
                   'unity_value', 'weight',
                   'published', 'created_at',
                   'available_at', 'view_on_site')
    column_searchable_list = ['title', 'summary', 'description']
    form_columns = [
        'title', 'slug', 'channel', 'related_channels', 'summary',
        'description', 'unity_value', 'weight', 'dimensions', 'extra_value',
        'published', 'show_on_channel',
        'available_at', 'available_until',
        'tags', 'contents', 'values', 'template_type'
    ]
    form_widget_args = {
        'description': {
            'rows': 20,
            'cols': 20,
            'class': 'text_editor',
            'style': "margin: 0px; width: 725px; height: 360px;"
        },
        'summary': {
            'style': 'width: 400px; height: 100px;'
        },
        'title': {'style': 'width: 400px'},
        'slug': {'style': 'width: 400px'},
    }


class CartAdmin(ModelAdmin):
    """
    All attributes added here for example
    more info in admin source
    github.com/mrjoes/flask-admin/blob/master/flask_admin/model/base.py
    or Flask-admin documentation
    """

    roles_accepted = ('admin', 'editor')
    can_create = True
    can_edit = True
    can_delete = True

    # list_template = 'admin/model/list.html'
    # edit_template = 'admin/custom/edit.html'
    # create_template = 'admin/custom/create.html'

    # column_list = ('title', 'slug', 'channel', 'published', 'view_on_site')

    #def view_on_site(self, request, obj, fieldname, *args, **kwargs):
    #    return html.a(
    #        href=obj.get_absolute_url('detail'),
    #        target='_blank',
    #    )(html.i(class_="icon icon-eye-open", style="margin-right: 5px;")(),
    #      lazy_gettext('View on site'))

    # column_exclude_list = []

    # column_formatters = {'view_on_site': view_on_site}
    # column_type_formatters = {}
    # column_labels = {}
    # column_descriptions = {}
    # column_sortable_list = [] / ('name', ('user', 'user.username'))
    # column_default_sort = 'pk'
    # column_choices = {'column': ('value', 'display')}
    # column_display_pk = True
    # column_filters = ['published', 'title']
    # column_searchable_list = ('title', 'body', 'summary')

    # form_columns = ['title', 'slug', 'channel', 'related_channels',
    #                 'summary', 'body', 'main_image', 'main_image_caption',
    #                 'published', 'show_on_channel', 'available_at', 'tags',
    #                 'comments', 'values']

    # form_excluded_columns = []
    # form = None
    # form_overrides = None

    # form_widget_args = {
    #    'body': {
    #        'rows': 20,
    #        'cols': 20,
    #        'class': 'text_editor',
    #        'style': "margin: 0px; width: 725px; height: 360px;"
    #    },
    #    'summary': {
    #        'style': 'width: 400px; height: 100px;'
    #    },
    #    'title': {'style': 'width: 400px'},
    #    'slug': {'style': 'width: 400px'},
    #}

    # form_args = {
    #     'body': {
    #         'widget': BigTextArea()
    #     }
    # }

    # form_extra_fields = {}

    # action_disallowed_list

    # page_size = 20
    #form_ajax_refs = {
    #    'main_image': {"fields": ('title',)}
    #}


class ProcessorAdmin(ModelAdmin):
    roles_accepted = ('admin', 'developer')


admin.register(Cart, CartAdmin, category=_("Cart"), name=_l("Cart"))
admin.register(Processor, ProcessorAdmin, category=_("Cart"),
               name=_l("Processor"))
