app_name = "masar_gig"
app_title = "Masar GIG"
app_publisher = "KCSC"
app_description = "Masar GIG"
app_email = "info@kcsc.com.jo"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "masar_gig",
# 		"logo": "/assets/masar_gig/logo.png",
# 		"title": "Masar GIG",
# 		"route": "/masar_gig",
# 		"has_permission": "masar_gig.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/masar_gig/css/masar_gig.css"
# app_include_js = "/assets/masar_gig/js/masar_gig.js"

# include js, css files in header of web template
# web_include_css = "/assets/masar_gig/css/masar_gig.css"
# web_include_js = "/assets/masar_gig/js/masar_gig.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "masar_gig/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Material Request" : "custom/material_request/material_request.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "masar_gig/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "masar_gig.utils.jinja_methods",
# 	"filters": "masar_gig.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "masar_gig.install.before_install"
# after_install = "masar_gig.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "masar_gig.uninstall.before_uninstall"
# after_uninstall = "masar_gig.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "masar_gig.utils.before_app_install"
# after_app_install = "masar_gig.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "masar_gig.utils.before_app_uninstall"
# after_app_uninstall = "masar_gig.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "masar_gig.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Material Request": {
		"validate": "masar_gig.custom.material_request.material_request.validate",
        "on_update": "masar_gig.custom.material_request.material_request.on_update"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"masar_gig.tasks.all"
# 	],
# 	"daily": [
# 		"masar_gig.tasks.daily"
# 	],
# 	"hourly": [
# 		"masar_gig.tasks.hourly"
# 	],
# 	"weekly": [
# 		"masar_gig.tasks.weekly"
# 	],
# 	"monthly": [
# 		"masar_gig.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "masar_gig.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "masar_gig.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "masar_gig.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["masar_gig.utils.before_request"]
# after_request = ["masar_gig.utils.after_request"]

# Job Events
# ----------
# before_job = ["masar_gig.utils.before_job"]
# after_job = ["masar_gig.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"masar_gig.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

fixtures = [
    {"dt": "Custom Field", "filters": [
        [
            "name", "in", [
                "Material Request-custom_section_break_nbpmo",
                "Material Request-custom_requester",
                "Material Request-custom_column_break_upw6h",
                "Material Request-custom_full_name",
                "Material Request-custom_reports_to",
                "Material Request-custom_manager_name",
                "Material Request-custom_department",
                "Material Request-custom_justification",
                "Material Request-custom_priority",
                "Material Request-custom_prices_inquiry",
                "Material Request-custom_total",
                "Material Request Item-custom_supplier_quotation_item",
                "Material Request Item-custom_supplier_quotation"
            ]
        ]
    ]}
]