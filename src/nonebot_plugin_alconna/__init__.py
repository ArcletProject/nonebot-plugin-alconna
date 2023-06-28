from nonebot import __version__ as nonebot_version
from nonebot.plugin import PluginMetadata

from .argv import MessageArgv as MessageArgv
from .consts import ALCONNA_RESULT as ALCONNA_RESULT
from .matcher import on_alconna as on_alconna
from .model import CommandResult as CommandResult
from .model import Match as Match
from .model import Query as Query
from .params import AlcMatches as AlcMatches
from .params import AlcResult as AlcResult
from .params import AlconnaDuplication as AlconnaDuplication
from .params import AlconnaMatch as AlconnaMatch
from .params import AlconnaMatches as AlconnaMatches
from .params import AlconnaQuery as AlconnaQuery
from .params import AlconnaResult as AlconnaResult
from .params import Check as Check
from .params import assign as assign
from .params import match_path as match_path
from .params import match_value as match_value
from .rule import alconna as alconna
from .rule import set_output_converter as set_output_converter
from .config import Config

__version__ = "0.8.3"

_meta_source = {
    "name": "Alconna 插件",
    "description": "提供 [Alconna](https://github.com/ArcletProject/Alconna) 的 Nonebot2 适配版本与工具",
    "usage": "matcher = on_alconna(...)",
    "homepage": "https://github.com/ArcletProject/Alconna",
    "type": "library",
    "supported_adapters": None,
    "config": Config,
    "extra": {
        "author": "RF-Tar-Railt",
        "priority": 1,
        "version": __version__,
    }
}


if not nonebot_version.split(".")[-1].isdigit():
    _meta_source["extra"]["homepage"] = _meta_source.pop("homepage")
    _meta_source["extra"]["type"] = _meta_source.pop("type")
    _meta_source["extra"]["config"] = _meta_source.pop("config")
    _meta_source["extra"]["supported_adapters"] = _meta_source.pop("supported_adapters")


__plugin_meta__ = PluginMetadata(**_meta_source)
