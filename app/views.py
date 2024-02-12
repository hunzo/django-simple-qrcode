import base64
from io import BytesIO
from uuid import uuid4

from django.shortcuts import render
from qrcode import QRCode


def Home(request):
    qr = QRCode(version=1, box_size=15, border=1)

    data = str(uuid4())

    qr.add_data(data)
    qr.make(fit=True)

    # img = qr.make_image(fill_color="black", back_color="white")
    img = qr.make_image()

    buffer = BytesIO()
    img.save(buffer)
    img_str = base64.b64encode(buffer.getvalue()).decode()
    dataUrls = f"data:image/png;base64,{img_str}"

    context = {
        "img": dataUrls,
        "data": data
    }

    return render(request, 'index.html', context)
