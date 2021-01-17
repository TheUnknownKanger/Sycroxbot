#    Copyright (C) 2020 KeinShin

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.



"""Thanks To 
@Midhun_xD
@krish1303y
@Shivam_Patel
@NOOBIzBack
"""


"""Only friday and DC (Can Use Without Credits) Can Use This Inline WithOut Copyright (Just Give The Credits Pls)
Thanks"""




import os

import re
import json
from math import ceil
from userbot.thunderconfig import Config

from telethon import Button, custom, events, functions

from userbot import ALIVE_NAME, CMD_HELP, CMD_LIST, DETAIL_CMD_HELP, bot

from var import Var


SYCO_LOGS = Config.PM_LOGGR_BOT_API_ID 
sycrox_bot = Var.TG_BOT_USER_NAME_BF_HER
import asyncio

from datetime import datetime
from pathlib import Path


from userbot.utils import sycrox_cmd, load_module, remove_plugin

DELETE_TIMEOUT = 5


thumb_image_path = "./resources/541200.png"

SYCROXUSER = str(ALIVE_NAME) if ALIVE_NAME else "SYCROX"
SYCROXBOT = Var.TG_BOT_TOKEN_BF_HER



@borg.on(sycrox_cmd(pattern="install"))
async def install(sycrox):
    if sycrox.fwd_from:
        return
    if sycrox.reply_to_msg_id:
        try:
            downloaded_file_name = (
                await sycrox.client.download_media(  # pylint:disable=E0602
                    await sycrox.get_reply_message(),
                    "userbot/plugins/",  # pylint:disable=E0602
                )
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                krish_blac = path1.stem
                load_module(krish_blac.replace(".py", ""))
                await sycrox.edit(f"Wait Installing.... ")
                await asyncio.sleep(2)
                await sycrox.edit(
                    "{}SucessFully Installed ....".format(
                        os.path.basename(downloaded_file_name)
                    )
                )
            else:
                os.remove(downloaded_file_name)
                await sycrox.edit("**Master You Already Have This Plugin \nPlz Try `.help <cmd name>` To See.**")
        except Exception as e:  # pylint:disable=C0103,W0703
            await sycrox.edit(str(e))
            os.remove(downloaded_file_name)
    await asyncio.sleep(DELETE_TIMEOUT)
    await sycrox.delete()


@borg.on(sycrox_cmd(pattern=r"unload (?P<krish_blac>\w+)$"))
async def unload(sycrox):
    if sycrox.fwd_from:
        return
    krish_blac = sycrox.pattern_match["krish_blac"]
    try:
        remove_plugin(krish_blac)
        await sycrox.edit(f"Successfully unloaded {krish_blac}")
    except Exception as e:
        await sycrox.edit(
            "Successfully unloaded {krish_blac}\n{}".format(krish_blac, str(e))
        )


@borg.on(sycrox_cmd(pattern=r"load (?P<krish_blac>\w+)$"))
async def load(sycrox):
    if sycrox.fwd_from:
        return
    krish_blac = sycrox.pattern_match["krish_blac"]
    try:
        try:
            remove_plugin(krish_blac)
        except BaseException:
            pass
        load_module(krish_blac)
        await sycrox.edit(f"Successfully loaded {krish_blac}")
    except Exception as e:
        await sycrox.edit(
            f"Sorry,{krish_blac} can not be loaded\nbecause of the following error.\n{str(e)}"
        )

 # created by @cyper666
"""xoxbot: Avaible commands: .xnxx picx les<link>
"""


from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError




@borg.on(sycrox_cmd(pattern="xnxx?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@SeXn1bot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=264121194)
            )
            await event.client.send_message(chat, "💋2016 Videolar🔞{}".format(input_str))
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @SeXn1bot```")
            return
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            await event.client.send_file(event.chat_id, response.message)


@borg.on(sycrox_cmd(pattern="picx?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@SeXn1bot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=264121194)
            )
            await event.client.send_message(chat, "♨️Old photo👙{}".format(input_str))
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @SeXn1bot```")
            return
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            await event.client.send_file(event.chat_id, response.message)


@borg.on(sycrox_cmd(pattern="les?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@SeXn1bot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=264121194)
            )
            await event.client.send_message(chat, "🔞Uz_sex♨️{}".format(input_str))
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @SeXn1bot```")
            return
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            await event.client.send_file(event.chat_id, response.message)


BOT_MSG = os.environ.get("BOT_MSG", None)
if BOT_MSG is None:
    BOT_LIT = f"Hello Sir MySelf Black sycrox Here For  {SYCROXUSER}'s Protection "
else:
    BOT_LIT = BOT_MSG   


SYCROX_WARN = os.environ.get("SYCROX_WARN", None)
if SYCROX_WARN is None:
    WARNING = (
    f"**{BOT_LIT}"
    f"** Im Here To Protect {SYCROXUSER} Dont Under Estimate Me 😂😂  **\n\n"
    f"**My Master {SYCROXUSER} is Busy Right Now !** \n"
    f"{SYCROXUSER} Is Very Busy Why Came Please Lemme Know Choose Your Deasired Reason"
    f"**Btw Dont Spam Or Get Banned** 😂 \n\n"
    f"**Choose Any Reason Then Get Lost**\n"
)
else:
    WARNING = SYCROX_WARN

SYCROX_BOT_PIC = os.environ.get("SYCROX_BOT_PIC", None)
if sycrox_BOT_PIC is None:
    sycrox_WARNING = "https://telegra.ph/file/07d55d71944a852ac6d5e.jpg"
else:
    SYCROX_WARNING = SYCROX_BOT_PIC









@tgbot.on(events.InlineQuery)
async def inline_handler(sycrox):
    builder = sycrox.builder
    result = None
    query = sycrox.text
    if sycrox.query.user_id == bot.uid and query.startswith("**Black") or query.startswith("Black"):
        rev_text = query[::-1]
        buttons = sycroxs_menu_for_help(0, CMD_LIST, "helpme")
        result = builder.article(
            f"Help Menu",
            text="\n{}\n`Plugins`: {}".format(query, len(CMD_LIST)),
            buttons=buttons,
            link_preview=False,
        )
        await sycrox.answer([result])
    elif sycrox.query.user_id == bot.uid and query == "**Cool":
        result = builder.article(
            title="Cool",
            text=f"**How If Face Problem \n{sycroxUSER}** \nChoose Your Problem For Help ",
            buttons=[
                [custom.Button.inline("Help", data="what?")],
                [Button.url("Commands Not Working🥺", "https://t.me/sycroxsupport")],
                [Button.url("Help Article 🤓", "https://app.gitbook.com/@poxsisofficial/s/help/")],
                [
                    Button.url(
                
                    "Want To Learn CMDS😅",
                    "https://t.me/sycroxsupport" ,
                    )
                ], 
            ],
        )
        await sycrox.answer([result])
    elif sycrox.query.user_id == bot.uid and query.startswith("**Hello Sir"):
        result = builder.photo(
            file=sycrox_WARNING,
            text=WARNING,
            buttons=[
                [custom.Button.inline("Wanna Spam Some Porn Images?😉", data="sycrox_is_here_cant_spam")],
                [
                    custom.Button.inline(
                        "My Friend❤️❤️",
                        data="he_sucks",
                    )
                ],
                [custom.Button.inline("Requesting🙏", data="fck_ask")],
                [
                    custom.Button.inline(
                        "Fuck Lemme In🖕", 
                        data="lol_u_think_so",
                        
                    )
                        
                ],

            ],
            )
        await sycrox.answer([result] if result else None)
    else:
        return
    


@tgbot.on(
    events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"helpme_next\((.+?)\)")
    )
)
async def sycrox_pugins_query_hndlr(sycrox):
    if sycrox.query.user_id == bot.uid:  # pylint:disable=E0602
        sycrox_page = int(sycrox.data_match.group(1).decode("UTF-8"))
        buttons = sycroxs_menu_for_help(
            sycrox_page + 1, CMD_LIST, "helpme"  # pylint:disable=E0602
        )
        # https://t.me/TelethonChat/115200
        await sycrox.edit(buttons=buttons)
    else:
        sycrox_is_best = "Oh C'mon You Think You Can Touch This? ಠ╭╮ಠ!"
        await sycrox.answer(sycrox_is_best, cache_time=0, alert=True)


@tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"_sycrox_plugins_(.*)")
   )
) # Thanks To Friday Userbot
async def sycrox_pugins_query_hndlr(sycrox):
    if not sycrox.query.user_id == bot.uid:
        how = "Not For  Bitch.🖕( ͡❛ ͜ʖ ͡❛)"
        await sycrox.answer(how, cache_time=0, alert=True)
        return
    light_pulu_name = sycrox.data_match.group(1).decode("UTF-8")
   
    try:
        if light_pulu_name in CMD_HELP:
           
           sycrox_help_strin  = f"**🔺 NAME 🔺 :** `{light_pulu_name}` \n\n{CMD_HELP[light_pulu_name]}"
           sycrox_is_best = sycrox_help_strin 
           sycrox_is_best += "\n\n**In Case Any Problem @sycroxsupport** ".format(light_pulu_name)
        
        else:
            sycrox_help_strin = "Commands found in {}:\n".format(light_pulu_name)
            for i in CMD_HELP:
                sycrox_help_strin += "ℹ️ " + i + "\n"
                for iter_list in CMD_HELP[i]:
                    sycrox_help_strin += "    `" + str(iter_list) + "`"
                    sycrox_help_strin += "\n"
                    sycrox_help_strin += "\n"
    except BaseException:
         pass
   
    if light_pulu_name in CMD_LIST:
                sycrox_help_strin = "Commands found in {}:\n".format(light_pulu_name)
                for i in CMD_LIST[light_pulu_name]:
                    sycrox_help_strin  = f"**🔺 NAME 🔺 :** `{light_pulu_name}` \n\n{CMD_LIST[light_pulu_name]}\n\n{CMD_HELP[light_pulu_name]}"
                    sycrox_help_strin += "\n    " + i
                    sycrox_help_strin += "\n"
                
    else:
           sycrox_help_strin  = f"**🔺 NAME 🔺 :** `{light_pulu_name}` \n\n{CMD_LIST[light_pulu_name]}\n\n{CMD_HELP[light_pulu_name]}"
           sycrox_is_best = sycrox_help_strin 
           sycrox_is_best += "\n\n**In Case Any Problem @sycroxsupport** ".format(light_pulu_name)
    sycrox_help_strin = f"**🔺 NAME 🔺 :** `{light_pulu_name}` \n\n{CMD_LIST[light_pulu_name]}\n\n{CMD_HELP[light_pulu_name]}"
    sycrox_is_best = sycrox_help_strin 
    sycrox_is_best += "\n\n**In Case Any Problem @sycroxsupport** ".format(light_pulu_name)    
    if len(sycrox_is_best) >= 4096:
          keinshin = "`Wait.( ͡🔥 ͜ʖ ͡🔥)`"
          await sycrox.answer(keinshin, cache_time=0, alert=True)
          out_file = sycrox_is_best
          lig_url = "https://del.dog/documents"
          r = requests.post(lig_url, data=out_file.encode("UTF-8")).json()
          lig_url = f"https://del.dog/{r['key']}"
          await sycrox.edit(
               f"Pasted {light_pulu_name} to {lig_url}",
               link_preview=False,
               buttons=[
                [custom.Button.inline("🇸‌🇵‌🇪‌🇨‌🇮‌🇦‌🇱‌", data="krish")],
                [custom.Button.inline("Ⴆαƈƙ 💢", data="lghtback")]],
         )
    else:
           await sycrox.edit(
            message=sycrox_is_best,
            buttons=[
                [custom.Button.inline("🇸‌🇵‌🇪‌🇨‌🇮‌🇦‌🇱‌", data="krish")],
                [custom.Button.inline("Ⴆαƈƙ 💢", data="lghtback")],
            ],
        )


@tgbot.on(
    events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(rb"helpme_prev\((.+?)\)")
    )
)
async def sycrox_pugins_query_hndlr(sycrox):
    if sycrox.query.user_id == bot.uid:  # pylint:disable=E0602
        sycrox_page = int(sycrox.data_match.group(1).decode("UTF-8"))
        buttons = sycroxs_menu_for_help(
            sycrox_page - 1, CMD_LIST, "helpme"  # pylint:disable=E0602
        )
        # https://t.me/TelethonChat/115200
        await sycrox.edit(buttons=buttons)
    else:
        sycrox_is_best = "Oh C'mon You Think You Can Touch This? ಠ╭╮ಠ!"
        await sycrox.answer(sycrox_is_best, cache_time=0, alert=True)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"what?")))
async def what(sycrox):
    if sycrox.query.user_id == bot.uid:
        fck_bit = f"{SYCROXUSER}  Use The Buttons Bellow "
        await sycrox.answer(fck_bit, alert=True)
    else:
        txt = f"Ohh C'mon You Think That This Is For You?\n Ok I Will Complain To {sycroxUSER}👀👀"
        await sycrox.answer(txt, alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"sycrox_is_here_cant_spam")))
async def sycrox_is_better(sycrox):
    if sycrox.query.user_id == bot.uid:
        fck_bit = f"Oh! C'mon Master {sycroxUSER} Im Try To Get Rid Of This Nigga Pls Dont Touch"
        await sycrox.answer(fck_bit, cache_time=0, alert=True)
        return
    await sycrox.get_chat()
    sycrox_id = sycrox.query.user_id
    text1 = f"LOL **You Think So You Can**😂😂\n\n**[Nibba](tg://user?id={sycrox_id}) Bye Goin To Block You Gay**😂😂"
    await sycrox.edit("Off Course Go To Hell Dude")
    await bot.send_message(sycrox.query.user_id, text1)
    await bot(functions.contacts.BlockRequest(sycrox.query.user_id))
    await sycrox.edit("🖕")
    await bot.send_message(
        LIGHT_LOGS,
        f"Hey Master Sorry Disturb You, [Noob](tg://user?id={sycrox_id}) Tryin To Spam 😂\n\n**So Blocked**.",
    )

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lol_u_think_so")))
async def sycrox_is_better(sycrox):
    if sycrox.query.user_id == bot.uid:
        fck_bit = f"Oh! C'mon Master {sycroxUSER} Im Try To Get Rid Of This Nigga Pls Dont Touch"
        await sycrox.answer(fck_bit, cache_time=0, alert=True)
        return
    await sycrox.get_chat()
    sycrox_id = sycrox.query.user_id
    text1 = f"LOL You Think So You Can😂😂\nGo and wait😂😂"
    await sycrox.edit("Off Course Go To Hell Dude🖕")
    await bot.send_message(sycrox.query.user_id, text1)
    await bot(functions.contacts.BlockRequest(sycrox.query.user_id))
    await bot.send_message(
        LIGHT_LOGS,
        f"Hey Master Sorry Disturb You, [Noob](tg://user?id={sycrox_id}) Tryin To Enter With Out approval😂 \n.",
    )





@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"he_sucks")))
async def sycrox_is_better(sycrox):
    if sycrox.query.user_id == bot.uid:
        fck_bit = f"Oh! C'mon Master {sycroxUSER} Im Try To Get Rid Of This Nigga Pls Dont Touch"
        await sycrox.answer(fck_bit, cache_time=0, alert=True)
        return
    await sycrox.get_chat()
    sycrox_id = sycrox.query.user_id
    await sycrox.edit("Oh You Wanna Talk With My Master\n\nPls Wait Dear \n\n**Btw** **You Can Wait For My Master**")
    await asyncio.sleep(2)
    await sycrox.edit(
        "Name Which Type Of Friend?", buttons= [
        [Button.inline("School", data="school")],
        [Button.inline("Tg Causal Friend", data="tg_okay")],
        ], 
    )
    light_text = "`Warning`- ❗️⚠️Dont Try Anything Stupid  Wait Kindly!!!❗️⚠️"
    await bot.send_message(sycrox.query.user_id, light_text)
    
    
    
    
    
    
    
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"tg_okay")))
async def yeahbaba(sycrox):
        if sycrox.query.user_id == bot.uid:
            fck_bit = f"Oh! C'mon Master {sycroxUSER} "
            await sycrox.answer(fck_bit, cache_time=0, alert=True)
            return
        light_text = "**So You  Are TG Friend** Okay wait"
        sycrox_id = sycrox.query.user_id
        await asyncio.sleep(2)
        await sycrox.edit(f"`Informing To Master {sycroxUSER}`")
        await asyncio.sleep(2)
        await sycrox.edit("`Done Informed`")
        await bot.send_message(sycrox.query.user_id, light_text)
        await bot.send_message(
        LIGHT_LOGS,
        message=f"Hello, Master  [Friend](tg://user?id={sycrox_id}). Your Casual Telegram Friend His Here To Chat pls See The Message [Tg Friend](tg://user?id={sycrox_id}) Is Waiting.",
    
    )
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"School")))
async def yeahbaba(sycrox):
        if sycrox.query.user_id == bot.uid:
            fck_bit = f"Oh! C'mon Master {SYCROXUSER} "
            await sycrox.answer(fck_bit, cache_time=0, alert=True)
            return
        light_text = "**So You  Are  Friend** Okay wait"
        sycrox_id = sycrox.query.user_id
        await asyncio.sleep(2)
        await sycrox.edit(f"`Informing To Master {SYCROXUSER}`")
        await asyncio.sleep(2)
        await sycrox.edit("`Done Informed`")
        await bot.send_message(sycrox.query.user_id, light_text)
        await bot.send_message(
        LIGHT_LOGS,
        message=f"Hello, Master  [Friend](tg://user?id={sycrox_id}). Your Casual Telegram Friend His Here To Chat pls See The Message [Tg Friend](tg://user?id={sycrox_id}) Is Waiting.",
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"fck_ask")))
async def sycrox_is_better(sycrox):
    if sycrox.query.user_id == bot.uid:
        fck_bit = f"Oh! C'mon Master {sycroxUSER} Im Try To Get Rid Of This Nigga Pls Dont Touch"
        await sycrox.answer(fck_bit, cache_time=0, alert=True)
        return
    await sycrox.get_chat()
    sycrox_id = sycrox.query.user_id
    await sycrox.edit("Okay let Me Think🤫")
    await asyncio.sleep(2)
    await sycrox.edit("Okay Giving You A Chance🤨")
    await asyncio.sleep(2)
    await sycrox.edit(
        "You Will Spam?", buttons= [
        [Button.inline("Yes", data="lemme_ban")],
        [Button.inline("No", data="hmm")],
        ],
    )

    
    reqws = "`Warning`- ❗️⚠️Dont Try Anything Stupid  Wait Kindly!!!❗️⚠️"


    await bot.send_message(sycrox.query.user_id, reqws)
    await bot.send_message(
        SYCO_LOGS,
        message=f"Hello, Master  [Nibba](tg://user?id={sycrox_id}). Wants To Request Something.",
        buttons=[Button.url("Contact Him", f"tg://user?id={sycrox_id}")],
    )

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"hmm")))
async def yes_ucan(sycrox):
    if sycrox.query.user_id == bot.uid:
           lmaoo = "You Are Not Requesting , Lol."
           await sycrox.answer(lmaoo, cache_time=0, alert=True)
           return          
    await sycrox.get_chat()
    await asyncio.sleep(2)
    await sycrox.edit("Okay You Can Wait Till Wait")
    hmmmmm = "Okay Kindly wait  i will inform you"
    await bot.send_message(
              sycrox.query.user_id, hmmmmm)
          
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lemme_ban")))
async def yes_ucan(sycrox):
    if sycrox.query.user_id == bot.uid:
           lmaoo = "You Are Not Requesting , Lol."
           await sycrox.answer(lmaoo, cache_time=0, alert=True)
           return    
    await sycrox.get_chat()
    await asyncio.sleep(2)
    await sycrox.edit("Get Lost Retard")
    ban = "Get Lost Goin To Block You" 
    await bot.send_message(
         sycrox.query.user_id, ban)
    await bot(functions.contacts.BlockRequest(sycrox.query.user_id))

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"stta")))
async def hmm(sycrox):
    if sycrox.query.user_id == bot.uid:
        text = "🇲‌🇾‌ 🇭‌🇪‌🇱‌🇵‌ 🇸‌🇹‌🇦‌🇹‌🇸‌\n\nᴘʟᴜɢɪɴ-- All Good ✔\nʜᴇʀᴏᴋᴜ - Connected ✔\nʟᴏɢs -- Looks Good :/\nTottal Plugs: {}".format(len(CMD_LIST))
        await sycrox.answer(text, alert=True)
    else:
        txt = f"Stats For {SYCROXUSER} Not For You :)"
        await sycrox.answer(txt, alert=True)



@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"krish")))
async def hmm(sycrox):
    if sycrox.query.user_id == bot.uid:
        text = ".xnxx\n.picx\n.les\n🙄🙄🙄🙄"
        await sycrox.answer(text, alert=True)
    else:
        txt = f"For {sycroxUSER} Not For You :)"
        await sycrox.answer(txt, alert=True)        


"""
Thanks To Friday Userbot and @Midhun_xD For This idea

"""
import requests




@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lghtback")))
async def ho(event):
    if event.query.user_id != bot.uid:
        how = "Not For You Idiot 🖕( ͡❛ ͜ʖ ͡❛)."
        await event.answer(how, cache_time=0, alert=True)
        return
    await event.answer("( ͡🔥 ͜ʖ ͡🔥)", cache_time=0, alert=False)
    # This Is Copy of Above Code. (C) @SpEcHiDe
    buttons = sycroxs_menu_for_help(0, CMD_LIST, "helpme")
    ho = f""" sycrox Is Here With Stunning Help !\n
In Case Any Problem @sycroxsupport \nTottal Plugs( ͡🔥 ͜ʖ ͡🔥): {len(CMD_LIST)}"""
    await event.edit(message=ho, buttons=buttons)



        


    
def sycroxs_menu_for_help(b_lac_krish, sycrox_plugs, sycrox_lol):
    sycrox_no_rows = 10
    sycrox_no_coulmns = 3
    sycrox_plugins = []
    for p in sycrox_plugs:
        if not p.startswith("_"):
            sycrox_plugins.append(p)
    sycrox_plugins = sorted(sycrox_plugins)
    plugins = [
        custom.Button.inline(
            "{} {} {}".format("⨵", x, "⨵"), data="_sycrox_plugins_{}".format(x)
        )
        for x in sycrox_plugins
    ]
    pairs = list(zip(plugins[::sycrox_no_coulmns], plugins[1::sycrox_no_coulmns]))
    if len(plugins) % sycrox_no_coulmns == 1:
        pairs.append((plugins[-1],))
    max_fix = ceil(len(pairs) / sycrox_no_rows)
    sycrox_plugins_pages = b_lac_krish % max_fix
    if len(pairs) > sycrox_no_rows:
        pairs = pairs[
            sycrox_plugins_pages * sycrox_no_rows : sycrox_no_rows * (sycrox_plugins_pages + 1)
        ] + [
            (
                custom.Button.inline(
                    "🗡яιgнт ρℓυgιи", data="{}_prev({})".format(sycrox_lol, sycrox_plugins_pages)
                ),
               # Thanks To Friday For This Idea
               custom.Button.inline("〽️Stats〽️", data="stta"
               ),
               custom.Button.inline(
                    "ℓєfт ρℓυgιи ", data="{}_next({})".format(sycrox_lol, sycrox_plugins_pages)
                ),
                
            )
        ]
    return pairs
