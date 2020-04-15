import keyboard
import win32clipboard
import time


def hotkey_copy(clipboard_data=""):
    time.sleep(0.01)
    try:
        win32clipboard.OpenClipboard()
        try:
            str(win32clipboard.GetClipboardData())
            clipboard_data = win32clipboard.GetClipboardData()
        except:
            print("error: only copy text")
        finally:
            win32clipboard.CloseClipboard()
    except:
        print("unknown error")
    print(clipboard_data)
    try:
        clipboard_file = open("clipboard.txt", "r")
    except:
        clipboard_file = open("clipboard.txt", "w")
        clipboard_file.close
        clipboard_file = open("clipboard.txt", "r")
    if clipboard_data != "":
        if clipboard_file.read() == "":
            clipboard_file.close()
            with open("clipboard.txt", "w") as clipboard_file:
                clipboard_file.write(clipboard_data)
        else:
            clipboard_file.close()
            with open("clipboard.txt", "a") as clipboard_file:
                clipboard_file.write("\n" + clipboard_data)


def hotkey_paste(clipboard_string=""):
    with open("clipboard.txt", "r") as clipboard_file:
        for line in clipboard_file:
            print(line)
            clipboard_string += line + "\n"
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(clipboard_string)
    win32clipboard.CloseClipboard()


keyboard.add_hotkey('ctrl+c', hotkey_copy)
keyboard.add_hotkey('ctrl+b', hotkey_paste)
keyboard.wait()
# hotkey = pyhk.pyhk()
# hotkey.addHotkey(["Ctrl", "C"], hotkey_function)
