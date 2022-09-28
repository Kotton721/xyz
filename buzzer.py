import requests
import RPi.GPIO as GPIO
import time
import sys
import subprocess

# LED_GPIO 変数に 24をセット
SW_GPIO = 25
Led_pin = 27


# GPIO.BCMを設定することで、GPIO番号で制御出来るようになります。
GPIO.setmode(GPIO.BCM)

# GPIO.INを設定することで、入力モードになります。
# pull_up_down=GPIO.PUD_DOWNにすることで、内部プルダウンになります。
GPIO.setup(SW_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(Led_pin, GPIO.OUT)
GPIO.output(Led_pin, GPIO.LOW)

LastStatus = False
# ボタン押し / 離し 動作確認用コード
while True:
    try:
        # GPIO24の値を読み込み、その値を出力します。
        # ボタンを押すと"1"（High）、離すと"0"（Low）。
        SwitchStatus = GPIO.input(SW_GPIO)
        if SwitchStatus == 1:
            print("LINE send")
            GPIO.output(Led_pin, GPIO.HIGH)
            time.sleep(5)
            GPIO.output(Led_pin, GPIO.LOW)
            time.sleep(5)
            GPIO.output(Led_pin, GPIO.HIGH)
            time.sleep(5)
            GPIO.output(Led_pin, GPIO.LOW)
            time.sleep(5)
            GPIO.output(Led_pin, GPIO.HIGH)
            time.sleep(3)
            Status2 = GPIO.input(SW_GPIO)
            if Status2 == 1:
                GPIO.output(Led_pin, GPIO.LOW)
                
                url = "https://notify-api.line.me/api/notify" 
                token = "KNy8yEdrxE8nPUnlFV3SZ7wm5i6c6KNt0DYNaGirSBm"
                headers = {"Authorization" : "Bearer "+ token} 
                message =  "sorry mistake"
                payload = {"message" :  message} 
                r = requests.post(url, headers = headers, params=payload)
                
            time.sleep(5)
                
                
            
    # Ctrl+Cキーを押すと処理を停止
    except KeyboardInterrupt:
        # ピンの設定を初期化
        # この処理をしないと、次回 プログラムを実行した時に「ピンが使用中」のエラーになります。
        GPIO.cleanup()
        sys.exit()
                