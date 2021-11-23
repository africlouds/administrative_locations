# Copyright (c) 2021, Africlouds Ltd and contributors
# For license information, please see license.txt

import frappe
from frappe.utils.nestedset import NestedSet


class AdministrativeLocation(NestedSet):
    def autoname(self):
        if self.parent_administrative_location:
            parent_location = frappe.get_doc(
                "Administrative Location", self.parent_administrative_location)
            self.name = self.location_name + \
                " (%s)" % parent_location.location_name
        else:
            self.name = self.location_name
