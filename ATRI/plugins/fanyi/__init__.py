from nonebot import on_command, CommandSession
from .data_source import get_translated_text

@on_command('trans', aliases=('翻译', '翻译:'), only_to_me=False)
async def trans(session: CommandSession):
	text=session.get('text', prompt='想翻译什么内容呢~')
	trans_text=await get_translated_text(text)
	await session.send(trans_text)

@trans.args_parser
async def _(session: CommandSession):
	stripped_arg = session.current_arg_text.strip() #去除信息首尾空白符
	
	if session.is_first_run:
		if stripped_arg:
			session.state['text'] = stripped_arg
		return
	
	if not stripped_arg:
		session.pause('你输了个啥？？？')
	
	session.state[session.current_key] = stripped_arg
