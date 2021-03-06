# -*- coding: utf-8 -*-
# vi:si:et:sw=4:sts=4:ts=4

##
## Copyright (C) 2012 Async Open Source <http://www.async.com.br>
## All rights reserved
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., or visit: http://www.gnu.org/.
##
## Author(s): Stoq Team <stoq-devel@async.com.br>
##

from kiwi.ui.forms import TextField

from stoq.lib.gui.editors.baseeditor import BaseEditorSlave
from stoq.lib.gui.test.uitestutils import GUITest
from stoq.lib.gui.dialogs.loandetails import LoanDetailsDialog
from stoqlib.lib.decorators import cached_property


class _TestSlave(BaseEditorSlave):
    model_type = object

    @cached_property()
    def fields(self):
        return dict(field_name=TextField('Slave field'))


class TestLoanDetails(GUITest):
    def test_create(self):
        loan = self.create_loan()
        self.create_loan_item(loan=loan)

        dialog = LoanDetailsDialog(self.store, loan)
        self.check_dialog(dialog, 'dialog-loan-details-create')

    def test_add_tab(self):
        loan = self.create_loan()
        dialog = LoanDetailsDialog(self.store, loan)
        dialog.add_tab(_TestSlave(self.store, object()), u'Test Tab')
        self.check_dialog(dialog, 'dialog-loan-details-add-tab')
