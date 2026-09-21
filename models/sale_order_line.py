import base64
import io
from PIL import Image
from odoo import models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def _get_product_image_png_data_uri(self):
        """Devuelve la imagen del producto en base64 con formato PNG compatible con wkhtmltopdf."""
        self.ensure_one()
        if not self.product_id or not self.product_id.image_128:
            return False
        try:
            if 'WEBP' not in Image.ID:
                Image._initialized = 0
                Image.init()
            raw_data = base64.b64decode(self.product_id.image_128)
            with Image.open(io.BytesIO(raw_data)) as img:
                if img.mode not in ('RGB', 'RGBA'):
                    img = img.convert('RGBA')
                output = io.BytesIO()
                img.save(output, format='PNG')
                png_bytes = output.getvalue()
                return 'data:image/png;base64,' + base64.b64encode(png_bytes).decode('utf-8')
        except Exception:
            return False
