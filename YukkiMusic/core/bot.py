import sys

from pyrogram import Client
from pyrogram.types import BotCommand

import config

from ..logging import LOGGER

class YukkiBot(Client):
    def init(self):
        LOGGER(name).info(f"Starting Bot")
        super().init(
            "YukkiMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        try:
            get_me = await self.get_me()
            self.username = get_me.username
            self.id = get_me.id

            video_url = "https://telegra.ph/file/622ca19c932af54a530a1.mp4"
            caption = "Bot Başladı"
            
            try:
                await self.send_video(
                    config.LOG_GROUP_ID,
                    video=video_url,
                    caption=caption,
                )
            except:
                LOGGER(name).error(
                    "Bot günlük kanalına erişemedi. Botu günlük kanalınıza eklediğinizfen ve admin olarak yetkilendirdiğinizden emin olun.!"
                )
                sys.exit()

            if config.SET_CMDS == str(True):
                try:
                    await self.set_bot_commands(
                        [
                            BotCommand("ping", "Botun canlı olup olmadığını kontrol edin"),
                            BotCommand("oynat", "İstenen şarkıyı çalmaya başlar"),
                            BotCommand("atla", "Sıradaki bir sonraki parçaya geçer"),
                            BotCommand("durdur", "Şu an çalan şarkıyı duraklat"),
                            BotCommand("devam", "Duraklatılan şarkılar devam ettiriliyor"),
                            BotCommand("son", "Sırayı temizleyin ve sesli sohbetten çıkın"),
                            BotCommand("karistir", "Sıraya alınmış çalma listesini rastgele karıştırır."),
                            BotCommand("playmode", "Sohbetiniz için varsayılan oynatma modunu değiştirmenizi sağlar"),
                            BotCommand("ayarlar", "Sohbetiniz için müzik botunun ayarlarını açın.")
                        ]
                    )
                except:
                    pass
            else:
                pass

            a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
            if a.status != ChatMemberStatus.ADMINISTRATOR:
                LOGGER(name).error(
                    "Please promote Bot as Admin in Logger Group"
                )
                sys.exit()

        except Exception as e:
            LOGGER(name).error(f"Error during bot start: {e}")
            sys.exit()

        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name

        LOGGER(name).info(f"MusicBot Started as {self.name}")
