import json
import os
import re

from telethon.events import CallbackQuery

from zthon import zedub


@zedub.tgbot.on(CallbackQuery(data=re.compile(b"troll_(.*)")))
async def on_plug_in_callback_query_handler(event):
    timestamp = int(event.pattern_match.group(1).decode("UTF-8"))
    if os.path.exists("./zthon/troll.txt"):
        jsondata = json.load(open("./zthon/troll.txt"))
        try:
            message = jsondata[f"{timestamp}"]
            userid = message["userid"]
            ids = userid
            if event.query.user_id in ids:
                reply_pop_up_alert = (
                    "يا حلو هذي الرسالة مو لك آسف"
                )
            else:
                encrypted_tcxt = message["text"]
                reply_pop_up_alert = encrypted_tcxt
        except KeyError:
            reply_pop_up_alert = "- عذرًا .. هذه الرسـالة لم تعد موجودة في سيـرفرات الــمـــــ🪐ــجـــرة"
    else:
        reply_pop_up_alert = "- عذرًا .. هذه الرسـالة لم تعد موجودة في سيـرفرات الــمـــــ🪐ــجـــرة"
    await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
