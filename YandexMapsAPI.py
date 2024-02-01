import requests


class YandexStaticApi:
    def __init__(self):
        self.scale = 1
        self.scale_step = 0.05

    def get_image(self, latitude, longitude):
        coords = f'{latitude},{longitude}'

        response = requests.get(f'https://static-maps.yandex.ru/1.x/?ll={coords}&spn={self.scale},0.00619&l=map')

        if response.status_code == 200:
            with open('image.png', 'wb') as f:
                f.write(response.content)

            return 'ok'
        raise ValueError

    def scale_up(self):
        if self.scale == 1:
            return

        self.scale += self.scale_step

    def scale_down(self):
        if self.scale == 0.05:
            return

        self.scale -= self.scale_step
