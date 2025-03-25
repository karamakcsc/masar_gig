import frappe
from frappe import _

def validate(self, method):
    calc_total(self)

@frappe.whitelist()
def get_emp(user):
    emp_sql = frappe.db.sql("""
            SELECT name FROM tabEmployee WHERE user_id = %s
        """, (user), as_dict=True)
    
    if emp_sql and emp_sql[0] and emp_sql[0]['name']:
        return emp_sql[0]['name']
    
@frappe.whitelist()
def get_supplier_quotation(mr_name):
    if mr_name:
        sql = frappe.db.sql("""
                SELECT DISTINCT tsq.name 
                FROM `tabSupplier Quotation` tsq 
                INNER JOIN `tabSupplier Quotation Item` tsqi ON tsqi.parent = tsq.name
                INNER JOIN `tabMaterial Request` tmr ON tsqi.material_request = tmr.name
                WHERE tmr.docstatus = 1 and tsq.docstatus = 1
            """, as_dict=True)
        
        if sql:
            return sql

@frappe.whitelist()
def get_sq_items(sq):
    sq_doc = frappe.get_doc("Supplier Quotation", sq)
    
    item_rates = {item.item_code: {"rate": item.rate, "qty": item.qty, "amount": item.amount, "item_name": item.item_name} 
                  for item in sq_doc.items}
    
    items = []
    for item in sq_doc.items:
        item_dict = {
            "item_code": item.item_code,
            "uom": item.uom,
            "conversion_factor": item.conversion_factor,
            "qty": item.qty,
            "rate": item.rate,
            "item_name": item.item_name,
            "amount": item.amount,
            "custom_supplier_quotation": sq,
            "custom_supplier_quotation_item": item.name
        }
        items.append(item_dict)
    
    return items

def calc_total(self):
    total = 0
    if self.items:
        for item in self.items:
            if hasattr(item, 'custom_supplier_quotation') and item.custom_supplier_quotation:
                sq_item = frappe.db.get_value(
                    "Supplier Quotation Item",
                    item.custom_supplier_quotation_item,
                    ["rate", "amount"],
                    as_dict=True
                )
                if sq_item:
                    item.rate = sq_item.rate
                    item.amount = item.qty * item.rate
            
            if item.amount:
                total += item.amount
                
    self.custom_total = total

def on_update(self, method):
    update_rates_from_sq(self)

def update_rates_from_sq(self):
    """Update rates from supplier quotation after save"""
    if self.items:
        for item in self.items:
            if hasattr(item, 'custom_supplier_quotation') and item.custom_supplier_quotation:
                sq_item = frappe.db.get_value(
                    "Supplier Quotation Item",
                    item.custom_supplier_quotation_item,
                    ["rate"],
                    as_dict=True
                )
                if sq_item:
                    frappe.db.set_value(
                        "Material Request Item",
                        item.name,
                        {
                            "rate": sq_item.rate,
                            "amount": item.qty * sq_item.rate
                        }
                    )
        