import vk_api
import requests


token = "<token>"
session = vk_api.VkApi(token=token)
vk = session.get_api()
from_group = 1
version = 5.131
owner_id = 221500656
url = "https://api.vk.com/method/wall.post"


def vk_post(message=None, photo_url=None):
    if not photo_url:
    	vk.wall.post(message=message, from_group=from_group, owner_id=-owner_id)
    else:
     upload_url = vk.photos.getWallUploadServer()["upload_url"]
     photo = requests.get(photo_url)
     files = {"photo": ("photo.jpg", photo.content, "image/jpeg")}
     response = requests.post(upload_url, files=files)
     result = response.json()
     
     save_response = vk.photos.saveWallPhoto(
     	server=result["server"],
     	photo=result["photo"],
     	hash=result["hash"]
     )
     photo_info = save_response[0]
     
     vk.wall.post(
     		from_group=from_group,
     		owner_id=-owner_id,
	        message=message,
	        attachments=f'photo{photo_info["owner_id"]}_{photo_info["id"]}'
	  )
    	
	
PHOTO_URL: str = "<url>"
TEXT: str = "<text>"

vk_post(photo_url=PHOTO_URL)
