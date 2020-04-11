from urllib.parse import quote

help_msg='''======= Minecraft Wiki Searcher =======
帮助你更好地搜索MCWiki~
'''

def on_info(server, info):
    if server.is_player:
