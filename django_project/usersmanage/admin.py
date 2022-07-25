from django.contrib import admin

from .models import User, Item, Purchase, Referral


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "name", "username")


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category_name", "subcategory_name")


@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    list_display = ("id", "referrer_id")


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("id", "buyer", "item_id", "quantity", "receiver", "successful")