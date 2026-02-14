import akshare as ak
import pandas as pd
from datetime import datetime

def get_market_overview():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] 开始获取A股大盘数据 (日线模式)...")
    
    # 指数代码映射
    indices = [
        {"name": "上证指数", "code": "sh000001"},
        {"name": "深证成指", "code": "sz399001"},
        {"name": "创业板指", "code": "sz399006"},
        {"name": "科创50",   "code": "sh000688"},
    ]
    
    results = []
    
    print(f"{'名称':<8} {'最新价':<10} {'涨跌幅':<10} {'成交额(亿)':<10}")
    print("-" * 45)

    for idx in indices:
        try:
            # 获取日线数据，取最后一行（即今天/最近交易日）
            df = ak.stock_zh_index_daily_em(symbol=idx["code"])
            if df.empty:
                continue
                
            latest = df.iloc[-1]
            # 计算涨跌幅 (今天收盘 - 昨天收盘) / 昨天收盘
            # 如果是刚开盘可能只有一行，需要容错
            if len(df) > 1:
                prev_close = df.iloc[-2]['close']
                curr_close = latest['close']
                pct_change = (curr_close - prev_close) / prev_close * 100
                change_val = curr_close - prev_close
            else:
                pct_change = 0.0
                change_val = 0.0
            
            # 成交额转换
            amount_e = float(latest['amount']) / 100000000 if 'amount' in latest else 0
            
            print(f"{idx['name']:<8} {latest['close']:<10.2f} {pct_change:+.2f}%      {amount_e:.2f}")
            
        except Exception as e:
            print(f"{idx['name']} 获取失败: {e}")

if __name__ == "__main__":
    get_market_overview()
