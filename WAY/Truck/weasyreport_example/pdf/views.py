from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from mysite.utils import render_to_pdf #created in step 4

import os

from django.conf import settings
from django.shortcuts import render
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    result = finders.find(uri)
    if result:
        if not isinstance(result, (list, tuple)):
            result = [result]
        result = list(os.path.realpath(path) for path in result)
        path = result[0]
    else:
        sUrl = settings.STATIC_URL  # Typically /static/
        sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL  # Typically /media/
        mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('pdf/invoice.html')
        return HttpResponse(pdf, content_type='application/pdf')


def generate_PDF(request):
    data = {}

    template = get_template('pdf/invoice.html')
    html  = template.render(data)

    file = open('test.pdf', "w+b")
    pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file,encoding='utf-8', link_callback=link_callback)

    file.seek(0)
    pdf = file.read()
    file.close()
    return HttpResponse(pdf, content_type='application/pdf')

def render_pdf(request):
    template_path = 'pdf/invoice.html'
    context = extract_request_variables(request)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    template = get_template(template_path)
    html = template.render(context)
    pisaStatus = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
    if pisaStatus.err:
        return HttpResponse('We had some errors with code %s <pre>%s</pre>' % (pisaStatus.err,                                                                              html))
    return response