import time
from piper_sdk import *

if __name__ == "__main__":
    piper = C_PiperInterface("can0")
    piper.ConnectPort()
    time.sleep(0.03) # 需要时间去读取固件反馈帧，否则会反馈-0x4AF
    print(piper.GetPiperFirmwareVersion())
