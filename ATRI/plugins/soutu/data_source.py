import requests
import io
from PIL import Image
	
async def soutu(img_url):
	apikey = ''                   #在saucenao注册并获取apikey
	apiurl = 'https://saucenao.com/search.php?'
	thumbSize = (250,250)         #直接发送缩略图尺寸
	
	url = apiurl + '&api_key=' + apikey + '&db=999&output_type=2&testmode=1&numres=2'
	response = requests.get(img_url)
	
	image = Image.open(io.BytesIO(response.content))
	image = image.convert('RGB')
	image.thumbnail(thumbSize, resample=Image.ANTIALIAS)
	imageData = io.BytesIO()
	image.save(imageData,format='PNG')
	
	files = {'file': ('image.png', imageData.getvalue())}
	imageData.close()

	req = requests.post(url,files = files)
	info = req.json()['results'][0]['data']
	sen=''
	for key,value in info.items():
		sen=sen+'{key}: {value}\n'.format(key=key,value=value)
	
	return sen + '[CQ:image,file='+req.json()['results'][0]['header']['thumbnail']+']'
