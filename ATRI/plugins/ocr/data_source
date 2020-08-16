import langid
import random
import hashlib
import requests
import config
	
async def ocr_translated_text(pic_url, user_info):
	#百度OCR的token获取
	host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={0}&client_secret={1}'.format(user_info['client_id'],user_info['client_secret'])
	response = requests.get(host)
	if response:
		user_info['access_token'] = response.json()['access_token']
	
	#百度OCR识图
	request_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'
	request_url = request_url + '?access_token=' + user_info['access_token']
	
	headers = {'content-type': 'application/x-www-form-urlencoded'}
	params = {
		'url': pic_url,
		'language_type': user_info['lang']
	}
	
	response = requests.post(request_url, data=params, headers=headers)
	if response:
		words = response.json()['words_result']
		sentence = ''
	for word in words:
		sentence += word['words']+' '
		
	#百度翻译
	apiurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
	appid = ''
	secretkey = ''
	cla = langid.classify(sentence)[0]
	salt = str(random.randint(32768, 65536))
	sign = appid + sentence + salt + secretkey
	sign = hashlib.md5(sign.encode('utf-8')).hexdigest()
	langid_dict={'zh':'中文', 'en':'英文', 'ja':'日文'}
	
	if cla=='zh':
		ori='zh'; tra='en'
	else:
		if cla=='ja':
			ori='ja'
		else:
			ori='en'
		tra='zh'
	
	data = {
		'q':sentence,
		'from':ori,
		'to':tra,
		'appid': appid,
		'salt':salt,
		'sign':sign
	}
	
	req = requests.get(apiurl, data)
	res = req.json()
	dst = str(res["trans_result"][0]["dst"])
	
	ori_lang=langid_dict[ori]
	return '待翻译内容识别为：{0} {1} \n翻译结果为：{2}'.format(ori_lang,sentence,dst)
