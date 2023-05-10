from nonebot_plugin_alconna.typings import SegmentPattern
from nonebot.adapters.ntchat.message import MessageSegment, BaseMessage, Message
from nonebot_plugin_alconna.argv import MessageArgv
from arclet.alconna import set_default_argv_type, argv_config


class WXMessageArgv(MessageArgv):
    ...


set_default_argv_type(WXMessageArgv)
argv_config(
    WXMessageArgv,
    filter_out=[],
    checker=lambda x: isinstance(x, BaseMessage),
    to_text=lambda x: x if x.__class__ is str else str(x) if x.is_text() else None,
    converter=lambda x: Message(x)
)

Text = str
RoomAtMsg = SegmentPattern("room_at_msg", MessageSegment, MessageSegment.room_at_msg)
Card = SegmentPattern("card", MessageSegment, MessageSegment.card)
Link = SegmentPattern("link", MessageSegment, MessageSegment.link)
Image = SegmentPattern("image", MessageSegment, MessageSegment.image)
File = SegmentPattern("file", MessageSegment, MessageSegment.file)
Video = SegmentPattern("video", MessageSegment, MessageSegment.video)
XML = SegmentPattern("xml", MessageSegment, MessageSegment.xml)
