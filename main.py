from dotenv import load_dotenv
import requests
import random
import os


def get_request(url, params={}):
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response


def get_xkcd_comic():
    last_comic_number = get_request('http://xkcd.com/info.0.json').json()['num']
    comic_number = random.randint(1, last_comic_number + 1)
    url = 'http://xkcd.com/{}/info.0.json'.format(comic_number)
    meta_info = get_request(url).json()
    comic_url = meta_info['img']
    comic_name = comic_url.split('/')[-1]
    comic_title = meta_info['title']
    comic_file = get_request(comic_url).content
    with open(comic_name, 'wb') as file:
        file.write(comic_file)

    return comic_name, comic_title


def get_url_for_uploading(params):
    url = 'https://api.vk.com/method/photos.getWallUploadServer'
    response = get_request(url, params=params)
    return response.json()['response']['upload_url']


def upload_image_to_server(url, file_name):
    with open(file_name, 'rb') as file:
        files = {
            'photo': file,
        }
        response = requests.post(url, files=files)
        response.raise_for_status()

    return {
                'server': response.json()['server'],
                'photo': response.json()['photo'],
                'hash': response.json()['hash'],
            }


def save_image_on_server(params, meta):
    url = 'https://api.vk.com/method/photos.saveWallPhoto'
    params.update(meta)
    response = get_request(url, params)
    return response.json()


def publish_image_in_group(params, message, meta):
    url = 'https://api.vk.com/method/wall.post'
    attachments = '{}{}_{}'.format(
        'photo',
        meta['response'][0]['owner_id'],
        meta['response'][0]['id']
    )
    params.update(
        {
            'owner_id': '-{}'.format(params['group_id']),
            'message': message,
            'attachments': attachments
        }
    )
    response = get_request(url, params=params)
    return response.json()['response']['post_id']


def main():
    load_dotenv()
    params = {
        'group_id': os.getenv('GROUP_ID'),
        'access_token': os.getenv('ACCESS_TOKEN'),
        'v': '5.130',
    }
    image_name, image_title = get_xkcd_comic()
    upload_url = get_url_for_uploading(params.copy())
    meta = upload_image_to_server(upload_url, image_name)
    if meta['photo']:
        meta = save_image_on_server(params.copy(), meta)
        post_id = publish_image_in_group(params.copy(), image_title, meta)
        os.remove(image_name)
    else:
        raise Exception('Не удалось загрузить изображение на сервер')

    print(post_id)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
