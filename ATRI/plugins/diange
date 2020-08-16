# -*- coding:utf-8 -*-
import json
from nonebot import on_command, CommandSession
import nonebot

from ATRI.modules import response

url = 'http://musicapi.leanapp.cn/search?keywords='
para = {
	'limit': 1
}

@on_command('music', aliases = ['点歌', '音乐'], only_to_me = False)
async def _(session: CommandSession):

	song_name = session.current_arg_text.strip()

	if not song_name:
		song_name = session.get('message', prompt = '请告诉ATRI要点的歌曲名~')
	await session.send('在找了在找了……')

	URL = url + song_name
	resp = response.request_api_params(URL, para)
	if not resp:
		session.finish('ATRI在网络上走散了...请重试...')
	else:
		resu = json.loads(resp)
		id = resu['result']['songs'][0]['id']
    
	msg = 'https://music.163.com/#/song?id='+str(id)
	await session.send(msg)
