from nonebot import on_command, CommandSession
from .data_source import soutu

@on_command('搜图', aliases=('以图搜图', '识图', '搜图:'), only_to_me=False)
async def ocr(session: CommandSession):
	img_url = session.get('img_url', prompt='发张图试试吧')
	ret = await soutu(img_url)
	await session.send(ret)

@ocr.args_parser
async def _(session: CommandSession):
		
	if session.current_arg_images:
		session.state['img_url'] = session.current_arg_images[0]
	else:
		if not session.is_first_run:
			session.finish()
	return
	
	session.state[session.current_key] = session.current_arg_images[0]
