import tushare as ts
import pandas as pd

TOKEN = "25af362da84d6a3ab017fef2d91df8176102d66cb0646ecbf7a28898"

def test_tushare_auth():
    print(">>> 开始 Tushare 权限诊断")
    ts.set_token(TOKEN)
    pro = ts.pro_api()
    
    # 1. 测试最基础的交易日历 (通常无需积分)
    try:
        print("\n1. 测试交易日历 (trade_cal)...")
        df = pro.trade_cal(exchange='', start_date='20250101', end_date='20250105')
        print(f"   成功! 获取到 {len(df)} 条记录")
    except Exception as e:
        print(f"   失败: {e}")
        return

    # 2. 测试股票列表 (通常无需积分)
    try:
        print("\n2. 测试股票列表 (stock_basic)...")
        df = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date', limit=5)
        print(f"   成功! 示例: {df.iloc[0]['name']} ({df.iloc[0]['ts_code']})")
    except Exception as e:
        print(f"   失败: {e}")

    # 3. 测试指数日线 (报错的接口)
    try:
        print("\n3. 测试指数日线 (index_daily)...")
        # 尝试只取一天，一个指数
        df = pro.index_daily(ts_code='000001.SH', start_date='20250101', end_date='20250105')
        print(f"   成功! 获取到 {len(df)} 条记录")
    except Exception as e:
        print(f"   失败: {e}")
        print("   >>> 提示: index_daily 通常需要 120 积分。如果刚充值/获取，可能需要等一会或重新登录 Tushare 网站刷新。")

if __name__ == "__main__":
    test_tushare_auth()
