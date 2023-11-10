import sys
sys.path.append("..")
sys.path.append("../..")
import Wannacry
import valid_case
import utils

qp_wannacry_path = r"D:/sample/WannaCry/qp_wannacry_pqh"

qp_wanna = Wannacry.Type_cases["qp_wannacry"]

#with open(qp_wannacry_path, "wb") as fp:
#     fp.write(qp_wanna)

case_struct = valid_case.test_cases["qp_wannacry_test"]["data"]
case_content = utils.insert_payload(case_struct, [])

case_content_path = "../qp_wannacry_email_1.eml"
with open(case_content_path, "wb") as fp:
    fp.write(case_content)

print("finish")
