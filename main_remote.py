import akshare as ak
import efinance as ef
import pandas as pd
from datetime import datetime
import time

def get_market_data():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] 正在获取 A股大盘行情 (Server: {pd.Timestamp.now()})")
    
    # 方案 1: eFinance (接口最简单，通常很稳)
    try:
        print("尝试 eFinance 接口...")
        # 代码: 上证, 深证, 创业板, 科创50
        codes = ['000001', '399001', '399006', '000688']
        df = ef.stock.get_realtime_quotes(codes)
        
        print("\n=== A股实时大盘 (来源: eFinance/东财) ===")
        print(f"{'名称':<8} {'最新价':<10} {'涨跌幅':<10} {'成交额(亿)':<10}")
        print("-" * 50)
        
        for _, row in df.iterrows():
            name = row['股票名称']
            price = row['最新价']
            pct = row['涨跌幅']
            # efinance 成交额单位通常是直接数值，需要转换
            amount = float(row['成交额']) / 100000000 
            print(f"{name:<8} {price:<10} {pct:>6}%      {amount:.2f}")
        return
        
    except Exception as e:
        print(f"eFinance 接口尝试失败: {e}")

    # 方案 2: AkShare (备用)
    try:
        print("\n切换至 AkShare 源...")
        # 获取上证指数作为测试
        df = ak.stock_zh_index_spot_em(symbol="主要指数")
        target = ['上证指数', '深证成指', '创业板指', '科创50']
        df_filter = df[df['名称'].isin(target)]
        
        print("\n=== A股实时大盘 (来源: AkShare/东财) ===")
        print(f"{'名称':<8} {'最新价':<10} {'涨跌幅':<10} {'成交额(亿)':<10}")
        print("-" * 50)
        
        for _, row in df_filter.iterrows():
            name = row['名称']
            price = row['最新价']
            pct = row['涨跌幅']
            amount = row['成交额'] / 100000000
            print(f"{name:<8} {price:<10} {pct:>6}%      {amount:.2f}")

    except Exception as e:
        print(f"AkShare 接口尝试失败: {e}")

if __name__ == "__main__":
    get_market_data()
