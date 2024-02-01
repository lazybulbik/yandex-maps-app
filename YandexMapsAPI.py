import requests


class YandexStaticApi:
    def get_image(self, latitude, longitude, scale):
        coords = f'{latitude},{longitude}'
        size = f'{scale}'

        response = requests.get(f'https://static-maps.yandex.ru/1.x/?ll={coords}8&spn={size},0.00619&l=map')

        if response.status_code == 200:
            with open('image.png', 'wb') as f:
                f.write(response.content)

            return 'ok'
        raise ValueError
