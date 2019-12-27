from base.runmethod import RunMethod
from data_operations.get_data import GetData
from tool.common_util import CommonUtil
from tool.log import Log
from tool.read_config import ReadConfig


class RunTest:
    def __init__(self):
        filename = self.read_con = ReadConfig().read("TestCase", "Testcase_Excel")
        self.run_method = RunMethod()
        self.data = GetData(filename)
        self.com_util = CommonUtil()
        self.log = Log()

    def run(self):
        res = None
        pass_count = []
        fail_count = []
        rows = self.data.get_case_lines()
        self.log.info("Excuting cases")
        for i in range(1, rows):
            is_run = self.data.get_is_run(i)
            if is_run:
                self.log.info("Excuting case:%d" % i)
                url = self.data.get_request_url(i)
                rdata = self.data.get_request_data(i)
                header = self.data.get_header(i)
                method = self.data.get_request_method(i)
                res = self.run_method.run_main(method, url, rdata, header)
                self.log.info(res)
                edata = self.data.get_expcet_data(i)
                bc = CommonUtil()
                if bc.is_contain(edata, res):
                    pass_count.append(i)
                    self.data.write_result(i, "Pass")
                    self.data.write_reponse(i, res)
                else:
                    self.data.write_result(i, "Failed")
                    self.data.write_reponse(i, res)
                    fail_count.append(i)
            else:
                self.log.info("Case%d skipped" % i)
        self.log.info('Failed case ID: %s' % fail_count)
        self.log.info('Passed case ID: %s' % pass_count)


if __name__ == '__main__':
    runtest = RunTest()
    runtest.run()
