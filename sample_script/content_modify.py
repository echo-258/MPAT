import os.path
import re
import math
import base64

# original_sample_path = r"../sample/wannacry/Ransom.WannaCryptor"
# b64_sample_path = r"../sample/wannacry/b64_wncr"
# qp_sample_path = r"../sample/wannacry/basic_qp_wncr"
# b64_modified_dir = r"../sample/wannacry/b64"
# qp_modified_dir = r"../sample/wannacry/qp"
# payload_name = "wncr"
original_sample_path = r"../sample/eicar/eicar_com"
b64_sample_path = r"../sample/eicar/b64_eicar"
qp_sample_path = r"../sample/eicar/basic_qp_eicar"
b64_modified_dir = r"../sample/eicar/b64"
qp_modified_dir = r"../sample/eicar/qp"
payload_name = "eicar"

MAX_LINE_LEN = 76


def generic_re_sub(sample_path, result_path, rg=rb"\r\n", rpl=b"=\r\n"):
    with open(sample_path, "rb") as fin:
        sample_content = fin.read()
    pattern = re.compile(rg)
    result_sample_content = re.sub(pattern, rpl, sample_content)
    with open(result_path, "wb") as fout:
        fout.write(result_sample_content)
    print("Finished: generic_re_sub", result_path)


def b64_junk_char(sample_path, result_path, jc=b'.', span=1):
    with open(sample_path, "rb") as fin:
        sample_content = fin.read()
    sample_lines = sample_content.split(b"\r\n")
    sample_lines.pop()
    with open(result_path, "wb") as fout:
        for line in sample_lines:
            # pattern = re.compile(rb'.{1}')
            pattern = re.compile(rb'.{' + str(span).encode() + rb'}')
            jc_line = jc.join(pattern.findall(line))
            jc_line += jc + b"\r\n"
            fout.write(jc_line)
    print("Finished: b64_junk_char", jc, span)


def b64_split_encoding(sample_path, result_path, split_span=2):
    with open(sample_path, "rb") as fin:
        sample_content = fin.read()

    sample_len = len(sample_content)
    section_num = math.ceil(sample_len / split_span)

    with open(result_path, "wb") as fout:
        aligned_buf = b""
        for i in range(section_num):
            section = sample_content[i * split_span: (i + 1) * split_span]
            section_b64 = base64.b64encode(section)
            aligned_buf += section_b64
            if len(aligned_buf) >= MAX_LINE_LEN:
                fout.write(aligned_buf + b"\r\n")
                aligned_buf = b""
        if len(aligned_buf) > 0:
            fout.write(aligned_buf + b"\r\n")
    print("Finished: b64_split_encoding", split_span)


def b64_redundant_blank_line(sample_path, result_path, rbl_span=1, rbl_num=1):
    with open(sample_path, "rb") as fin:
        sample_content = fin.read()
    sample_lines = sample_content.split(b"\r\n")
    sample_lines.pop()

    with open(result_path, "wb") as fout:
        while len(sample_lines) > rbl_span:
            # print(len(sample_lines))
            buf = sample_lines[:rbl_span]
            sample_lines = sample_lines[rbl_span:]
            for line in buf:
                fout.write(line + b"\r\n")
            fout.write(b"\r\n" * rbl_num)
        for line in sample_lines:
            fout.write(line + b"\r\n")
    print("Finished: b64_redundant_blank_line. span", rbl_span, "num", rbl_num)


def b64_set_line_len(sample_path, result_path, align=6):
    with open(sample_path, "rb") as fin:
        sample_content = fin.read()
    overall_sample = sample_content.replace(b"\r\n", b"")

    pattern = re.compile(rb"(.{" + str(align).encode() + rb"})")
    aligned_sample_content = re.sub(pattern, b"\g<1>\r\n", overall_sample) + b"\r\n"
    with open(result_path, "wb") as fout:
        fout.write(aligned_sample_content)
    print("Finished: b64_improper_align", align)


# suitable ONLY for basic-qp-encoded content
def basic_qp_set_line_len(basic_qp_sample_path, result_path, ecd_chars=8):
    with open(basic_qp_sample_path, "rb") as fin:
        sample_content = fin.read()
    overall_sample = sample_content.replace(b"=\r\n", b"")
    pattern = re.compile(rb"((=[0-9A-F]{2}){" + str(ecd_chars).encode() + rb"})(?!\r\n)")
    # avoid extra \r\n in the end
    aligned_sample_content = re.sub(pattern, b"\g<1>=\r\n", overall_sample)
    with open(result_path, "wb") as fout:
        fout.write(aligned_sample_content)
    print("Finished: basic_qp_set_line_len", ecd_chars * 3 + 1)

def hex_lower(match):
    upper_hex = match.group()
    # return upper_hex.lower()
    return bytes(chr(upper_hex[0]) + chr(upper_hex[1]).lower() + chr(upper_hex[2]), encoding="utf-8")


def qp_improper_hex_case(sample_path, result_path):
    with open(sample_path, "rb") as fin:
        sample_content = fin.read()
    pattern = re.compile(rb"=[0-9A-F]{2}")
    # tmp = re.search(pattern, sample_content)
    ihc_content = re.sub(pattern, hex_lower, sample_content)
    # ihc_content = re.sub(pattern, b"=xx", sample_content)
    with open(result_path, "wb") as fout:
        fout.write(ihc_content)
    print("Finished: qp_improper_hex_case")


def qp_blank_char(sample_path, result_path, line_break: bytes = b' \r\n'):
    with open(sample_path, "rb") as fin:
        sample_content = fin.read()

    sample_lines = sample_content.split(b"\r\n")
    sample_lines.pop()
    bc_sample_content = line_break.join(sample_lines)
    with open(result_path, "wb") as fout:
        fout.write(bc_sample_content + b"\r\n")
    print("Finished: qp_blank_char", line_break)


def qp_improper_eq_position(sample_path, sample_name, rg=rb"=\r\n", rpl=b"==\r\n"):
    # rg=rb"(\r\n=[0-9A-F]{2})(=[0-9A-F]{2})", rpl=b"\g<1>=2\g<2>"
    # rg=rb"(=[0-9A-F])([0-9A-F])=\r\n", rpl=b"\g<1>=\r\n\g<2>"
    qp_iep_sample_path = r"../qp_improper_eq_position_" + sample_name
    with open(sample_path, "rb") as fin:
        sample_content = fin.read()

    pattern = re.compile(rg)
    iep_sample_content = re.sub(pattern, rpl, sample_content)
    with open(qp_iep_sample_path, "wb") as fout:
        fout.write(iep_sample_content)


def qp_illegal_char(sample_path, result_path, illegal_char=b"\x09"):
    with open(sample_path, "rb") as fin:
        sample_content = fin.read()

    pattern = re.compile(rb"(\r\n=[0-9A-F]{2})(=[0-9A-F]{2})")  # insert char after first "=xx" in a line
    ic_sample_content = re.sub(pattern, b"\g<1>" + illegal_char + b"\g<2>", sample_content)
    with open(result_path, "wb") as fout:
        fout.write(ic_sample_content)
    print("Finished: qp_illegal_char", illegal_char)


def b64_related_modification():
    b64_set_line_len(b64_sample_path, os.path.join(b64_modified_dir, "b64_6char_per_line_" + payload_name))  # b64_6_char_per_line
    b64_junk_char(b64_sample_path, os.path.join(b64_modified_dir, "b64_junk_char_dot_" + payload_name), b".")  # b64_junk_char_dot"
    b64_junk_char(b64_sample_path, os.path.join(b64_modified_dir, "b64_junk_char_dash_" + payload_name), b"-")  # b64_junk_char_dash"
    b64_junk_char(b64_sample_path, os.path.join(b64_modified_dir, "b64_junk_char_space_" + payload_name), b" ")  # b64_junk_char_space"
    b64_junk_char(b64_sample_path, os.path.join(b64_modified_dir, "b64_junk_char_pound_" + payload_name), b"#")  # b64_junk_char_pound"
    b64_junk_char(b64_sample_path, os.path.join(b64_modified_dir, "b64_junk_char_4_dot_" + payload_name), b".", 4)  # b64_junk_char_4_dot"
    b64_junk_char(b64_sample_path, os.path.join(b64_modified_dir, "b64_junk_char_4_eq_" + payload_name), b"=", 4)  # b64_junk_char_4_eq"
    # generic_re_sub(b64_sample_path, result_path, rg=rb"(.{4})", rpl=b"\g<1>=")
    generic_re_sub(b64_sample_path, os.path.join(b64_modified_dir, "b64_line_end_eq_" + payload_name), rg=rb"(.{4})[\r\n]*", rpl=rb"\g<1>=\r\n")  # b64_line_end_eq
    b64_redundant_blank_line(b64_sample_path, os.path.join(b64_modified_dir, "b64_redundant_blank_line_3_" + payload_name), 3, 1)  # b64_redundant_blank_line_3
    b64_redundant_blank_line(b64_sample_path, os.path.join(b64_modified_dir, "b64_redundant_blank_line_5_" + payload_name), 5, 1)  # b64_redundant_blank_line_5
    b64_split_encoding(original_sample_path, os.path.join(b64_modified_dir, "b64_split_1_" + payload_name), 1)  # b64_split_1
    b64_split_encoding(original_sample_path, os.path.join(b64_modified_dir, "b64_split_2_" + payload_name), 2)  # b64_split_2
    b64_set_line_len(b64_sample_path, os.path.join(b64_modified_dir, "b64_overlong_line_" + payload_name), 2000)  # b64_overlong_line


def qp_related_modification():
    # adjust line length to 25
    new_qp_path = os.path.join(qp_modified_dir, "short_line_basic_qp_" + payload_name)
    print("--------- ---------")
    basic_qp_set_line_len(qp_sample_path, new_qp_path, 8)
    print("--------- ---------")

    rg_1st_set = rb"(=[0-9A-F]{2})(.*\r\n)"
    rg_2_line = rb"(.*\r\n.*=[0-9A-F])([0-9A-F])=\r\n"  # split a =xx per 2 lines, in case a overline without \r\n

    generic_re_sub(new_qp_path, os.path.join(qp_modified_dir, "qp_blank_char_l09_" + payload_name), rg=rb"(.*\r\n)", rpl=b"\x09\g<1>")   # qp_blank_char_l09
    generic_re_sub(new_qp_path, os.path.join(qp_modified_dir, "qp_blank_char_l20_" + payload_name), rg=rb"(.*\r\n)", rpl=b"\x20\g<1>")   # qp_blank_char_l20
    generic_re_sub(new_qp_path, os.path.join(qp_modified_dir, "qp_blank_char_r09_" + payload_name), rg=rb"=\r\n", rpl=b"=\x09\r\n")  # qp_blank_char_r09
    generic_re_sub(new_qp_path, os.path.join(qp_modified_dir, "qp_blank_char_r20_" + payload_name), rg=rb"=\r\n", rpl=b"=\x20\r\n")  # qp_blank_char_r20

    generic_re_sub(new_qp_path, os.path.join(qp_modified_dir, "qp_lb_r_" + payload_name), rg=rg_2_line, rpl=b"\g<1>\g<2>=\r")  # qp_lb_r
    generic_re_sub(new_qp_path, os.path.join(qp_modified_dir, "qp_lb_n_" + payload_name), rg=rg_2_line, rpl=b"\g<1>\g<2>=\n")  # qp_lb_n
    generic_re_sub(new_qp_path, os.path.join(qp_modified_dir, "qp_lb_rrn_" + payload_name), rg=rg_2_line, rpl=b"\g<1>\g<2>=\r\r\n")  # qp_lb_rrn
    generic_re_sub(new_qp_path, os.path.join(qp_modified_dir, "qp_lb_rnn_" + payload_name), rg=rg_2_line, rpl=b"\g<1>\g<2>=\r\n\n")  # qp_lb_rnn

    generic_re_sub(new_qp_path, os.path.join(qp_modified_dir, "qp_illegal_char_09_" + payload_name), rg=rg_1st_set, rpl=b"\g<1>\x09\g<2>")  # qp_illegal_char_09
    generic_re_sub(new_qp_path, os.path.join(qp_modified_dir, "qp_illegal_char_12_" + payload_name), rg=rg_1st_set, rpl=b"\g<1>\x12\g<2>")  # qp_illegal_char_12
    generic_re_sub(new_qp_path, os.path.join(qp_modified_dir, "qp_illegal_char_aa_" + payload_name), rg=rg_1st_set, rpl=b"\g<1>\xAA\g<2>")  # qp_illegal_char_aa

    generic_re_sub(new_qp_path, os.path.join(qp_modified_dir, "qp_line_end_split_r_" + payload_name), rg=rg_2_line, rpl=b"\g<1>\r\g<2>")  # qp_line_end_split_r
    generic_re_sub(new_qp_path, os.path.join(qp_modified_dir, "qp_line_end_split_n_" + payload_name), rg=rg_2_line, rpl=b"\g<1>\n\g<2>")  # qp_line_end_split_n
    generic_re_sub(new_qp_path, os.path.join(qp_modified_dir, "qp_line_end_split_ern_" + payload_name), rg=rg_2_line, rpl=b"\g<1>=\r\n\g<2>")  # qp_line_end_split_ern

    generic_re_sub(new_qp_path, os.path.join(qp_modified_dir, "qp_line_end_e_" + payload_name), rg=rb"=\r\n", rpl=rb"==\r\n")  # qp_line_end_e
    generic_re_sub(new_qp_path, os.path.join(qp_modified_dir, "qp_line_end_e2_" + payload_name), rg=rb"=\r\n", rpl=rb"=2=\r\n")  # qp_line_end_e2
    generic_re_sub(new_qp_path, os.path.join(qp_modified_dir, "qp_line_end_eat_" + payload_name), rg=rb"=\r\n", rpl=rb"=@=\r\n")  # qp_line_end_eat
    generic_re_sub(new_qp_path, os.path.join(qp_modified_dir, "qp_line_end_e20e_" + payload_name), rg=rb"=\r\n", rpl=b"=\x20=\r\n")  # qp_line_end_e20e

    generic_re_sub(new_qp_path, os.path.join(qp_modified_dir, "qp_inline_e_" + payload_name), rg=rg_1st_set, rpl=b"\g<1>=\g<2>")  # qp_inline_e
    generic_re_sub(new_qp_path, os.path.join(qp_modified_dir, "qp_inline_e2_" + payload_name), rg=rg_1st_set, rpl=b"\g<1>=2\g<2>")  # qp_inline_e2
    generic_re_sub(new_qp_path, os.path.join(qp_modified_dir, "qp_inline_eat_" + payload_name), rg=rg_1st_set, rpl=b"\g<1>=@\g<2>")  # qp_inline_eat
    generic_re_sub(new_qp_path, os.path.join(qp_modified_dir, "qp_inline_e20e_" + payload_name), rg=rg_1st_set, rpl=b"\g<1>=\x20=\g<2>")  # qp_inline_e20e
    generic_re_sub(new_qp_path, os.path.join(qp_modified_dir, "qp_inline_e09_" + payload_name), rg=rg_1st_set, rpl=b"\g<1>=\x09\g<2>")  # qp_inline_e09
    generic_re_sub(new_qp_path, os.path.join(qp_modified_dir, "qp_inline_e12_" + payload_name), rg=rg_1st_set, rpl=b"\g<1>=\x12\g<2>")  # qp_inline_e12
    generic_re_sub(new_qp_path, os.path.join(qp_modified_dir, "qp_inline_e0_" + payload_name), rg=rg_1st_set, rpl=b"\g<1>=0\g<2>")  # qp_inline_e0
    generic_re_sub(new_qp_path, os.path.join(qp_modified_dir, "qp_inline_e0x_" + payload_name), rg=rg_1st_set, rpl=b"\g<1>=0x\g<2>")  # qp_inline_e0x

    qp_improper_hex_case(new_qp_path, os.path.join(qp_modified_dir, "qp_improper_hex_case_" + payload_name))  # qp_improper_hex_case
    generic_re_sub(new_qp_path, os.path.join(qp_modified_dir, "qp_no_soft_lb_" + payload_name), rg=rb"=\r\n", rpl=b"\r\n")  # qp_no_soft_lb
    basic_qp_set_line_len(qp_sample_path, os.path.join(qp_modified_dir, "qp_overlong_line_" + payload_name), 666)  # qp_overlong_line


if __name__ == '__main__':
    # b64_related_modification()
    qp_related_modification()
    # re_test()
    print("\n========= All Finished =========")
