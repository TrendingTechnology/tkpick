from .workbench import Tool
from threading import Thread


def launch():
    bench = Tool()
    Thread(target=bench.listener_mouse).start()
    Thread(target=bench.listener_keyboard).start()

    try:
        bench.mainloop()
    except SystemExit:
        bench.destroy()

    return 0
