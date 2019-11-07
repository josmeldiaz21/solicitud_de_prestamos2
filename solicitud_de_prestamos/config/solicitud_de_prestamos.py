from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
      {
        "label":_("Solicitud de Prestamos"),
        "icon": "octicon octicon-flame",
        "items": [
            {
              "type": "doctype",
              "name": "Solicitud de Capital",
              "label": _("Solicitud de Capital"),
              "description": _("Crear un nuevo prestamo"),
            },
            {
              "type": "doctype",
              "name": "Desembolsos",
              "label": _("Entrega de Dinero"),
              "description": _("Entrega de Dinero a cliente"),
            }
          ]
      }
  ]
