import _thread as thread
import utime as time


def th_func(thread_id, delay):
    print("thread:{} delay {}".format(thread_id, delay))
    time.sleep_ms(delay)


def main():
    print("线程传递多个参数测试")
    for i in range(5):
        thread.start_new_thread(th_func, (i + 1, 2))
    # 等待所有子线程回收
    time.sleep_ms(100)


main()
