// Copyright (c) 2019, Josmel Diaz and contributors
// For license information, please see license.txt

frappe.ui.form.on("Solicitud de Capital", "desembolso",
    function(frm) {
        frappe.call({
            "method": "frappe.client.get",
            args: {
                doctype: "Desembolsos",
                name: frm.doc.desembolso
            },
            callback: function (data) {
                frappe.model.set_value(frm.doctype,
                    frm.docname, "id_de_desembolso",
                    data.message.id_de_desembolso)
            }
        })
    });
frappe.ui.form.on('Solicitud de Capital', {
    refresh: function(frm) {
      frm.add_custom_button(__('Pago'), function(){
        frappe.msgprint(frm.doc.email);
    }, __("Make"));
  }
});

