# -*- coding: utf-8 -*-

"""sysdescrparser.huawei."""

from sysdescrparser.sysdescr import SysDescr


# pylint: disable=no-name-in-module
class Huawei(SysDescr):

    """Class Huawei.

    This class is only for vendor definition.

    """

    def __init__(self, raw):
        """Constructor."""
        super(Huawei, self).__init__(raw)
        self.vendor = 'HUAWEI'
        self.model = self.UNKNOWN
        self.os = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parsing for sysDescr value."""
        return self
