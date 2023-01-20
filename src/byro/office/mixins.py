from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class TransactionMixin:
    def add_or_update_transaction(self, form, t, action):

        arguments = dict(
            memo=form.cleaned_data["memo"],
            account=form.cleaned_data["account"],
            member=form.cleaned_data["member"],
            user_or_context=self,
        )
        if form.cleaned_data["debit_value"]:
            t.debit(amount=form.cleaned_data["debit_value"], **arguments)
        if form.cleaned_data["credit_value"]:
            t.credit(amount=form.cleaned_data["credit_value"], **arguments)

        t.save()

        messages.success(self.request, _("The transactions was created/updated."))
        t.log(self, action)
