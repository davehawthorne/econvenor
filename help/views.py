from django.shortcuts import render

from help.utils import convert_markdown_to_html
from utilities.commonutils import set_path


def quick_start_guide(request):

    menu = {'parent': 'help'}            	         
    return render(request, 'quick_start_guide.html', {
                  'menu': menu,
    })


def user_guide(request):

    menu = {'parent': 'help'}            	         
    return render(request, 'user_guide.html', {
                  'menu': menu,
    })


def faqs(request):

    menu = {'parent': 'help'}            	         
    return render(request, 'faqs.html', {
                  'menu': menu,
    })


def ask_question(request):
    MARKDOWN_PATH = set_path('help/markdown/',
        '/home/econvenor/webapps/econvenor/econvenor/help/markdown/')
    page_content = convert_markdown_to_html(MARKDOWN_PATH + 'ask_question.mkd')

    menu = {'parent': 'help'}            	
    return render(request, 'markdown_template.html', {
                  'menu': menu,
                  'page_content': page_content
                  })
