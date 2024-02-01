import requests


class YandexStaticApi:
    def __init__(self, latitude, longitude):
        self.scale = 0.01
        self.scale_step = 0.005
        self.move_step = 0.025
        self.latitude = latitude
        self.longitude = longitude

    def get_image(self):
        coords = f'{self.latitude},{self.longitude}'

        response = requests.get(f'https://static-maps.yandex.ru/1.x/?ll={coords}&spn={self.scale},{self.scale}&l=map')

        if response.status_code == 200:
            with open('image.png', 'wb') as f:
                f.write(response.content)

            return 'ok'
        raise ValueError

    def scale_up(self):
        if self.scale == 1:
            return

        self.scale -= self.scale_step
        print(self.scale)

    def scale_down(self):
        if self.scale == 0.05:
            return

        self.scale += self.scale_step
        print(self.scale)

    def move_left(self):
        if self.latitude - self.scale >= -180:
            self.latitude -= self.move_step
            print(f"New longitude: {self.longitude}")
        else:
            print("0")

    def move_right(self):
        if self.latitude + self.scale <= 180:
            self.latitude += self.move_step
            print(f"New longitude: {self.longitude}")
        else:
            print("0")

    def move_up(self):
        if self.longitude + self.scale <= 90:
            self.longitude += self.move_step
            print(f"New latitude: {self.latitude}")
        else:
            print("0")

    def move_down(self):
        if self.longitude - self.scale >= -90:
            self.longitude -= self.move_step
            print(f"New latitude: {self.latitude}")
        else:
            print("0")
