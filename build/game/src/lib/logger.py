from datetime import datetime as dt
import time


class Logger:
    @staticmethod
    def log(func):
        def wrapper(*args, **kwargs):

            func_start_point = time.time()
            time.sleep(0.000001)
            result = func(*args, **kwargs)
            func_work_time = time.time() - func_start_point - 0.000001

            with open("log/log.txt", "a") as f:
                f.write("------\n")
                f.write(f"F_NAME: {func.__name__}\n")
                f.write(f"F_CALL_TIME: {dt.now()}\n")
                f.write(f"F_WORKTIME: {func_work_time} seconds\n")
                f.write(f"F_ARGS: {list(args)}\n")
                f.write(f"F_KWARGS: {list(kwargs)}\n")
                f.write(f"F_RETURN: {result}\n")
                f.write("------\n")
            return result

        return wrapper
