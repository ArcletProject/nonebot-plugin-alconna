from nonebot_plugin_alconna.analyser import MessageContainer

MessageContainer.config(
    preprocessors={"MessageSegment": lambda x: str(x) if x.type == "markdown" else None}
)

Markdown = str
