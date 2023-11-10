import os

cur_path = os.path.dirname(os.path.abspath(__file__))

config = {
    # MX record for whu.edu.cn:
    # whu.edu.cn      MX preference = 10, mail exchanger = whu.edu.cn
    # whu.edu.cn      MX preference = 1, mail exchanger = mx-whu-edu-cn.icoremail.net
    # "mail_server": "mx-whu-edu-cn.icoremail.net",
    "mail_server_port": 25,

    "smtp_header": {
        "helo": b"vps3.hostoftroubles.com",
        "mail_from": b"<echo@vps3.hostoftroubles.com>",
        "rcpt_to": b"<2019302180042@whu.edu.cn>"
    },

    "data": {
        "mime_version": b"MIME-Version: 1.0\r\n",
        "from_header": b"From: <echo@vps3.hostoftroubles.com>\r\n",
        "to_header": b"To:<2019302180042@whu.edu.cn>\r\n",
    },
}

payload_token_dict = {
    b"<normal_data>": os.path.join(cur_path, "./sample/normal/normal_data"),
    b"<b64_normal_data>": os.path.join(cur_path, "./sample/normal/b64_normal_data"),
    b"<qp_normal_data>": os.path.join(cur_path, "./sample/normal/basic_qp_normal_data"),
    b"<greeting>": os.path.join(cur_path, "./sample/normal/greeting"),

    b"<eicar_sample>": os.path.join(cur_path, "./sample/eicar/eicar_crlf"),
    b"<b64_eicar>": os.path.join(cur_path, "./sample/eicar/b64_eicar"),
    b"<qp_eicar>": os.path.join(cur_path, "./sample/eicar/basic_qp_eicar"),
    b"<eicar_zip>": os.path.join(cur_path, "./sample/eicar/ascii04.zip"),
    b"<b64_eicar_zip>": os.path.join(cur_path, "./sample/eicar/b64_eicar_zip"),
    b"<qp_eicar_zip>": os.path.join(cur_path, "./sample/eicar/basic_qp_eicar_zip"),

    b"<wncr_zip>": os.path.join(cur_path, "./sample/wannacry/wncr_zip_crlf"),
    b"<wncr>": os.path.join(cur_path, "./sample/wannacry/wncr_crlf"),

    b"<This is b64_wannacry.>": os.path.join(cur_path, "./sample/wannacry/b64_wannacry"),
    b"<This is qp_wannacry.>": os.path.join(cur_path, "./sample/wannacry/qp_wannacry_1"),
    b"<basic qp wncr here>": os.path.join(cur_path, "./sample/wannacry/basic_qp_wncr"),

    b"<b64_4char_eq wncr here>": os.path.join(cur_path, "./sample/wannacry/b64_4char_eq_wncr"),
    b"<b64_6char_per_line wncr here>": os.path.join(cur_path, "./sample/wannacry/b64_6char_per_line_wncr"),
    b"<b64_junk_char wncr1 here>": os.path.join(cur_path, "./sample/wannacry/b64_junk_char_wncr1"),
    b"<b64_junk_char wncr2 here>": os.path.join(cur_path, "./sample/wannacry/b64_junk_char_wncr2"),
    b"<b64_junk_char wncr3 here>": os.path.join(cur_path, "./sample/wannacry/b64_junk_char_wncr3"),
    b"<b64_junk_char wncr4 here>": os.path.join(cur_path, "./sample/wannacry/b64_junk_char_wncr4"),
    b"<b64_line_end_eq wncr here>": os.path.join(cur_path, "./sample/wannacry/b64_line_end_eq"),
    b"<b64_redundant_bl wncr here>": os.path.join(cur_path, "./sample/wannacry/b64_redundant_bl_wncr"),
    b"<b64_split_encoding wncr1 here>": os.path.join(cur_path, "./sample/wannacry/b64_split_encoding_wncr1"),
    b"<b64_split_encoding wncr2 here>": os.path.join(cur_path, "./sample/wannacry/b64_split_encoding_wncr2"),

    b"<qp_blank_char_l09 wncr here>": os.path.join(cur_path, "./sample/wannacry/qp_blank_char_l09_wncr"),
    b"<qp_blank_char_l20 wncr here>": os.path.join(cur_path, "./sample/wannacry/qp_blank_char_l20_wncr"),
    b"<qp_blank_char_r09 wncr here>": os.path.join(cur_path, "./sample/wannacry/qp_blank_char_r09_wncr"),
    b"<qp_blank_char_r20 wncr here>": os.path.join(cur_path, "./sample/wannacry/qp_blank_char_r20_wncr"),
    b"<qp_illegal_char_09 wncr here>": os.path.join(cur_path, "./sample/wannacry/qp_illegal_char_wncr_09"),
    b"<qp_illegal_char_12 wncr here>": os.path.join(cur_path, "./sample/wannacry/qp_illegal_char_wncr_12"),
    b"<qp_illegal_char_aa wncr here>": os.path.join(cur_path, "./sample/wannacry/qp_illegal_char_wncr_aa"),

    b"<qp_improper_eq_position_line_end_split wncr1 here>": os.path.join(cur_path, "./sample/wannacry/qp_improper_eq_position_line_end_split_wncr1"),
    b"<qp_improper_eq_position_line_end_split wncr2 here>": os.path.join(cur_path, "./sample/wannacry/qp_improper_eq_position_line_end_split_wncr2"),
    b"<qp_improper_eq_position_line_end_split wncr3 here>": os.path.join(cur_path, "./sample/wannacry/qp_improper_eq_position_line_end_split_wncr3"),
    b"<qp_improper_eq_position_line_end wncr1 here>": os.path.join(cur_path, "./sample/wannacry/qp_improper_eq_position_line_end_wncr1"),
    b"<qp_improper_eq_position_line_end wncr2 here>": os.path.join(cur_path, "./sample/wannacry/qp_improper_eq_position_line_end_wncr2"),

    b"<qp_improper_eq_position_within_line wncr1 here>": os.path.join(cur_path, "./sample/wannacry/qp_improper_eq_position_within_line_wncr1"),
    b"<qp_improper_eq_position_within_line wncr2 here>": os.path.join(cur_path, "./sample/wannacry/qp_improper_eq_position_within_line_wncr2"),
    b"<qp_improper_eq_position_within_line wncr3 here>": os.path.join(cur_path, "./sample/wannacry/qp_improper_eq_position_within_line_wncr3"),
    b"<qp_improper_eq_position_within_line wncr4 here>": os.path.join(cur_path, "./sample/wannacry/qp_improper_eq_position_within_line_wncr4"),
    b"<qp_improper_eq_position_within_line wncr5 here>": os.path.join(cur_path, "./sample/wannacry/qp_improper_eq_position_within_line_wncr5"),
    b"<qp_improper_eq_position_within_line wncr6 here>": os.path.join(cur_path, "./sample/wannacry/qp_improper_eq_position_within_line_wncr6"),
    b"<qp_improper_eq_position_within_line wncr7 here>": os.path.join(cur_path, "./sample/wannacry/qp_improper_eq_position_within_line_wncr7"),
    b"<qp_improper_eq_position_within_line wncr8 here>": os.path.join(cur_path, "./sample/wannacry/qp_improper_eq_position_within_line_wncr8"),
    b"<qp_improper_hex_case wncr here>": os.path.join(cur_path, "./sample/wannacry/qp_improper_hex_case_wncr"),
    b"<qp_no_soft_linebreak wncr here>": os.path.join(cur_path, "./sample/wannacry/qp_no_soft_linebreak_wncr"),
}
