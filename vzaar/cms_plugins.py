from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.utils.translation import ugettext_lazy as _
from cms.plugins.vzaar import settings
from cms.plugins.vzaar.models import Vzaar
from cms.plugins.vzaar.forms import VzaarForm

class VzaarPlugin(CMSPluginBase):
    model = Vzaar
    name = _("Vzaar")
    form = VzaarForm
    
    render_template = "cms/plugins/vzaar.html"
    
    general_fields = [
        ('vzaar_video_name', 'vzaar_video_id'),
        'vzaar_video_alt',
        ('vzaar_video_height', 'vzaar_video_width')
    ]

    fieldsets = [
        (None, {
            'fields': general_fields,
        }),
    ]

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder':placeholder,
        })
        return context
    
plugin_pool.register_plugin(VzaarPlugin)