import _thread as thread
import utime as time

exited = False


def th_func(thread_id, delay):
    global exited
    print("thread:{} delay {}".format(thread_id, delay))
    time.sleep_ms(delay)
    exited = True


def main():
    print("线程传递多个参数测试")
    # for i in range(5):
    thread.start_new_thread(th_func, (1, 2000))
    # 等待所有子线程回收
    while exited is False:
        time.sleep_ms(100)
        print("等待线程退出")


main()
