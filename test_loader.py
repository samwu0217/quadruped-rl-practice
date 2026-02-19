import mujoco
import mujoco.viewer

# 注意：路徑要指向你剛剛下載的資料夾中的 scene.xml
model_path = "anybotics_anymal_c/scene.xml"

try:
    model = mujoco.MjModel.from_xml_path(model_path)
    data = mujoco.MjData(model)
    mujoco.viewer.launch(model, data)
    print("ANYmal C 載入成功！")
except Exception as e:
    print(f"載入失敗，請檢查 assets 路徑。錯誤訊息：{e}")