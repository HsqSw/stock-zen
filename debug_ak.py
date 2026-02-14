import requests
import time
import akshare as ak

def debug_connection():
    print(">>> 开始 AkShare / 东方财富 连接诊断")
    
    # 1. 直接测试东财 API 连通性 (绕过 AkShare 封装)
    url = "https://push2.eastmoney.com/api/qt/clist/get"
    params = {
        "pn": "1", "pz": "5", "po": "1", "np": "1", 
        "ut": "bd1d9ddb04089700cf9c27f6f7426281", "fltt": "2", "invt": "2", 
        "fid": "f3", "fs": "m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048", 
        "fields": "f1,f2,f3,f4,f12,f13,f14", "_" : str(int(time.time() * 1000))
    }
    
    print(f"\n1. 尝试直连东财接口: {url} ...")
    try:
        start = time.time()
        # 设置短超时，避免死等
        resp = requests.get(url, params=params, timeout=5, headers={"User-Agent": "Mozilla/5.0"})
        print(f"   HTTP状态码: {resp.status_code}")
        print(f"   耗时: {time.time() - start:.2f}s")
        print(f"   响应前50字符: {resp.text[:50]}")
    except Exception as e:
        print(f"   直连失败: {e}")
        
    # 2. 测试 AkShare 封装
    print("\n2. 测试 AkShare 库调用 (stock_zh_index_spot_em) ...")
    try:
        start = time.time()
        # 这里实际上会调用上面的类似接口
        df = ak.stock_zh_index_spot_em(symbol="主要指数")
        print(f"   调用成功! 获取到 {len(df)} 行数据")
        print(f"   耗时: {time.time() - start:.2f}s")
    except Exception as e:
        print(f"   AkShare 调用失败: {e}")

if __name__ == "__main__":
    debug_connection()
