import requests
import RPi.GPIO as GPIO
import time
import sys
import subprocess
import pyaudio
import wave
# LED_GPIO 変数に 24をセット
SW_GPIO = 25


# GPIO.BCMを設定することで、GPIO番号で制御出来るようになります。
GPIO.setmode(GPIO.BCM)

# GPIO.INを設定することで、入力モードになります。
# pull_up_down=GPIO.PUD_DOWNにすることで、内部プルダウンになります。
GPIO.setup(SW_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
LastStatus = False
# ボタン押し / 離し 動作確認用コード
while True:
    try:
        # GPIO24の値を読み込み、その値を出力します。
        # ボタンを押すと"1"（High）、離すと"0"（Low）。
        SwitchStatus = GPIO.input(SW_GPIO)
        if LastStatus != SwitchStatus:
            
            if SwitchStatus == 1:
                    print("LINE send")
                
                    #LINE通知
                    url = "https://notify-api.line.me/api/notify" 
                    token = "KNy8yEdrxE8nPUnlFV3SZ7wm5i6c6KNt0DYNaGirSBm"
                    headers = {"Authorization" : "Bearer "+ token} 
                    message =  "SOS! HELP ME! https://calm-everglades-24284.herokuapp.com/"
                    payload = {"message" :  message} 
                    r = requests.post(url, headers = headers, params=payload)
                
                    #subprocess.run(['sudo','gnome-terminal','--','gpsmon'])
                    subprocess.run(['sudo','systemctl','start','gpxlogger.service'])
                    subprocess.run(['sudo','python','/home/xyz/xyz/record2.py'])
                    print("syuuryou")
                    time.sleep(30)
                    subprocess.run(['sudo','systemctl','stop','gpxlogger.service'])
                    subprocess.run(['sudo','python','/home/xyz/xyz/run.py'])
                    print("ok")
                
            time.sleep(0.2)
        LastStatus = SwitchStatus
            
    # Ctrl+Cキーを押すと処理を停止
    except KeyboardInterrupt:
        # ピンの設定を初期化
        # この処理をしないと、次回 プログラムを実行した時に「ピンが使用中」のエラーになります。
        GPIO.cleanup()
        sys.exit()