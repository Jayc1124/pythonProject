import os
import pandas as pd
import yagmail
from os import listdir
from chardet import detect
def newduanshu():
    ztp_num1 = 0
    ztp_num2 = 0
    temp = 1
    for index, row in data.iterrows():
        if (index > 0):
            ztp_num1 = data.at[index, '涨跌特征值']
            ztp_num2 = data.at[index - 1, '涨跌特征值']
            if (ztp_num2 != ztp_num1):
                temp += 1
            data.at[index, '涨跌段数'] = temp
path = r'D:/已处理文件2/'
filenames = os.listdir(path)
for filename in filenames:
    print(filename)

    data = pd.read_csv(
        path + filename, header=None, encoding='utf_8_sig', low_memory=False,names=[
            "InstrumentID合约代码", "TradingDay交易日", "ActionDay业务日期", "UpdateTime最后修改时间", "UpdateMillisec最后修改毫秒",
            "ExchangeID交易所代码", "ExchangeInstID合约在交易所的代码", "LastPrice最新价", "PreSettlementPrice上次结算价", "PreClosePrice昨收盘",
            "PreOpenInterest昨持仓量", "OpenPrice今开盘", "HighestPrice最高价", "LowestPrice最低价", "Volume数量",
            "Turnover成交金额", "OpenInterest持仓量", "ClosePrice今收盘", "SettlementPrice本次结算价", "UpperLimitPrice涨停板价",
            "LowerLimitPrice跌停板价", "PreDelta昨虚实度", "CurrDelta今虚实度",
            "BidPrice1申买价一", "BidVolume1申买量一", "AskPrice1申卖价一", "AskVolume1申卖量一", "BidPrice2申买价二", "BidVolume2申买量二",
            "AskPrice2申卖价二", "AskVolume2申卖量二", "BidPrice3申买价三", "BidVolume3申买量三", "AskPrice3申卖价三", "AskVolume3申卖量三",
            "BidPrice4申买价四", "BidVolume4申买量四", "AskPrice4申卖价四", "AskVolume4申卖量四", "BidPrice5申买价五", "BidVolume5申买量五",
            "AskPrice5申卖价五", "AskVolume5申卖量五", "AveragePrice当日均价", "RecvTime接收时间","涨跌特征值","涨跌段数"]
    )
























 '''  def add_tendrow():  ###涨跌平 和趋势  添加 两列
        global data

        data['tend'] = '1'  # 开始 第二个任务
        ztp_num1 = 0
        ztp_num2 = 0
        temp = 1
        for index, row in data.iterrows():
            if (index > 0):
                ztp_num1 = data.at[index, 'ztp']
                ztp_num2 = data.at[index - 1, 'ztp']
                if (ztp_num2 != ztp_num1):
                    temp += 1

                data.at[index, 'tend'] = temp
            if (data.at[index,'tend']!=data.at[index,'tend'])
                print(index)
    add_tendrow() '''

