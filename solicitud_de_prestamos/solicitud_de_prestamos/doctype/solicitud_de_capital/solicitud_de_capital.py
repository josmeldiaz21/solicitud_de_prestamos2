# -*- coding: utf-8 -*-
# Copyright (c) 2019, Josmel Diaz and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class SolicituddeCapital(Document):
	def on_submit(self):
		asiento = frappe.new_doc("Journal Entry")
		asiento.prestamo = self.name
		'''asiento["accounts"][0] = "1110 - Efectivo - JD"'''
		asiento.save()