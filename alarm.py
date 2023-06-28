import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print("时间到！")

if __name__ == "__main__":
    minutes = int(input("请输入专注时长（分钟）："))
    focus_timer(minutes)