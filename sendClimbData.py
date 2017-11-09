import requests

data = {
'__RequestVerificationToken':'vWGur0948kxFP2CJYx_Z7jzvUFQ6fwORaeFyzcCut3aflC9Ije5yTVq1_oL-dMkWWFKJQt_QkOLvySenl8VTOXCYroG9QZgLMdsamgE6D6JT_9V439nZsnCqNIRRebIr2k1s4SUcX45htrFEtd_HnA2',
'Problem.Holdsetup.Id':'1',
'Problem.Name':'NN2',
'Problem.Grade':'6B+',
'Problem.Method':'',
'Problem.MoonBoardConfiguration.Id':'',
'Problem.Id':'',
'hidHoldset':'3,4,5',
'Problem.Holdsets[0].Description':'Original School Holds',
'Problem.Holdsets[1].Description':'Hold Set A',
'Problem.Holdsets[2].Description':'Hold Set B',
'Problem.Moves[0].Description':'F5',
'Problem.Moves[0].IsStart':'true',
'Problem.Moves[1].Description':'F10',
'Problem.Moves[2].Description':'G18',
'Problem.Moves[2].IsEnd':'true',
'Problem.Moves[3].Description':'G16'
}

post_url='https://www.moonboard.com/Problems/Create'

Cookie= {
	'__RequestVerificationToken':'pyZsWOXYthUrg8Z9sOPZnfO2HsKGcVrPiAVGg8o3B5-vB66DSkw5zIPwnWI6nQMR_QCq_9_f0v1JnABI7Xi-kY_uGSB_-h05N_ENXZVr3aw1',
	'.AspNet.TwoFactorRememberBrowser':'y3p1cw0BbS-Vy-bFCBC1PtH3dsTnMucxcJC16JmUrZaC5J1eKPh_jNIO2dsKAx_TXKPifphzh1_JRXPn7IWYsxC2DxHb2RKXga568FtLbLctJXGOsYpC3BBx3fNbp6AL03M9jav7fmArLJqUcTmtrPwsDtGfPdMWbzns7W5LeX6yQ1m5CQza64GaGpByBBFLGarRUhl3HUs79qehRWc6SkHBYNN4y8S8RA9Zilmtm9fy5q792pJI8BKG_GQdE5zKmgOfCqHPCoFJRUmcveBMwtUZsGLfzfZY9tAcufwHPGi0wEcO208p6tZaxivM2BZ8TA2QYSoyO31a6xdDMBLRVfT3_QFewJMUMgx-vrULTds',
	'_MoonBoard':'KMA6YxmO8Kxd3FmnNm4uIM1GX20c1T-yP2SkEwArWTja_ocXYkEL2mEwGAwP4_9oTDUl9L0t4gnfpSv-2An2ZZXPKJshWqv6kCxCPuPcosbeQmFdTzd4FLsNb9Qx8spkv6i7SplF7aB-g-dDu2J3gs3bt6KzffLQqVEH9ca5Fs7R2Z471vTpCMqvVxoLiB8qjiS3zQji2WlPzhNE4uix-NVXV5qoMQw4jRLWhwv94gUsDJsPjEIqF3U0xPDsoZiCd-OotM_-WasYKpjjBqPuIpA3jLlPzO6XYIclvKnsrshu9KqWiTAlsyJhp93WnjCkTne9u8-tL1apxXK7SD0RuT8BUSjSFFtZZ53QCEGSu9FrKMVinF8ksu_CBInPe3RK2UYPPzo7QIElcYgUHUy2ruvzMO-kzjzD7F7d3r9p27JWZ04B172qTxO9dmkG7p4g2KF8FDP3MqNoHWwV8wyCeDpmbRKoyC6dca5wCP_kmtwoUzPrXSfvOfJhvXYdtufS'
}

r=requests.post(post_url,data=data,cookies=Cookie)
print(r.status_code, r.reason)
print(r.text)