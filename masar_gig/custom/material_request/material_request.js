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
                var emp_name = r.message;

                frm.doc.custom_requester = emp_name;
                frm_refresh_field("custom_requester");
            }
        }
    });
  }

  function setReadOnly(frm) {
    if (frm.doc.workflow_state == "Draft") {
        frappe.call({
            method: "masar_gig.custom.material_request.material_request.get_manager",
            callback: function(r) {
                if (r.message) {
                    var manager_user = r.message;
                    if (frappe.session.user != manager_user) {
                        frm.set_read_only(true);
                    }
                }
            }
        });
    }
  }
  ////