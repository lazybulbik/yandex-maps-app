import requests

class YandexStaticApi:
    def __init__(self, latitude, longitude):
        self.scale = 0.01
        self.scale_step = 0.0005
        self.latitude = latitude
        self.longitude = longitude
        self.map_type = 'map'  # Изначально установим тип карты как "схема"

    def get_image(self):
        coords = f'{self.latitude},{self.longitude}'
        response = requests.get(f'https://static-maps.yandex.ru/1.x/?ll={coords}&spn={self.scale},{self.scale}&l={self.map_type}')
        if response.status_code == 200:
            with open('image.png', 'wb') as f:
                f.write(response.content)
            return 'ok'
        raise ValueError

    def scale_up(self):
        if self.scale == 1:
            return
        self.scale -= self.scale_step

    def scale_down(self):
        if self.scale == 0.05:
            return
        self.scale += self.scale_step

    def move_left(self):
        if self.longitude - self.scale >= -180:
            self.longitude -= self.scale

    def move_right(self):
        if self.longitude + self.scale <= 180:
            self.longitude += self.scale

    def move_up(self):
        if self.latitude + self.scale <= 90:
            self.latitude += self.scale

    def move_down(self):
        if self.latitude - self.scale >= -90:
            self.latitude -= self.scale

    def change_map_type(self, map_type):
        self.map_type = map_type
