import json

a = {"success": False, "code": "1000", "message": "当前阶段下用例为空，请添加用例后执行", "object": None}

_json = {
    "test_tool": "perfma",
    "test_stage": "smoke",
    "case_count": 100,
    "fail_case": 10,
    "success_case": 90,
    "preset_success_rate": 100.00,
    "real_rate": 90.00,
    "test_result": "FAIL",
    "link_url": "url",
}
print(type(a))
print(type(json.dumps(a)))
print(json.dumps(a))
