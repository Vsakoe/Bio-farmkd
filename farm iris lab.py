from .. import loader, utils
from telethon import types, events
import asyncio
from telethon.errors.rpcerrorlist import YouBlockedUserError

@loader.tds
class stickersMod(loader.Module):
  """by @Vsakoe0 | этот модуль позволт копить био опыт/ресурсы
  
  (на балансе необходимо иметь био опыт)"""
  strings = {'name':'bio farm'}
  async def zarazcmd(self, message):
      """количисво"""
      chat = 5443619563
      args = utils.get_args_raw(message)
      if not args:
	        await message.edit("Вы не указали количество")
	        return
      async with message.client.conversation(chat) as conv:
          try:
              await message.edit('Фарм запущен')
              for i in range(0, int(args)+1):
                await message.client.send_message(chat, "заразить сильного")
                await asyncio.sleep(3)
                await message.client.send_message(chat, "!купить вакцину")
                await asyncio.sleep(3)
          except YouBlockedUserError:
              await message.edit("Ирис заблокирован")
              return
