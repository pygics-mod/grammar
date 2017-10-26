# -*- coding: utf-8 -*-
'''
Created on 2017. 6. 12.
@author: HyechurnJang
'''

import re

class Network:

    @classmethod
    def isIP(cls, ip):
        kv = re.match('\s*(?P<ip>\d\d?\d?\.\d\d?\d?\.\d\d?\d?\.\d\d?\d?)', ip)
        if kv != None: return kv.group('ip')
        return None
    
    @classmethod
    def isMAC(cls, mac):
        kv = re.match('\s*(?P<mac>\w\w\:\w\w\:\w\w\:\w\w\:\w\w\:\w\w)', mac)
        if kv != None: return kv.group('mac').lower()
        return None
    
    @classmethod
    def isCIDR(cls, net):
        kv = re.match('\s*(?P<net>\d\d?\d?\.\d\d?\d?\.\d\d?\d?\.\d\d?\d?)/(?P<prefix>\d\d?)', net)
        if kv != None: return kv.group('net'), kv.group('prefix')
        return None, None