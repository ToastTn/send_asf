import requests
import time
import json 
import re 


welcome ='''                                                                                                       _ _                   
 _____ _____ ____  _____    _____ __ __            _   _                  _    _       _   _ _       _| | |_ ___ ___ ___ ___ 
|     |  _  |    \|   __|  | __  |  |  |   ___ ___| |_| |___    _ _ _ ___| |  | |_ ___| |_|_| |_ ___|_     _|_  |_  |_  |  _|
| | | |     |  |  |   __|  | __ -|_   _|  | . | .'| . | | . |  | | | | -_| |  | '_| -_|  _| | . | .'|_     _| | |  _|_  |_  |
|_|_|_|__|__|____/|_____|  |_____| |_|    |  _|__,|___|_|___|  |_____|___|_|  |_,_|___|_| |_|___|__,| |_|_|   |_|___|___|___|
                                          |_|                                                                                '''


def sendMessage(token, channel_id, message):
    url = 'https://discord.com/api/v9/channels/{}/messages'.format(channel_id)
    data = {"content": message}
    header = {"authorization": token}
    r = requests.post(url, data=data, headers=header)
    #print(r.status_code)
    data = json.loads(r.text)
    message_id = data["id"]
    url_del = url + "/" + message_id
    
    r_del = requests.delete(url_del,headers=header)
    #print(r_del.status_code)
    

def start_bot(my_token,channel_id):
    while True:
        for token in my_tokens.values():
            #print(token)
            sendMessage(token,channel_id,"hi")
        time.sleep(60)

my_tokens = { "Luca_Theo" : "ODUxOTMzNjQ1MTAyNzc2Mzcw.Ygu2kA.F8tDwJNGnCNuRhCscJKI-0IYwOs", 
#"plermo" : "OTQ1ODAyMjc0ODE3NTkzNDA2.YhVdfw.t86vlm1kj7aNEb23SZe9fba1tkI",
"tmatem" : "NTM3OTI2MjU0MjkzNDE3OTg1.YhVojQ.rNgvo6utw6on4F6o1TxENOZX8X0",
"bilsol" : "OTUzNjEyMTM5MzYzNDY3Mjk0.YjpHzA.RmWFzpPHBOJLmR_7fi3EgFIXI9o",
"xnoor" : "OTUyODcxNjQyOTE5NDczMTk0.YjpKeQ.5dStDWuRr63xJSUvwczMjDMxNbk",
"solpl" : "OTUzNjEwMDA3NDgyNjA5NjY0.YjpKHQ.1-F6nf5SVdctvczJDO1V6DibpUQ",
"hediwl" : "OTU3Mzk2Mjk3ODAxOTMyOTAw.Yj-Q6w.GoS2XghkwLUmqW_cfXxMXdehano",
"bilbasse" : "OTU3Mzk4MjAwNjczNzkyMDQw.Yj-SAw.5okJsIhuuSSx801Q0Jb8tFupOL4",
"armsl" : "OTU3NDAxNzU3OTU1MjgwOTg2.Yj-S-w.YP8vlBmzieCscabRCOAa6e2N2js",
"pablo_wel_ketiba" : "mfa.F0_UW_F_A_jHAImMfpD8gapOVSV2vXeATbLXUXxRkCEEohI187UGrdoE-SOozC2MPtsw7ASZ7XLpqTcR95Wl",
"tmatemtal" : "OTU3Mzk0MTE5MDcwNzQ0NjI3.Yj-P6A.V5g0mGWuMkQeVbmZBf8LiPVJiSc",
"PASTArk" : "ODUzMzAyMjA0MzA3MzQxMzI3.Yjm_QQ.WQ5XF2w5XNMToty_GfkDP61muQU"}

hhhh =''' "poor_sol_token" : "OTQ5OTk4OTg4OTk4OTAxNzky.YiSh3A.Qw4ZKqX7TAWbEmN2YoeDLDko5ac",
"lorenzo_token" : "OTUwMDE0MDMyNzE3NDQzMDgy.YiSvzw.lsAJjSNU2DWNGdlhfWE51fb2OV0",
"i_buy_the_dip" : "mfa.WOHEFq00mZe-A6SV2EbziXxbE9uhHKr5RhrqNRnoDe65Lsn-H9KUw36TaxELbgjjmm8v9pNVupcooZgmcrd3",
#"dump_it" : "OTUwMDA0NjI1ODA3OTI1MjQ4.Yjh01g.iUC5vTWeQYnUwX9rVG2ZAe2B-ec",
#"pablo" : "OTQ5OTkwMTEwNDYyNjIzNzk1.Yjh7_A.yWOukA6ekxQUm051MHXiu2qZosM",
"rayen1" : "OTUyODcxNjQyOTE5NDczMTk0.YjG8NQ.X0kEykMFNx3-ZnFtxKXFwBGnVvg",
"rayen2" : "OTUzNjEwMDA3NDgyNjA5NjY0.YjHE7Q.KqxsqxB5kC7GyoSnh7uD_OQQxq4",
"rayen3" : "OTUzNjEyMTM5MzYzNDY3Mjk0.YjHG6g.bVTZKf2nlO8qCWSo2O-qcqccmOc",
"pablo_wel_ketiba" : "mfa.F0_UW_F_A_jHAImMfpD8gapOVSV2vXeATbLXUXxRkCEEohI187UGrdoE-SOozC2MPtsw7ASZ7XLpqTcR95Wl",
"dotsol" : "mfa.GzFzhaTnEHe1Kgd_0DZRrOcjmoH6olQy1WwaSIVv3XiQM4Ujgmzpr-YPw0n_Jl8Ry4jQfZP6lzUxTkeE8jjA"}

my_tokens = {"tmatemtal" : "OTU3Mzk0MTE5MDcwNzQ0NjI3.Yj-P6A.V5g0mGWuMkQeVbmZBf8LiPVJiSc",
"hediwl14@gmail.com" : "OTU3Mzk2Mjk3ODAxOTMyOTAw.Yj-Q6w.GoS2XghkwLUmqW_cfXxMXdehano",
"bilbasse" : "OTU3Mzk4MjAwNjczNzkyMDQw.Yj-SAw.5okJsIhuuSSx801Q0Jb8tFupOL4",
"armsl" : "OTU3NDAxNzU3OTU1MjgwOTg2.Yj-S-w.YP8vlBmzieCscabRCOAa6e2N2js",
"pablo_wel_ketiba" : "mfa.F0_UW_F_A_jHAImMfpD8gapOVSV2vXeATbLXUXxRkCEEohI187UGrdoE-SOozC2MPtsw7ASZ7XLpqTcR95Wl",
"PASTArk" : "ODUzMzAyMjA0MzA3MzQxMzI3.Yjm_QQ.WQ5XF2w5XNMToty_GfkDP61muQU"}
#"dotsol" : "mfa.GzFzhaTnEHe1Kgd_0DZRrOcjmoH6olQy1WwaSIVv3XiQM4Ujgmzpr-YPw0n_Jl8Ry4jQfZP6lzUxTkeE8jjA",
#"Luca_Theo_token" : "ODUxOTMzNjQ1MTAyNzc2Mzcw.Ygu2kA.F8tDwJNGnCNuRhCscJKI-0IYwOs", 
#"plermo_token" : "OTQ1ODAyMjc0ODE3NTkzNDA2.YhVdfw.t86vlm1kj7aNEb23SZe9fba1tkI",
#"tmatem_token" : "NTM3OTI2MjU0MjkzNDE3OTg1.YhVojQ.rNgvo6utw6on4F6o1TxENOZX8X0",
#"poor_sol_token" : "OTQ5OTk4OTg4OTk4OTAxNzky.YiSh3A.Qw4ZKqX7TAWbEmN2YoeDLDko5ac",
#"lorenzo_token" : "OTUwMDE0MDMyNzE3NDQzMDgy.YiSvzw.lsAJjSNU2DWNGdlhfWE51fb2OV0",
#"i_buy_the_dip" : "mfa.WOHEFq00mZe-A6SV2EbziXxbE9uhHKr5RhrqNRnoDe65Lsn-H9KUw36TaxELbgjjmm8v9pNVupcooZgmcrd3",
#"rayen1" : "OTUyODcxNjQyOTE5NDczMTk0.YjG8NQ.X0kEykMFNx3-ZnFtxKXFwBGnVvg",
#"rayen2" : "OTUzNjEwMDA3NDgyNjA5NjY0.YjHE7Q.KqxsqxB5kC7GyoSnh7uD_OQQxq4",
#"rayen3" : "OTUzNjEyMTM5MzYzNDY3Mjk0.YjHG6g.bVTZKf2nlO8qCWSo2O-qcqccmOc"}

#"jawad_token" : "OTUxNDk4NDMxNjkwNTg0MTQ2.YitBkQ.C4dUBVcNRXGu--FHuUjSj3YH4x8" '''


crypto_coral_trab_id ="817630414428307456"

komradz_id = "963679665602584696"
asba = "913305586467229726"
my_token = "ODUzMzAyMjA0MzA3MzQxMzI3.Yjm_QQ.WQ5XF2w5XNMToty_GfkDP61muQU"
MMCc = "913305586467229726"
print(welcome)
start_bot(my_tokens,komradz_id)

 