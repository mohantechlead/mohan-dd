from ninja import Router
from typing import List
from django.shortcuts import get_object_or_404
from .models import GRN, GrnItems, DN, DNItems
from .schemas import GrnCreateSchema, GrnDetailSchema, GRNListSchema 
from .schemas import DnCreateSchema, DnDetailSchema, DNListSchema 
import uuid

router = Router()


@router.post("/grn/create", response=GrnDetailSchema)
def create_grn(request, payload: GrnCreateSchema):

    # Create GRN
    grn = GRN.objects.create(
        id=uuid.uuid4(),
        supplier_name=payload.supplier_name,
        grn_no=payload.grn_no,
        plate_no=payload.plate_no,
        purchase_no=payload.purchase_no,
    )

    # Create Items
    created_items = []
    for item in payload.items:
        new_item = GrnItems.objects.create(
            item_id=uuid.uuid4(),
            grn=grn,
            item_name=item.item_name,
            quantity=item.quantity,
            unit_measurement=item.unit_measurement,
            internal_code = item.internal_code
        )
        created_items.append(new_item)

    # Return structured response
    return {
        "id": grn.id,
        "supplier_name": grn.supplier_name,
        "grn_no": grn.grn_no,
        "plate_no": grn.plate_no,
        "purchase_no": grn.purchase_no,
        "items": created_items
    }

@router.get("", response=List[GRNListSchema])
def list_GRN(request):
    qs = GRN.objects.all()
    return qs

@router.get("/grn/{grn_no}", response=GrnDetailSchema)
def get_GRN(request, grn_no: str):
    return get_object_or_404(GRN, grn_no=grn_no)


# Add more endpoints as needed for DN and other functionalities

@router.post("/dn/create", response=DnDetailSchema)
def create_dn(request, payload: DnCreateSchema):

    # Create DN
    dn = DN.objects.create(
        id=uuid.uuid4(),
        customer_name=payload.customer_name,
        dn_no=payload.dn_no,
        plate_no=payload.plate_no,
        sales_no=payload.sales_no,
    )

    # Create Items
    created_items = []
    for item in payload.items:
        new_item = DNItems.objects.create(
            item_id=uuid.uuid4(),
            dn=dn,
            item_name=item.item_name,
            quantity=item.quantity,
            unit_measurement=item.unit_measurement,
            internal_code = item.internal_code
        )
        created_items.append(new_item)

    # Return structured response
    return {
        "id": dn.id,
        "customer_name": dn.customer_name,
        "dn_no": dn.dn_no,
        "plate_no": dn.plate_no,
        "sales_no": dn.sales_no,
        "items": created_items
    }

@router.get("/dn/list", response=List[DNListSchema])
def list_DN(request):
    qs = DN.objects.all()
    return qs

@router.get("/dn/{dn_no}", response=DnDetailSchema)
def get_DN(request, dn_no: str):
    return get_object_or_404(DN, dn_no=dn_no)

