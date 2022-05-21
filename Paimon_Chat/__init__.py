import random
import requests

from ssl import SSLCertVerificationError
from nonebot import on_regex, on_command, logger
from nonebot.matcher import matchers
from nonebot.rule import Rule
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, GroupMessageEvent, MessageSegment
from nonebot.exception import FinishedException

from utils.config import config
from utils.auth_util import FreqLimiter2

voice_url = 'https://static.cherishmoon.fun/LittlePaimon/voice/'
chat_lmt = FreqLimiter2(60)

update_voice = on_command('更新派蒙语音', priority=2)


def check_group(event: GroupMessageEvent) -> bool:
    if event.group_id in config.paimon_chat_group:
        return True
    return False


@update_voice.handle()
async def update_paimon_voice(event: MessageEvent):
    try:
        old_len = len([m for m in matchers[10] if m.plugin_name == 'Paimon_Chat'])
        matchers[10] = [m for m in matchers[10] if m.plugin_name != 'Paimon_Chat']
        try:
            voice_list = requests.get('https://static.cherishmoon.fun/LittlePaimon/voice/voice_list.json').json()
        except SSLCertVerificationError:
            voice_list = requests.get('http://static.cherishmoon.fun/LittlePaimon/voice/voice_list.json').json()
        for key, value in voice_list.items():
            create_matcher(key, value['pattern'], value['cooldown'], value['pro'], value['files'])
        new_len = len(voice_list) - old_len
        await update_voice.send(f'派蒙语音更新成功，本次获取到{len(voice_list)}种语音， 新增{new_len}种语音')
    except FinishedException:
        raise
    except Exception as e:
        await update_voice.send(f'派蒙语音更新失败：{e}')


def create_matcher(chat_word: str, pattern: str, cooldown: int, pro: float, responses):

    def check_pro() -> bool:
        return random.random() < pro

    def check_cooldown(event: GroupMessageEvent) -> bool:
        return chat_lmt.check(event.group_id, chat_word)

    hammer = on_regex(pattern, priority=10, rule=Rule(check_group, check_pro, check_cooldown))
    hammer.plugin_name = 'Paimon_Chat'

    @hammer.handle()
    async def handler(event: GroupMessageEvent):
        try:
            chat_lmt.start_cd(event.group_id, chat_word, cooldown)
            response = random.choice(responses)
            if '.mp3' not in response:
                await hammer.finish(response)
            else:
                try:
                    await hammer.finish(MessageSegment.record(file=voice_url + response))
                except SSLCertVerificationError:
                    await hammer.finish(MessageSegment.record(file=voice_url.replace('https', 'http') + response))
        except FinishedException:
            raise
        except Exception as e:
            logger.error('派蒙发送语音失败', e)


try:
    voice_list = requests.get('https://static.cherishmoon.fun/LittlePaimon/voice/voice_list.json').json()
except SSLCertVerificationError:
    voice_list = requests.get('http://static.cherishmoon.fun/LittlePaimon/voice/voice_list.json').json()
for k, v in voice_list.items():
    create_matcher(k, v['pattern'], v['cooldown'], v['pro'], v['files'])
