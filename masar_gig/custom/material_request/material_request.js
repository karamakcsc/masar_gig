frappe.ui.form.on('Material Request', {
    refresh: function(frm) {
        setDefaultRequester(frm);
        setReadOnly(frm);
    },
    setup: function(frm) {
        setDefaultRequester(frm);
        setReadOnly(frm);
    },
    onload: function(frm) {
        setDefaultRequester(frm);
        setReadOnly(frm);
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

  function setReadOnly(frm) {
    if (frm.doc.workflow_state == "Manager Approval") {
        if (!frappe.user.has_role('Request Approver')) {
            frm.set_read_only(true);
        }
    }
  }
  ////