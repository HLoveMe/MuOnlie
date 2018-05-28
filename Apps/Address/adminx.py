"""
    author:ZZH
    git:HLoveMe
    date:2018/5/28 下午3:22
"""

import xadmin
from .models import Country,Province,City,Town,Village


class CountryAdmin(object):
    pass


class ProvinceAdmin(object):
    search_fields = ["name"]
    show_detail_fields = ["name", "desc"]
    pass


class CityAdmin(object):

    pass


class TownAdmin(object):
    pass


class VillageAdmin(object):
    pass


xadmin.site.register(Country,CountryAdmin)
xadmin.site.register(Province,ProvinceAdmin)
xadmin.site.register(City,CityAdmin)
xadmin.site.register(Town,TownAdmin)
xadmin.site.register(Village,VillageAdmin)
