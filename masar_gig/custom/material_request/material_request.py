import frappe


@frappe.whitelist()
def get_emp(user):
    emp_sql = frappe.db.sql("""
            SELECT name FROM tabEmployee WHERE user_id = %s
        """, (user), as_dict=True)
    
    if emp_sql and emp_sql[0] and emp_sql[0]['name']:
        return emp_sql[0]['name']