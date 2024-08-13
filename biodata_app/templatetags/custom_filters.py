from django import template

register = template.Library()


@register.filter
def add_required(field):
    if field.field.required:
        return field.as_widget(attrs={'required': 'required'})
    return field
