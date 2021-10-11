#-*- coding:utf-8 -*-

import unittest
from django.test import TestCase
from sptrans import SPTransClient

class TesteSPTransClient(TestCase):

    def test_auth_true(self):

        client = SPTransClient()
        self.assertEqual(client.auth(), True)

    def test_auth_false(self):

        client = SPTransClient()
        client.token = '000'

        self.assertEqual(client.auth(), False)
