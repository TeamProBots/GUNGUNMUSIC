from pyrogram import Client, filters
from PROMUSIC import app
from config import OWNER_ID, BOT_USERNAME, MAIN_OWNER
from pyrogram.types import Message


@app.on_message(filters.command(["post"], prefixes=["/", "."]) & filters.user(MAIN_OWNER))
async def copy_messages(_, message):

    if message.reply_to_message:
      
        destination_group_id = -1002100130095
 

        
        await message.reply_to_message.copy(destination_group_id)
        await message.reply("ᴘᴏsᴛ sᴜᴄᴄᴇssғᴜʟ ᴅᴏɴᴇ ")

@app.on_message(filters.command(["cpost"], prefixes=["/", "."]) & filters.user(MAIN_OWNER))
async def copy_messages(_, message):

    if message.reply_to_message:
      
        destination_group_id = -1002228715294
 

        
        await message.reply_to_message.copy(destination_group_id)
        await message.reply("Cʜᴀɴɴᴇʟ ᴘᴏsᴛ sᴜᴄᴄᴇssғᴜʟ ᴅᴏɴᴇ !")
