from nonebot import on_command, CommandSession
from .data_source import ocr_translated_text

#采用百度智能云的文字识别API
user_info={
    'client_id': '',
    'client_secret': '',
    'access_token': '',   #程序自动获取
    'lang': 'JAP',        #识别语言
    }
	
@on_command('OCR', aliases=('识图翻译', 'ocr', 'OCR:', 'ocr:', '识图翻译:'), only_to_me=False)
async def ocr(session: CommandSession):
	pic_url=session.get('pic_url', prompt='发张含文字的图试试吧')
	ocr_text=await ocr_translated_text(pic_url,user_info)
	await session.send(ocr_text)
	session.pause()

@ocr.args_parser
async def _(session: CommandSession):
	
	if session.current_arg_text == '结束':
		session.finish('收工啦')
		
	if session.current_arg_images:
		session.state['pic_url'] = session.current_arg_images[0]
	
	if not session.is_first_run:
		if not session.current_arg_images:
			session.finish()
		
	return
	

	session.state[session.current_key] = session.current_arg_images[0]
