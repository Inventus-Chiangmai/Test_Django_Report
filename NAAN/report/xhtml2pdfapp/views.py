from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from io import BytesIO

from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

class truck_control_pdf(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('xhtml2pdfapp/truck_control.html')
        return HttpResponse(pdf, content_type='application/pdf')

class replacement_order_pdf(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('xhtml2pdfapp/replacement_order.html')
        return HttpResponse(pdf, content_type='application/pdf')

class delivery_note_pdf(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('xhtml2pdfapp/delivery_note.html')
        return HttpResponse(pdf, content_type='application/pdf')
        