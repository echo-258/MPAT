import os

cur_path = os.path.dirname(os.path.abspath(__file__))

mail_server_port = 25

disp_flag = False
log_flag = False
log_path = r""

payload_root_path = os.path.join(cur_path, "sample")

# payload_token_dict = {
#     b"<normal_data>": os.path.join(cur_path, "./sample/normal/normal_data"),
#     b"<b64_normal_data>": os.path.join(cur_path, "./sample/normal/b64_normal_data"),
#     b"<basic_qp_normal_data>": os.path.join(cur_path, "./sample/normal/basic_qp_normal_data"),
#     b"<greeting>": os.path.join(cur_path, "./sample/normal/greeting"),
# }
