# -*- coding: utf-8 -*-
# Copyright (c) 2019, Josmel Diaz and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import nowdate

class SolicituddeCapital(Document):
	def on_submit(self):
		asiento = frappe.new_doc("Journal Entry")
		asiento.prestamo = self.name
		asiento.posting_date = nowdate()
		asiento.append("accounts",{
			"account": "1110 - Efectivo - JD",
			"debit_in_account_currency": "200"
			})
		asiento.append("accounts",{
			"account": "4110 - Ventas - JD",
			"credit_in_account_currency": "200"
			})
		asiento.save()
		asiento.submit()