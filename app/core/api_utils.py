from rest_framework import status
from core.models import Item
import json
import os


class FilteredListMixin(object):

    LOOKUP_PARAM = '_filter'

    class Meta:
        abstract = True

    @classmethod
    def filter_qs(cls, request, qs):
        try:
            body = json.loads(request.body.strip())
            print(body)
        except Exception:
            body = {}

        if FilteredListMixin.LOOKUP_PARAM not in body:
            return qs, status.HTTP_200_OK

        try:
            return qs.filter(**body[FilteredListMixin.LOOKUP_PARAM]), status.HTTP_200_OK
        except Exception:
            return None, status.HTTP_400_BAD_REQUEST


def get_filepath_and_extension(filepath):
    source, extension = os.path.splitext(str(filepath))

    formats = [extension, ]
    if extension in (".jpg", ".png"):
        if os.path.exists(source + ".webp"):
            formats.append(".webp")
    return {"path": source, "formats": formats}


def get_status_description(status: int):
    for st_id, st_desc in Item.STATUS_OPTS:
        if st_id == status:
            return {"status_id": st_id, "status_description": st_desc}
    return None


def get_image_json(item: Item):
    if not item.image:
        return {}

    if not item.image.path:
        return {}

    return get_filepath_and_extension(item.image.path)
