#curl -o image.jpeg https://t0.gstatic.com/licensed-image?q=tbn:ANd9GcQ_Kevbk21QBRy-PgB4kQpS79brbmmEG7m3VOTShAn4PecDU5H5UxrJxE3Dw1JiaG17V88QIol19-3TM2wCHw

import google.generativeai as genai
from PIL import Image

# https://aistudio.google.com/app/apikey
import env 


genai.configure(api_key=env.GOOGLE_API_KEY)

img = Image.open(telegram_img_path)
# img.show()

model = genai.GenerativeModel('gemini-pro-vision')
response = model.generate_content(img)
#print(response.text)

response = model.generate_content(
        [
            telegram_text,
            img
        ],
        stream=True
    )
response.resolve()
print(response.text)