try:
    from .workbench import Tool
except ImportError:
    from workbench import Tool
    
from threading import Thread


def main():
    bench = Tool()
    Thread(target=bench.listener_mouse).start()
    Thread(target=bench.listener_keyboard).start()

    try:
        bench.mainloop()
    except SystemExit:
        bench.destroy()

    return 0


if __name__ == "__main__":
    main()
