frappe.ui.form.on('Material Request', {
    refresh: function(frm) {
        if (frm.doc.__islocal == 1) {
            setDefaultRequester(frm);
        }

        // if (frm.doc.docstatus == 1) {
            addSQItems(frm);
        // }
    },
    onload: function(frm) {
        if (frm.doc.__islocal == 1) {
            setDefaultRequester(frm);
        }

        // if (frm.doc.docstatus == 1) {
            addSQItems(frm);
        // }
    }
  });

  function setDefaultRequester(frm) {
    frappe.call({
        method: "masar_gig.custom.material_request.material_request.get_emp",
        args: {
            user: frappe.session.user
        },
        callback: function(r) {
            if (r.message) {
                console.log(r.message);
                var emp_name = r.message;
                console.log("Test 1", emp_name);
                frappe.model.set_value(frm.doc.doctype, frm.doc.name, "custom_requester", emp_name);
                frm.refresh_field("custom_requester");
                console.log("Test 2", frm.doc.custom_requester);
            }
        }
    });
  }


  function addSQItems(frm) {
    if (!frm.doc.custom_prices_inquiry && frm.doc.docstatus == 0) {
        frm.add_custom_button(__('Get Items from Supplier Quotation'), function () {
            frappe.call({
                method: 'masar_gig.custom.material_request.material_request.get_supplier_quotation',
                args: { mr_name: frm.doc.name },
                callback: function (r) {
                    if (r.message && r.message.length) {
                        let dialog = new frappe.ui.Dialog({
                            title: __('Select Supplier Quotation'),
                            fields: [
                                {
                                    fieldtype: 'Link',
                                    fieldname: 'sq_name',
                                    label: __('Supplier Quotation'),
                                    options: 'Supplier Quotation',
                                    reqd: 1,
                                    get_query: function() {
                                        return {
                                            filters: { docstatus: 1 }
                                        };
                                    }
                                }
                            ],
                            primary_action_label: __('Select The Supplier Quotation'),
                            primary_action: function () {
                                let selected_data = dialog.get_values();
                                if (!selected_data || !selected_data.sq_name) {
                                    frappe.msgprint(__('Please select a Supplier Quotation.'));
                                    return;
                                }

                                frappe.call({
                                    method: "masar_gig.custom.material_request.material_request.get_sq_items",
                                    args: { sq: selected_data.sq_name },
                                    callback: function (r) {
                                        if (r.message && r.message.length) {
                                            frm.clear_table("items");
                                            r.message.forEach(item => {
                                                let child = frm.add_child("items");
                                                Object.assign(child, item);
                                            });
                                            frm.refresh_field("items");
                                            dialog.hide();
                                            frm.save();
                                        } else {
                                            frappe.msgprint(__('No items found in the selected Supplier Quotation.'));
                                        }
                                    }
                                });
                            }
                        });

                        dialog.show();
                    } else {
                        frappe.msgprint(__('No Supplier Quotations available.'));
                    }
                }
            });
        });
    }
}

