from dotenv import load_dotenv
import requests
import random
import os


def check_response_from_vk_api(response):
    if response.get('error'):
        raise Exception(response['error']['error_msg'])


def get_request(url, params={}):
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response


def get_xkcd_comic():
    last_comic_number = get_request('http://xkcd.com/info.0.json').json()['num']
    comic_number = random.randint(1, last_comic_number)
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
    response = get_request(url, params=params).json()
    check_response_from_vk_api(response)
    return response['response']['upload_url']


def upload_image_to_server(url, file_name):
    with open(file_name, 'rb') as file:
        files = {'photo': file}
        response = requests.post(url, files=files).json()
        response.raise_for_status()

    if response['photo']:
        return response['server'], response['photo'], response['hash']
    else:
        raise Exception('Не удалось загрузить изображение на сервер')


def save_image_on_server(params, server, photo, hash):
    url = 'https://api.vk.com/method/photos.saveWallPhoto'
    params.update({
        'server': server,
        'photo': photo,
        'hash': hash,
    })
    response = get_request(url, params).json()
    check_response_from_vk_api(response)
    return response['response'][0]['owner_id'], response['response'][0]['id']


def publish_image_in_group(params, message, owner_id, media_id):
    url = 'https://api.vk.com/method/wall.post'
    attachments = '{}{}_{}'.format('photo', owner_id, media_id)
    params.update({
        'owner_id': '-{}'.format(params['group_id']),
        'message': message,
        'attachments': attachments
        }
    )
    response = get_request(url, params=params).json()
    check_response_from_vk_api(response)
    return response['response']['post_id']


def main():
    load_dotenv()
    params = {
        'group_id': os.getenv('GROUP_ID'),
        'access_token': os.getenv('VK_API_ACCESS_TOKEN'),
        'v': '5.130',
    }
    try:
        image_name, image_title = get_xkcd_comic()
        upload_url = get_url_for_uploading(params.copy())
        server, photo, hash = upload_image_to_server(upload_url, image_name)
        owner_id, media_id = save_image_on_server(params.copy(), server, photo, hash)
        post_id = publish_image_in_group(params.copy(), image_title, owner_id, media_id)
    except Exception as e:
        print(e)
    finally:
        os.remove(image_name)


if __name__ == '__main__':
    main()
