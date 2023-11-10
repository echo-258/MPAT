import re
import base64
import email.encoders as e_ecd
import quopri
from tqdm import tqdm

raw_sample_path = r"../sample/eicar/eicar.zip"
b64_sample_path = r"../sample/eicar/b64_eicar_zip"
qp_sample_path = r"../sample/eicar/qp_eicar_zip"
basic_qp_path = r"../sample/eicar/basic_qp_eicar_zip"

MAX_LINE_LEN = 76


def b64_encode_sample():
    with open(raw_sample_path, "rb") as raw_fp:
        sample_content = raw_fp.read()

    b64_sample = base64.b64encode(sample_content)
    # b64_wncr_str = str(b64_wncr)
    # print(len(b64_wncr), len(b64_wncr_str))
    # aligned_b64_wncr = b""
    # while len(b64_wncr) > 0:
    #     # print(len(b64_wncr))
    #     buf = b64_wncr[:MAX_LINE_LEN]
    #     aligned_b64_wncr += buf
    #     aligned_b64_wncr += b"\r\n"
    #     b64_wncr = b64_wncr[MAX_LINE_LEN:]

    pattern = re.compile(rb"(.{76})")
    aligned_b64_sample = re.split(pattern, b64_sample)
    # while b"" in aligned_b64_sample:
    #     aligned_b64_sample.remove(b"")

    with open(b64_sample_path, "wb") as b64_sample_fp:
        for line in aligned_b64_sample:
            if line != b"":
                b64_sample_fp.write(line + b"\r\n")
    # with open(b64_wannacry_str_path, "w") as b64_sample_str_fp:
    #     b64_sample_str_fp.write(b64_sample_str)


def qp_encode_sample():
    # problem exist. use \n as line break
    return

    # with open(raw_sample_path, "rb") as raw_fp:
    #     with open(qp_sample_path, "wb") as qp_sample_fp:
    #         quopri.encode(raw_fp, qp_sample_fp, 1)
    #         qp_sample_fp.write(b"\r\n")


def basic_qp_encode_sample():
    with open(raw_sample_path, "rb") as raw_fp:
        sample_content = raw_fp.read()

    line_buf = ""
    lines = []
    for b in tqdm(sample_content):
        line_buf += "={:02X}".format(b)
        if len(line_buf) >= 75:
            lines.append(bytes(line_buf, "utf-8"))
            line_buf = ""
    if len(line_buf) > 0:       # final line, incomplete
        lines.append(bytes(line_buf, "utf-8"))
    basic_qp_content = b"=\r\n".join(lines)
    with open(basic_qp_path, "wb") as basic_qp_fp:
        basic_qp_fp.write(basic_qp_content)
        basic_qp_fp.write(b"\r\n")


b64_encode_sample()
qp_encode_sample()
basic_qp_encode_sample()
