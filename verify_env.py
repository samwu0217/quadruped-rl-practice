import numpy as np
from anymal_c_env import AnymalCMujocoEnv # 假設你的檔名是 anymal_c_env.py

def verify_env():
    print("=== 開始環境驗證 ===")
    
    # 測試項目 1: 測試加載 (Ensuring path correctness)
    try:
        # 這裡會觸發 __init__ 中的 MujocoEnv 初始化，檢查 XML 與 Assets 路徑
        env = AnymalCMujocoEnv(render_mode="human") 
        print(" [成功] 1. 模型加載正常，未發現路徑錯誤。")
    except Exception as e:
        print(f" [失敗] 1. 模型加載出錯，請檢查 XML 路徑或 Assets 資料夾：{e}")
        return

    # 測試項目 2: 列印 Observation (Checking vector length)
    obs, _ = env.reset()
    print(f" [資訊] 2. Observation 向量長度: {len(obs)}")
    
    # 根據 go1_mujoco_env.py 邏輯，長度應包含：
    # 線性速度(3) + 角速度(3) + 投影重力(3) + 目標速度(3) + 關節位置(12) + 關節速度(12) + 最後動作(12) = 48
    expected_length = 48 
    if len(obs) == expected_length:
        print(f" [成功] 2. Observation 長度符合預期 ({expected_length})。")
    else:
        print(f" [警告] 2. Observation 長度為 {len(obs)}，與預期 {expected_length} 不符，請檢查 _get_obs()。")

    # 測試項目 3: 手動步進 (Manual stepping)
    # 呼叫 step 並傳入 12 個關節的零動作向量
    action = np.zeros(12)
    next_obs, reward, terminated, truncated, info = env.step(action)
    
    print(f" [資訊] 3. Step 測試結果 - Terminated: {terminated}, Reward: {reward}")
    
    if not terminated:
        print(" [成功] 3. 機器人初次步進後維持健康狀態。")
    else:
        # 如果一開始就 Terminated，通常是 _healthy_z_range 設定太低
        print(" [失敗] 3. 機器人立即崩潰或判定不健康，請檢查 is_healthy 中的高度設定。")

    env.close()
    print("=== 驗證完成 ===")

if __name__ == "__main__":
    verify_env()