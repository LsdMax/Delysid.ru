# -*- coding: cp1251 -*-
from gui import SystemMessages
from gui.Scaleform.daapi.view.lobby.LobbyView import LobbyView
global isLogin
isLogin = True
LOGIN_TEXT_MESSAGE = '<font color="#cc9933"><b>--= ПРИВЕТ КРУТОЙ! https://delysid.ru/index.php =--</b></font>'.decode('cp1251')


old_populate = LobbyView._populate

def new_populate(self):
    global isLogin
    old_populate(self)
    if isLogin:
        SystemMessages.pushI18nMessage(LOGIN_TEXT_MESSAGE, type=SystemMessages.SM_TYPE.Warning)
        isLogin = False


LobbyView._populate = new_populate