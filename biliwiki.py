from urllib.parse import quote

help_msg='''
§r======= §6Minecraft biliWiki Searcher §r=======
帮助你更好地搜索Minecraft Wiki~
使用§6!!wiki§r可以叫出本使用方法
使用§6!!wiki [搜索内容]§r可以调用搜索
Minecraft biliWiki Searcher Plugin by §6GamerNoTitle
§r======= §6Minecraft biliWiki Searcher §r=======
'''

def on_info(server, info):
    if info.content == '!!wiki':
        server.tell(info.player, help_msg)
    else:
        if info.content.startswith('!!wiki') and info.is_player:
            if len(info.content[7:])==0:
                server.tell(info.player, '[biliwiki]§6参数错误！')
            else:
                search_content=info.content[7:]
                server.execute('tellraw ' + info.player + ' {"text":"[biliwiki]: 搜索 §6' + search_content + '§r 的结果","underlined":"false","clickEvent":{"action":"open_url","value":"https://searchwiki.biligame.com/mc/index.php?search=' + quote(search_content) + '"}}')
