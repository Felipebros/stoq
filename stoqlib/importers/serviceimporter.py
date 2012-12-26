# -*- coding: utf-8 -*-
# vi:si:et:sw=4:sts=4:ts=4

##
## Copyright (C) 2007-2008 Async Open Source
##
## This program is free software; you can redistribute it and/or
## modify it under the terms of the GNU Lesser General Public License
## as published by the Free Software Foundation; either version 2
## of the License, or (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU Lesser General Public License for more details.
##
## You should have received a copy of the GNU Lesser General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., or visit: http://www.gnu.org/.
##
##
## Author(s): Stoq Team <stoq-devel@async.com.br>
##
##

from stoqdrivers.enum import TaxType

from stoqlib.database.runtime import get_default_store
from stoqlib.domain.service import Service
from stoqlib.domain.sellable import (Sellable,
                                     SellableTaxConstant)
from stoqlib.importers.csvimporter import CSVImporter


class ServiceImporter(CSVImporter):
    fields = ['description',
              'barcode',
              'price',
              'cost',
              ]

    def __init__(self):
        super(ServiceImporter, self).__init__()
        store = get_default_store()
        self.tax_constant = SellableTaxConstant.get_by_type(
            TaxType.SERVICE, store)
        assert self.tax_constant

    def process_one(self, data, fields, trans):
        tax = trans.get(self.tax_constant)
        sellable = Sellable(connection=trans,
                            tax_constant=tax,
                            description=data.description,
                            price=int(data.price),
                            cost=int(data.cost),
                            code=data.barcode,
                            barcode=data.barcode)
        Service(sellable=sellable,
                connection=trans)
