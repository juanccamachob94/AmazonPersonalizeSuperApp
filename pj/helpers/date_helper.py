import pytz
import time

from datetime import datetime
from datetime import timedelta

class DateHelper:
    CMT_FORMAT = '%Y-%m-%dT%H:%M:%S%z'
    GMT_FORMAT = '%a, %d %b %Y %H:%M:%S%z'

    @classmethod
    def round_time(cls):
        return round(time.time())


    @classmethod
    def cmtstr_to_datetime(cls, cmtstr):
        # expected parameter value (example): 2019-06-22T11:03:00-05:00
        return datetime.strptime(cmtstr, cls.CMT_FORMAT)


    @classmethod
    def gmtstr_to_datetime(cls, gmtstr):
        return datetime.strptime(cls.gmt_replace(gmtstr, False), cls.GMT_FORMAT)

    @classmethod
    def ago(cls, **time_delta):
        tz = pytz.timezone('America/Mexico_City')
        delta = timedelta(
            days=time_delta.get('days', 0),
            hours=time_delta.get('hours', 0)
        )
        return cls.cmtstr_to_datetime(tz.localize(datetime.now() - delta).strftime(cls.CMT_FORMAT))


    @classmethod
    def gmt_replace(cls, str_date, replace_type=True):
        if replace_type:
            return str_date.replace('-0600', ' GMT-6').replace('-0500', ' GMT-5')
        return str_date.replace(' GMT-6', '-06:00').replace(' GMT-5', '-05:00')
