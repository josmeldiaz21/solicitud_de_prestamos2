from __future__ import unicode_literals

from frappe import _


def get_data():
	return {
		'heatmap': False,
		'heatmap_message': _('This is based on transactions against this Customer. See timeline below for details'),
		'fieldname': 'desembolso',
		'transactions': [
			{
				'label': _('Solicitudes de Capital'),
				'items': ['Solicitud de Capital']
			}
		]
	}