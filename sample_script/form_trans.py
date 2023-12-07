import sys
sys.path.append("..")
sys.path.append("../..")
import bhv_test_cases.behave_test as cases
import utils
from tqdm import tqdm


from_to_date = b"From: Attacker\r\n" \
               b"To: Victim\r\n" \
               b"Date: Sat, 1 Jul 2023 10:10:10 +0000\r\n"


def case2eml(case_IDs: list, payload_list: list):
    for case_ID in tqdm(case_IDs):
        case_struct = cases.test_cases[case_ID]["data"]
        case_content = from_to_date + utils.insert_payload(case_struct, payload_list)

        case_content_path = "../eml/" + case_ID + ".eml"
        with open(case_content_path, "wb") as fp:
            fp.write(case_content)


def case2text(case_IDs: list, payload_list: list):
    for case_ID in tqdm(case_IDs):
        case_struct = cases.test_cases[case_ID]["data"]
        case_content = from_to_date + utils.insert_payload(case_struct, payload_list)
        print(case_content.decode())


def text2case(text: str):
    print(text)


if __name__ == "__main__":
    case_IDs = ["comment_CTE_wrap_invalid", ]
    payload_list = ["virus_symbol", ]
    # case2eml(case_IDs, [])
    case2text(case_IDs, payload_list)
