import json
import os

#------------------------------------------------------------------------

# acccount_termination(QQ, 素材位置) 注销账户 
# 如用户存在，删除user_list.txt中该用户数据及'用户数据'文件夹下'[QQ].json'用户
# 数据文件，返回值为提示信息
# 如用户不存在，仅返回提示信息
def account_termination(ID, loc = ''):
    filename = loc + '用户数据\\user.txt'
    try:
        with open(filename) as file_object:
            user_list = json.load(file_object)
    except:
        with open(filename, 'w') as file_object:
            json.dump({}, file_object)
    if str(ID) in user_list.keys():
        user_name = user_list[ID]
        del user_list[ID]
        with open(filename, 'w') as file_object:
            json.dump(user_list, file_object)
        filename = loc + '用户数据\\' + str(ID) + '.json'
        os.remove(filename)
        return 'Dr.' + user_name + '已离职，相关档案已销毁且无法恢复'
    else:
        return '用户不存在'

#------------------------------------------------------------------------

# 后续改进：
# 在文件删除之前二次提示用户进行确认，以防误操作导致数据丢失
