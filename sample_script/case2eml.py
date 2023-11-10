import sys
sys.path.append("..")
sys.path.append("../..")
import valid_case as cases
import utils
from tqdm import tqdm


# case_IDs = cases.test_cases.keys()
case_IDs = ["comment_boundary_6", "comment_boundary_7", "comment_boundary_8", "comment_boundary_9", "comment_boundary_10", ]

# Date: Sat, 1 Jul 2023 10:10:10 +0000

from_to_date = b"From: <echo@vps3.hostoftroubles.com>\r\n" \
               b"To: <jiahe@zhangjh.xyz>\r\n" \
               b"Date: Sat, 1 Jul 2023 10:10:10 +0000\r\n"
payload_list = []
for caseID in tqdm(case_IDs):
    case_struct = cases.test_cases[caseID]["data"]
    case_content = from_to_date + utils.insert_payload(case_struct, payload_list)

    case_content_path = "../eml/" + caseID + ".eml"
    with open(case_content_path, "wb") as fp:
        fp.write(case_content)

print("finish")
