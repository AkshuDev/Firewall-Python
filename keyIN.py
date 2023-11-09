import win32api

class KEYCODE:
        LEFT_MB = 0x01
        RIGHT_MB = 0x02
        MIDDLE_MB = 0x04
        X1_MB = 0x05
        X2_MB = 0x06
        CBP = 0x03
        RES1 = 0x07
        RES3 = 0x5E
        RES6 = 0xE0
        BACKSPACE = 0x08
        TAB = 0x09
        CLEAR = 0x0C
        RETURN = 0x0D
        SHIFT = 0x10
        CONTROL = 0x11
        MENU = 0x12
        PAUSE = 0x13
        CAPSLOCK = 0x14
        ESCAPE = 0x1B
        SPACE = 0x20
        PAGE_UP = 0x21
        PAGE_DOWN = 0x22
        END = 0x23
        HOME = 0x24
        UP_ARROW = 0x25
        LEFT_ARROW = 0x26
        RIGHT_ARROW = 0x27
        DOWN_ARROW = 0x28
        SELECT = 0x29
        PRINT = 0x2A
        EXE = 0x2B

CLOSE = KEYCODE().ESCAPE
RUN = KEYCODE().EXE

def GetKey(key):
    keyg = win32api.GetKeyState(key)
    if keyg < 0:
        return True
    else:
        return False