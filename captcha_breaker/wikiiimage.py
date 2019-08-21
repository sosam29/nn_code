from PIL import Image
from io import BytesIO
import requests

response = requests.get("http://www.gucci.com/images/ecommerce/styles_new/201501/web_full/277520_F4CYG_4080_001_web_full_new_theme.jpg")
bytes = BytesIO(response.content)
image = Image.open(bytes)
image.save("1.jpg")