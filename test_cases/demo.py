test_cases = {
    "normal_msg": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: simplest case - test sending function\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"Hi, this is a test message! Best wishes.\r\n"
        ,
        "description": b"The simplest test case, just to test sending function."
    },

    "b64_wannacry_test": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64 wannacry test case\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=b64_wanna\r\n"
            b"Content-Disposition: attachment; filename=b64_wanna\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"<This is b64_wannacry.>"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw sample with Base 64. Use app/octet type header."
    },
    "multiple_encoding": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: multiple encoding\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=b64_sample\r\n"
            b"Content-Disposition: attachment; filename=b64_sample\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"<This is b64_wannacry.>"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Multiple CTE header."
    },
    "b64_split_encoding_1": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64_split_encoding_1\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=hello.exe\r\n"
            b"Content-Disposition: attachment; filename=hello.exe\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"<b64_split_encoding wncr1 here>"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Employ split encoding."
    },

    "normal_att_4": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: normal attachment test case\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=a.txt\r\n"
            b"Content-Disposition: attachment; filename=b.exe\r\n"
            b"Content of a text attachment.\r\nJust for testing sending function.\r\n"
            b"--foo--\r\n"
        ,
        "description": b"A textual attachment. Lack blank line within attachment part."
    },
    "b64_eicar": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64 eicar test case\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=b64_eicar\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n"
            b"1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Use app/octet type header."
    },
    "special_boundary": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64 eicar test case with special boundary\r\n"
            b"Content-Type: multipart/mixed; boundary=1URVNULUZJTEUhJEgrSCo=\r\n"
            b"\r\n"
            b"--1URVNULUZJTEUhJEgrSCo=\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--1URVNULUZJTEUhJEgrSCo=\r\n"
            b"Content-type: application/octet-stream; name=b64_eicar\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r"
            b"--1URVNULUZJTEUhJEgrSCo=--\r\n"
        ,
        "description": b"Special boundary extracted from eicar content. Use Base64 encoding."
    },
    "qp_eicar": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp eicar test case\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=qp_eicar\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\n"
            b"TEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Use text/plain type header."
    },

    "qp_wannacry_test": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp wannacry test case\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=qp_wanna\r\n"
            b"Content-Disposition: attachment; filename=qp_wanna\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"<This is qp_wannacry.>"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw sample with Quoted-printable. Use app/octet type header."
    },
    "mul_bound_statement_3": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: mul_bound_statement_3\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"Content-Type: multipart/mixed; boundary=faa\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=b64_att_3\r\n"
            b"Content-Disposition: attachment; filename=b64_att3\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"<b64_eicar>"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw sample with Base 64. Use app/octet type header. Use .txt filename."
    },
    "mul_bound_statement_7": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: mul_bound_statement_7\r\n"
            b"Content-Type: multipart/mixed; boundary=faa\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=b64_att_7\r\n"
            b"Content-Disposition: attachment; filename=b64_att7\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"<b64_eicar>"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw sample with Base 64. Use app/octet type header. Use .txt filename."
    },
    "1123_b64": {
        "data":
            b"Subject: multiple type header\r\n"
            b"MIME-Version: 1.0\r\n"
            b"Content-Type: multipart/mixed; boundary=+++boundary_multipart-1_boundary+++\r\n"
            b"Content-Type: application/octet-stream\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"Content-ID: 1\r\n"
            b"Content-Disposition: attachment; filename=sample\r\n"
            b"\r\n"
            b"<This is b64_wannacry.>"
    },
    "comment_boundary_125": {
        "data":
            b"Subject: comment_boundary_125\r\n"
            b"MIME-Version: 1.0\r\n"
            b"Content-Type: multipart/mixed; boundary=\"\"1\r\n"
            b"\r\n"
            b"--123\n\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\n"
            b"This is the main body text part.\r\n"
            b"--1\r\n"
            b"Content-type: application/octet-stream; name=b64_att_10\r\n"
            b"Content-Disposition: attachment; filename=b64_att10\r\n"
            b"Content-Transfer-Encoding: utf-7\r\n"
            b"\r\n"
            b"X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*\r\n"
            b"--1--\r\n"
    },
    "missing_end_hyphen": {
        "data":
            b"Subject: missing_end_hyphen\r\n"
            b"MIME-Version: 1.0\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"Content-Disposition: attachment; filename=att_2\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n"
            b"1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo \r\n"
    },
    "qp_blank_char": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp_blank_char\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=qp_eicar\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\x09\r\n"
            b"TEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"blank char (tab) at the end of qp line"
    },

    "basic_structure": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: basic_structure\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=att\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "basic_structure_binary": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: basic_structure_binary\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=att\r\n"
            b"Content-Transfer-Encoding: binary\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "basic_structure_b64": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: basic_structure_b64\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=att\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "basic_structure_qp": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: basic_structure_qp\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=att\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },

    "special_boundary_r_bound": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: special_boundary_r_bound\r\n"
            b"Content-Type: multipart/mixed; boundary=AacWt5K1CCNo9ashLndz1QL8NIKlgk\r\n"
            b"\r\n"
            b"--AacWt5K1CCNo9ashLndz1QL8NIKlgk\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--AacWt5K1CCNo9ashLndz1QL8NIKlgk\r\n"
            b"Content-type: application/octet-stream; name=b64_att_6\r\n"
            b"Content-Disposition: attachment; filename=b64_att6\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"WrIS53c9UC/DSCpYJPQ0P4WTMPrK+W\r"
            b"--AacWt5K1CCNo9ashLndz1QL8NIKlgk--\r\n"
            b"9DQ/hZMw+sr5YBpxa3krUII2j1qyEu\r\n"
            b"d3PVAvw0gqWCT0ND+FkzD6yvlgGnFr\r\n"
            b"eStQgjaP\r\n"
        ,
        "description": b"Special boundary extracted from sample content. Use Base 64 encoding."
    },
    "special_boundary_n_bound": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: special_boundary_n_bound\r\n"
            b"Content-Type: multipart/mixed; boundary=AacWt5K1CCNo9ashLndz1QL8NIKlgk\r\n"
            b"\r\n"
            b"--AacWt5K1CCNo9ashLndz1QL8NIKlgk\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--AacWt5K1CCNo9ashLndz1QL8NIKlgk\r\n"
            b"Content-type: application/octet-stream; name=b64_att_6\r\n"
            b"Content-Disposition: attachment; filename=b64_att6\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"WrIS53c9UC/DSCpYJPQ0P4WTMPrK+W\n"
            b"--AacWt5K1CCNo9ashLndz1QL8NIKlgk--\r\n"
            b"9DQ/hZMw+sr5YBpxa3krUII2j1qyEu\r\n"
            b"d3PVAvw0gqWCT0ND+FkzD6yvlgGnFr\r\n"
            b"eStQgjaP\r\n"
        ,
        "description": b"Special boundary extracted from sample content. Use Base 64 encoding."
    },

    "boundary_eq_folding": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: boundary_eq_folding\r\n"
            b"Content-Type: multipart/mixed; boundary=\r\n"
            b" foofoo\r\n"
            b"Content-ID: 3\r\n"
            b"\r\n"
            b"--foofoo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foofoo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=att\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foofoo--\r\n"
        ,
        "description": b""
    },
    "boundary_eq_space_folding": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: boundary_eq_space_folding\r\n"
            b"Content-Type: multipart/mixed; boundary= \r\n"
            b" foofoo\r\n"
            b"Content-ID: 3\r\n"
            b"\r\n"
            b"--foofoo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foofoo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=att\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foofoo--\r\n"
        ,
        "description": b""
    },
    "boundary_folding_eq": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: boundary_folding_eq\r\n"
            b"Content-Type: multipart/mixed; boundary\r\n"
            b" =foofoo\r\n"
            b"Content-ID: 3\r\n"
            b"\r\n"
            b"--foofoo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foofoo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=att\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foofoo--\r\n"
        ,
        "description": b""
    },
    "boundary_space_folding_eq": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: boundary_space_folding_eq\r\n"
            b"Content-Type: multipart/mixed; boundary \r\n"
            b" =foofoo\r\n"
            b"Content-ID: 3\r\n"
            b"\r\n"
            b"--foofoo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foofoo\r\n"
            b"Content-Type: application/octet-stream; name=att\r\n"
            b"Content-Disposition: attachment; filename=att\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"<specified_payload_here>"
            b"--foofoo--\r\n"
        ,
        "description": b""
    },

    "question": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: hello\r\n"
            b"Content-Type: multipart/mixed; boundary=bound_0123abcd\r\n"
            b"\r\n"
            b"--bound_0123abcd--\r\n"
            b"Content-Type: text/plain; charset=UTF-8\r\n"
            b"\r\n"
            b"Email with an attachment.\r\n"
            b"--bound_0123abcd--\r\n"
            b"Content-Type: text/plain; charset=UTF-8, name=a.txt\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"Content-Disposition: attachment; filename=\"a.txt\"\r\n"
            b"\r\n"
            b"5bqK5YmN5piO5pyI5YWJ55aR5piv5Zyw5LiK6Zyc\r\n"
            b"--bound_0123abcd--\r\n"
        ,
        "description": b"The simplest test case, just to test sending function."
    },
}
