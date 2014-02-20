from cms.utils.compat.dj import python_2_unicode_compatible
from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin
from cms.plugins.vzaar import settings
from os.path import basename

@python_2_unicode_compatible
class Vzaar(CMSPlugin):
    # Vzaar player settings
    vzaar_video_name = models.CharField(_('video Name'), max_length=250,blank=True, null=True)
    vzaar_video_id = models.CharField(_('video ID'), max_length=50, help_text=_('Numeric ID from Vzaar'), blank=True, null=True)
    vzaar_video_alt = models.CharField(_('video Alt Text'), max_length=250, help_text=_('Video Alt Text'), blank=True, null=True)
    vzaar_video_height = models.PositiveSmallIntegerField(_('Video Height'))
    vzaar_video_width = models.CharField(_('Video Width'), max_length=50, help_text=_('Numeric or Percentage'), blank=True, null=True)

    #Default Values for Output
    def __str__(self):
        if self.vzaar_video_name:
            name = self.vzaar_video_name
        return u"%s" % basename(name)

    def get_height(self):
        if self.vzaar_video_height:
            height = self.vzaar_video_height
        else:
            height = "389"
        return "%s" % (height)
    
    def get_width(self):
        if self.vzaar_video_width:
            width = self.vzaar_video_width
        else:
            width = "100%"
        return "%s" % (width)
    
    def get_alt(self):
        return u"%s" % (self.vzaar_video_alt)

    def get_id(self):
        return "%s" % (self.vzaar_video_id)

