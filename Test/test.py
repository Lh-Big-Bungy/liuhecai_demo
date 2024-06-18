import json

a = {'success': False, 'code': '1000', 'message': '当前阶段下用例为空，请添加用例后执行', 'object': None}
print(type(a))
print(type(json.dumps(a)))
print(json.dumps(a))
