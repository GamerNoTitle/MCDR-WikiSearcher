from urllib.parse import quote

help_msg='''
§r======= §6Minecraft Wiki Searcher §r=======
帮助你更好地搜索Minecraft Wiki~
使用§6!!wiki§r可以叫出本使用方法
使用§6!!wiki [搜索内容]§r可以调用搜索
Minecraft Wiki Searcher Plugin by §6GamerNoTitle
§r======= §6Minecraft Wiki Searcher §r=======
'''

def on_info(server, info):
    if info.content == '!!wiki':
        server.tell(info.player, help_msg)
    else:
        if info.content.startswith('!!wiki') and info.is_player:
            if len(info.content[7:])==0:
                server.tell(info.player, '[wiki]§6参数错误！')
            else:
                search_content=info.content[7:]
                server.execute('tellraw ' + info.player + ' {"text":"[wiki]: 搜索 §6' + search_content + '§r 的结果","underlined":"false","clickEvent":{"action":"open_url","value":"https://minecraft-zh.gamepedia.com/index.php?search=' + quote(search_content) + '"}}')

def on_load(server, old_module):
    server.add_help_message('!!wiki', '§f获取Wiki插件使用方法')