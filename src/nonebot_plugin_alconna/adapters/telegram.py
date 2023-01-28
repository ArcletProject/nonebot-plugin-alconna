from nonebot_plugin_alconna.typings import gen_unit
from nonebot_plugin_alconna.analyser import MessageContainer

MessageContainer.config(
    preprocessors={
        "MessageSegment": lambda x: str(x) if x.type == "text" else None,
        "Entity": lambda x: str(x) if x.type == "text" else None
    }
)

Text = str
Location = gen_unit("location")
Venue = gen_unit("venue")
Poll = gen_unit("poll")
Dice = gen_unit("dice")
ChatAction = gen_unit("chat_action")

Mention = gen_unit("mention")
HashTag = gen_unit("hashtag")
CashTag = gen_unit("cashtag")
BotCommand = gen_unit("bot_command")
Url = gen_unit("url")
Email = gen_unit("email")
PhoneNumber = gen_unit("phone_number")
Bold = gen_unit("bold")
Italic = gen_unit("italic")
Underline = gen_unit("underline")
Strikethrough = gen_unit("strikethrough")
Spoiler = gen_unit("spoiler")
Code = gen_unit("code")
Pre = gen_unit("pre")
TextLink = gen_unit("text_link")
TextMention = gen_unit("text_mention")
CustomEmoji = gen_unit("custom_emoji")

Photo = gen_unit("photo")
Voice = gen_unit("voice")
Animation = gen_unit("animation")
Audio = gen_unit("audio")
Document = gen_unit("document")
Video = gen_unit("video")

Sticker = gen_unit("sticker")
VideoNote = gen_unit("video_note")
