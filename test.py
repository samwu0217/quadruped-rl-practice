import gymnasium as gym
from anymal_c_env import AnymalCMujocoEnv
import time

# 建立環境並開啟畫面渲染
env = AnymalCMujocoEnv(ctrl_type="position", render_mode="human")
obs, info = env.reset()

for i in range(1000):
    # 隨機亂動
    action = env.action_space.sample() * 0.0  # 🌟 乘以 0，代表我們不亂動，只看它「預設微蹲」能不能站穩
    obs, reward, terminated, truncated, info = env.step(action)
    
    if terminated or truncated:
        print(f"在第 {i} 步死掉了！")
        obs, info = env.reset()
        time.sleep(1) # 暫停一下讓你觀察

env.close()