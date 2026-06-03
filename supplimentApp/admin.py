from django.contrib import admin
from supplimentApp.models import *

# Register your models here.

class OrdersInline(admin.TabularInline):
    model = Orders
    extra = 0
    fields = (
        "product",
        "quantity",
        "status",
        "price",
        "is_active",
        "created_at",
    )
    
    readonly_fields = (
        "updated_at",
    )


# ---------- USER TYPE ADMIN ----------

@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "is_active",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "name",
    )

    list_filter = (
        "is_active",
        "created_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = ("-created_at",)


# ---------- PRODUCT ADMIN ----------

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "product_id",
        "name",
        "is_active",
        "created_at",
    )

    search_fields = (
        "name",
    )

    list_filter = (
        "is_active",
        "created_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = ("-created_at",)


# ---------- CUSTOMER ADMIN ----------

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = (
        "user_id",
        "name",
        "product",
        "price",
        "is_active",
        "created_at",
    )

    search_fields = (
        "name",
        "product__name",
    )

    list_filter = (
        "product",
        "is_active",
        "created_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    autocomplete_fields = (
        "product",
    )

    ordering = ("-created_at",)

    inlines = [OrdersInline]


# ---------- ORDERS ADMIN ----------

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):

    list_display = (
        "order_id",
        "user",
        "product",
        "quantity",
        "status",
        "price",
        "is_active",
        "is_deleted",
        "created_at",
    )

    search_fields = (
        "order_id",
        "user__name",
        "product__name",
    )

    list_filter = (
        "status",
        "is_active",
        "is_deleted",
        "created_at",
        "product",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    autocomplete_fields = (
        "user",
        "product",
    )

    ordering = ("-created_at",)

    list_editable = (
        "status",
        "is_active",
        "is_deleted",
    )