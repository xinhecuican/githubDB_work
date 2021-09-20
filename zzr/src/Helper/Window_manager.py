from zzr.src.Helper.Register import Registers

window_list = {}
old_window = ""
now_window = ""


def change_window(name: str, args = None):
    global now_window
    global old_window
    if name in Registers.model.dict.keys() and name not in window_list:
        if args is not None:
            window_list[name] = Registers.model.dict[name](*args)
        else:
            window_list[name] = Registers.model.dict[name]()

    if now_window != "":
        window_list[now_window].on_window_cancel()
        window_list[now_window].hide()

    old_window = now_window
    now_window = name

    window_list[now_window].on_window_select(args)
    window_list[now_window].show()


def pop_window(name: str):
    change_window(old_window)

