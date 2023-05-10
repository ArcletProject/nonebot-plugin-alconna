from nonebot_plugin_alconna.typings import SegmentPattern
from nepattern import (
    BasePattern,
    PatternModel,
    UnionPattern,
)
from nepattern.main import INTEGER
from nonebot.adapters.feishu.message import MessageSegment
from nonebot_plugin_alconna.argv import MessageArgv
from arclet.alconna import set_default_argv_type

set_default_argv_type(MessageArgv)

Text = str
At = SegmentPattern("at", MessageSegment, MessageSegment.at)
Post = SegmentPattern("post", MessageSegment, MessageSegment.post)
Image = SegmentPattern("image", MessageSegment, MessageSegment.image)
Interactive = SegmentPattern("interactive", MessageSegment, MessageSegment.interactive)
ShareChat = SegmentPattern("share_chat", MessageSegment, MessageSegment.share_chat)
ShareUser = SegmentPattern("share_user", MessageSegment, MessageSegment.share_user)
Audio = SegmentPattern("audio", MessageSegment, MessageSegment.audio)
Media = SegmentPattern("media", MessageSegment, MessageSegment.media)
File = SegmentPattern("File", MessageSegment, MessageSegment.file)
Sticker = SegmentPattern("sticker", MessageSegment, MessageSegment.sticker)


AtID = (
    UnionPattern(
        [
            BasePattern(
                model=PatternModel.TYPE_CONVERT,
                origin=int,
                alias="At",
                accepts=[At],
                converter=lambda _, x: int(x.data['user_id']),
            ),
            BasePattern(
                r"@(\d+)",
                model=PatternModel.REGEX_CONVERT,
                origin=int,
                alias="@xxx",
                accepts=[str],
            ),
            INTEGER,
        ]
    )
    @ "at_id"
)
"""
内置类型，允许传入提醒元素(At)或者'@xxxx'式样的字符串或者数字, 返回数字
"""
