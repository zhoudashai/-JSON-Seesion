import json
import os

# 打开包含多个JSON数据的文件
with open('D:\桌面\multiple_data.json', 'r') as file:
    json_data = file.read()

# 解析JSON数据
data_list = json.loads(json_data)['Content']

# 提取所有SESSIONID的值
session_ids = [data['SESSIONID'] for data in data_list if 'SESSIONID' in data]

# 获取用户输入的保存路径和文件名
save_path = input("请输入保存路径（例如 C:/Users/YourUsername/Documents/）：")
file_name = input("请输入文件名（例如 output.txt）：")

# 构造完整的文件路径
file_path = os.path.join(save_path, file_name)

# 将SESSIONID的值写入文件
with open(file_path, 'w') as f:
    for session_id in session_ids:
        f.write(session_id + '\n')

print(f'Saved {len(session_ids)} SESSIONIDs to {file_path}')
