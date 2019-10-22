from django import template

register = template.Library()

def cut(value,arg):
    """ this cuts off all the values of args from string """
    return value.replace(arg,'')

register.filter('cut',cut)    # 1st param is string called in custome template tag and is registered as cut into library
                              #2nd param is function
