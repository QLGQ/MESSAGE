'''
       @author:wuqiang,windyStreet
       @time:2017年8月7日10:14:09
       @version:V0.1.0
       @func:""
       @param:data:{
           "A":"a",# string 用于判定
       } json #(able null)
       @param:xxx:"xxx用于区别发信息的类型"（
                               1、xxx=1，发邮件;
                               2、xxx=2，发微信;
                               3、xxx=5，发邮件和短信
                               ）
                               string （# not null）
       @notice:""
       @return:PR
'''
INSERT_INTERVAL_TIME = 3
COMPUTE_DATA_INTERVAL_TIME = 30
MAX_INSERT_COUNT = 50
MAX_PER_RECEIVE_COUNT = 51
START_COMPUTE_COUNT = 1

CONF_INFO = {}  # 配置文件信息
EXIST_ITEM_DATAS = []  # 已经存在的统计项

COMPUTE_STATE_INFO = {}
