from django import template
register=template.Library()

def truncate4(value):
    res=value[0:4]
    return res


@register.filter(name='t_n')
def truncate_n(value,n):
    res=value[0:n]
    return res


register.filter('truncate4',truncate4)
#register.filter('t_n',truncate_n)