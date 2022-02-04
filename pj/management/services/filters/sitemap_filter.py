from pj.helpers.date_helper import DateHelper

class SitemapFilter:
    LIMIT_DATE = None # depends of execution intervals

    @classmethod
    def perform(cls, data_list, data_type):
        if data_type == 'news':
            return cls.__news_list(data_list)
        elif data_type == 'videos':
            return cls.__video_list(data_list)
        return data_list


    @classmethod
    def __news_list(cls, data_list):
        return list(
            filter(lambda item: cls.__is_valid_item(item, 'news'), data_list)
        )


    @classmethod
    def __video_list(cls, data_list):
        return list(
            filter(lambda item: cls.__is_valid_item(item, 'video'), data_list)
        )


    @classmethod
    def __is_valid_item(cls, item, expected_type):
        label = ''.join([expected_type, ':', expected_type])
        str_publication_date = item.get(label, {}) \
            .get(''.join([expected_type, ':publication_date']))
        return str_publication_date \
            and (
                not(cls.LIMIT_DATE) \
                    or DateHelper.cmtstr_to_datetime(str_publication_date) >= cls.LIMIT_DATE
                )
