from django.contrib import admin
from django.shortcuts import redirect
from admin_views.admin import AdminViews
from analytics.models import *

class FacebookStatInline(admin.StackedInline):
    model = FacebookStat

class LinkedinStatInline(admin.StackedInline):
    model = LinkedinStat

class GoogleAdWordsStatInline(admin.StackedInline):
    model = GoogleAdWordsStat

class SaleOportunityAdmin(admin.ModelAdmin):
    model = SaleOportunity

class StatRegisterAdmin(AdminViews):
    raw_id_fields = ('ad',)
    inlines = [
        FacebookStatInline, GoogleAdWordsStatInline, LinkedinStatInline,
    ]
    #model = StatRegister
    admin_views = (
                    ('Redirect to CNN', 'redirect_to_cnn'),
                    ('Go to revsys.com', 'http://www.revsys.com'),
        )

    def redirect_to_cnn(self, *args, **kwargs):
        return redirect('http://www.cnn.com')

admin.site.register(SaleOportunity)
admin.site.register(StatRegister, StatRegisterAdmin)
