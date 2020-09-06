import langid
import random
import hashlib
import requests

async def get_translated_text(text: str) -> str:
	apiurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
	appid = ''
	secretkey = ''
	cla = langid.classify(text)[0]
	salt = str(random.randint(32768, 65536))
	sign = appid + text + salt + secretkey
	sign = hashlib.md5(sign.encode('utf-8')).hexdigest()
	
	langid_dict={'zh':'中文', 'en':'英文', 'ja':'日文', 'jp':'日文'}
	#别的语言？在写了再写了.jpg
	if cla=='zh':
		ori='zh'; tra='en'
	else:
		if cla=='ja':
			ori='jp'
		else:
			ori='en'
		tra='zh'
		
	data = {
		'q':text,
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
	return '待翻译内容识别为：{0}\n翻译结果为：{1}'.format(ori_lang,dst)
