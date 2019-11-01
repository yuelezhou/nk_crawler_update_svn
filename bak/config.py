#-*- coding:utf-8 -*-
from fake_useragent import UserAgent
from easydict import EasyDict as edict
import datetime
today = datetime.date.today()
yesterday = str(today - datetime.timedelta(days=1))
today = str(today)

# default settings
default = edict()

default.start_time = "05:00:00"
default.file_path = r'./data'
default.save_path = r'./data_result'
default.interactive_file = 'result_merge.xls'
default.choice_run = '1'                       #'1': run all!，‘2’run single choice

# driver settings  （linux or winsows ）
config = edict()
config.driver_windows = r'chromedriver.exe'
config.driver_linux = r'./chromedriver'

# search keywords

include_keys = ['中国','翔安']
exclude_keys = ['废标']
#exclude_add_list = ['维修']

#include_keys = ['银行', '外包', '人力', '开发', '测试', '保险', '扫描', '录入', '入围']

# exclude_keys = ['废标', '餐厅','餐饮','食品','保证金专户','保证金银行','银行账号','股份转让','开户银行','账户资金',
#            '装修',  '修缮', '食堂', '装饰', '律师', '律所', '转让', '厨房设施', '保洁', '保安', '体检','公务车辆','宣传品',
#            '资格考试', '培训', '招聘', '办公楼', '软装', '租赁', '服装', '排水', '拍摄', '宣传', '施工','电梯','布线',
#            '地板', '耗材', '空调', '家具', '煤']
#
# exclude_add_list = ['维修', '空气', '工装', '采暖', '急救', '发电机','工作服',
#                     '绿化', '公厕', '天然气', '消防', '农田', '拍卖', '土地',
#                     '分红','股权','水土','失败','房产处置','门面处置','花卉',
#                     '电池','双肩包','礼品','机具','道路','住房贷款','作废','债权',
#                     '安置房','栽培','抵债','厕所','棚改项目','债权处置']
# exclude_keys.extend(exclude_add_list)

#信息集合
information = {#"jincai_1" : {"original_url" : "http://www.cfcpn.com/plist/caigou?pageNo=1&kflag=0&keyword=&keywordType=0&province=&city=&typeOne=&ptpTwo=,", "csv" : "1.csv", "classname" : "Loop1"}, #金采网,
                #"CaiGouYuZhaoBiao_02" : "", #采购与招标网
               #"zhongguozhaobiaoyucaigouwang_3" : {"original_url":"http://www.gc-zb.com/search/index.html?page=1&keyword={}&h_lx={}&h_province=0&vague=0&date=1&search_field=1", "csv":"3.csv", "classname":"Loop3"}, #中国招标与采购网
               #"zhonguozhengfucaigouwang_4" : {"original_url" : "http://search.ccgp.gov.cn/bxsearch?searchtype=1&page_index=1&bidSort=0&buyerName=&projectId=&pinMu=0&bidType=1&dbselect=bidx&kw={}&start_time=2019%3A07%3A28&end_time=2019%3A07%3A31&timeType=3&displayZone=&zoneId=&pppStatus=0&agentName=", "csv" : "4.csv", "classname" : "Loop4"}, #中国政府采购网
               #"zhongguoyidong_5" : {"original_url" : "https://b2b.10086.cn/b2b/main/listVendorNoticeResult.html?noticeBean.noticeType=2", "csv" : "5.csv", "classname" : "Loop5"}, #中国移动采购与招标网  Pipeline_02
               #"guodian_7" : {"original_url" : "http://www.cgdcbidding.com/zbgg/index_%d.jhtml", "csv" : "7.csv", "classname" : "Loop7"}, #国电招投标网
               #"beijingshizhengfucaigouwang_8" : {"original_url" : "http://www.ccgp-beijing.gov.cn/xxgg/{}/index.html", "csv" : "8.csv", "classname" : "Loop8"}, #北京市政府采购网
               #"zhonghua_9" : {"original_url" : "http://e.sinochemitc.com/cms/channel/ywgg1qb/index.htm?keyword=", "csv" : "9.csv", "classname" : "Loop9"},  #中化招标平台
               #"renbao_10" : {"original_url" : "http://caigou.epicc.com.cn/epp-esp/notice/noticePageList?title={}&newsType={}&sendTimeMin=&sendTimeMax=&page=1", "csv" : "10.csv", "classname" : "Loop10"}, #人保
               #"guoshou_11" : {"original_url" : "http://cpmsx.e-chinalife.com/xycms/cggg/index.jhtml", "csv" : "11.csv", "classname" : "Loop11"}, #国寿
               #"anbang_12" : {"original_url" : "http://ab.anbanggroup.com/abjr/cgyb/index", "csv" : "12.csv", "classname" : "Loop12"}, #安邦
               #"taikang_13" : {"original_url" : "http://eps.taikang.com/ggxx/index_", "csv" : "13.csv", "classname" : "Loop13"}, #泰康
               #"changchengzichan_14" : {"original_url" : "http://www.gwamcc.com/Hiring.aspx?liName=119", "csv" : "14.csv", "classname" : "Loop14"}, #长城资产
               #"xinda_15" : {"original_url" : "", "csv" : "15.csv", "classname" : "Loop15"}, #信达资产
               #"yangguang_16" : {"original_url" : "http://sunshine-eps.sinosig.com/search_1.jspx?seachname=%E6%90%9C+%E7%B4%A2&q={}", "csv" : "16.csv", "classname" : "Loop16"},#阳光保险
               #"chukouxinyong_17" : {"original_url" : "http://www.sinosure.com.cn/gywm/gsjj/xxpl/jzcg/index", "csv" : "17.csv", "classname" : "Loop17"},#出口信用保险
               #"HuaHai_18" : {"original_url" : "", "csv" : "18.csv", "classname" : "Loop18"},#华海
               #"zhongxin_19" : {"original_url" : "http://www.bidding.citic/news_list2/&FrontNews_list01-1450865603055_pageNo=", "csv" : "19.csv", "classname" : "Loop19"},#中信招标
               #"zhongzhengxinxi_20" : {"original_url" : "http://www.csits.org.cn/csits/zbxm/hydt.shtml", "csv" : "20.csv", "classname" : "Loop20"},#中证信息
               #"guojiadianwang_21" : {"original_url" : "http://ecp.sgcc.com.cn/project_list.jsp?site=global&column_code=014002007&project_type=2", "csv" : "21.csv", "classname" : "Loop21"},#国家电网
               #"guohang_22" : {"original_url" : "http://www.airchina.com.cn/cn/contact_us/cgpt/cgxmgg/index.shtml", "csv" : "22.csv", "classname" : "Loop22"},#国航
               #"youzheng_23" : {"original_url" : "http://www.chinapost.com.cn/html1/category/181313/7345-1.htm", "csv" : "23.csv", "classname" : "Loop23"},#邮政系统
               #"tietagongsi_24" : {"original_url" : "http://www.tower.com.cn/default/main/index/cn.chinatowercom.obp.main.index.obphomepage.queryNoticeDetails.biz.ext", "csv" : "24.csv", "classname" : "Loop24"},#铁塔公司
               #"ZhongGuoDianZiJinChuKou_26" : {"original_url" : "https://www.ceiec.com.cn/notice?page={}", "csv" : "26.csv", "classname" : "Loop26"},#中国电子进出口有限公司
               #"ZhongGuoDianWang_27" : {"original_url" : "http://www.cpeinet.com.cn/cpcec/bul/bul_list.jsp?&PageIndex=1&name={}&beginTime={}&endTime={}", "csv" : "27.csv", "classname" : "Loop27"},#中国电网注册信息
               #"chengEzhaobiaowang_28" : {"original_url" : "https://www.chengezhao.com/cms/channel/ywgg/index.htm?pageNo=1", "csv" : "28.csv", "classname" : "Loop28"},#诚E招标网
               #"NeiMengGuZhaoBiaoTouBiaoWang_29" : {"original_url" : "http://www.nmgztb.com.cn/search?titleLike={}&pageNo=1&infoType=11&pageSize=10&publisTimeRangeType=0", "csv" : "29.csv", "classname" : "Loop29"},#内蒙古招标投标网
               #"sinochemitc" : {"original_url" : "http://e.sinochemitc.com/cms/channel/ywgg1qb/index.htm?pageNo=1", "csv" : "30.csv", "classname" : "Test"}, #中化
               #"zhongguorenminbaoxian" : {"original_url" : "http://caigou.epicc.com.cn/epp-esp/notice/noticePageList?", "csv" : "31.csv", "classname" : "Test"},#中国人民财产保险
               #"neimengguzhaobiao" : {"original_url" : "http://zbgg.nmgztb.com.cn/xxfbcms/category/bulletinList.html?", "csv" : "32.csv", "classname" : "Test"},#内蒙古招标投标网
               #"shangdongcaigouyuzhaobiao" : {"original_url" : "https://www.sdbidding.org.cn/bulletins?", "csv" : "33.csv", "classname" : "Test"},#山东省采购与招标网
               #"shanxishenzhaobiaogonggongfuwupingtai" : {"original_url" : "http://www.sxbid.com.cn/f/list-6796f0c147374f85a50199b38ecb0af6.html?", "csv" : "34.csv", "classname" : "Test"},#山西省招标投标公共服务平台
               #"zhongyuanzhaocai" : {"original_url" : "http://www.zybtp.com/ggxx/index.jhtml", "csv" : "35.csv", "classname" : "Test"},#中原招采网
               #"heibeishenzhaobiaotoubiao" : {"original_url" : "http://www.hebeieb.com/tender/xxgk/list.do?selectype=zbgg", "csv" : "36.csv", "classname" : "Test"},#河北省招标投标公共服务平台
              
               #"heilongjiangcaigou" : {"original_url" :{"type":"onclick",
                                                        #"onclick":[{"button":"//*[@id='confive1']/div[2]/a","params":[],"url":"http://www.hljcg.gov.cn/welcome.jsp?dp=23"}
                                                                   #],
                                                        #},
                                       #"csv" : "heilongjiangcaigou.csv", 
                                       #"classname" : "Test"},#黑龙江政府采购网  
               #"guangdongshenzhengfucaigou" : {"original_url" :{"type":"onclick",
                                                                #"onclick":[{"button":"//*[@id='regionULId']/li[23]/a",
                                                                            #"params":[],
                                                                            #"url":"http://www.ccgp-guangdong.gov.cn/queryMoreInfoList/channelCode/0005.html"}
                                                                           #],
                                                                #},
                                       #"csv" : "guangdongshenzhengfucaigou.csv", 
                                       #"classname" : "Test"},#广东省政府采购网 
               #




                # zl execl的第三列
                #"zhonggangzhaobiaoyouxianzerengongsi" :{"original_url" : "http://tendering.sinosteel.com/zgzb/zbzq/005001/secondPage.html" , "csv" : "zhonggangzhaobiaoyouxianzerengongsi.csv" , "classname" : "Test","type":"招标" },#1中港招标有限责任公司
                #"zhonggangzhaobiaoyouxianzerengongsi2" :{"original_url" : "http://tendering.sinosteel.com/zgzb/zbzq/005004/secondPage2.html" , "csv" : "zhonggangzhaobiaoyouxianzerengongsi2.csv" , "classname" : "Test","type":"中标" },#1中港招标有限责任公司
                #"taipingyangbaoxian" :{"original_url" : "http://purchase.cpic.com.cn/cms/channel/ywgg/index.htm" , "csv" : "taipingyangbaoxian.csv" , "classname" : "Test","type":"招标" },#2太平洋保险
                #"tianjinshizhengfucaigoupingtai" :{"original_url" : "http://60.30.25.51/portal/topicView.do?method=find" , "csv" : "tianjinshizhengfucaigoupingtai.csv" , "classname" : "Test","type":"" },#3天津市政府采购网
                #"neimengguzizhiqugonggongziyuanjiaoyiwang": {"original_url" : "http://ggzyjy.nmg.gov.cn/jyxx/jsgcZbgg" , "csv" : "neimengguzizhiqugonggongziyuanjiaoyiwang.csv" , "classname" : "Test","type":"招标" },#4内蒙古自治区公共资源交易网
                #"neimengguzizhiqugonggongziyuanjiaoyiwang2": {"original_url" : "http://ggzyjy.nmg.gov.cn/jyxx/jsgcZbhxrgs" , "csv" : "neimengguzizhiqugonggongziyuanjiaoyiwang2.csv" , "classname" : "Test","type":"中标" },#4-2内蒙古自治区公共资源交易网
                #"shandongshengzhengfucaigouxinxigongkaipingtai": {"original_url" : "http://www.ccgp-shandong.gov.cn/sdgp2017/site/channelall.jsp?colcode=0301" , "csv" : "shandongshengzhengfucaigouxinxigongkaipingtai.csv" , "classname" : "Test","type":"招标" },#5山东省政府采购信息公开平台
                #"shandongshengzhengfucaigouxinxigongkaipingtai2": {"original_url" : "http://www.ccgp-shandong.gov.cn/sdgp2017/site/channelall.jsp?colcode=0302" , "csv" : "shandongshengzhengfucaigouxinxigongkaipingtai2.csv" , "classname" : "Test","type":"中标" },#5-2山东省政府采购信息公开平台
                #"shanghaigonggongziyuanjiaoyiwang" : {"original_url" : "http://www.zgazxxw.com/sh-000012.html" , "csv" : "shanghaigonggongziyuanjiaoyiwang.csv" , "classname" : "Test" ,"type":""},#7上海公共资源交易网
                #"zhejiangshenggonggongziyuanjiaoyiwang" : {"original_url" : "http://new.zmctc.com/zjgcjy/jyxx/004001/004001003/?Paging=1" , "csv" : "zhejiangshenggonggongziyuanjiaoyiwang.csv" , "classname" : "Test","type":"招标" },#8浙江省公共资源交易网
                #"zhejiangshenggonggongziyuanjiaoyiwang2" : {"original_url" : "http://new.zmctc.com/zjgcjy/jyxx/004010/004010003/?Paging=1" , "csv" : "zhejiangshenggonggongziyuanjiaoyiwang2.csv" , "classname" : "Test","type":"中标" },#8-2浙江省公共资源交易网
                #"jiangsuzhengfucaigouwang" : {"original_url" : "http://www.ccgp-jiangsu.gov.cn/ggxx/gkzbgg/index.html" , "csv" : "jiangsuzhengfucaigouwang.csv" , "classname" : "Test","type":"招标" },#9江苏政府采购网
                #"jiangsuzhengfucaigouwang2" : {"original_url" : "http://www.ccgp-jiangsu.gov.cn/ggxx/zbgg/index.html" , "csv" : "jiangsuzhengfucaigouwang2.csv" , "classname" : "Test","type":"中标" },#9-2江苏政府采购网
                # "xiamenshigongongziyuanjiaoyiwang" : {"original_url" :{"type":"onclick",
                #                                       "onclick":[{"button":'//*[@id="searchMoreContent"]/a',"params":[],"url":"http://www.xmzyjy.cn/XmUiForWeb2.0/xmebid/default.do"}], },
                #                                       "csv" : "xiamenshigongongziyuanjiaoyiwang.csv","classname" : "Test","type":"招标"},#10厦门政府采购网

                # "xiamenshigongongziyuanjiaoyiwang2" : {"original_url" :{"type":"onclick",
                #                                       "onclick":[{"button":['//*[@id="noticeTypeList"]/li[6]','//*[@onclick="clickMore(3)"]'],"params":[],"url":"http://www.xmzyjy.cn/XmUiForWeb2.0/xmebid/default.do"}], },
                #                                       "csv" : "xiamenshigongongziyuanjiaoyiwang2.csv","classname" : "Test","type":"中标"},#10-2厦门政府采购网
                 #"guangxizhaobiaotoubiaogonggongfuwupingtai" : {"original_url" : "http://zbtb.gxi.gov.cn:9000/xxfbcms/category/bulletinList.html?dates=300&categoryId=88&tabName=%E6%8B%9B%E6%A0%87%E5%85%AC%E5%91%8A&page=1&showStatus=1" , "csv" : "guangxizhaobiaotoubiaogonggongfuwupingtai.csv" , "classname" : "Test","type":"招标" },#11 广西招标投标公共服务平台
                 #"guangxizhaobiaotoubiaogonggongfuwupingtai2" : {"original_url" : "http://zbtb.gxi.gov.cn:9000/xxfbcms/category/resultBulletinList.html?searchDate=1994-10-30&dates=300&word=&categoryId=90&industryName=&area=&status=&publishMedia=&sourceInfo=&showStatus=&page=1" , "csv" : "guangxizhaobiaotoubiaogonggongfuwupingtai2.csv" , "classname" : "Test","type":"中标" },#11-2 广西招标投标公共服务平台
                #"hainanshenggonggongziyuanjiaoyiwang": {"original_url": "http://www.zgazxxw.com/wap/hi-001012.html","csv": "hainanshenggonggongziyuanjiaoyiwang.csv", "classname": "Test","type":""},  # 12 海南省公共资源交易网
                #"hunanguolianzhaobiaoyouxiangongsi": {"original_url": "https://hnglzb.dlzb.com/fuwu/","csv": "hunanguolianzhaobiaoyouxiangongsi.csv", "classname": "Test","type":"招标"},  # 13 湖南国联招标有限公司
                #"anzhaocai": {"original_url": "http://www.anzhaocai.com/Transaction?","csv": "anzhaocai2.csv", "classname": "Test","type":"招标"},  # 14 安招采
                #"jiangxiguozhengzhaobiaoyouxiangongsi": {"original_url": "http://www.jxgzzb.com.cn/Index/notice/inftype/1/page/1.html","csv": "jiangxiguozhengzhaobiaoyouxiangongsi.csv", "classname": "Test","type":"招标"},  # 15 江西国政招标有限公司
                #"jiangxiguozhengzhaobiaoyouxiangongsi2": {"original_url": "http://www.jxgzzb.com.cn/notice/2.html","csv": "jiangxiguozhengzhaobiaoyouxiangongsi2.csv", "classname": "Test","type":"中标"},  # 15 江西国政招标有限公司
                #"yunnanshengzhengfucaigouwang": {"original_url": "http://www.yngp.com/bulletin.do?method=moreList","csv": "yunnanshengzhengfucaigouwang.csv", "classname": "Test","type":"招标"},  # 16 云南省政府采购网

                # "yunnanshengzhengfucaigouwang" : {"original_url" :{"type":"onclick",
                #                                                       "onclick":[{"button":'/html/body/div[3]/div[2]/div[2]/div[1]/div/a',"params":[],"url":"http://www.yngp.com/login.do?method=beginlogin&menuSelect=nav1"}], },
                #                                                       "csv" : "yunnanshengzhengfucaigouwang.csv","classname" : "Test","type":"招标"},#16 云南省政府采购网-test
                #"lasagonggongziyuanjiaoyiwang": {"original_url": "http://ggzy.lasa.gov.cn/Category/More?id=643&typeId=0","csv": "lasagonggongziyuanjiaoyiwang.csv", "classname": "Test","type":"招标"},  # 17拉萨公共资源交易网
                #"lasagonggongziyuanjiaoyiwang2": {"original_url": "http://ggzy.lasa.gov.cn/Category/More?id=661&typeId=0","csv": "lasagonggongziyuanjiaoyiwang2.csv", "classname": "Test","type":"中标"},  # 17-2拉萨公共资源交易网
                #"chengdushigonggongziyuanjiaoyizhongxin": {"original_url": "https://www.cdggzy.com/site/JSGC/List.aspx","csv": "chengdushigonggongziyuanjiaoyizhongxin.csv", "classname": "Test","type":"招标"},  # 18 成都市公共资源交易服务中心
                #"zhongguoyouzheng": {"original_url": "http://www.chinapost.com.cn/html1/category/181313/7338-1.htm","csv": "zhongguoyouzheng.csv", "classname": "Test","type":"招标"},  # 19 中国邮政
                #"zhongguoyouzheng2": {"original_url": "http://www.chinapost.com.cn/html1/category/181313/7334-1.htm","csv": "zhongguoyouzheng2.csv", "classname": "Test","type":"中标"},  # 19-2 中国邮政
                #"bingtuanzhengfucaigouwang": {"original_url": "http://cgw.xjbt.gov.cn/cggg/index.shtml","csv": "bingtuanzhengfucaigouwang.csv", "classname": "Test","type":"招标"},  # 20 兵团政府采购网
               }

# province and area settings
p1 = '''
东城区　西城区　崇文区　宣武区　朝阳区　海淀区　丰台区　房山区　通州区 顺义区　
昌平区　大兴区　怀柔区　平谷区　密云县　延庆县门头沟区　石景山区
'''
p2 = '''
和平区　河东区　河西区　南开区　河北区　红桥区　塘沽区　汉沽区　大港区 东丽区　
西青区　北辰区　津南区　武清区　宝坻区　静海县　宁河县　蓟　县
'''
p3 = '''辛集市　藁城市　晋州市　新乐市　鹿泉市　平山县　井陉县　栾城县　正定县
行唐县　灵寿县　高邑县　赵　县　赞皇县　深泽县　无极县　元氏县　唐山市  大厂县
遵化市　迁安市　迁西县　滦南县　玉田县　唐海县　乐亭县　滦县　  昌黎县
卢龙县　抚宁县　邯郸市　武安市　邯郸县　永年县　曲周县　馆陶县　魏县
成安县　大名县　涉县  　鸡泽县　邱县　  广平县　肥乡县　临漳县　磁县
邢台市　南宫市　沙河市　邢台县　柏乡县　任县　  清河县　宁晋县　威县
隆尧县　临城县　广宗县　临西县　内丘县　平乡县　巨鹿县　新河县　南和县
保定市　涿州市　定州市　安国市　满城县　清苑县　涞水县　阜平县　徐水县
定兴县　唐县　  高阳县　容城县　涞源县　望都县　安新县　易县　 曲阳县
蠡县　  顺平县　博野县　雄　县　宣化县　康保县　张北县　阳原县　赤城县
沽源县　怀安县　怀来县　崇礼县　尚义县　蔚县  　涿鹿县　万全县　承德市
承德县　兴隆县　隆化县　平泉县　滦平县　沧州市　泊头市　任丘市　黄骅市
河间市　沧县　  青县　  献县　  东光县　海兴县　盐山县　肃宁县　南皮县
吴桥县　廊坊市　霸州市　三河市　固安县　永清县　香河县　大城县　文安县
衡水市　冀州市　深州市　饶阳县　枣强县　故城县　阜城县　安平县　武邑县
景县　  武强县　石家庄市　张家口市　高碑店市　秦皇岛市　大厂回族自治县
青龙满族自治县　丰宁满族自治县　宽城满族自治县　孟村回族自治县
围场满族蒙古族自治县　
'''
p4 = '''
太原市　古交市　阳曲县　清徐县　娄烦县　大同市　大同县　天镇县　灵丘县
阳高县　左云县　广灵县　浑源县　阳泉市　平定县　盂县　  长治市　潞城市
长治县　长子县　平顺县　襄垣县　沁源县　屯留县　黎城县　武乡县　沁县
壶关县　晋城市　高平市　泽州县　陵川县　阳城县　沁水县　朔州市　山阴县
右玉县　应县　  怀仁县　晋中市  介休市　昔阳县　灵石县　祁县　 左权县
寿阳县　太谷县　和顺县　平遥县　榆社县　运城市　河津市　永济市　闻喜县
新绛县　平陆县　垣曲县　绛县　  稷山县　芮城县　夏县　  万荣县　临猗县
忻州市　原平市　代县　  神池县　五寨县　五台县　偏关县　宁武县　静乐县
繁峙县　河曲县　保德县　定襄县　岢岚县　临汾市　侯马市　霍州市　汾西县
吉县　  安泽县　大宁县　浮山县　古县　  隰县  　襄汾县　翼城县　永和县
乡宁县　曲沃县　洪洞县　蒲县　  吕梁市　孝义市　汾阳市　文水县　中阳县
兴县　  临县　  方山县　柳林县　岚县　交口县　交城县　石楼县
'''
p5 = '''
武川县　包头市　固阳县　乌海市　赤峰市　宁城县　林西县　敖汉旗　开鲁县
通辽市　库伦旗　奈曼旗　乌审旗　杭锦旗　根河市　阿荣旗　五原县　磴口县
丰镇市　兴和县　卓资县　商都县　凉城县　化德县　多伦县　正蓝旗　镶黄旗
兴安盟　突泉县　　　　
托克托县　清水河县　喀喇沁旗　巴林左旗　翁牛特旗　巴林右旗　扎鲁特旗
准格尔旗　鄂托克旗　达拉特旗　满洲里市　牙克石市　扎兰屯市　杭锦后旗
四子王旗　阿巴嘎旗　太仆寺旗　正镶白旗　阿尔山市　扎赉特旗　阿拉善盟
额济纳旗
呼和浩特市　和林格尔县　土默特左旗　土默特右旗　克什克腾旗　霍林郭勒市
鄂尔多斯市　伊金霍洛旗　鄂托克前旗　呼伦贝尔市　额尔古纳市　陈巴尔虎旗
巴彦淖尔市　乌拉特中旗　乌拉特前旗　乌拉特后旗　乌兰察布市　锡林浩特市
二连浩特市　苏尼特左旗　苏尼特右旗　锡林郭勒盟　乌兰浩特市　阿拉善左旗
阿拉善右旗　
阿鲁科尔沁旗　新巴尔虎左旗　新巴尔虎右旗　鄂伦春自治旗　西乌珠穆沁旗
东乌珠穆沁旗　科尔沁左翼中旗　科尔沁左翼后旗　鄂温克族自治旗
察哈尔右翼前旗　察哈尔右翼中旗　察哈尔右翼后旗　科尔沁右翼前旗
科尔沁右翼中旗　达尔罕茂明安联合旗　莫力达瓦达斡尔族自治旗　

'''
p6 = '''
沈阳市　新民市　法库县　辽中县　康平县　大连市　庄河市　长海县　鞍山市
海城市　台安县　抚顺市　抚顺县　本溪市　丹东市　东港市　凤城市　锦州市
凌海市　北宁市　黑山县　义县　  营口市　盖州市　阜新市　彰武县　辽阳市
灯塔市　辽阳县　盘锦市　盘山县　大洼县　铁岭市　开原市　铁岭县　昌图县
西丰县　朝阳市　凌源市　北票市　朝阳县　建平县　兴城市　绥中县　建昌县
大石桥市　瓦房店市　普兰店市　调兵山市　葫芦岛市
岫岩满族自治县　清原满族自治县　新宾满族自治县　阜新蒙古族自治县　
宽甸满族自治县　桓仁满族自治县　本溪满族自治县　喀喇沁左翼蒙古族自治县　
'''
p7 = '''
长春市　九台市　榆树市　德惠市　农安县　吉林市　舒兰市　桦甸市　蛟河市
磐石市　永吉县　四平市　双辽市　梨树县　辽源市　东辽县　东丰县　通化市
集安市　通化县　辉南县　柳河县　白山市　临江市　靖宇县　抚松县　江源县
松原市　乾安县　长岭县　扶余县　白城市　大安市　洮南市　镇赉县　通榆县
延吉市　图们市　敦化市　龙井市　珲春市　和龙市　安图县　汪清县
公主岭市　梅河口市　伊通满族自治县　长白朝鲜族自治县　延边朝鲜族自治州
前郭尔罗斯蒙古族自治县　

'''
p8 = '''
阿城市　尚志市　双城市　五常市　方正县　宾县  　依兰县　巴彦县　通河县
木兰县　延寿县　讷河市　富裕县　拜泉县　甘南县　依安县　克山县　泰来县
克东县　龙江县　鹤岗市　萝北县　绥滨县　集贤县　宝清县　友谊县　饶河县
鸡西市　密山市　虎林市　鸡东县　大庆市　林甸县　肇州县　肇源县　漠河县
伊春市　铁力市　嘉荫县　宁安市　海林市　穆棱市　林口县　东宁县　同江市
富锦市　桦川县　抚远县　桦南县　汤原县　勃利县　黑河市　北安市　逊克县
嫩江县　孙吴县　绥化市　安达市　肇东市　海伦市　绥棱县　兰西县　明水县
青冈县　庆安县　望奎县　呼玛县　塔河县　
七台河市　双鸭山市　牡丹江市　佳木斯市　绥芬河市　哈尔滨市　齐齐哈尔市
杜尔伯特蒙古族自治县　
'''
p9 = '''
黄浦区　卢湾区　徐汇区　长宁区　静安区　普陀区　闸北区　虹口区　杨浦区
宝山区　闵行区　嘉定区　松江区　金山区　青浦区　南汇区　奉贤区　崇明县浦东新区　

'''
p10 = '''
南京市　溧水县　高淳县　无锡市　江阴市　宜兴市　徐州市　邳州市　新沂市
铜山县　睢宁县　沛县　  丰县　  常州市　金坛市　溧阳市　苏州市　常熟市
太仓市　昆山市　吴江市　南通市　如皋市　通州市　海门市　启东市　海安县
如东县　东海县　灌云县　赣榆县　灌南县　淮安市　涟水县　洪泽县　金湖县
盱眙县　盐城市　东台市　大丰市　建湖县　响水县　阜宁县　射阳县　滨海县
扬州市　高邮市　江都市　仪征市　宝应县　镇江市　丹阳市　扬中市　句容市
泰州市　泰兴市　姜堰市　靖江市　兴化市　宿迁市　沭阳县　泗阳县　泗洪县
连云港市　张家港市　
'''
p11 = '''
杭州市　建德市　富阳市　临安市　桐庐县　淳安县　宁波市　余姚市　慈溪市
奉化市　宁海县　象山县　温州市　瑞安市　乐清市　永嘉县　洞头县　平阳县
苍南县　文成县　泰顺县　嘉兴市　海宁市　平湖市　桐乡市　嘉善县　海盐县
湖州市　长兴县　德清县　安吉县　绍兴市　诸暨市　上虞市　嵊州市　绍兴县
新昌县　金华市　兰溪市　义乌市　东阳市　永康市　武义县　浦江县　磐安县
衢州市　江山市　龙游县　常山县　开化县　舟山市　岱山县　嵊泗县　台州市
临海市　玉环县　天台县　仙居县　三门县　丽水市　龙泉市　缙云县　青田县
云和县　遂昌县　松阳县　庆元县　景宁畲族自治县　
'''
p12 = '''
合肥市　长丰县　肥东县　肥西县　芜湖市　芜湖县　南陵县　繁昌县　蚌埠市
怀远县　固镇县　五河县　淮南市　凤台县　当涂县　淮北市　濉溪县　铜陵市
安庆市　桐城市　宿松县　枞阳县　太湖县　怀宁县　岳西县　望江县　潜山县
黄山市　休宁县　歙　县　祁门县 　黟县　滁州市　天长市　明光市　全椒县
来安县　定远县　凤阳县　阜阳市　界首市　临泉县　颍上县　阜南县　太和县
宿州市　萧县  　泗县　  砀山县　灵璧县　巢湖市　含山县　无为县　庐江县
和县　  六安市　寿县  　霍山县　霍邱县　舒城县　金寨县　亳州市　利辛县
涡阳县　蒙城县　池州市　东至县　石台县　青阳县　宣城市　宁国市　广德县
郎溪县　泾县  　旌德县　绩溪县　马鞍山市　
'''
p13= '''
福州市　福清市　长乐市　闽侯县　闽清县　永泰县　连江县　罗源县　平潭县
厦门市　莆田市　仙游县　三明市　永安市　明溪县　将乐县　大田县　宁化县
建宁县　沙县　  尤溪县　清流县　泰宁县　泉州市　石狮市　晋江市　南安市
惠安县　永春县　安溪县　德化县　金门县　漳州市　龙海市　平和县　南靖县
诏安县　漳浦县　华安县　东山县　长泰县　云霄县　南平市　建瓯市　邵武市
建阳市　松溪县　光泽县　顺昌县　浦城县　政和县　龙岩市　漳平市　长汀县
武平县　上杭县　永定县　连城县　宁德市　福安市　福鼎市　寿宁县　霞浦县
柘荣县　屏南县　古田县　周宁县　武夷山市
'''
p14 = '''
南昌市　新建县　南昌县　进贤县　安义县　乐平市　浮梁县　萍乡市　莲花县
上栗县　芦溪县　九江市　瑞昌市　九江县　星子县　武宁县　彭泽县　永修县
修水县　湖口县　德安县　都昌县　新余市　分宜县　鹰潭市　贵溪市　余江县
赣州市　瑞金市　南康市　石城县　安远县　赣县　  宁都县　寻乌县　兴国县
定南县　上犹县　于都县　龙南县　崇义县　信丰县　全南县　大余县　会昌县
吉安市　吉安县　永丰县　永新县　新干县　泰和县　峡江县　遂川县　安福县
吉水县　万安县　宜春市　丰城市　樟树市　高安市　铜鼓县　靖安县　宜丰县
奉新县　万载县　上高县　抚州市　南丰县　乐安县　金溪县　南城县　东乡县
资溪县　宜黄县　广昌县　黎川县　崇仁县　上饶市　德兴市　上饶县　广丰县
鄱阳县　婺源县　铅山县　余干县　横峰县　弋阳县　玉山县　万年县
井冈山市　景德镇市　
'''
p15 = '''
济南市　章丘市　平阴县　济阳县　商河县　青岛市　胶南市　胶州市　平度市
莱西市　即墨市　淄博市　桓台县　高青县　沂源县　枣庄市　滕州市　垦利县
广饶县　利津县　烟台市　龙口市　莱阳市　莱州市　招远市　蓬莱市　栖霞市
海阳市　长岛县　潍坊市　青州市　诸城市　寿光市　安丘市　高密市　昌邑市
昌乐县　临朐县　济宁市　曲阜市　兖州市　邹城市　鱼台县　金乡县　嘉祥县
微山县　汶上县　泗水县　梁山县　泰安市　新泰市　肥城市　宁阳县　东平县
威海市　乳山市　文登市　荣成市　日照市　五莲县　莒县　  莱芜市　临沂市
沂南县　郯城县　沂水县　苍山县　费县　  平邑县　莒南县　蒙阴县　临沭县
德州市　乐陵市　禹城市　陵县　  宁津县　齐河县　武城县　庆云县　平原县
夏津县　临邑县　聊城市　临清市　高唐县　阳谷县　茌平县　莘县　  东阿县
冠县  　滨州市　邹平县　沾化县　惠民县　博兴县　阳信县　无棣县　菏泽市
鄄城县　单　县　郓城县　曹　县　定陶县　巨野县　东明县　成武县
'''
p16 = '''
郑州市　巩义市　新郑市　新密市　登封市　荥阳市　中牟县　开封市　开封县
尉氏县　兰考县　杞县　  通许县　洛阳市　偃师市　孟津县　汝阳县　伊川县
洛宁县　嵩　县　宜阳县　新安县　栾川县　汝州市　舞钢市　宝丰县　叶县
郏县　  鲁山县　安阳市　林州市　安阳县　滑县　  内黄县　汤阴县　鹤壁市
浚县　  淇县　  新乡市　卫辉市　辉县市　新乡县　获嘉县　原阳县　长垣县
封丘县　延津县　焦作市　沁阳市　孟州市　修武县　温县　  武陟县　博爱县
濮阳市　濮阳县　南乐县　台前县　清丰县　范县　许昌市　  禹州市　长葛市
许昌县　鄢陵县　襄城县　漯河市　临颍县　舞阳县　义马市　灵宝市　渑池县
卢氏县　陕县　  南阳市　邓州市　桐柏县　方城县　淅川县　镇平县　唐河县
南召县　内乡县　新野县　社旗县　西峡县　商丘市　永城市　宁陵县　虞城县
民权县　夏邑县　柘城县　睢县　  信阳市　潢川县　淮滨县　息县　  新县
商城县　固始县　罗山县　光山县　周口市　项城市　商水县　淮阳县　太康县
鹿邑县　西华县　扶沟县　沈丘县　郸城县　确山县　新蔡县　上蔡县　西平县
泌阳县　平舆县　汝南县　遂平县　正阳县　济源市
三门峡市　平顶山市　驻马店市　
'''
p17 = '''
武汉市　黄石市　大冶市　阳新县　十堰市　郧　县　竹山县　房　县　郧西县
竹溪县　荆州市　洪湖市　石首市　松滋市　监利县　公安县　江陵县　宜昌市
宜都市　当阳市　枝江市　秭归县　远安县　兴山县　襄樊市　枣阳市　宜城市
南漳县　谷城县　保康县　鄂州市　荆门市　钟祥市　京山县　沙洋县　孝感市
应城市　安陆市　汉川市　云梦县　大悟县　孝昌县　黄冈市　麻城市　武穴市
红安县　罗田县　浠水县　蕲春县　黄梅县　英山县　团风县　咸宁市　赤壁市
嘉鱼县　通山县　崇阳县　通城县　随州市　广水市　仙桃市　天门市　潜江市
恩施市　利川市　建始县　来凤县　巴东县　鹤峰县　宣恩县　咸丰县
丹江口市　老河口市　神农架林区　五峰土家族自治县　长阳土家族自治县　
'''
p18 = '''
长沙市　浏阳市　长沙县　望城县　宁乡县　株洲市　醴陵市　株洲县　炎陵县
茶陵县　攸　县　湘潭市　湘乡市　韶山市　湘潭县　衡阳市　耒阳市　常宁市
衡阳县　衡东县　衡山县　衡南县　祁东县　邵阳市　武冈市　邵东县　洞口县
新邵县　绥宁县　新宁县　邵阳县　隆回县　城步苗族自治县　岳阳市　临湘市
汨罗市　岳阳县　湘阴县　平江县　华容县　常德市　津市市　澧　县　临澧县
桃源县　汉寿县　安乡县　石门县　慈利县　桑植县　益阳市　沅江市　桃江县
南　县　安化县　郴州市　资兴市　宜章县　汝城县　安仁县　嘉禾县　临武县
桂东县　永兴县　桂阳县　永州市　祁阳县　蓝山县　宁远县　新田县　东安县
江永县　道　县　双牌县　怀化市　洪江市　会同县　沅陵县　辰溪县　溆浦县
中方县　娄底市　涟源市　新化县　双峰县　吉首市　古丈县　龙山县　永顺县
凤凰县　泸溪县　保靖县　花垣县　冷水江市　张家界市
江华瑶族自治县　芷江侗族自治县　新晃侗族自治县　通道侗族自治县
靖州苗族侗族自治县　麻阳苗族自治县　湘西土家族苗族自治州　
'''
p19 = '''
广州市　从化市　增城市　深圳市　珠海市　汕头市　南澳县　韶关市　乐昌市
南雄市　仁化县　始兴县　翁源县　新丰县　佛山市　江门市　台山市　开平市
鹤山市　恩平市　湛江市　廉江市　雷州市　吴川市　遂溪县　徐闻县　茂名市
高州市　化州市　信宜市　电白县　肇庆市　高要市　四会市　广宁县　德庆县
封开县　怀集县　惠州市　惠东县　博罗县　龙门县　梅州市　兴宁市　梅　县
蕉岭县　大埔县　丰顺县　五华县　平远县　汕尾市　陆丰市　海丰县　陆河县
河源市　和平县　龙川县　紫金县　连平县　东源县　阳江市　阳春市　阳西县
阳东县　清远市　英德市　连州市　佛冈县　阳山县　清新县　东莞市　中山市
潮州市　潮安县　饶平县　揭阳市　普宁市　揭东县　揭西县　惠来县　云浮市
罗定市　云安县　新兴县　郁南县
乳源瑶族自治县　连山壮族瑶族自治县　连南瑶族自治县　
'''
p20 = '''
南宁市　武鸣县　隆安县　马山县　上林县　宾阳县　横　县　柳州市　柳江县
桂林市　阳朔县　临桂县　灵川县　全州县　平乐县　兴安县　灌阳县　荔浦县
资源县　永福县　梧州市　岑溪市　苍梧县　藤县　  蒙山县　北海市　合浦县
东兴市　上思县　钦州市　灵山县　浦北县　贵港市　桂平市　平南县　玉林市
北流市　容县  　陆川县　博白县　兴业县　百色市　凌云县　平果县　西林县
乐业县　德保县　田林县　田阳县　靖西县　田东县　那坡县　贺州市　钟山县
昭平县　河池市　宜州市　天峨县　凤山县　南丹县　东兰县　来宾市　合山市
象州县　武宣县　忻城县　崇左市　凭祥市　宁明县　扶绥县　龙州县　大新县
天等县　防城港市
三江侗族自治县　大化瑶族自治县　巴马瑶族自治县　龙胜各族自治县
金秀瑶族自治县　融水苗族自治县　隆林各族自治县　恭城瑶族自治县
都安瑶族自治县　富川瑶族自治县　环江毛南族自治县　罗城仫佬族自治县
'''
p21 = '''
海口市　琼海市　儋州市　文昌市　万宁市　东方市　澄迈县　定安县　屯昌县
临高县　三亚市　五指山市
白沙黎族自治县　昌江黎族自治县　乐东黎族自治县　陵水黎族自治县
保亭黎族苗族自治县　琼中黎族苗族自治县　
'''
p22 = '''
渝中区　江北区　南岸区　北碚区　万盛区　双桥区　渝北区　巴南区　万州区
涪陵区　黔江区　长寿区　九龙坡区　大渡口区　沙坪坝区　
永川市　合川市　江津市　南川市　綦江县　潼南县　荣昌县　璧山县　大足县
铜梁县　梁平县　城口县　垫江县　武隆县　丰都县　奉节县　开县　云阳县
忠县  　巫溪县　巫山县
石柱土家族自治县　秀山土家族苗族自治县　酉阳土家族苗族自治县
彭水苗族土家族自治县　
'''
p23= '''
成都市　彭州市　邛崃市　崇州市　金堂县　郫　县　新津县　双流县　蒲江县
大邑县　自贡市　荣　县　富顺县　米易县　盐边县　泸州市　泸　县　合江县
叙永县　古蔺县　德阳市　广汉市　什邡市　绵竹市　罗江县　中江县　绵阳市
江油市　盐亭县　三台县　平武县　安　县　梓潼县　广元市　青川县　旺苍县
剑阁县　苍溪县　遂宁市　射洪县　蓬溪县　大英县　内江市　资中县　隆昌县
威远县　乐山市　夹江县　井研县　犍为县　沐川县　南充市　阆中市　营山县
蓬安县　仪陇县　南部县　西充县　眉山市　仁寿县　彭山县　洪雅县　丹棱县
青神县　宜宾市　宜宾县　兴文县　南溪县　珙　县　长宁县　高　县　江安县
筠连县　屏山县　广安市　华蓥市　岳池县　邻水县　武胜县　达州市　万源市
达　县　渠　县　宣汉县　开江县　大竹县　雅安市　芦山县　石棉县　名山县
天全县　荥经县　宝兴县　汉源县　巴中市　南江县　平昌县　通江县　资阳市
简阳市　安岳县　乐至县　红原县　汶川县　阿坝县　理　县　小金县　黑水县
金川县　松潘县　壤塘县　茂　县　康定县　丹巴县　炉霍县　九龙县　甘孜县
雅江县　新龙县　道孚县　白玉县　理塘县　德格县　乡城县　石渠县　稻城县
色达县　巴塘县　泸定县　得荣县　西昌市　美姑县　昭觉县　金阳县　甘洛县
布拖县　雷波县　普格县　宁南县　喜德县　会东县　越西县　会理县　盐源县
德昌县　冕宁县　
马尔康县　九寨沟县　峨眉山市　都江堰市　攀枝花市　若尔盖县　
北川羌族自治县　木里藏族自治县　马边彝族自治县　峨边彝族自治县
甘孜藏族自治州　凉山彝族自治州　阿坝藏族羌族自治州　
'''
p24 = '''
贵阳市　清镇市　开阳县　修文县　息烽县　水城县　盘　县　遵义市　赤水市
仁怀市　遵义县　绥阳县　桐梓县　习水县　凤冈县　正安县　余庆县　湄潭县
安顺市　普定县　德江县　江口县　思南县　石阡县　毕节市　黔西县　大方县
织金县　金沙县　赫章县　纳雍县　兴义市　望谟县　兴仁县　普安县　册亨县
晴隆县　贞丰县　安龙县　凯里市　施秉县　从江县　锦屏县　镇远县　麻江县
台江县　天柱县　黄平县　榕江县　剑河县　三穗县　雷山县　黎平县　岑巩县
丹寨县　都匀市　福泉市　贵定县　惠水县　罗甸县　瓮安县　荔波县　龙里县
平塘县　长顺县　独山县　六盘水市　六枝特区　万山特区
三都水族自治县　松桃苗族自治县　玉屏侗族自治县　沿河土家族自治县
道真仡佬族苗族自治县　务川仡佬族苗族自治县平坝县　镇宁布依族苗族自治县
紫云苗族布依族自治县　关岭布依族苗族自治县铜仁市　印江土家族苗族自治县
黔东南苗族侗族自治州　黔西南布依族苗族自治州　威宁彝族回族苗族自治县
黔南布依族苗族自治州
'''
p25 = '''
昆明市　安宁市　富民县　嵩明县　呈贡县　晋宁县　宜良县　曲靖市　宣威市
陆良县　会泽县　富源县　罗平县　马龙县　师宗县　沾益县　玉溪市　华宁县
澄江县　易门县　通海县　江川县　保山市　施甸县　昌宁县　龙陵县　腾冲县
昭通市　永善县　绥江县　镇雄县　大关县　盐津县　巧家县　彝良县　威信县
水富县　鲁甸县　丽江市　华坪县　永胜县　思茅市　临沧市　镇康县　凤庆县
云　县　永德县　文山县　砚山县　广南县　马关县　富宁县　西畴县　丘北县
蒙自县　个旧市　开远市　弥勒县　红河县　绿春县　泸西县　建水县　元阳县
石屏县　景洪市　勐海县　楚雄市　元谋县　南华县　牟定县　武定县　大姚县
双柏县　禄丰县　永仁县　姚安县　大理市　剑川县　弥渡县　云龙县　洱源县
鹤庆县　祥云县　宾川县　永平县　潞西市　瑞丽市　盈江县　梁河县　陇川县
泸水县　福贡县　德钦县　麻栗坡县　香格里拉县　
宁蒗彝族自治县　河口瑶族自治县　玉龙纳西族自治县　普洱哈尼族彝族自治县　
漾濞彝族自治县　寻甸回族自治县　墨江哈尼族自治县　江城哈尼族彝族自治县　
峨山彝族自治县　屏边苗族自治县　澜沧拉祜族自治县　兰坪白族普米族自治县　
石林彝族自治县　西盟佤族自治县　维西傈僳族自治县　贡山独龙族怒族自治县　
景东彝族自治县　沧源佤族自治县　巍山彝族回族自治县　景谷彝族傣族自治县　
南涧彝族自治县　新平彝族傣族自治县　禄劝彝族苗族自治县　
孟连傣族拉祜族佤族自治县　金平苗族瑶族傣族自治县　
元江哈尼族彝族傣族自治县　镇沅彝族哈尼族拉祜族自治县　
双江拉祜族佤族布朗族傣族自治县　耿马傣族佤族自治县　

'''
p26 = '''
拉萨市　林周县　达孜县　尼木县　当雄县　曲水县　那曲县　嘉黎县　申扎县
巴青县　聂荣县　尼玛县　比如县　索　县　班戈县　安多县　昌都县　芒康县
贡觉县　八宿县　左贡县　边坝县　洛隆县　江达县　丁青县　察雅县　乃东县
琼结县　措美县　加查县　贡嘎县　洛扎县　曲松县　桑日县　扎囊县　错那县
隆子县　定结县　萨迦县　江孜县　拉孜县　定日县　康马县　吉隆县　亚东县
昂仁县　岗巴县　仲巴县　萨嘎县　仁布县　白朗县　噶尔县　措勤县　普兰县
革吉县　日土县　札达县　改则县　林芝县　墨脱县　朗　县　米林县　察隅县
波密县　日喀则市　类乌齐县　浪卡子县　聂拉木县　谢通门县　南木林县
工布江达县　墨竹工卡县　堆龙德庆县　
'''
p27 = '''
西安市　高陵县　蓝田县　户县　周至县　铜川市　宜君县　宝鸡市　岐山县
凤翔县　陇县　太白县　麟游县　扶风县　千阳县　眉县  　凤县　咸阳市
礼泉县　泾阳县　永寿县　三原县　彬县　旬邑县　长武县　乾县　武功县
淳化县　渭南市　韩城市　华阴市　蒲城县　潼关县　白水县　澄城县　华县
合阳县　富平县　大荔县　延安市　安塞县　洛川县　子长县　黄陵县　延川县
富县　延长县　甘泉县　宜川县　志丹县　黄龙县　吴旗县　汉中市　留坝县
镇巴县　城固县　南郑县　洋县　宁强县　佛坪县　勉县　西乡县　略阳县
榆林市　清涧县　绥德县　神木县　佳县　府谷县　子洲县　靖边县　横山县
米脂县　吴堡县　定边县　安康市　紫阳县　岚皋县　旬阳县　镇坪县　平利县
石泉县　宁陕县　白河县　汉阴县　商洛市　镇安县　山阳县　洛南县　商南县
丹凤县　柞水县

'''
p28 = '''
兰州市　永登县　榆中县　皋兰县　金昌市　永昌县　白银市　靖远县　景泰县
会宁县　天水市　武山县　甘谷县　清水县　秦安县　武威市　民勤县　古浪县
张掖市　民乐县　山丹县　临泽县　高台县　平凉市　灵台县　静宁县　崇信县
华亭县　泾川县　庄浪县　酒泉市　玉门市　敦煌市　安西县　金塔县　庆阳市
庆城县　镇原县　合水县　华池县　环县　宁县　正宁县　定西市　岷县
渭源县　陇西县　通渭县　漳县　临洮县　陇南市　成县　礼县　康县
文县　两当县　徽县　宕昌县　西和县　临夏市　临夏县　康乐县　永靖县
广河县　和政县　合作市　临潭县　卓尼县　舟曲县　迭部县　玛曲县　碌曲县
夏河县　嘉峪关市　东乡族自治县　阿克塞哈萨克族自治县　肃北蒙古族自治县
张家川回族自治县　天祝藏族自治县　肃南裕固族自治县
积石山保安族东乡族撒拉族自治县　
'''
p29 = '''
西宁市　湟源县　湟中县　平安县　乐都县　海晏县　祁连县　刚察县　同仁县
泽库县　尖扎县　共和县　同德县　贵德县　兴海县　贵南县　玛沁县　班玛县
甘德县　达日县　久治县　玛多县　玉树县　杂多县　称多县　治多县　囊谦县
乌兰县　天峻县　都兰县　曲麻莱县　德令哈市　格尔木市
门源回族自治县　大通回族土族自治县　河南蒙古族自治县　化隆回族自治县　
互助土族自治县　民和回族土族自治县　循化撒拉族自治县　　　

'''
p30 = '''
银川市　灵武市　永宁县　贺兰县　平罗县　吴忠市　同心县　盐池县　固原市
西吉县　隆德县　泾源县　彭阳县　中卫市　中宁县　海原县　
石嘴山市　青铜峡市

'''
p31 = '''
鄯善县　哈密市　伊吾县　和田市　和田县　洛浦县　民丰县　皮山县　策勒县
于田县　墨玉县　温宿县　沙雅县　拜城县　库车县　柯坪县　新和县　乌什县
喀什市　巴楚县　泽普县　伽师县　叶城县　疏勒县　莎车县　疏附县　乌恰县
和静县　尉犁县　和硕县　且末县　博湖县　轮台县　若羌县　昌吉市　阜康市
米泉市　奇台县　博乐市　精河县　温泉县　伊宁市　奎屯市　伊宁县　昭苏县
新源县　霍城县　巩留县　塔城市　乌苏市　额敏县　裕民县　沙湾县　托里县
青河县　富蕴县　福海县　
石河子市　阿拉尔市　五家渠市　吐鲁番市　托克逊县　阿克苏市　阿瓦提县
岳普湖县　麦盖提县　英吉沙县　阿图什市　阿合奇县　阿克陶县　库尔勒市
玛纳斯县　呼图壁县　特克斯县　尼勒克县　吉木乃县　布尔津县　哈巴河县　
阿勒泰市　乌鲁木齐市　乌鲁木齐县　克拉玛依市　图木舒克市　吉木萨尔县　
巴里坤哈萨克自治县　塔什库尔干塔吉克自治县　焉耆回族自治县　
察布查尔锡伯自治县　木垒哈萨克自治县　和布克赛尔蒙古自治县　

'''
p32 = '''
中西区　东区　观塘区　南区　湾仔区　离岛区　葵青区　北区　西贡区
沙田区　屯门区　大埔区　荃湾区　元朗区　九龙城区　油尖旺区　深水埗区
黄大仙区　
'''
p33= '''

'''
p34 = '''
台北市　高雄市　基隆市　台中市　台南市　新竹市　嘉义市　台北县　板桥市
宜兰县　宜兰市　新竹县　竹北市　桃园县　桃园市　苗栗县　苗栗市　台中县
丰原市　彰化县　彰化市　南投县　南投市　嘉义县　太保市　云林县　斗六市
台南县　新营市　高雄县　凤山市　屏东县　屏东市　台东县　台东市　花莲县
花莲市　澎湖县　马公市
'''
#省份关键字，用于判别区域所在省份
province_key = ["北京市", "天津市", "河北省", "山西省", "内蒙古自治区", "辽宁省", "吉林省",
                 "黑龙江省", "上海市", "江苏省", "浙江省", "安徽省", "福建省", "江西省",
                 "山东省","河南省", "湖北省", "湖南省", "广东省", "广西壮族自治区", "海南省",
                 "重庆市",  "四川省", "贵州省", "云南省", "西藏自治区", "陕西省", "甘肃省",
                 "青海省", "宁夏回族自治区", "新疆维吾尔自治区", "香港特别行政区", "澳门别行政区",
                 "台湾省"]
createVar = locals()
province_value = [createVar['p' + str(i)].split() for i in range(1, 35)]  #省份所对应区域组成的列表
area_dict = dict(zip(province_key, province_value))  #构造{省份:区域}字典

#简化省份关键字，用于判断title所在省份及html页面中的项目地点
area_list = ['北京', '上海', '天津', '重庆', '河北', '山西', '辽宁', '吉林', '大连', '亦庄', '黑龙江', '江苏', '浙江','珠海',
              '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南', '广东','广州', '深圳', '海南', '四川', '贵州', '云南', '苏州',
             '陕西', '甘肃', '青海', '台湾', '内蒙古', '广西', '西藏', '宁夏', '新疆', '香港', '澳门',
             '黄冈', '日照', ' 昆明', '江苏']


bank= ["中国工商银行股份有限公司","中国邮政储蓄银行股份有限公司","中国银行股份有限公司","中国光大银行股份有限公司","中国农业发展银行","中国进出口银行"
       ,"国家开发银行","中国农业银行股份有限公司","中国建设银行股份有限公司","中信银行股份有限公司","中信百信银行股份有限公司","华夏银行股份有限公司",
       "中国人民银行股份有限公司","中国民生银行股份有限公司"]
if __name__ == '__main__':
    """
    test coding
    """
    # print(default)



