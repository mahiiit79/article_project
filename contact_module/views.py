from django.shortcuts import render

from django.views.generic.edit import CreateView

from contact_module.forms import ContactUsModelForm
from contact_module.models import ContactUs
from site_module.models import SiteSetting


class ContactUsView(CreateView):
    template_name = 'contact_module/contact_us_page.html'
    model = ContactUs
    form_class = ContactUsModelForm
    success_url = '/contact-us/'

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        setting : SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        context['site_setting'] = setting
        return context

