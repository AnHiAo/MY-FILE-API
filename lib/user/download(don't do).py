import requests
from datetime import datetime
import re
def calc_divisional_range(filesize, chuck=10):
    step = filesize//chuck
    arr = list(range(0, filesize, step))
    result = []
    for i in range(len(arr)-1):
        s_pos, e_pos = arr[i], arr[i+1]-1
        result.append([s_pos, e_pos])
        result[-1][-1] = filesize-1
    return result
def range_download(url,save_name, s_pos, e_pos):
    headers = {
    "Range": f"bytes={ s_pos}-{ e_pos}"}
    res = requests.get(url, headers=headers, stream=True)
    f  = open(save_name, "rb+")
    f.seek(s_pos)
    for chunk in res.iter_content(chunk_size=64*1024):
        if chunk:
            f.write(chunk)
    f.close()
mainData =[
    "https://files.yande.re/image/b68cbe2502b8fb890025b439d1a3e487/yande.re%20853389%20alexanderdinh%20anus%20ass%20christmas%20cum%20horns%20naked%20nipples%20penis%20pussy%20sex%20topless.jpg",
    "https://files.yande.re/image/0585d644dfbf4ebae049d0fe0f911bfd/yande.re%20853388%20alexanderdinh%20christmas%20horns%20no_bra%20pantsu.jpg",
    "https://files.yande.re/image/94b42a8937fa7a8361668ecf1a84fce5/yande.re%20853385%20azur_lane%20feet%20hood_%28azur_lane%29%20kome_cola%20naked%20nipples%20pubic_hair%20pussy%20tagme%20uncensored.jpg",
    "https://files.yande.re/jpeg/2e26652c2d72b34510c69231c1726668/yande.re%20853384%20angel%20arknights%20horns%20mostima_%28arknights%29%20see_through%20shokuyou_koori%20tail.jpg",
    "https://files.yande.re/jpeg/4e3a2b08c2b93174a887892d72df0bcf/yande.re%20853383%20angel%20arknights%20fishnets%20horns%20mostima_%28arknights%29%20see_through%20shokuyou_koori%20tail.jpg",
    "https://files.yande.re/jpeg/88fafc96c62d91d5cd998d6a94796020/yande.re%20853382%20angel%20blue_archive%20horns%20megane%20pantyhose%20pointy_ears%20seifuku%20shiromi_iori%20skirt_lift%20sorasaki_hina%20stockings%20sweater%20tagme%20thighhighs%20wings.jpg",
    "https://files.yande.re/image/70bc254684420d85a12f9cc46770e927/yande.re%20853379%20ceres_fauna%20cleavage%20dress%20hana3901%20hololive%20horns%20thighhighs.jpg",
    "https://files.yande.re/jpeg/0eec9a989e33fbd3489d096c91d98434/yande.re%20853378%20bang_dream%21%20maid%20maruyama_aya%20nogi_momoko.jpg",
    "https://files.yande.re/image/dc8e112607d93bd70869b156945e80db/yande.re%20853376%20feet%20genshin_impact%20hong_bai%20pantyhose%20sangonomiya_kokomi.jpg",
    "https://files.yande.re/image/d17afdb1ed5985e58b079b71effc76c8/yande.re%20853375%20feet%20genshin_impact%20hong_bai%20pantyhose%20sangonomiya_kokomi.jpg",
    "https://files.yande.re/image/b1a8c8e40c935fc9f082afb8e2191fd9/yande.re%20853373%20463_jun%20animal_ears%20azur_lane%20bunny_ears%20chikuma_%28azur_lane%29%20no_bra%20pantsu%20skirt_lift%20sword%20thighhighs.jpg",
    "https://files.yande.re/jpeg/18b08d218948d1d2c953ef04de22826a/yande.re%20853372%20ass%20azur_lane%20belfast_%28azur_lane%29%20breasts%20enterprise_%28azur_lane%29%20garter%20horns%20leotard%20lordol%20no_bra%20symmetrical_docking%20thighhighs.jpg",
    "https://files.yande.re/jpeg/6896948c600d487c51029edc758d47ea/yande.re%20853371%20animal_ears%20artist_revision%20bunny_ears%20bunny_girl%20dstwins97%20no_bra%20pantyhose.jpg",
    "https://files.yande.re/image/309c7af2b12a985323860ed650de2756/yande.re%20853366%20aegir_%28azur_lane%29%20azur_lane%20horns%20no_bra%20pantyhose%20see_through%20shigatsu_%284gate%29.jpg",
    "https://files.yande.re/image/0f9f085b334353edc4fa392b47620167/yande.re%20853364%20anus%20ass%20ayanami_%28azur_lane%29%20azur_lane%20breasts%20censored%20nipples%20no_bra%20nopan%20pussy%20ryara_vivi%20seifuku%20shirt_lift%20skirt_lift%20thighhighs.jpg",
    "https://files.yande.re/image/27f067361aa60ff901a74643ae94e869/yande.re%20853363%20ass%20ayanami_%28azur_lane%29%20azur_lane%20cameltoe%20no_bra%20pantsu%20ryara_vivi%20seifuku%20skirt_lift%20thighhighs%20underboob.jpg",
    "https://files.yande.re/image/bf216ac7403e9f6e68aa1be82d351df6/yande.re%20853362%20hajirau_kimi_ga_mitainda%20honjou_natsuho%20megane%20no_bra%20open_shirt%20umagome_rakure.jpg",
    "https://files.yande.re/image/8fcd772344360487fb0f02e5f6749f8b/yande.re%20853361%20bikini_top%20hololive%20maid%20minato_aqua%20pixiv44198374%20swimsuits%20thighhighs.jpg",
    "https://files.yande.re/jpeg/875cb8f6c73a642c0828d9234032c97a/yande.re%20853360%20asian_clothes%20genshin_impact%20keqing_%28genshin_impact%29%20pantyhose%20pixiv44198374%20skirt_lift.jpg",
    "https://files.yande.re/jpeg/2a97ab406468ed3a6f1dc3b6b8adcbf7/yande.re%20853359%20asian_clothes%20genshin_impact%20keqing_%28genshin_impact%29%20pantyhose%20pixiv44198374%20skirt_lift.jpg",
    "https://files.yande.re/jpeg/a5440a759efa0bc757128871d23be217/yande.re%20853358%20asian_clothes%20feet%20ganyu_%28genshin_impact%29%20genshin_impact%20horns%20leotard%20no_bra%20pantyhose%20pixiv44198374.jpg",
    "https://files.yande.re/jpeg/3e8daf9c8728da578df9d2aae3c26e96/yande.re%20853357%20asian_clothes%20feet%20ganyu_%28genshin_impact%29%20genshin_impact%20horns%20leotard%20no_bra%20pantyhose%20pixiv44198374.jpg",
    "https://files.yande.re/image/4612c3b5600850ca0b2497b6127291dd/yande.re%20853356%20bikini%20hololive%20narukamiarei%20oozora_subaru%20swimsuits%20wet.jpg",
    "https://files.yande.re/image/505064d3f868614d4a48ea09b4690605/yande.re%20853355%20animal_ears%20cleavage%20raindrop746079%20satono_diamond_%28umamusume%29%20school_swimsuit%20swimsuits%20uma_musume_pretty_derby.jpg",
    "https://files.yande.re/image/a25ae22d9ef8150f652f2846280084f0/yande.re%20853352%20azur_lane%20bikini%20formidable_%28azur_lane%29%20qiao_gongzi%20swimsuits.jpg",
    "https://files.yande.re/image/429791c1c2a0af4ea6600e58f2df56ba/yande.re%20853351%20fuwafuwa-chan%2A%2A%20hatsune_miku%20vocaloid.jpg",
    "https://files.yande.re/image/b5b40fc6d35577dd0be50d288c88692b/yande.re%20853350%20cosplay%20dress%20ganyu_%28genshin_impact%29%20genshin_impact%20hestia_%28dungeon%29%20horns%20no_bra%20tutsucha_illust.jpg",
    "https://files.yande.re/jpeg/db965e929de2176d272b199cde0da6d0/yande.re%20853349%20animal_ears%20azur_lane%20bunny_ears%20bunny_girl%20cameltoe%20fishnets%20lomocya%20no_bra%20shimakaze_%28azur_lane%29%20thighhighs.jpg",
    "https://files.yande.re/image/06d1a6e8dbc46b8e7d2130fc39c86386/yande.re%20853348%20animal_ears%20no_bra%20pantsu%20shirt_lift%20tail%20thighhighs%20tutsucha_illust%20wallpaper.jpg",
    "https://files.yande.re/jpeg/6dcade76ca5843d8029e98603d3a4f30/yande.re%20853345%20animal_ears%20bunny_ears%20bunny_girl%20fishnets%20no_bra%20pantyhose%20tooga_mashiro.jpg",
    "https://files.yande.re/jpeg/4bcabbe548946844aeee4a435bd206c0/yande.re%20853344%20nanohana_kohina%20nurse%20skirt_lift%20thighhighs%20wings.jpg",
    "https://files.yande.re/jpeg/56c0dc87bacadcde41a784ce80828a83/yande.re%20853343%20364%20ayanami_rei%20bodysuit%20neon_genesis_evangelion.jpg",
    "https://files.yande.re/image/70ce9c864338c3caf53fa18e1cb8798c/yande.re%20853342%20alter_%28kxk7357%29%20animal_ears%20bikini%20open_shirt%20satono_diamond_%28umamusume%29%20swimsuits%20uma_musume_pretty_derby.jpg",
    "https://files.yande.re/jpeg/e62a8251f020c7ae7448be4526f74534/yande.re%20853341%20azur_lane%20bikini_top%20breast_hold%20censored%20cum%20paizuri%20penis%20renetan%20swimsuits%20taihou_%28azur_lane%29.jpg",
    "https://files.yande.re/jpeg/a2ec789a0ccd5e48908761636b7c31b8/yande.re%20853340%20angel%20blue_archive%20bra%20hayase_yuuka%20narynn%20pantsu.jpg",
    "https://files.yande.re/jpeg/923f0bddd873349aa40724833cb7bffe/yande.re%20853339%20angel%20blue_archive%20bra%20hayase_yuuka%20narynn%20pantsu.jpg",
    "https://files.yande.re/jpeg/54bbff51b2961723b2fc338acee55a9b/yande.re%20853338%20animal_ears%20ass%20comeback_magnum%20feet%20mayano_top_gun_%28umamusume%29%20pantsu%20seifuku%20skirt_lift%20uma_musume_pretty_derby.jpg",
    "https://files.yande.re/jpeg/0052c05163d18325e51846bb6695245c/yande.re%20853337%20animal_ears%20ass%20comeback_magnum%20feet%20mayano_top_gun_%28umamusume%29%20pantsu%20seifuku%20skirt_lift%20thighhighs%20uma_musume_pretty_derby.jpg",
    "https://files.yande.re/image/bd7ed00105e0d2d6cebc198361665a52/yande.re%20853336%20beijiushui%20eyepatch%20genshin_impact%20no_bra%20signora_%28genshin_impact%29.jpg",
    "https://files.yande.re/jpeg/a925a4d2d3b9b6a91f8f139e93b0548d/yande.re%20853335%20animal_ears%20bunny_ears%20bunny_girl%20dstwins97%20hololive%20no_bra%20pantyhose%20usada_pekora.jpg"
]
for d in mainData:

    save_name = "imgs/"+re.search(r'[^\/]+$',d).group(0)
    f = open(save_name,"wb")
    f.close()
    beforeTime = datetime.now()
    print(d)
    res = requests.get(d,headers={"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate, br","accept-language":"zh-CN,zh;q=0.9","cache-control":"no-cache","pragma":"no-cache","sec-ch-ua":"\"Google Chrome\";v=\"93\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"93\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\"","sec-fetch-dest":"document","sec-fetch-mode":"navigate","sec-fetch-site":"none","sec-fetch-user":"?1","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"})
    divisional_ranges = calc_divisional_range(int(res.headers["Content-Length"]))
    # for s_pos, e_pos in divisional_ranges:
    #     range_download(save_name, s_pos, e_pos)
    from concurrent.futures import ThreadPoolExecutor, as_completed
    with ThreadPoolExecutor() as p:
        futures = []
        for s_pos, e_pos in divisional_ranges:
            print(s_pos, e_pos)
            futures.append(p.submit(range_download, d,save_name, s_pos, e_pos))
            as_completed(futures)
        for future in as_completed(futures):
            data = future.result()
            print(f"main: {data}")
        nowTime = datetime.now()
        print(nowTime-beforeTime)