#!/usr/bin/env python
# encoding: utf-8
"""
parsing.py

Created by Thomas Mangin on 2009-09-06.
Copyright (c) 2009-2015 Exa Networks. All rights reserved.
"""

import unittest

import os
import sys
import glob

from exabgp.configuration.current import Configuration
from exabgp.configuration.check import check_neighbor

from exabgp.configuration.setup import environment
env = environment.setup('')
env.log.enable = True
env.log.all = False
env.log.configuration = False
env.log.parser = False

class TestControl (unittest.TestCase):
	def setUp (self):
		location = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','conf','*.conf'))
		self.files = glob.glob(location)

	# These files contains invalid attribute we can not parse
	skip = 'attributes.conf'

	def test_all_configuration (self):
		for filename in self.files:
			if filename.endswith(self.skip):
				continue
			print '-'*80
			print filename
			print '='*80
			sys.stdout.flush()
			configuration = Configuration([filename,])
			configuration.reload()
			self.assertEqual(check_neighbor(configuration.neighbor),True)
			del configuration

if __name__ == '__main__':
	unittest.main()
