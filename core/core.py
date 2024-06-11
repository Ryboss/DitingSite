import smtplib

from math import sin, cos, sqrt, atan2, trunc
from PIL import Image, ImageDraw, ImageFont

from core.config import GMAIL_PASSWORD, GMAIL_USERNAME, EARTH_RADIUS


class Distance:
    def __init__(self, longitude_auth, longitude2, latitude_auth, latitude2):
        self.longitude_auth = longitude_auth
        self.longitude2 = longitude2
        self.latitude_auth = latitude_auth
        self.latitude2 = latitude2

    def get_distance(self) -> int:
        delta_long = self.longitude2 - self.longitude_auth
        delta_latit = self.latitude2 - self.latitude_auth

        a = sin(delta_latit / 2) ** 2 + cos(self.latitude_auth) * cos(self.latitude2) * sin(delta_long / 2) ** 2

        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        self.distance = trunc(EARTH_RADIUS * c)

        return self.distance

    def __str__(self):
        return self.distance


class Watermark:
    def __init__(self, img_url, user_id):
        self.img = Image.open(img_url)
        self.text = "amirchik"
        self.user_id = user_id

    def watermark_image(self):
        width, height = self.img.size

        draw = ImageDraw.Draw(self.img)

        font = ImageFont.truetype('arial.ttf', 36)
        textwidth, textheight = draw.textsize(self.text, font)

        # calculate the x,y coordinates of the text
        margin = 10
        x = width - textwidth - margin
        y = height - textheight - margin

        draw.text((x, y), self.text, font=font)
        url_to_save = f"media/watermark_images/{self.user_id}_image.jpg"
        return self.save_image(url_to_save)

    def save_image(self, url_to_save):
        self.img.save(url_to_save)
        return url_to_save


def send_email(message: str, email: str) -> bool:
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    s.login(GMAIL_USERNAME, GMAIL_PASSWORD)

    s.sendmail(GMAIL_USERNAME, email, message)

    return True
