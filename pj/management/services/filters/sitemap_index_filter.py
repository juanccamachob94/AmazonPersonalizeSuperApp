from pj.helpers.list_helper import ListHelper

class SitemapIndexFilter:
    @classmethod
    def perform(cls, data_list, lastmod, data_type):
        # returns an array of OrderedDict instances
        if data_type == 'first':
            return ListHelper.compact([cls.__first_by_lastmod(data_list, lastmod)])
        elif data_type == 'last':
            return ListHelper.compact([cls.__last_by_lastmod(data_list, lastmod)])
        return cls.__list_by_lastmod(data_list, lastmod)


    @classmethod
    def __list_by_lastmod(cls, data_list, lastmod):
        """
            lastmod represents a date when the resource was modified
            lastmod is a <str> that allows the next formats:
            aaaa-mm- => 2021-09-
            aaaa-mm-dd => 2021-09-03
            aaaa-mm-ddThh:mm-ss:mmmm => 2021-09-03T10:20-05:00
        """
        return list(filter(lambda sitemap: cls.__is_valid_sitemap(sitemap, lastmod), data_list))


    @classmethod
    def __first_by_lastmod(cls, data_list, lastmod):
        # first in the list based on the xml file location
        lastmod_list = cls.__list_by_lastmod(data_list, lastmod)
        return lastmod_list[0] if len(lastmod_list) else None


    @classmethod
    def __last_by_lastmod(cls, data_list, lastmod):
        # last in the list based on the xml file locations
        lastmod_list = cls.__list_by_lastmod(data_list, lastmod)
        return lastmod_list[len(lastmod_list) - 1] if len(lastmod_list) else None


    @classmethod
    def __is_valid_sitemap(cls, sitemap, lastmod):
        sitemap_loc = sitemap.get('loc')
        return sitemap_loc and sitemap_loc.endswith(''.join([lastmod, '.xml']))
