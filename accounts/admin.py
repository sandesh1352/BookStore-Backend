from django.contrib import admin
from . models import Customer, OTP
from .forms import CustomerCreationForm
from django.contrib.auth.admin import UserAdmin


class CustomerAdmin(UserAdmin):
    model = Customer
    add_form = CustomerCreationForm
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Customer Phone Number',
            {
                'fields': (
                    'phone_number',
                )
            }
        )
    )

    list_display = ("id", "username", "first_name", "last_name",
                    "phone_number", "email", "is_staff", "is_superuser")


class OTPAdmin(admin.ModelAdmin):
    list_display = ("id", "phone_number", "otp", "is_verfied")


admin.site.register(Customer, CustomerAdmin)
admin.site.register(OTP, OTPAdmin)
