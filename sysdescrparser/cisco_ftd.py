# -*- coding: utf-8 -*-

"""sysdescrparser.cisco_iosxe."""

import re
from sysdescrparser.cisco import Cisco


# pylint: disable=no-member
class CiscoFTD(Cisco):
    """Class CiscoFTD.

    SNMP sysDescr for CiscoFTD.

    """

    def __init__(self, raw):
        """Constructor."""
        super(CiscoFTD, self).__init__(raw)
        self.os = 'FTD'
        self.model = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parse.
        Cisco FirePOWER FPR-2140 Security Appliance, System Version 2.10(1.175)
        Cisco Firepower Threat Defense, Version 7.2.5.2 (Build 4), ASA Version 9.18(3)61
        """
        regex = (r'Cisco FirePOWER (\w+-\d+)\s'
                 r'Version (\d.*)')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            self.model = res.group(1)
            self.version = res.group(2)
            return self

        regex = (r'Cisco Firepower Threat Defense, Version (\d.*),'
                 r'ASA Version (\d.*)')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            self.model = res.group(1)
            self.version = res.group(2)
            return self

        return False



