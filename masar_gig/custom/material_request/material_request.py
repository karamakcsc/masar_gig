import frappe


@frappe.whitelist()
def get_emp(user):
    emp_sql = frappe.db.sql("""
            SELECT reports_to FROM tabEmployee WHERE user_id = %s
        """, (user), as_dict=True)
    
    if emp_sql and emp_sql[0] and emp_sql[0]['name']:
        return emp_sql[0]['name']
    
def get_manager():
    manager_name = get_emp(user=frappe.session.user)
    manager_sql = frappe.db.sql("""
            SELECT user_id FROM tabEmployee WHERE name = %s
        """, (manager_name), as_dict=True)
    
    if manager_sql and manager_sql[0] and manager_sql[0]['user_id']:
        return manager_sql[0]['user_id']