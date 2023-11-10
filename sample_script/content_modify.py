import re
import math
import base64

sample_path = r"D:\sample\WannaCry\Ransom.WannaCryptor"
b64_wannacry_path = r"../b64_wannacry"
qp_wannacry_path = r"../qp_wannacry_1"
MAX_LINE_LEN = 76


def b64_junk_char(sample_path, sample_name, jc=b'.'):
    b64_jc_sample_path = r"../b64_junk_char_" + sample_name
    with open(sample_path, "rb") as fin:
        sample_content = fin.read()
    sample_lines = sample_content.split(b"\r\n")
    sample_lines.pop()
    with open(b64_jc_sample_path, "wb") as fout:
        for line in sample_lines:
            pattern = re.compile(rb'.{1}')
            jc_line = jc.join(pattern.findall(line))
            jc_line += jc + b"\r\n"
            fout.write(jc_line)


def b64_split_encoding(sample_path, sample_name, split_span=2):
    b64_se_sample_path = r"../b64_split_encoding_" + sample_name
    with open(sample_path, "rb") as fin:
        sample_content = fin.read()

    sample_len = len(sample_content)
    section_num = math.ceil(sample_len / split_span)

    with open(b64_se_sample_path, "wb") as fout:
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


def b64_redundant_blank_line(sample_path, sample_name, rbl_span=1, rbl_num=1):
    b64_rbl_sample_path = r"../b64_redundant_bl_" + sample_name
    with open(sample_path, "rb") as fin:
        sample_content = fin.read()
    sample_lines = sample_content.split(b"\r\n")
    sample_lines.pop()

    with open(b64_rbl_sample_path, "wb") as fout:
        while len(sample_lines) > rbl_span:
            # print(len(sample_lines))
            buf = sample_lines[:rbl_span]
            sample_lines = sample_lines[rbl_span:]
            for line in buf:
                fout.write(line + b"\r\n")
            fout.write(b"\r\n" * rbl_num)
        for line in sample_lines:
            fout.write(line + b"\r\n")


def b64_improper_align(sample_path, result_path, align=6):
    with open(sample_path, "rb") as fin:
        sample_content = fin.read()
    overall_sample = sample_content.replace(b"\r\n", b"")

    pattern = re.compile(rb"(.{6})")
    # a = re.split(pattern, overall_sample)
    # b = a.remove(b"")
    aligned_sample_content = re.sub(pattern, b"\g<1>\r\n", overall_sample) + b"\r\n"

    with open(result_path, "wb") as fout:
        fout.write(aligned_sample_content)


def b64_re_sub(sample_path, result_path, rg=rb"\r\n", rpl=b"=\r\n"):
    with open(sample_path, "rb") as fin:
        sample_content = fin.read()
    pattern = re.compile(rg)
    result_sample_content = re.sub(pattern, rpl, sample_content)
    with open(result_path, "wb") as fout:
        fout.write(result_sample_content)


def hex_lower(match):
    upper_hex = match.group()
    # return upper_hex.lower()
    return bytes(chr(upper_hex[0]) + chr(upper_hex[1]).lower() + chr(upper_hex[2]), encoding="utf-8")


def qp_improper_hex_case(sample_path, sample_name):
    qp_ihc_sample_path = r"../qp_improper_hex_case_" + sample_name
    with open(sample_path, "rb") as fin:
        sample_content = fin.read()

    pattern = re.compile(rb"=[0-9A-F]{2}")
    # tmp = re.search(pattern, sample_content)
    ihc_content = re.sub(pattern, hex_lower, sample_content)
    # ihc_content = re.sub(pattern, b"=xx", sample_content)
    with open(qp_ihc_sample_path, "wb") as fout:
        fout.write(ihc_content)


def qp_blank_char(sample_path, sample_name, line_break: bytes = b' \r\n'):
    qp_bc_sample_path = r"../qp_blank_char_" + sample_name
    with open(sample_path, "rb") as fin:
        sample_content = fin.read()

    sample_lines = sample_content.split(b"\r\n")
    sample_lines.pop()
    bc_sample_content = line_break.join(sample_lines)
    with open(qp_bc_sample_path, "wb") as fout:
        fout.write(bc_sample_content + b"\r\n")


def qp_no_soft_linebreak(sample_path, sample_name):
    qp_nslb_sample_path = r"../qp_no_soft_linebreak_" + sample_name
    with open(sample_path, "rb") as fin:
        sample_content = fin.read()

    pattern = re.compile(rb'=\r\n')
    nslb_sample_content = re.sub(pattern, b"\r\n", sample_content)
    with open(qp_nslb_sample_path, "wb") as fout:
        fout.write(nslb_sample_content)


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


def qp_illegal_char(sample_path, sample_name, line_pos=4, illegal_char=b"\x09"):
    qp_ic_sample_path = r"../qp_illegal_char_" + sample_name
    with open(sample_path, "rb") as fin:
        sample_content = fin.read()

    pattern = re.compile(rb"(\r\n=[0-9A-F]{2})(=[0-9A-F]{2})")
    ic_sample_content = re.sub(pattern, b"\g<1>" + illegal_char + b"\g<2>", sample_content)
    with open(qp_ic_sample_path, "wb") as fout:
        fout.write(ic_sample_content)


def test():
    sample_content = b"=A3"
    sample_content_2 = b"hijklmn"
    a = sample_content.lower()
    b = bytes(chr(sample_content[0]) + chr(sample_content[1]).lower() + chr(sample_content[2]), encoding="utf-8")
    print("finish")


def re_test():
    sample = b"=AF$a=11=82f(z=B9=A7=EA=FEq=BD=14=9E0=95C=098=1C=D2=B6`=07D=C6=8D=7FZ=FD>z?=\r\n" \
             b"=E3=A1=C3=D9]=F6v>=C9s=B4b=BE=BF++=EB=8C$=12=BF0|=07\"zv=C8=8E=B1(v=F5:=EC=\r\n" \
             b"=88\r\n" \
             b"A=C8=84)=FE=AA=F6=BC=ED=C0*=F4=E0=9C=B6=D3=8A+=05=9CkQ=FA=F2T=F4'e=1Ec7dU=\r\n" \
             b"=DEG=CB=DE=87=B2H=B4=C9|=AD>=F0=1Da=A9=DB=F0=87>=F6=D6=82=8A=EC=A2=EF=87=CE=\r\n" \
             b"^l^@x=86=B7=B0=C8=A1s@=9A=FB=95=E6=A7=8A=C2}~=E2=89=9E=20=9F=BD=8FD7=EC=16=\r\n" \
             b"\=87=1A=C73e=04=FD=7Fu=C0=CA=F4=A7=9E=B0=A3&1=F6=1EJ4=193z=9D=08=F7=84.?=C1=\r\n" \
             b"A=D4J=BE=09=04=9E=1DM=F2/e=1F<=F0=E6+=05@|r'=D7=A0=9E=199=C2=E7=A1W=98=FD=\r\n" \
             b"=E7=1F=95jYv=A8\=CB=925=8B=ADn=8Dp=18iG=D1=A7=A12[=FB=F8=B7s=DB[=C0=94=B2iH=\r\n" \
             b"=00\r\n" \
             b">!Z=C4=D1(=F9h1=AA=D7=9E%=916F=FD=9B=B3>=FD=CC=CB=8E=E8kU=BF=B2Y=18=EF(=\r\n" \
             b"=A1=1DI=A9=1F=3D=\r\n"

    sample2 = b"E8kU=BF=B2Y=18=EF(=\r\n=A1=1DI=A9=1F=3D=\r\n"
    sample3 = "E8kU=BF=B2Y=18=EF(=\r\n=A1=1DI=A9=1F=3D=\r\n"

    rg1 = re.compile(rb"(=)([0-9A-Z])\2")

    s2r1 = re.compile(b"\r\n")
    s2r2 = re.compile(rb"\r\n")
    s3r1 = re.compile("\r\n")
    s3r2 = re.compile(r"\r\n")

    a = re.search(rg1, sample)
    b = re.match(rg1, sample)
    c = re.findall(rg1, sample)
    d = re.finditer(rg1, sample)

    for it in d:
        print("hello")

    s2a1 = re.search(s2r1, sample2)
    s2a2 = re.search(s2r2, sample2)
    s3a1 = re.search(s3r1, sample3)
    s3a2 = re.search(s3r2, sample3)

    print("finish")


if __name__ == '__main__':
    # b64_junk_char(b64_wannacry_path, sample_name="wncr4", jc=b"#")
    b64_split_encoding(sample_path, sample_name="wncr1", split_span=1)
    # b64_redundant_blank_line(b64_wannacry_path, sample_name="wncr")
    # b64_improper_align(b64_wannacry_path, result_path=r"../b64_wncr_6char_per_line")
    # b64_re_sub(b64_wannacry_path, result_path=r"../b64_4char_eq", rg=rb"(.{4})", rpl=b"\g<1>=")


    # qp_improper_hex_case(qp_wannacry_path, sample_name="wncr")
    # qp_blank_char(qp_wannacry_path, sample_name="l20_wncr", line_break=b"\r\n\x20")
    # qp_no_soft_linebreak(qp_wannacry_path, sample_name="wncr")
    # qp_improper_eq_position(qp_wannacry_path, sample_name="wncr_within_line8", rg=rb"(\r\n=[0-9A-F]{2})(=[0-9A-F]{2})", rpl=b"\g<1>=0x\g<2>")
    # qp_illegal_char(qp_wannacry_path, sample_name="wncr_AA", illegal_char=b"\xAA")

    # test()
    # re_test()
