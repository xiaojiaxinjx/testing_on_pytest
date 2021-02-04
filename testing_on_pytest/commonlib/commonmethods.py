import json
import yaml

class read_data(object):

    def read_json_data(self,file_path,*args,**kwargs ):
        # case: 存储测试用例名称
        # http：存储请求对象
        # expected: 存储预期结果
        case = []
        http = []
        expected = []

        with open(file_path)  as f:
            data = json.loads(f.read())
            test = data["testcases"]
            for t in test:
                case.append(t.get("case"))
                http.append(t.get("http"))
                expected.append(t.get("expected"))

        info = list(zip(case, http, expected))
        return case, info