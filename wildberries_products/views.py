from io import BytesIO

import openpyxl
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .parser import wildberries_parser
from .serializers import UploadExelSerializer


class UploadExelViewSet(ViewSet):
    serializer_class = UploadExelSerializer

    def list(self, request):
        return Response("Chose the xlsx file")

    def create(self, request):
        file_uploaded = request.FILES.get("file")
        file_name = file_uploaded.name
        if not file_name.endswith(".xlsx"):
            return Response(
                f"Error. The file must have the xlsx extension. You have uploaded {file_name}"
            )
        try:
            file_data_binary = file_uploaded.read()
            book = openpyxl.open(filename=BytesIO(file_data_binary))
            sheet = book.active
            rows_count = sheet.max_row
            articles = []
            for row_index in range(1, rows_count + 1):
                cell_value = sheet[row_index][0].value
                if isinstance(cell_value, int):
                    articles.append(cell_value)
            products_data = wildberries_parser(articles)
            if len(products_data) == 1:
                data = products_data[0]
            elif len(products_data) == 0:
                data = "No results"
            else:
                data = products_data
            return Response(data)
        except Exception:
            return Response("File data is not valid")


def main_page(request):
    return redirect("upload-list")
