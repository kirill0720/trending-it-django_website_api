from itobj.models import Category

menu = [{'title': 'Add Post', 'url_name': 'add_post'},
        {'title': 'Contact', 'url_name': 'contact'},
        {'title': 'Register', 'url_name': 'register'},
        {'title': 'Login', 'url_name': 'login'},
        ]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['menu'] = menu
        context['cats'] = cats
        return context
