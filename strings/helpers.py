#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

HELP_1 = """✅**<u>Yönetici Komutları:</u>**

**c**, kanal oynatma anlamına gelir.

/pause veya /cpause - Çalan müziği duraklatın.
/resume veya /cresume- Duraklatılan müziği devam ettirin.
/mute veya /cmute- Çalan müziğin sesini kapatın.
/unmute veya /cunmute- Sessize alınan müziğin sesini açın.
/skip veya /cskip- Çalan müziği atla.
/stop veya /cstop- Çalan müziği durdurun.
/shuffle veya /cshuffle- Kuyruğa alınan çalma listesini rastgele karıştırır.
/seek veya /cseek - Müziği kendi sürenize kadar iletin
/seekback veya /cseekback - Geriye Müziği sürenize göre arayın
/restart - Sohbetiniz için botu yeniden başlatın.


✅<u>**Belirli Atlama:**</u>
/skip veya /cskip [Sayı(örnek: 3)]
    - Müziği belirtilen sıraya alınmış bir numaraya atlar. Örnek: /skip 3, müziği sıradaki üçüncü müziğe atlar ve sıradaki 1 ve 2 müziği yok sayar.

✅<u>**Döngü Oynatma:**</u>
/loop veya /cloop [etkinleştir/devre dışı bırak] veya [1-10 arasındaki sayılar]
    - Etkinleştirildiğinde, bot mevcut çalan müziği sesli sohbette 1-10 kez döngüye alır. Varsayılan olarak 10 kez.

✅<u>**Doğru Kullanıcılar:**</u>
Kimlik Doğrulama Kullanıcılar, sohbetinizde yönetici hakları olmadan yönetici komutlarını kullanabilir.

/auth [Kullanıcı adı] - Grubun AUTH LIST'ine bir kullanıcı ekleyin.
/unauth [Kullanıcı adı] - Grubun AUTH LIST'inden bir kullanıcıyı kaldırır.
/authusers - Grubun KİMLİK LİSTESİNİ kontrol et."""


HELP_2 = """✅<u>**Çalma Komutları:**</u>

Mevcut Komutlar = play , vplay , cplay

ForcePlay Komutları = playforce, vplayforce, cplayforce

**c**, kanal oynatma anlamına gelir.
**v** video oynatma anlamına gelir.
**force**, force play anlamına gelir.

/play veya /vplay veya /cplay - Bot, verilen sorguyu sesli sohbette oynatmaya veya sesli sohbetlerde canlı bağlantıları yayınlamaya başlar.

/playforce veya /vplayforce veya /cplayforce - **Force Play** sesli sohbette çalmakta olan parçayı durdurur ve sırayı bozmadan/temizlemeden aranan parçayı anında oynatmaya başlar.

/channelplay [Sohbet kullanıcı adı veya kimliği] veya [Devre Dışı Bırak] - Kanalı bir gruba bağlayın ve grubunuzdan kanalın sesli sohbetinde müzik akışı yapın.


✅**<u>Bot'un Sunucu Oynatma Listeleri:</u>**
/playlist - Sunucularda Kayıtlı Oynatma Listenizi Kontrol Edin.
/deleteplaylist - Çalma listenizdeki kaydedilmiş tüm müzikleri silin
/play - Kayıtlı Oynatma Listenizi Sunuculardan oynatmaya başlayın."""


HELP_3 = """✅<u>**Bot Komutları:**</u>

/stats - İlk 10 Parça Global İstatistiklerini, Bot'un İlk 10 Kullanıcısını, Bot'ta İlk 10 Sohbeti, Sohbette Oynanan İlk 10'u vb. alın.

/sudolist - Yukki Müzik Botunun Sudo Kullanıcılarını Kontrol Edin

/lyrics [Müzik Adı] - Web'de belirli bir Müziğin Sözlerini arar.

/song [Parça Adı] veya [YT Bağlantısı] - Youtube'dan herhangi bir parçayı mp3 veya mp4 formatlarında indirin.

/player - Etkileşimli bir Oyun Paneli edinin.

**c**, kanal oynatma anlamına gelir.

/queue veya /cqueue- Müzik Sıra Listesini Kontrol Et."""

HELP_4 = """✅<u>**Ek Komutlar:**</u>
/start - Müzik Botunu başlatın.
/help - Komutların ayrıntılı açıklamalarını içeren Komutlar Yardımcı Menüsünü edinin.
/ping- Bot'a ping atın ve Bot'un Ram, Cpu vb. istatistiklerini kontrol edin.

✅<u>**Grup Ayarları:**</u>
/ settings - Satır içi düğmelerle eksiksiz bir grubun ayarlarını alın

🔗 **Ayarlardaki seçenekler:**

1️⃣ Sesli sohbette yayınlamak istediğiniz **Ses Kalitesini** ayarlayabilirsiniz.

2️⃣ Sesli sohbette yayınlamak istediğiniz **Video Kalitesini** ayarlayabilirsiniz.

3️⃣ **Auth Users**:- Yönetici komutları modunu buradan herkese veya yalnızca yöneticilere değiştirebilirsiniz. Eğer grubunuzdaki herkes yönetici komutlarını kullanabilecekse (/skip, /stop vb.)

4️⃣ **Temizlik Modu:** Etkinleştirildiğinde, sohbetinizin temiz ve iyi kalmasını sağlamak için botun mesajlarını grubunuzdan 5 dakika sonra siler.

5️⃣ **Komut Temizleme** : Etkinleştirildiğinde, Bot çalıştırdığı komutları (/play, /pause, /shuffle, /stop vb.) hemen siler.

6️⃣ **Oyun Ayarları:**

/playmode - Grubunuzun oynatma ayarlarını yapabileceğiniz düğmeler içeren eksiksiz bir oynatma ayarları paneli edinin.

<u>Oyun modundaki seçenekler:</u>

1️⃣ **Arama Modu** [Doğrudan veya Satır İçi] - /oynatma modunu verirken arama modunuzu değiştirir.

2️⃣ **Yönetici Komutları** [Herkes veya Yöneticiler] - Grubunuzdaki herkes, herkes yönetici komutlarını kullanabilecekse (/skip, /stop vb.)

3️⃣ **Çalma Türü** [Herkes veya Yöneticiler] - Yöneticiler ise, yalnızca grupta bulunan yöneticiler sesli sohbette müzik çalabilir."""

HELP_5 = """🔰**<u>SUDO KULLANICILARINI EKLE VE KALDIR :</u>**
/addsudo [Kullanıcı adı veya bir kullanıcıya yanıt]
/ delsudo [Kullanıcı adı veya bir kullanıcıya cevap]

🛃**<u>HEROKU:</u>**
/use - Dyno Kullanımı.

🌐**<u>AYARLANDIRMA DEĞİŞKENLERİ:</u>**
/get_var - Heroku veya .env'den bir yapılandırma değişkeni alın.
/del_var - Heroku veya .env'deki tüm değişkenleri silin.
/set_var [Var Adı] [Değer] - Heroku veya .env'de bir Var Ayarlayın veya Bir Var Güncelleyin. Var ve Değerini bir boşlukla ayırın.

🤖**<u>BOT KOMUTLARI:</u>**
/reboot - Botunuzu yeniden başlatın.
/ update - Botu güncelle.
/speedtest - Sunucu hızlarını kontrol edin
/bakım [etkinleştir / devre dışı bırak]
/logger [etkinleştir / devre dışı bırak] - Bot, aranan sorguları logger grubunda günlüğe kaydeder.
/get_log [Satır Sayısı] - Botunuzun günlüğünü heroku veya vps'den alın. Her ikisi için de çalışır.
/autoend [etkinleştir|devre dışı bırak] - Kimse dinlemiyorsa 3 dakika sonra Otomatik yayın bitişini etkinleştirin.

📈**<u>İSTATİSTİK KOMUTLARI:</u>**
/activevoice - Bottaki aktif sesli sohbetleri kontrol edin.
/activevideo - Bottaki etkin görüntülü görüşmeleri kontrol edin.
/stats - Bot İstatistiklerini Kontrol Et

⚠️**<u>KARA LİSTE SOHBET İŞLEVİ:</u>**
/blacklistchat [CHAT_ID] - Müzik Botu kullanan herhangi bir sohbeti kara listeye alın
/whitelistchat [CHAT_ID] - Kara listeye alınmış herhangi bir sohbeti Music Bot kullanarak beyaz listeye alın
/blacklistedchat - Kara listedeki tüm sohbetleri kontrol edin.

👤**<u>BLOKLANAN İŞLEV:</u>**
/block [Kullanıcı adı veya Kullanıcıyı yanıtla] - Bir kullanıcının bot komutlarını kullanmasını engeller.
/unblock [Kullanıcı Adı veya Kullanıcıya Cevap Ver] - Bir kullanıcıyı Bot'un Engellenenler Listesinden kaldırın.
/blockedusers - Engellenen Kullanıcı Listelerini kontrol edin

👤**<u>GBAN İŞLEVİ:</u>**
/gban [Kullanıcı adı veya Kullanıcıyı yanıtla] - Bir kullanıcıyı botun sunduğu sohbetten Gbanlayın ve botunuzu kullanmasını engelleyin.
/ungban [Kullanıcı adı veya Kullanıcıyı yanıtla] - Bir kullanıcıyı Bot'un gbanlı Listesinden çıkarın ve botunuzu kullanmasına izin verin
/gbannedusers - Gbanlı Kullanıcı Listelerini Kontrol Edin

🎥**<u>GÖRÜNTÜLÜ ARAMA İŞLEVİ:</u>**
/set_video_limit [Sohbet Sayısı] - Bir seferde Görüntülü Aramalar için izin verilen maksimum Sohbet Sayısını ayarlayın. Varsayılan olarak 3 sohbet.
/videomode [indir|m3u8] - İndirme modu etkinleştirilirse, Bot videoları M3u8 biçiminde oynatmak yerine indirir. Varsayılan olarak M3u8'e. m3u8 modunda herhangi bir sorgu yürütülmediğinde indirme modunu kullanabilirsiniz.

⚡️**<u>ÖZEL BOT İŞLEVİ:</u>**
/yetkilendir [CHAT_ID] - Botunuzu kullanmak için bir sohbete izin verin.
/unauthorize [CHAT_ID] - Bir sohbetin botunuzu kullanmasına izin vermeyin.
/yetkili - Botunuzun izin verilen tüm sohbetlerini kontrol edin.

🌐**<u>YAYIN İŞLEVİ:</u>**
/broadcast [Mesaj veya Mesaja Cevap Ver] - Herhangi bir mesajı Bot'un Sunulan Sohbetlerine yayınlayın.

<u>yayın seçenekleri:</u>
**-pin** : Bu, mesajınızı sabitler
**-pinloud** : Bu, mesajınızı yüksek sesli bildirimle sabitler
**-user** : Bu, mesajınızı botunuzu başlatan kullanıcılara yayınlayacaktır.
**-yardımcı** : Bu, botunuzun yardımcı hesabından mesajınızı yayınlayacaktır.
**-nobot** : Bu, botunuzu mesaj yayınlamamaya zorlar

**Örnek:** `/broadcast -user -assistant -pin Hello Testing`

"""
