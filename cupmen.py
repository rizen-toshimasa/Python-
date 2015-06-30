import sys # モジュール属性 argv を取得するため
import time
import os
import subprocess
argvs = sys.argv  # コマンドライン引数を格納したリストの取得
argc = len(argvs) # 引数の個数
if (argc != 2): 
    count = 3*60
else:
    count = argvs[1]
    if("s" in count):
        count,tmp = count.split("s")
        count = int(count)
    else:
        count = int(count)*60
print("タイマーセット"+str(count))        
countdown = count
while(countdown!=0):
    os.system("clear")
    print("残り:"+str(countdown))
    countdown -= 1
    time.sleep(1)
cmd = "mplayer 'http://translate.google.com/translate_tts?tl=ja&q=かっぷめんができました。"+str(count)+"秒まったかいがあったね'"
subprocess.call(cmd, shell=True)
print("時間になったぜ")
