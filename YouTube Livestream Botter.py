import os
import random
import string
import threading
import time
from queue import Queue
import platform
import requests
from colorama import Fore, init

intro = """
███████╗████████╗██████╗ ███████╗ █████╗ ███╗   ███╗      ██████╗  ██████╗ ████████╗████████╗███████╗██████╗
██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔══██╗████╗ ████║      ██╔══██╗██╔═══██╗╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗
███████╗   ██║   ██████╔╝█████╗  ███████║██╔████╔██║█████╗██████╔╝██║   ██║   ██║      ██║   █████╗  ██████╔╝
╚════██║   ██║   ██╔══██╗██╔══╝  ██╔══██║██║╚██╔╝██║╚════╝██╔══██╗██║   ██║   ██║      ██║   ██╔══╝  ██╔══██╗
███████║   ██║   ██║  ██║███████╗██║  ██║██║ ╚═╝ ██║      ██████╔╝╚██████╔╝   ██║      ██║   ███████╗██║  ██║
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝      ╚═════╝  ╚═════╝    ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝

https://github.com/KevinLage/YouTube-Livestream-Botter
"""

print(intro)
if platform.system() == "Windows": #checking OS
    clear = "cls"
else:
    clear = "clear"

iPhone_UA =Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
Mozilla/5.0 (Linux; U; Android 4.0.3; de-ch; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
Mozilla/5.0 (Linux; U; Android 2.3; en-us) AppleWebKit/999+ (KHTML, like Gecko) Safari/999.9
Mozilla/5.0 (Linux; U; Android 2.3.5; zh-cn; HTC_IncredibleS_S710e Build/GRJ90) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; HTC Vision Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
Mozilla/5.0 (Linux; U; Android 2.3.4; fr-fr; HTC Desire Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
Mozilla/5.0 (Linux; U; Android 2.3.4; en-us; T-Mobile myTouch 3G Slide Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC_Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC_Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari
Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
Mozilla/5.0 (Linux; U; Android 2.3.3; ko-kr; LG-LU3000 Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
Mozilla/5.0 (Linux; U; Android 2.3.3; en-us; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
Mozilla/5.0 (Linux; U; Android 2.3.3; en-us; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile
Mozilla/5.0 (Linux; U; Android 2.3.3; de-de; HTC Desire Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
Mozilla/5.0 (Linux; U; Android 2.3.3; de-ch; HTC Desire Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
Mozilla/5.0 (Linux; U; Android 2.2; fr-lu; HTC Legend Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
Mozilla/5.0 (Linux; U; Android 2.2; en-sa; HTC_DesireHD_A9191 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
Mozilla/5.0 (Linux; U; Android 2.2.1; fr-fr; HTC_DesireZ_A7272 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
Mozilla/5.0 (Linux; U; Android 2.2.1; en-gb; HTC_DesireZ_A7272 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
Mozilla/5.0 (Linux; U; Android 2.2.1; en-ca; LG-P505R Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
Mozilla/5.0 (Linux; U; Android 2.2.1; de-de; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
Mozilla/5.0 (Linux; U; Android 2.1-update1; es-mx; SonyEricssonE10a Build/2.0.A.0.504) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17
Mozilla/5.0 (Linux; U; Android 1.6; ar-us; SonyEricssonX10i Build/R2BA026) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1
Mozilla/5.0 (BlackBerry; U; BlackBerry 9900; en) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.346 Mobile Safari/534.11+
Mozilla/5.0 (BlackBerry; U; BlackBerry 9860; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.254 Mobile Safari/534.11+
Mozilla/5.0 (BlackBerry; U; BlackBerry 9850; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.254 Mobile Safari/534.11+
Mozilla/5.0 (BlackBerry; U; BlackBerry 9850; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.115 Mobile Safari/534.11+
Mozilla/5.0 (BlackBerry; U; BlackBerry 9850; en) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.254 Mobile Safari/534.11+
Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; zh-TW) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.448 Mobile Safari/534.8+
Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; zh-TW) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.246 Mobile Safari/534.1+
Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; tr) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.246 Mobile Safari/534.1+
Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; it) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.668 Mobile Safari/534.8+
Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; fr) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.246 Mobile Safari/534.1+
Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-US) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.701 Mobile Safari/534.8+
Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-US) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.466 Mobile Safari/534.8+
Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-US) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.450 Mobile Safari/534.8+
Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-US) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.448 Mobile Safari/534.8+
Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-US) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.446 Mobile Safari/534.8+
Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-US) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.201 Mobile Safari/534.1+
Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-US) AppleWebKit/534.1+ (KHTML, like Gecko)
Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-GB) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+
Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.448 Mobile Safari/534.8+
Mozilla/5.0 (BlackBerry; U; BlackBerry 9700; pt) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.546 Mobile Safari/534.8+
Mozilla/5.0 (BlackBerry; U; BlackBerry 9700; en-US) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.546 Mobile Safari/534.8+
Mozilla/5.0 (BlackBerry; U; BlackBerry 9380; en-GB) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.117 Mobile Safari/534.11+
Mozilla/5.0 (BlackBerry; U; BlackBerry 9360; it) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.336 Mobile Safari/534.11+
Mozilla/5.0 (BlackBerry; U; BlackBerry 9360; en) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.530 Mobile Safari/534.11+
Mozilla/5.0 (BlackBerry; U; BlackBerry 9330; en) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.346 Mobile Safari/534.11+
Mozilla/5.0 (BlackBerry; U; BlackBerry 9300; it) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.666 Mobile Safari/534.8+
Mozilla/5.0 (BlackBerry; U; BlackBerry 9300; es) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.668 Mobile Safari/534.8+
Mozilla/5.0 (BlackBerry; U; BlackBerry 9300; en) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.570 Mobile Safari/534.8+
BlackBerry9800/5.0.0.862 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/331 UNTRUSTED/1.0 3gpp-gba
BlackBerry9700/5.0.0.862 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/331 UNTRUSTED/1.0 3gpp-gba
BlackBerry9700/5.0.0.862 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/331
BlackBerry9700/5.0.0.862 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/167
BlackBerry9700/5.0.0.862 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/120
BlackBerry9700/5.0.0.770 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/100
BlackBerry9700/5.0.0.743 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/606
BlackBerry9700/5.0.0.743 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/107
BlackBerry9700/5.0.0.743 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/100
BlackBerry9700/5.0.0.593 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/603
BlackBerry9700/5.0.0.593 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/1
BlackBerry9700/5.0.0.586 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/120
BlackBerry9700/5.0.0.442 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/603
BlackBerry9700/5.0.0.423 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/10
BlackBerry9700/5.0.0.400 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/609
BlackBerry9700/5.0.0.351 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/603
BlackBerry9700/5.0.0.351 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/131
BlackBerry9700/5.0.0.344 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/229
BlackBerry9700/5.0.0.344 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/129
BlackBerry9650/5.0.0.975 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/105
BlackBerry9650/5.0.0.1006 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/105
BlackBerry9630/5.0.0.975 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/105
BlackBerry9630/5.0.0.624 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/104
BlackBerry9550/5.0.0.607 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/-1
BlackBerry9550/5.0.0.334 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/-1
BlackBerry9520/5.0.0.713 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/1
BlackBerry9520/5.0.0.306 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/120
BlackBerry9330/5.0.0.913 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/104
BlackBerry9330/5.0.0.857 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/105
BlackBerry9300/5.0.0.977 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/167
BlackBerry9300/5.0.0.955 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/102
BlackBerry9300/5.0.0.912 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/378
BlackBerry9300/5.0.0.888 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/331
BlackBerry9105/5.0.0.783 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/1
BlackBerry9000/4.6.0.303 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/302
BlackBerry8900/5.0.0.681 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/302
BlackBerry8900/5.0.0.681 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/179
BlackBerry8900/5.0.0.411 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/132
BlackBerry8900/5.0.0.1022 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/100
BlackBerry8700/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179
BlackBerry8530/5.0.0.654 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/104
BlackBerry8520/5.0.0.886 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/613
BlackBerry8520/5.0.0.822 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/298
BlackBerry8520/5.0.0.681 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/217
BlackBerry8520/4.6.1.314 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/611
BlackBerry8520/4.6.1.314 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/102
BlackBerry8520/4.6.1.272 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/132
BlackBerry8330/4.5.0.186 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/104
BlackBerry8320/4.5.0.52 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179
BlackBerry8320/4.5.0.188 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/100
BlackBerry8310/4.5.0.55 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/302
BlackBerry8310/4.5.0.110 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/-1
BlackBerry8110m/4.4.0.112 Profile/MIDP-1.9 Configuration/CLDC-1.0 VendorID/203
BlackBerry8100/4.2.1
BlackBerry8100/4.2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/155
BlackBerry8100/4.2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/116
BlackBerry8100/4.2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/114
BlackBerry8100/4.2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/102
BlackBerry8100/4.2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/100
BlackBerry8100/4.2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/1
BlackBerry8100/4.2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/-1
BlackBerry8100/4.2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1
BlackBerry8100/4.2.0 Profile/MIDP-2.0 Configuration/ CLDC-1.1 VendorID/100
BlackBerry8100/4.2.0
BlackBerry8100/2.7.0.60 Profile/MIDP-2.0 Configuration/CLDC-1.1
BlackBerry7520/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/103
BlackBerry7520/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1
BlackBerry7520/4.0.2 Profile/MIDP-2.0 Configuration/CLDC-1.1
BlackBerry7520/4.0.0 Profile/MIDP-2.0 Configuration/CLDC-1.1
BlackBerry7290/4.1.0Profile/MIDP-2.0 Configuration/CLDC-1.1
BlackBerry7290/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/163
BlackBerry7290/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/104
BlackBerry7290/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/100
BlackBerry7250/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/105
BlackBerry7250/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/104
BlackBerry7250/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1
BlackBerry7250/4.0.0 Profile/MIDP-2.0 Configuration/CLDC-1.1
BlackBerry7130e/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/104
BlackBerry7130e/4.1.0
BlackBerry7130/4.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/120
BlackBerry7130/4.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/102
BlackBerry7130/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/125
BlackBerry7100i/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/111
BlackBerry7100i/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/103
BlackBerry7100/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/102
BlackBerry7100/4.0.2 Profile/MIDP-2.0 Configuration/CLDC-1.1
BlackBerry7100/4.0.0 Profile/MIDP-2.0 Configuration/CLDC-1.1
BlackBerry 9700/5.0.0.351 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/123
BlackBerry 9000: BlackBerry9000/4.6.0.65 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/102
Mozilla/4.0 (compatible; MSIE 6.0; Windows 95; PalmSource; Blazer 3.0) 16; 160x160
Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; BOLT/2.340) AppleWebKit/530+ (KHTML, like Gecko) Version/4.0 Safari/530.17 UNTRUSTED/1.0 3gpp-gba
SamsungI8910/SymbianOS/9.1 Series60/3.0
NokiaN97i/SymbianOS/9.1 Series60/3.0
NokiaE52-1/SymbianOS/9.1 Series60/3.0 3gpp-gba
NokiaE5-00/SymbianOS/9.1 Series60/3.0 3gpp-gba
NokiaC7-00/SymbianOS/9.1 Series60/3.0 3gpp-gba
Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaC6-00/20.0.042; Profile/MIDP-2.1 Configuration/CLDC-1.1; zh-hk) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.2.6.9 3gpp-gba
Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba
NokiaC6-00/10.0.021 (SymbianOS/9.4; Series60/5.0 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebkit/525 (KHTML, like Gecko) BrowserNG/7.2.6 UNTRUSTED/1.0 3gpp-gba
NokiaN97/21.1.107 (SymbianOS/9.4; Series60/5.0 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebkit/525 (KHTML, like Gecko) BrowserNG/7.1.4
NokiaC5-00/061.005 (SymbianOS/9.3; U; Series60/3.2 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 Safari/525 3gpp-gba
Nokia5250/11.0.008 (SymbianOS/9.4; U; Series60/5.0 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Safari/525 3gpp-gba
Nokia5250/10.0.011 (SymbianOS/9.4; U; Series60/5.0 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Safari/525 3gpp-gba
Doris/1.15 [en] (Symbian)
Mozilla/5.0 (Windows; U; Windows CE; Mobile; like iPhone; ko-kr) AppleWebKit/533.3 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.3 Dorothy
Mozilla/5.0 (Windows; U; Windows CE; Mobile; like Android; ko-kr) AppleWebKit/533.3 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.3 Dorothy
Mozilla/5.0 (Windows; U; Mobile; Dorothy Browser; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Version/3.1.2 Mobile Safari/533.3
Mozilla/5.0 (Windows; U; Dorothy Browser; ko-kr) AppleWebKit/533.3 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.3
Mozilla/5.0 (Android; Linux armv7l; rv:9.0) Gecko/20111216 Firefox/9.0 Fennec/9.0
Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1 Fennec/7.0a1
Mozilla/5.0 (Maemo; Linux armv7l; rv:6.0a1) Gecko/20110526 Firefox/6.0a1 Fennec/6.0a1
Mozilla/5.0 (Maemo; Linux armv7l; rv:6.0a1) Gecko/20110522 Firefox/6.0a1 Fennec/6.0a1
Mozilla/5.0 (Maemo; Linux armv7l; rv:6.0a1) Gecko/20110518 Firefox/6.0a1 Fennec/6.0a1
Mozilla/5.0 (Maemo; Linux armv7l; rv:6.0a1) Gecko/20110510 Firefox/6.0a1 Fennec/6.0a1
Mozilla/5.0 (Windows; U; Windows NT 6.1; fr; rv:1.9.2.18) Gecko/20110614 Mozilla/5.0 (Android; Linux armv7l; rv:5.0) Gecko/20110615 Firefox/5.0 Fennec/5.0
Mozilla/5.0 (Maemo; Linux armv7l; rv:5.0) Gecko/20110615 Firefox/5.0 Fennec/5.0
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:5.0) Gecko/20110517 Firefox/5.0 Fennec/5.0
Mozilla/5.0 (Android; WOW64; Linux armv7l;rv:5.0) Gecko/20110603 Firefox/5.0 Fennec/5.0
Mozilla/5.0 (Android; Linux armv7l;rv:5.0) Gecko/20110603 Firefox/5.0 Fennec/5.0
Mozilla/5.0 (Android; Linux armv7l; rv:5.0) Gecko/20110615 Firefox/5.0 Fennec/5.0
Mozilla/5.0 (Android; Linux armv7l; rv:5.0) Gecko/20110614 Firefox/5.0 Fennec/5.0
Mozilla/5.0 (Android; Linux armv7l; rv:5.0) Gecko/20110517 Firefox/5.0 Fennec/5.0
Mozilla/5.0 (Android; Linux armv71; rv:5.0) Gecko/20110615 Fennec/5.0
Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.2a1pre) Gecko/20110331 Firefox/4.2a1pre Fennec/4.1a1pre
Mozilla/5.0 (Android; Linux armv7l; rv:2.2a1pre) Gecko/20110403 Firefox/4.2a1pre Fennec/4.1a1pre
Mozilla/5.0 (Android; Linux armv7l; rv:2.2a1pre) Gecko/20110402 Firefox/4.2a1pre Fennec/4.1a1pre
Mozilla/5.0 (Maemo; Linux armv7l; rv:2.0b13pre) Gecko/20110315 Firefox/4.0b13pre Fennec/4.0b6pre
Mozilla/5.0 (Android; Linux armv7l; rv:2.0b9pre) Gecko/20110103 Firefox/4.0b9pre Fennec/4.0b4pre
Mozilla/5.0 (Maemo; Linux armv7l; rv:2.0b8pre) Gecko/20110328 Firefox/4.0b8pre Fennec/4.0b3pre
Mozilla/5.0 (X11; Linux x86_64; rv:2.0) Gecko/20110402 Firefox/4.0 Fennec/4.0b3
Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b8) Gecko/20101221 Firefox/4.0b8 Fennec/4.0b3
Mozilla/5.0 (X11; Linux i686; rv:2.0b7pre) Gecko/20101103 Firefox/4.0b8pre Fennec/4.0b2
Mozilla/5.0 (X11; Linux i686; rv:2.1.1) Gecko/20110415 Firefox/4.0.2pre Fennec/4.0.1
Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.1.1) Gecko/20110415 Firefox/4.0.2pre Fennec/4.0.1
Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.1.1) Gecko/20110415 Firefox/4.0.2pre Fennec/4.0.1
Mozilla/5.0 (Windows NT 6.1; rv:2.1.1) Gecko/20110415 Firefox/4.0.2pre Fennec/4.0.1
Mozilla/5.0 (Windows NT 6.0; rv:2.1.1) Gecko/20110415 Firefox/4.0.2pre Fennec/4.0.1
Mozilla/5.0 (Windows NT 5.1; rv:2.1.1) Gecko/20110415 Firefox/4.0.2pre Fennec/4.0.1
Mozilla/5.0 (Linux; U; Android 2.2; en-us; T-Mobile HTC_G2 Build/FRF91) Gecko/20110415 Firefox/4.0.2pre Fennec/4.0.1
Mozilla/5.0 (Android; Linux armv7l; rv:2.1.1) Gecko/20110415 Firefox/4.0.2pre Fennec/4.0.1
Mozilla/5.0 (Android; Linux armv7l; rv:2.1.1) Gecko/20110415 Fennec/4.0.1
Mozilla/5.0 (Android; Linux arm7l; rv:2.1.1) Gecko/20110415 Firefox/4.0.2pre Fennec/4.0.1
Mozilla/5.0 (Android; Linux arm71; rv:2.1.1) Gecko/20110415 Firefox/4.0.2pre Fennec/4.0.1
Mozilla/5.0 (X11; Linux i686; rv:2.1) Gecko/20110318 Firefox/4.0b13pre Fennec/4.0
Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.9.2.13) Gecko/20101203 
Mozilla/5.0 (Android;Linux armv7l;rv:2.1) Gecko/20110318 Firefox/4.0b13pre Fennec/4.0 ( .NET CLR 3.5.30729)
Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.1) Gecko/20110318 Firefox/4.0b13pre Fennec/4.0
Mozilla/5.0 (Windows NT 6.1; rv:2.1) Gecko/20110318 Firefox/4.0b13pre Fennec/4.0
Mozilla/5.0 (Windows NT 5.1; rv:2.1) Gecko/20110318 Firefox/4.0b13pre Fennec/4.0
Mozilla/5.0 (Maemo; Linux armv7l; rv:2.1) Gecko/20110318 Firefox/4.0b13pre Fennec/4.0
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.1) Gecko/20110318 Firefox/4.0b13pre Fennec/4.0
Mozilla/5.0 (Linux arm) Gecko/20110318 Firefox/4.0b13pre Fennec/4.0
Mozilla/5.0 (Android; Linux armv7l; rv:2.1) Gecko/20110318 Firefox/4.0b13pre Fennec/4.0
Mozilla/5.0 (Android; Linux armv7l; rv:2.0) Gecko/20110103 Firefox/4.0 Fennec/4.0
Mozilla/5.0 (Android; Linux armv71; rv:2.1) Gecko/20110318 Firefox/4.0b13pre Fennec/4.0
Mozilla/5.0 (Android) Gecko/20110318 Firefox/4.0 Fennec/4.0
Mozilla/5.0 (Android) Gecko Firefox Fennec/4.0
Mozilla/5.0 (Windows NT 5.1; rv:2.0b6pre) Gecko/20100902 Firefox/4.0b6pre Fennec/2.0b1pre
Mozilla/5.0 (X11; Linux armv7l; rv:2.0b4pre) Gecko/20100818 Firefox/4.0b4pre Fennec/2.0a1pre
Mozilla/5.0 (X11; Linux armv7l; rv:2.0b4pre) Gecko/20100812 Firefox/4.0b4pre Fennec/2.0a1pre
Mozilla/5.0 (X11; Linux armv7l; rv:2.0b3pre) Gecko/20100730 Firefox/4.0b3pre Fennec/2.0a1pre
Mozilla/5.0 (X11; Linux armv71; en-US; rv:2.0b2pre) Gecko/20100722 Firefox/4.0b2pre Fennec/2.0a1pre
Mozilla/5.0 (X11; Linux armv71; rv:2.0b4pre) Gecko/20100818 Firefox/4.0b4pre Fennec/2.0a1pre
Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Fennec/2.0.1
Mozilla/5.0 (X11; U; Linux armv7l; pl-PL; rv:1.9.2.5) Gecko/20100614 Firefox/3.6.5pre Fennec/1.1
Mozilla/5.0 (X11; U; Linux armv7l; en-US; rv:1.9.2a1pre) Gecko/20090322 Fennec/1.0b2pre
Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.8.1.17) Gecko/20080829 Mozilla/5.0 (X11; U; Linux armv7l; en-US; rv:1.9.2a1pre) Gecko/20090322 Fennec/1.0b2pre
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.2a1pre) Gecko/20090626 Fennec/1.0b2
Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2a1pre) Gecko/20090317 Fennec/1.0b1
Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2a1pre) Gecko/20090317 Fennec/1.0b1
Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.1b2pre) Gecko/20081116 Fennec/1.0a2pre
Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081116 Fennec/1.0a2pre
Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2a1pre) Gecko/20081222 Fennec/1.0a2
Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1b4pre) Gecko/20090401 Fennec/1.0a2
Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1b3pre) Gecko/20090106 Fennec/1.0a2
Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.2a1pre) Gecko/20081222 Fennec/1.0a2
Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.2a1pre) Gecko/20081222 Fennec/1.0a2
Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2a1pre) Gecko/20081222 Fennec/1.0a2
Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1
Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1
Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1
Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1
Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1
Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.1b1pre) Gecko/20081005220218 Gecko/2008052201 Fennec/0.9pre
Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.1b1pre) Gecko/20080923171103 Fennec/0.8
Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.1a2pre) Gecko/20080820121708 Fennec/0.7
Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.1a1pre) Gecko/2008071707 Fennec/0.5
Mozilla/5.0 (Windows; U; Windows CE 5.2; en-US; rv:1.9.2a1pre) Gecko/20090210 Fennec/0.11
NokiaE66/GoBrowser/2.0.297
NokiaN81/GoBrowser/2.0.290
NokiaE72/GoBrowser/2.0.290
NokiaC5-00/GoBrowser/2.0.290
Nokia6120c/GoBrowser/2.0.290
Nokia5320XpressMusic/GoBrowser/2.0.290
NokiaN85/GoBrowser/1.6.91
NokiaN81/GoBrowser/1.6.91
NokiaE72/GoBrowser/1.6.91
NokiaC5-00/GoBrowser/1.6.91
Nokia6700s/GoBrowser/1.6.91
Nokia5700XpressMusic/GoBrowser/1.6.91
Nokia5630XpressMusic/GoBrowser/1.6.91
Nokia5320XpressMusic/GoBrowser/1.6.91
NokiaN82/GoBrowser/1.6.86
NokiaE63/GoBrowser/1.6.86
NokiaE5-00/GoBrowser/1.6.86
Nokia6220c/GoBrowser/1.6.86
Nokia6120c/GoBrowser/1.6.86
NokiaN97_mini/GoBrowser/1.6.0.75
NokiaN85/GoBrowser/1.6.0.75
NokiaN78/GoBrowser/1.6.0.75
Nokia5800XpressMusic/GoBrowser/1.6.0.75
Nokia5730XpressMusic/GoBrowser/1.6.0.75
Nokia5320XpressMusic/GoBrowser/1.6.0.75
Nokia5230/GoBrowser/1.6.0.75
NokiaN97_mini/GoBrowser/1.6.0.70
NokiaN81/GoBrowser/1.6.0.70
NokiaN78/GoBrowser/1.6.0.70
Nokia6700s/GoBrowser/1.6.0.70
Nokia6120c/GoBrowser/1.6.0.70
Nokia5320XpressMusic/GoBrowser/1.6.0.70
Nokia5230/GoBrowser/1.6.0.70
NokiaN86_8MP/GoBrowser/1.6.0.4868.208.92;
NokiaN79/GoBrowser/1.6.0.48-cn
NokiaN97_mini/GoBrowser/1.6.0.48
NokiaN82/GoBrowser/1.6.0.48
NokiaN79/GoBrowser/1.6.0.48
Nokia6124c/GoBrowser/1.6.0.48
Nokia6120c/GoBrowser/1.6.0.48
Nokia5530XpressMusic/GoBrowser/1.6.0.48
Nokia5320XpressMusic/GoBrowser/1.6.0.48
Nokia5800XpressMusic/GoBrowser/1.6.0.46
NokiaX6/GoBrowser
NokiaN97_mini/GoBrowser
NokiaN97/GoBrowser
NokiaN95_8GB/GoBrowser
NokiaN95/GoBrowser
NokiaN86_8MP/GoBrowser
NokiaN85/GoBrowser
NokiaN82/GoBrowser
NokiaN81/GoBrowser
NokiaN79/GoBrowser
NokiaN70/GoBrowser
NokiaC6-00/GoBrowser
NokiaC5-00/GoBrowser
Nokia6120c/GoBrowser
Nokia5800XpressMusic/GoBrowser
Nokia5730XpressMusic/GoBrowser
Mozilla/5.0 (Android 2.2; zh-cn; HTC Desire)/GoBrowser
Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)
HTC_Touch_3G Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 7.11)
Mozilla/4.0 (compatible; MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0; Nokia;N70)
Mozilla/5.0 (Windows NT; U; en) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Iris/1.1.7 Safari/525.20
Mozilla/5.0 (X11; U; Linux armv7l; ru-RU; rv:1.9.2.3pre) Gecko/20100723 Firefox/3.5 Maemo Browser 1.7.4.8 RX-51 N900
Mozilla/5.0 (X11; U; Linux armv7l; pt-PT; rv:1.9.2.3pre) Gecko/20100723 Firefox/3.5 Maemo Browser 1.7.4.8 RX-51 N900
Mozilla/5.0 (X11; U; Linux armv7l; no-NO; rv:1.9.2.3pre) Gecko/20100723 Firefox/3.5 Maemo Browser 1.7.4.8 RX-51 N900
MOT-L7/NA.ACR_RB MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1
MOT-L7/08.D5.09R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1
MOT-L7/08.B7.ACR MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1
MOT-L6i/0A.64.19R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1
MOT-L6/0A.60.1BR MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1
MOT-V300/0B.09.19R MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.0
Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025
Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.8) Gecko/20071018 Minimo/0.024
Mozilla/5.0 (X11; U; Linux armv6l; rv: 1.8.1.5pre) Gecko/20070619 Minimo/0.020
Mozilla/5.0 (Windows; Windows; U; Windows NT 5.1; Windows CE 5.2; rv:1.8.1.4pre) Gecko/20070327 Minimo/0.020
Mozilla/5.0 (Windows; U; Windows CE 5.2; rv:1.8.1.4pre) Gecko/20070327 Minimo/0.020
Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1.4pre) Gecko/20070327 Minimo/0.020
Mozilla/5.0 (X11; U; OpenBSD macppc; rv:1.8.1) Gecko/20070222 Minimo/0.016
Mozilla/5.0 (Windows; U; Windows CE 5.2; rv:1.8.1a3) Gecko/20060610 Minimo/0.016
Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016
Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8) Gecko/20060428 Minimo/0.015
Mozilla/5.0 (Windows; U; Windows CE 4.20; rv:1.8) Gecko/20060215 Minimo/0.013
Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007
SAMSUNG-C5212/C5212XDIK1 NetFront/3.4 Profile/MIDP-2.0 Configuration/CLDC-1.1
MozillaMozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.5 (screen 824x1200;rotate)
Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.5 (screen 824x1200;rotate)
Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.5 (screen 824x1200; rotate)
Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.5 (screen 600x800; rotate)
Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.5 (screen 1200x824; rotate)
Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.3 (screen 600x800; rotate)
Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.3 (screen 1200x824; rotate)
Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.1 (screen 824x1200; rotate)
Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.0 (screen 824x1200; rotate)
Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.0 (screen 600x800)
Mozilla/4.0 (compatible; Linux 2.6.10) NetFront/3.4 Kindle/1.0 (screen 600x800)
SonyEricssonK800c/R8BF Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1
SonyEricssonK530i/R6BA Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1
SonyEricssonK530c/R8BA Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1
SonyEricssonK510c/R4EA Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1
Mozilla/4.0 (compatible; Linux 2.6.10) NetFront/3.3 Kindle/1.0 (screen 600x800)
Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.334; U; id) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (J2ME/23.377; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (J2ME/22.478; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/9 (Compatible; MSIE:9.0; iPhone; BlackBerry9700; AppleWebKit/24.746; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (Android; Opera Mini/7.6.35766/35.5706; U; en) Presto/2.8.119 Version/11.10
Opera/9.80 (Android; Opera Mini/7.5.33361/31.1350; U; en) Presto/2.8.119 Version/11.10
Opera/9.80 (Android; Opera Mini/7.29530/27.1407; U; en) Presto/2.8.119 Version/11.10
Opera/9.80 (iPhone; Opera Mini/7.1.32694/27.1407; U; en) Presto/2.8.119 Version/11.10
Opera/9.80 (iPad; Opera Mini/7.1.32694/27.1407; U; en) Presto/2.8.119 Version/11.10
Opera/9.80 (Series 60; Opera Mini/7.1.32444/35.5706; U; en) Presto/2.8.119 Version/11.10
Opera/9.80 (Series 60; Opera Mini/7.1.32444/35.2883; U; ru) Presto/2.8.119 Version/11.10
Opera/9.80 (J2ME/MIDP; Opera Mini/7.1.32052/35.5706; U; id) Presto/2.8.119 Version/11.10
Opera/9.80 (iPhone; Opera Mini/7.0.4/28.2555; U; fr) Presto/2.8.119 Version/11.10
Opera/9.80 (Android; Opera Mini/7.0.29952/28.2075; U; es) Presto/2.8.119 Version/11.10
Opera/9.80 (Series 60; Opera Mini/6.5.29702/28.2647; U; es) Presto/2.8.119 Version/11.10
Opera/9.80 (J2ME/MIDP; Opera Mini/6.5.26955/27.1407; U; en) Presto/2.8.119 Version/11.10
Opera/9.80 (J2ME/MIDP; Opera Mini/6.24288/25.729; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (BlackBerry; Opera Mini/6.24209/27.1366; U; en) Presto/2.8.119 Version/11.10
Opera/9.80 (Series 60; Opera Mini/6.24096/25.657; U; id) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/6.24093/26.1305; U; en) Presto/2.8.119 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/6.24093/25.657; U; id) Presto/2.5.25 Version/10.54
Opera/9.80 (Series 60; Opera Mini/6.1.25759/25.872; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/6.1.25378/25.677; U; th) Presto/2.5.25 Version/10.54
Opera/9.80 (Android; Opera Mini/6.1.25375/25.657; U; es) Presto/2.5.25 Version/10.54
Opera/9.80 (Series 60; Opera Mini/6.0.24455/28.2766; U; en) Presto/2.8.119 Version/11.10
Opera/9.80 (Android;Opera Mini/6.0.24212/24.746 U;en) Presto/2.5.25 Version/10.5454
Opera/9.80 (Series 60; Opera Mini/6.0.24095/24.760; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (Series 60; Opera Mini/6.0.24095/24.741; U; zh) Presto/2.5.25 Version/10.54
Opera/9.80 (Series 60; Opera Mini/5.1.22784/23.334; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (Series 60; Opera Mini/5.1.22784/22.394; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (Series 60; Opera Mini/5.1.22784/22.387; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (Series 60; Opera Mini/5.1.22783/23.334; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (Series 60; Opera Mini/5.1.22783/22.478; U; id) Presto/2.5.25 Version/10.54
Opera/9.80 (Series 60; Opera Mini/5.1.22783/22.478; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (Android; Opera Mini/5.1.22460/23.334; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (Android; Opera Mini/5.1.22460/22.478; U; fr) Presto/2.5.25 Version/10.54
Opera/9.80 (Android; Opera Mini/5.1.22460/22.414; U; de) Presto/2.5.25 Version/10.54
Opera/9.80 (Series 60; Opera Mini/5.1.22396/22.478; U; id) Presto/2.5.25 Version/10.54
Opera/9.80 (BlackBerry; Opera Mini/5.1.22303/22.387; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.22296; BlackBerry9800; U; AppleWebKit/23.370; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.22296/22.87; U; fr) Presto/2.5.25
Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.22296/22.87; U; en) Presto/2.5.25
Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.22296/22.478; U; fr) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.22296/22.387; U; fr) Presto/2.5.25 Version/10.54
Opera/9.50 (J2ME/MIDP; Opera Mini/5.1.21965/20.2513; U; en)
Opera/9.80 (Windows Mobile; Opera Mini/5.1.21595/25.657; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (Windows Mobile; Opera Mini/5.1.21594/22.387; U; ru) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.21415/22.387; U; en) Presto/2.5.25 Version/10.54
Opera/10.61 (J2ME/MIDP; Opera Mini/5.1.21219/19.999; en-US; rv:1.9.3a5) WebKit/534.5 Presto/2.6.30
Opera/9.80(J2ME/MIDP; Opera Mini/5.1.21214/22.414; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.21214/22.414; U; ro) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.21214/22.387; U; id) Presto/2.5.25 Version/10.54
Opera/9.80 (Android; Opera Mini/5.1.21126/19.892; U; de) Presto/2.5.25
Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.21051/27.1573; U; en) Presto/2.8.119 Version/11.10
Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.21051/23.377; U; id) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.21051/20.2477; U; en) Presto/2.5.25
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.3521/886; U; en) Presto/2.4.15
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.3521/22.414; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.3521/18.684; U; en) Presto/2.4.15
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.22349/37.6584; U; en) Presto/2.12.423 Version/12.16
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.20873/19.916; U; en) Presto/2.5.25
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.19693Mod.by.Handler/23.390; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.19693Mod.by.Handler/18.794; U; id) Presto/2.4.15
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.19693/870; U; en) Presto/2.4.15
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.19683/1278; U; ko) Presto/2.2.0
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18741Mod.by.Handler/22.414; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18741/886; U; id) Presto/2.4.15
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18741/886; U; en) Presto/2.4.15
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18741/870; U; fr) Presto/2.4.15
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18741/870; U; en) Presto/2.4.15
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18741/18.794; U; en) Presto/2.4.15
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18635Mod.by.Handler/23.377; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (Windows NT 5.1; U; Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18635/1030; U; en) Presto/2.4.15; ru) Presto/2.8.99 Version/11.10
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18635/886; U; en) Presto/2.4.15
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.17443/886; U; en) Presto/2.4.15
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.17443/20.2477; U; en) Presto/2.5.25
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.17381/886; U; en) Presto/2.4.15
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.16823Mod.by.Handler/22.387; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.16823/870; U; en) Presto/2.4.15
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.15650/20.2479; U; en) Presto/2.5.25
Opera/9.80 (J2ME/iPhone;Opera Mini/5.0.019802/886; U; ja)Presto/2.4.15
Opera/9.80 (J2ME/iPhone;Opera Mini/5.0.019802/886; U; ja)Presto/ 2.4.15
Opera/9.80 (J2ME/iPhone;Opera Mini/5.0.019802/886; U; ja) Presto/2.4.15
Opera/9.80 (iPhone; Opera Mini/5.0.019802/886; U; ja) Presto/2.4.15
Opera/9.80 (iPhone; Opera Mini/5.0.019802/886; U; en) Presto/2.4.15
Opera/9.80 (iPhone; Opera Mini/5.0.019802/22.414; U; de) Presto/2.5.25 Version/10.54
Opera/9.80 (iPhone; Opera Mini/5.0.019802/18.738; U; en) Presto/2.4.15
Opera/9.80 (iPhone; Opera Mini/5.0.0176/764; U; en) Presto/2.4.154.15
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.0.862 Profile/24.743; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.0.423 Profile/18.684; U; en) Presto/2.4.15
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.0.351 Profile/22.478; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0/870; U; en) Presto/2.4.15
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0(Windows; U; Windows NT 5.1; en-US)/23.390; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows; U; Windows NT 6.1; sv-SE) AppleWebKit/23.411; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/24.838; U; id) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/23.411; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/22.478; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/23.377; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows NT 6.1; WOW64) AppleWebKit/23.411; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (SymbianOS/24.838; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Linux; U; Android 2.2; fr-lu; HTC Legend Build/24.838; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Linux; U; Android 2.2; en-sa; HTC_DesireHD_A9191 Build/24.741; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (iPhone; U; xxxx like Mac OS X; en) AppleWebKit/24.838; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (iPhone; U; fr; CPU iPhone OS 4_2_1 like Mac OS X; fr) AppleWebKit/23.405; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/23.411; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/23.377; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (BlackBerry; U; BlackBerry9800; en-GB) AppleWebKit/24.783; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (BlackBerry; U; BlackBerry 9800) AppleWebKit/24.783; U; es) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.5.33867/35.2883; U; en) Presto/2.8.119 Version/11.10
Opera/9.80 (J2ME/MIDP; Opera Mini/4.4.Vista/19.916; U; en) Presto/2.5.25
Opera/9.80 (J2ME/MIDP; Opera Mini/4.4.29476/27.1573; U; id) Presto/2.8.119 Version/11.10
Opera/9.80 (J2ME/MIDP; Opera Mini/4.4.26736/28.2647; U; it) Presto/2.8.119 Version/11.10
Opera/9.80 (J2ME/MIDP; Opera Mini/4.4.0.60 (Windows XP)/886; U; en) Presto/2.4.15
Opera/9.80 (J2ME/MIDP; Opera Mini/4.3.24214; iPhone; CPU iPhone OS 4_2_1 like Mac OS X; AppleWebKit/24.783; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.3.24214/27.1407; U; id) Presto/2.8.119 Version/11.10
Opera/9.80 (J2ME/MIDP; Opera Mini/4.3.24214 (Windows; U; Windows NT 6.1) AppleWebKit/24.838; U; id) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.3.13337/25.657; U; ro) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.24721/30.3316; U; en) Presto/2.8.119 Version/11.10
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.23453/28.2647; U; en) Presto/2.8.119 Version/11.10
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.21465/22.478; U; id) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.21465/22.387; U; id) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.19634/23.333; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.18887/22.478; U; id) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.16320/29.3594; U; en) Presto/2.8.119 Version/11.10
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.16007Mod.by.Handler/23.390; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15410QUAIN/22.478; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15410Mod.by.Handler/23.334; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15410Mod.by.Handler/23.333; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15410Mod.by.Handler/22.401; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15410Mod.by.Handler/20.2485; U; en) Presto/2.5.25
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15410Mod.by.Handler/18.678; U; en) Presto/2.4.15
Opera/9.60 (J2ME/MIDP;Opera Mini/4.2.15410Mod.by.Handler/503; U; en)Presto/2.2.0
Opera/9.50 (J2ME/MIDP; Opera Mini/4.2.15410Mod.by.Handler/20.2590; U; en)
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15410/870; U; en) Presto/2.4.15
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15410/24.899; U; id) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15410/22.394; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15066/886; U; en) Presto/2.4.15
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912mod.By.onome/22.401; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912Mod.by.Handler/24.783; U; id) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912Mod.by.Handler/23.377; U; id) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912Mod.By.www.9jamusic.cz.cc/22.387; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912/870; U; id) Presto/2.4.15
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912/35.5706; U; id) Presto/2.8.119 Version/11.10
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912/24.746; U; id) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912/23.334; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912/23.333; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912/22.394; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14885/20.2485; U; zh) Presto/2.5.25
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14881Mod.by.Handler/24.743; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14881Mod.by.Handler/23.317; U; id) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14753/20.2485; U; zh) Presto/2.5.25
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14409/20.2485; U; zh) Presto/2.5.25
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14320/886; U; id) Presto/2.4.15
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14320/22.478; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14320/20.2485; U; zh) Presto/2.5.25
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.13943/20.2485; U; zh) Presto/2.5.25
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.13918/22.414; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.13400/20.2485; U; zh) Presto/2.5.25
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.13337.Mod.by.Handler/870; U; en) Presto/2.4.15
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.13337/886; U; en) Presto/2.4.15
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.13337/870; U; en) Presto/2.4.15
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.13337/19.916; U; en) Presto/2.5.25
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.13265/870; U; ro) Presto/2.4.15
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.13221/886; U; en) Presto/2.4.15
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.13221/870; U; en) Presto/2.4.15
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.13057/870; U; ja) Presto/2.4.15
Opera/9.80 (J2ME/MIDP; Opera Mini/4.2 19.42.55/19.892; U; en) Presto/2.5.25
Opera/9.80 (J2ME/MIDP; Opera Mini/4.18061/27.1407; U; en) Presto/2.8.119 Version/11.10
Opera/9.80 (J2ME/MIDP; Opera Mini/4.1.15082/870; U; en) Presto/2.4.15
Opera/9.80 (J2ME/MIDP; Opera Mini/4.1.15082/25.677; U; vi) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.1.15082/20.2489; U; en) Presto/2.5.25
Opera/9.80 (J2ME/MIDP; Opera Mini/4.1.14287/22.387; U; id) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.1.13907/21.529; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.1.13573/20.2485; U; zh) Presto/2.5.25
Opera/9.80 (J2ME/MIDP; Opera Mini/4.1.12965/19.892; U; en) Presto/2.5.25
Opera/9.80 (J2ME/MIDP; Opera Mini/4.1.11321/24.871; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.0.8462/22.414; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.0.8462/19.916; U; en) Presto/2.5.25
Opera/9.80 (J2ME/MIDP; Opera Mini/4.0.10247/19.916; U; en) Presto/2.5.25
Opera/9.80 (J2ME/MIDP; Opera Mini/4.0.10031/22.453; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.0/886; U; en) Presto/2.4.15
Opera/9.80 (J2ME/MIDP; Opera Mini/4.0/870; U; id) Presto/2.4.15
Opera/9.80 (J2ME/MIDP; Opera Mini/4.0/22.453; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.0/22.401; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.0/22.394; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.11) Gecko/23.390; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.0 (Linux; U;
Opera/9.80 (J2ME/MIDP; Opera Mini/4.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/23.411; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.0 (compatible; MSIE 5.0; UNIX) Opera 6.12 [en]/24.838; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/4.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/24.705; U; en) Presto/2.5.25 Version/10.54
Opera/9.60 (J2ME/MIDP; Opera Mini/4.0/490; U; en) Presto/2.2.0
Opera/9.80 (J2ME/MIDP; Opera Mini/3.1.10423/22.387; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/1.6.0_13/22.478; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/1.6.0_13/19.916; U; en) Presto/2.5.25
Opera/9.80 (Series 60; Opera Mini/1.0.30710/29.3594; U; en) Presto/2.8.119 Version/11.10
Opera/9.80 (J2ME/MIDP; Opera Mini/1.0/886; U; en) Presto/2.4.15
Opera/9.80 (J2ME/MIDP; Opera Mini/SymbianOS/22.478; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/Nokia2730c-1/22.478; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/Mozilla/23.334; U; en) Presto/2.5.25 Version/10.54
Opera/9.80 (J2ME/MIDP; Opera Mini/(Windows; U; Windows NT 5.1; en-US) AppleWebKit/23.411; U; en) Presto/2.5.25 Version/10.54
Opera/12.02 (Android 4.1; Linux; Opera Mobi/ADR-1111101157; U; en-US) Presto/2.9.201 Version/12.02
Opera/9.80 (Android 2.3.3; Linux; Opera Mobi/ADR-1111101157; U; es-ES) Presto/2.9.201 Version/11.50
Opera/9.80 (S60; SymbOS; Opera Mobi/SYB-1107071606; U; en) Presto/2.8.149 Version/11.10
Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10
Opera/9.80 (Android 2.2.1; Linux; Opera Mobi/ADR-1107051709; U; pl) Presto/2.8.149 Version/11.10
Opera/9.80 (S60; SymbOS; Opera Mobi/SYB-1104061449; U; da) Presto/2.7.81 Version/11.00
Opera/9.80 (S60; SymbOS; Opera Mobi/SYB-1103211396; U; es-LA) Presto/2.7.81 Version/11.00
Opera/9.80 (Android; Linux; Opera Mobi/ADR-1012221546; U; pl) Presto/2.7.60 Version/10.5
Opera/9.80 (Android 2.2;;; Linux; Opera Mobi/ADR-1012291359; U; en) Presto/2.7.60 Version/10.5
Opera/9.80 (Android 2.2; Opera Mobi/ADR-2093533608; U; pl) Presto/2.7.60 Version/10.5
Opera/9.80 (Android 2.2; Opera Mobi/-2118645896; U; pl) Presto/2.7.60 Version/10.5
Opera/9.80 (Android 2.2; Linux; Opera Mobi/ADR-2093533312; U; pl) Presto/2.7.60 Version/10.5
Opera/9.80 (Android 2.2; Linux; Opera Mobi/ADR-2093533120; U; pl) Presto/2.7.60 Version/10.5
Opera/9.80 (Android 2.2; Linux; Opera Mobi/8745; U; en) Presto/2.7.60 Version/10.5
Opera/9.80 (S60; SymbOS; Opera Mobi/1209; U; sk) Presto/2.5.28 Version/10.1
Opera/9.80 (S60; SymbOS; Opera Mobi/1209; U; fr) Presto/2.5.28 Version/10.1
Opera/9.80 (S60; SymbOS; Opera Mobi/1181; U; en-GB) Presto/2.5.28 Version/10.1
Opera/9.80 (Android; Linux; Opera Mobi/ADR-1012211514; U; en) Presto/2.6.35 Version/10.1
Opera/9.80 (Android; Linux; Opera Mobi/ADR-1011151731; U; de) Presto/2.5.28 Version/10.1
Opera/9.80 (S60; SymbOS; Opera Mobi/498; U; sv) Presto/2.4.18 Version/10.00
Opera/9.80 (S60; SymbOS; Opera Mobi/447; U; en) Presto/2.4.18 Version/10.00
Mozilla/4.0 (compatible; Windows Mobile; WCE; Opera Mobi/WMD-50433; U; de) Presto/2.4.13 Version/10.00
Opera/9.80 (Android; Linux; Opera Mobi/ADR-1012272315; U; pl) Presto/2.7.60 Version/10.5
Opera/9.80 (Windows NT 6.1; Opera Mobi/49; U; en) Presto/2.4.18 Version/10.00
Opera/9.80 (Windows NT 6.0; Opera Mobi/49; U; en) Presto/2.4.18 Version/10.00
Opera/9.80 (Windows NT 5.1; Opera Mobi/49; U; en) Presto/2.4.18 Version/10.00
Opera/9.80 (Windows Mobile; WCE; Opera Mobi/49; U; en) Presto/2.4.18 Version/10.00
Opera/9.80 (Macintosh; Intel Mac OS X; Opera Mobi/3730; U; en) Presto/2.4.18 Version/10.00
Opera/9.80 (Macintosh; Intel Mac OS X; Opera Mobi/27; U; en) Presto/2.4.18 Version/10.00
Opera/9.80 (Linux i686; Opera Mobi/1040; U; en) Presto/2.5.24 Version/10.00
Opera/9.80 (Linux i686; Opera Mobi/1038; U; en) Presto/2.5.24 Version/10.00
Opera/9.80 (Android; Linux; Opera Mobi/49; U; en) Presto/2.4.18 Version/10.00
Opera/9.80 (Android; Linux; Opera Mobi/27; U; en) Presto/2.4.18 Version/10.00
Mozilla/5.0 (S60; SymbOS; Opera Mobi/SYB-1103211396; U; es-LA; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.00
Mozilla/5.0 (S60; SymbOS; Opera Mobi/1209; U; it; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 10.1
Mozilla/5.0 (S60; SymbOS; Opera Mobi/1181; U; en-GB; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 10.1
Mozilla/5.0 (Linux armv7l; Maemo; Opera Mobi/4; U; fr; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 10.1
Mozilla/5.0 (Linux armv6l; Maemo; Opera Mobi/8; U; en-GB; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.00
Mozilla/5.0 (Android 2.2.2; Linux; Opera Mobi/ADR-1103311355; U; en; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.00
Mozilla/4.0 (compatible; MSIE 8.0; S60; SymbOS; Opera Mobi/SYB-1107071606; en) Opera 11.10
Mozilla/4.0 (compatible; MSIE 8.0; Linux armv7l; Maemo; Opera Mobi/4; fr) Opera 10.1
Mozilla/4.0 (compatible; MSIE 8.0; Linux armv6l; Maemo; Opera Mobi/8; en-GB) Opera 11.00
Mozilla/4.0 (compatible; MSIE 8.0; Android 2.2.2; Linux; Opera Mobi/ADR-1103311355; en) Opera 11.00
SonyEricssonW800i/R1BD001/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1
SonyEricssonW800c/R1L Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1
SonyEricssonW800c/R1BC Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1
SonyEricssonW800c/R1AA Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1
SonyEricssonW700c/R1DB Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1
SonyEricssonW700c/R1CA Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1
SonyEricssonK750c/R1DB Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1
SonyEricssonK750c/R1CA Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1
SonyEricssonK750c/R1BC Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1
SonyEricssonK700c/R2CA SEMC-Browser/4.0.3 Profile/MIDP-2.0 Configuration/CLDC-1.1
SonyEricssonK700c/R2AE SEMC-Browser/4.0.3 Profile/MIDP-2.0 Configuration/CLDC-1.1
SonyEricssonK500c/R2AT SEMC-Browser/4.0.3 Profile/MIDP-2.0 Configuration/CLDC-1.1
SonyEricssonK300c/R2BA SEMC-Browser/4.0.3 Profile/MIDP-2.0 Configuration/CLDC-1.1
SonyEricssonJ300c/R2BA SEMC-Browser/4.0.3 Profile/MIDP-2.0 Configuration/CLDC-1.1
SonyEricssonK506c/R2AA SEMC-Browser/4.0.2 Profile/MIDP-2.0 Configuration/CLDC-1.1
SonyEricssonS700i/R3B SEMC-Browser/4.0.1 Profile/MIDP-2.0 Configuration/CLDC-1.1
SonyEricssonS700c/R3B SEMC-Browser/4.0.1 Profile/MIDP-2.0 Configuration/CLDC-1.1
SonyEricssonK500c/R2L SEMC-Browser/4.0.1 Profile/MIDP-2.0 Configuration/CLDC-1.1
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7; en-us) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Safari/530.17 Skyfire/2.0
Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en) AppleWebKit/418.9.1 (KHTML, like Gecko) Safari/419.3 TeaShark/0.8
Mozilla/5.0 (compatible; Teleca Q7; Brew 3.1.5; U; en) 480X800 LGE VX11000
Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; WOW64; Trident/4.0; uZardWeb/1.0; Server_USA)
Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; WOW64; Trident/4.0; uZardWeb/1.0; Server_KO_KTF)
Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; WOW64; Trident/4.0; uZard/1.0; Server_KO_SKT)
Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; WOW64; SV1; uZardWeb/1.0; Server_HK)
Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; WOW64; SV1; uZardWeb/1.0; Server_EN)
Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; WOW64; SV1; uZardWeb/1.0; Server_CN)
Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; SV1; uZardWeb/1.0; Server_JP)

proxy_loading = input("[1] Load Proxys from APIs\n[2] Load Proxys from proxys.txt\n")

token = input("ID?\n")
class main(object):
    def __init__(self):
        self.combolist = Queue()
        self.Writeing = Queue()
        self.printing = []
        self.botted = 0
        self.combolen = self.combolist.qsize()

    def printservice(self): #print screen
        while True:
            if True:
                os.system(clear)
                print(Fore.LIGHTCYAN_EX + intro + Fore.LIGHTMAGENTA_EX)
                print(
                    Fore.LIGHTCYAN_EX + f"Botted:{self.botted}\n")
                for i in range(len(self.printing) - 10, len(self.printing)):
                    try:
                        print(self.printing[i])
                    except (ValueError, Exception):
                        pass
                time.sleep(0.5)
a = main()
class proxy():
    global proxy_loading
    def update(self):
        while True:

            if proxy_loading == "2":
                data = ''
                data = open("proxys.txt", "r").read()
                self.splited += data.split("\n") #scraping and splitting proxies
            else:
                data = ''
                urls = ["https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt","https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&ssl=yes","https://www.proxy-list.download/api/v1/get?type=https&anon=elite"]
                for url in urls:
                    try:
                        data += requests.get(url).text
                        self.splited += data.split("\n")
                        self.splited = [s.replace('\r', "") for s in self.splited]
                    except:
                        print("Proxy loading failed!")
                        pass
            time.sleep(600)

    def get_proxy(self):
        random1 = random.choice(self.splited) #choose a random proxie
        return random1
    def FormatProxy(self):
	    proxyOutput = {'https' :'https://'+self.get_proxy()}
	    return proxyOutput

    def __init__(self):
        self.splited = []
        threading.Thread(target=self.update).start()
        time.sleep(3)

proxy1 = proxy()
def bot():
    while True:
        try:
            ua = random.choice(iPhone_UA)
            s = requests.session()
            random_proxy = proxy1.FormatProxy()

            resp = s.get("https://m.youtube.com/watch?v=" + token + "?disable_polymer=1",headers={'Host': 'https://www.youtube.com', 'Proxy-Connection': 'Keep-Alive', 'User-Agent': ua, 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7', 'Accept-Encoding': 'gzip, deflate', 'Cache-Control': 'no-cache', 'Pragma': 'no-cache'},proxies=random_proxy)   # simple get request to youtube for the base URL
            url = resp.text.split(r'videostatsWatchtimeUrl\":{\"baseUrl\":\"')[1].split(r'\"}')[0].replace(r"\\u0026",r"&").replace('%2C',",").replace("\/","/")  #getting the base url for parsing
            cl = url.split("cl=")[1].split("&")[0] #parsing some infos for the URL
            ei = url.split("ei=")[1].split("&")[0]
            of = url.split("of=")[1].split("&")[0]
            vm = url.split("vm=")[1].split("&")[0]
            s.get("https://s.youtube.com/api/stats/watchtime?ns=yt&el=detailpage&cpn=isWmmj2C9Y2vULKF&docid=" + token + "&ver=2&cmt=7334&ei=" + ei + "&fmt=133&fs=0&rt=1003&of=" + of +"&euri&lact=4418&live=dvr&cl=" + cl + "&state=playing&vm=" + vm + "&volume=100&c=MWEB&cver=2.20200313.03.00&cplayer=UNIPLAYER&cbrand=apple&cbr=Safari%20Mobile&cbrver=12.1.15E148&cmodel=iphone&cos=iPhone&cosver=12_2&cplatform=MOBILE&delay=5&hl=ru&cr=GB&rtn=1303&afmt=140&lio=1556394045.182&idpj=&ldpj=&rti=1003&muted=0&st=7334&et=7634",headers={'Host': 's.youtube.com', 'Proxy-Connection': 'Keep-Alive', 'User-Agent': ua, 'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5', 'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Referer': 'https://m.youtube.com/watch?v=' + token},proxies=random_proxy)   # API GET request

            a.botted += 1
        except:
            pass



maxthreads = int(input("How many Threads? Recommended: 500 - 1000\n"))

threading.Thread(target=a.printservice).start()
num = 0
while num < maxthreads :
    num += 1
    threading.Thread(target=bot).start()


threading.Thread(target=bot).start()
