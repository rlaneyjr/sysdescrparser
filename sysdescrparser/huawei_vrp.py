# -*- coding: utf-8 -*-

"""sysdescrparser.cisco_vrp."""


import re
from sysdescrparser.huawei import Huawei


# pylint: disable=no-member
class HuaweiVRP(Huawei):

    """Class HuaweiVRP.

    SNMP sysDescr for HuaweiVRP.

    """

    def __init__(self, raw):
        """Constructor."""
        super(HuaweiVRP, self).__init__(raw)
        self.os = 'VRP'
        self.model = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parse."""
        regex = (r'Huawei Versatile Routing Platform Software.*\n'
                 r'VRP.*\((.*) (.*)\).*\n'
                 r'.*\n'
                 r'.*')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            self.model = res.group(1)
            self.version = res.group(2)
            return self

        regex = (r'S[5-6]7\d\d-.*\nHuawei Versatile Routing Platform Software.*\n VRP.*\((.*) (.*)\).*\n Copyright.*')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            self.model = res.group(1)
            self.version = res.group(2)
            return self

        return False
