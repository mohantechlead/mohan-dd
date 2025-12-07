from django.db import models
import uuid

# Create your models here.
class GRN(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    supplier_name = models.CharField(max_length=255)
    grn_no = models.CharField(max_length=255)
    plate_no = models.CharField(max_length=255)
    purchase_no = models.CharField(max_length=255)
    date = models.DateField(null=False, blank=False, auto_now = True)
    ECD_no = models.CharField(max_length=255, blank=True, null=True)
    transporter_name = models.CharField(max_length=255, blank=True, null=True)
    storekeeper_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.grn_no} ({self.supplier_name})"

class GrnItems(models.Model):
    item_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    grn = models.ForeignKey(GRN, on_delete=models.CASCADE, related_name='items')
    item_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    unit_measurement = models.CharField(max_length=100)
    internal_code = models.CharField(max_length=100, blank=True, null=True)
    bags = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.grn} - {self.item_name} "

class DN(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    customer_name = models.CharField(max_length=255)
    dn_no = models.CharField(max_length=255, unique=True)
    plate_no = models.CharField(max_length=255)
    sales_no = models.CharField(max_length=255)
    date = models.DateField(null=False, blank=False, auto_now=True)
    ECD_no = models.CharField(max_length=255, blank=True, null=True)
    transporter_name = models.CharField(max_length=255, blank=True, null=True)
    storekeeper_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.dn_no} ({self.customer_name})"

class DNItems(models.Model):
    item_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    dn = models.ForeignKey(DN, on_delete=models.CASCADE, related_name='dn_items')
    item_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    unit_measurement = models.CharField(max_length=100)
    internal_code = models.CharField(max_length=100, blank=True, null=True)
    bags = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.dn} - {self.item_name} "

