import tushare as ts
import pandas as pd
from datetime import datetime

# 请替换为你自己的 Tushare Token
TOKEN = "25af362da84d6a3ab017fef2d91df8176102d66cb0646ecbf7a28898"

def get_market_overview_ts(token):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] 初始化 Tushare Pro...")
    
    try:
        ts.set_token(token)
        pro = ts.pro_api()
        
        # 获取交易日历，确认今天是交易日吗？如果不交易取最近一天
        today = datetime.now().strftime('%Y%m%d')
        cal = pro.trade_cal(exchange='', start_date='20250101', end_date=today)
        last_trade_day = cal[cal['is_open'] == 1]['cal_date'].values[-1]
        
        print(f"最近交易日: {last_trade_day}")
        
        # 主要指数代码 (Tushare 格式)
        # 上证指数: 000001.SH
        # 深证成指: 399001.SZ
        # 创业板指: 399006.SZ
        # 科创50:   000688.SH
        codes = ['000001.SH', '399001.SZ', '399006.SZ', '000688.SH']
        
        print(f"{'名称':<8} {'收盘价':<10} {'涨跌幅':<10} {'成交额(亿)':<10}")
        print("-" * 45)
        
        # 获取日线行情
        df = pro.index_daily(ts_code=','.join(codes), trade_date=last_trade_day)
        
        # 映射名称 (API返回里没有中文名，只有代码)
        name_map = {
            '000001.SH': '上证指数',
            '399001.SZ': '深证成指',
            '399006.SZ': '创业板指',
            '000688.SH': '科创50'
        }
        
        for _, row in df.iterrows():
            name = name_map.get(row['ts_code'], row['ts_code'])
            close = row['close']
            pct_chg = row['pct_chg']
            amount = row['amount'] / 100000 # Tushare amount单位是千元 -> 亿 (100000千 = 1亿)
            
            print(f"{name:<8} {close:<10.2f} {pct_chg:+.2f}%      {amount:.2f}")

    except Exception as e:
        print(f"Tushare 请求失败: {e}")

if __name__ == "__main__":
    if TOKEN == "YOUR_TOKEN_HERE":
        print("请先设置 TOKEN 变量！")
    else:
        get_market_overview_ts(TOKEN)
