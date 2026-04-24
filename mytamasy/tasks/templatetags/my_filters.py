from django.template.defaultfilters import register

@register.filter(name='dict_key')
def dict_key(d, k):
    '''Returns the given key from a dictionary.'''
    return d[k]

@register.filter(name='is_selected')
def is_selected(value, compare):
    '''Returns 'SELECTED' string if compare equals value'''
    return 'SELECTED' if value == compare else ''
