import os

cur_path = os.path.dirname(os.path.abspath(__file__))

MAX_time_out = 4
time_out_cnt = 0

mail_server_port = 25

args_mode = False
disp_lim = 0        # 0: don't display data  -1: display all data  >0: display first *disp_lim* lines of data
interval = 3.5
log_flag = False    # enable logging or not
log_dir = os.path.join(cur_path, "log")
if not os.path.exists(log_dir):
    os.mkdir(log_dir)
log_name = r""      # the name can be automatically generated if not specified
log_path = os.path.join(log_dir, log_name)

payload_root_path = os.path.join(cur_path, "sample")

filename_ext = ""

# payload_token_dict = {
#     b"<normal_data>": os.path.join(cur_path, "./sample/normal/normal_data"),
#     b"<b64_normal_data>": os.path.join(cur_path, "./sample/normal/b64_normal_data"),
#     b"<basic_qp_normal_data>": os.path.join(cur_path, "./sample/normal/basic_qp_normal_data"),
#     b"<greeting>": os.path.join(cur_path, "./sample/normal/greeting"),
# }
