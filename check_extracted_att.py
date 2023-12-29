import os
import re

import bhv_test_cases.behave_test as cases

att_dir = "/Users/zjh/temp/mime_test/outlook_temp"
ref_original_path = "./att_ref/eicar"
ref_undecoded_path = "./att_ref/basic_qp_eicar"

bypass_subdir = os.path.join(att_dir, "bypass")
undecoded_subdir = os.path.join(att_dir, "undecoded")

# if subdir not exists, create it
if not os.path.exists(bypass_subdir):
    os.mkdir(bypass_subdir)
if not os.path.exists(undecoded_subdir):
    os.mkdir(undecoded_subdir)

with open(ref_original_path, "rb") as fp:
    ref_original = fp.read()
with open(ref_undecoded_path, "rb") as fp:
    ref_undecoded = fp.read()

case_result = {case_id: "" for case_id in list(cases.test_cases.keys())}
unknown_f_result = {}
case_result_cnt, unknown_f_result_cnt = 0, 0

# patterns = [re.compile("-att\d+"), re.compile("_b64"), re.compile("_qp")]
patterns = [re.compile("-att\d+")]

file_list = os.listdir(att_dir)
file_list = [f for f in file_list if os.path.isfile(os.path.join(att_dir, f)) and not f.startswith(".")]
print("Total:", len(file_list), " ---------")

for f in file_list:
    case_name = f
    for p in patterns:
        case_name = re.sub(p, "", case_name)
    # read file
    with open(os.path.join(att_dir, f), "rb") as fp:
        content = fp.read()

    # compare with reference
    if content == ref_original:
        f_result = "bypass"
        os.rename(os.path.join(att_dir, f), os.path.join(bypass_subdir, f))
    # if content is part of ref_original
    elif ref_original.find(content) != -1:
        f_result = "weak_bypass_partial"
        os.rename(os.path.join(att_dir, f), os.path.join(bypass_subdir, f))
    elif content == ref_undecoded:
        f_result = "undecoded"
        os.rename(os.path.join(att_dir, f), os.path.join(undecoded_subdir, f))
    # if difference between content and ref only lies in CRLF
    elif content.replace(b"\n", b"") == ref_undecoded.replace(b"\r\n", b""):
        f_result = "undecoded_with_diff_crlf"
        os.rename(os.path.join(att_dir, f), os.path.join(undecoded_subdir, f))
    else:
        f_result = "unknown"

    if case_name in case_result.keys():
        case_result[case_name] = f_result
    else:
        unknown_f_result[f] = f_result

print("\n>>> case result:")
for case_id, result in case_result.items():
    print(case_id, end="")
    if result != "":
        case_result_cnt += 1
        print(":", result, end=" =====")
    print()
print("--- case result cnt:", case_result_cnt)
print("\n>>> unknown file result:")
for f, result in unknown_f_result.items():
    print(f, result)
print("--- unknown file result cnt:", len(unknown_f_result))
