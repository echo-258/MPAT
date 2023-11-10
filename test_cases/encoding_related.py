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
    "b64_eicar_4": {
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
            b"Content-type: application/octet-stream; name=b64_eicar_4\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar4\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n"
            b"1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Use app/octet type header."
    },
    "qp_eicar_4": {
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
            b"Content-type: text/plain; name=qp_eicar_4\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar4\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\n"
            b"TEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Use text/plain type header."
    },
    "raw_wannacry": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: simplest case - test sending function\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"Hi, this is a test message! Best wishes.\r\n"
            b"<This is wannacry.>\r\n"
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

    "b64_4char_eq": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64_4char_eq\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=b64_att_4char_eq\r\n"
            b"Content-Disposition: attachment; filename=b64_att4char_eq\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"<b64_4char_eq wncr here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "b64_6char_per_line": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64_6char_per_line\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=b64_att_6char_per_line\r\n"
            b"Content-Disposition: attachment; filename=b64_att6char_per_line\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"<b64_6char_per_line wncr here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "b64_junk_char_1": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64_junk_char_1\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=b64_att_1\r\n"
            b"Content-Disposition: attachment; filename=b64_att1\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"<b64_junk_char wncr1 here>"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw sample with Base 64. Add junk chars in data."
    },
    "b64_junk_char_2": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64_junk_char_2\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=b64_att_2\r\n"
            b"Content-Disposition: attachment; filename=b64_att2\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"<b64_junk_char wncr2 here>"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw sample with Base 64. Add junk chars in data."
    },
    "b64_junk_char_3": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64_junk_char_3\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
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
            b"<b64_junk_char wncr3 here>"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw sample with Base 64. Add junk chars in data."
    },
    "b64_junk_char_4": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64_junk_char_4\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=b64_att_4\r\n"
            b"Content-Disposition: attachment; filename=b64_att4\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"<b64_junk_char wncr4 here>"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw sample with Base 64. Add junk chars in data."
    },
    "b64_line_end_eq": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64_line_end_eq\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=b64_att_line_end_eq\r\n"
            b"Content-Disposition: attachment; filename=b64_attline_end_eq\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"<b64_line_end_eq wncr here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "b64_redundant_blank_line_3": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64_redundant_blank_line_3\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
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
            b"<b64_redundant_bl wncr here>"
            b"--foo--\r\n"
        ,
        "description": b"extra blank line within b64 content. type: application"
    },
    "b64_redundant_blank_line_5": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64_redundant_blank_line_5\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=b64_att_5\r\n"
            b"Content-Disposition: attachment; filename=b64_att5\r\n"
            b"\r\n"
            b"<b64_redundant_bl wncr here>"
            b"--foo--\r\n"
        ,
        "description": b"extra blank line within b64 content. type: application. no CTE header"
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
            b"Content-type: application/octet-stream; name=att_b64_split_encoding_1\r\n"
            b"Content-Disposition: attachment; filename=attb64_split_encoding_1\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"<b64_split_encoding wncr1 here>"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Employ split encoding."
    },
    "b64_split_encoding_2": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64_split_encoding_2\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=att_b64_split_encoding_2\r\n"
            b"Content-Disposition: attachment; filename=attb64_split_encoding_2\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"<b64_split_encoding wncr2 here>"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Employ split encoding."
    },

    "qp_blank_char_l09": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp_blank_char_l09\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=qp_att_l09\r\n"
            b"Content-Disposition: attachment; filename=qp_attl09\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"<qp_blank_char_l09 wncr here>"
            b"--foo--\r\n"
        ,
        "description": b"blank char (tab) at the end of qp line"
    },
    "qp_blank_char_l20": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp_blank_char_l20\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=qp_att_l20\r\n"
            b"Content-Disposition: attachment; filename=qp_attl20\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"<qp_blank_char_l20 wncr here>"
            b"--foo--\r\n"
        ,
        "description": b"blank char (tab) at the end of qp line"
    },
    "qp_blank_char_r09": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp_blank_char_r09\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=qp_att_r09\r\n"
            b"Content-Disposition: attachment; filename=qp_attr09\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"<qp_blank_char_r09 wncr here>"
            b"--foo--\r\n"
        ,
        "description": b"blank char (tab) at the end of qp line"
    },
    "qp_blank_char_r20": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp_blank_char_r20\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=qp_att_r20\r\n"
            b"Content-Disposition: attachment; filename=qp_attr20\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"<qp_blank_char_r20 wncr here>"
            b"--foo--\r\n"
        ,
        "description": b"blank char (tab) at the end of qp line"
    },
    "qp_illegal_char_09": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp_illegal_char_09\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=qp_att_illegal_char_09\r\n"
            b"Content-Disposition: attachment; filename=qp_attillegal_char_09\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"<qp_illegal_char_09 wncr here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "qp_illegal_char_12": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp_illegal_char_12\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=qp_att_illegal_char_12\r\n"
            b"Content-Disposition: attachment; filename=qp_attillegal_char_12\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"<qp_illegal_char_12 wncr here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "qp_illegal_char_aa": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp_illegal_char_aa\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=qp_att_illegal_char_aa\r\n"
            b"Content-Disposition: attachment; filename=qp_attillegal_char_aa\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"<qp_illegal_char_aa wncr here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },

    "qp_improper_eq_position_line_end_split_1": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp_improper_eq_position_line_end_split_1\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=att_line_end_split1\r\n"
            b"Content-Disposition: attachment; filename=attline_end_split1\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"<qp_improper_eq_position_line_end_split wncr1 here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "qp_improper_eq_position_line_end_split_2": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp_improper_eq_position_line_end_split_2\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=att_line_end_split2\r\n"
            b"Content-Disposition: attachment; filename=attline_end_split2\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"<qp_improper_eq_position_line_end_split wncr2 here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "qp_improper_eq_position_line_end_split_3": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp_improper_eq_position_line_end_split_3\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=att_line_end_split3\r\n"
            b"Content-Disposition: attachment; filename=attline_end_split3\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"<qp_improper_eq_position_line_end_split wncr3 here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "qp_improper_eq_position_line_end_1": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp_improper_eq_position_line_end_1\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=att_line_end_1\r\n"
            b"Content-Disposition: attachment; filename=attline_end_1\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"<qp_improper_eq_position_line_end wncr1 here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "qp_improper_eq_position_line_end_2": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp_improper_eq_position_line_end_2\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=att_line_end_2\r\n"
            b"Content-Disposition: attachment; filename=attline_end_2\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"<qp_improper_eq_position_line_end wncr2 here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "qp_improper_eq_position_within_line_1": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp_improper_eq_position_within_line_1\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=att_within_line_1\r\n"
            b"Content-Disposition: attachment; filename=attwithin_line_1\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"<qp_improper_eq_position_within_line wncr1 here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "qp_improper_eq_position_within_line_2": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp_improper_eq_position_within_line_2\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=att_within_line_2\r\n"
            b"Content-Disposition: attachment; filename=attwithin_line_2\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"<qp_improper_eq_position_within_line wncr2 here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "qp_improper_eq_position_within_line_3": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp_improper_eq_position_within_line_3\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=att_within_line_3\r\n"
            b"Content-Disposition: attachment; filename=attwithin_line_3\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"<qp_improper_eq_position_within_line wncr3 here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "qp_improper_eq_position_within_line_4": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp_improper_eq_position_within_line_4\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=att_within_line_4\r\n"
            b"Content-Disposition: attachment; filename=attwithin_line_4\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"<qp_improper_eq_position_within_line wncr4 here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "qp_improper_eq_position_within_line_5": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp_improper_eq_position_within_line_5\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=att_within_line_5\r\n"
            b"Content-Disposition: attachment; filename=attwithin_line_5\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"<qp_improper_eq_position_within_line wncr5 here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "qp_improper_eq_position_within_line_6": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp_improper_eq_position_within_line_6\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=att_within_line_6\r\n"
            b"Content-Disposition: attachment; filename=attwithin_line_6\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"<qp_improper_eq_position_within_line wncr6 here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "qp_improper_eq_position_within_line_7": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp_improper_eq_position_within_line_7\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=att_within_line_7\r\n"
            b"Content-Disposition: attachment; filename=attwithin_line_7\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"<qp_improper_eq_position_within_line wncr7 here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "qp_improper_eq_position_within_line_8": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp_improper_eq_position_within_line_8\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=att_within_line_8\r\n"
            b"Content-Disposition: attachment; filename=attwithin_line_8\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"<qp_improper_eq_position_within_line wncr8 here>"
            b"--foo--\r\n"
        ,
        "description": b""
    },

    "qp_improper_hex_case_2": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp_improper_hex_case_2\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=qp_att_2\r\n"
            b"Content-Disposition: attachment; filename=qp_att2\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"<qp_improper_hex_case wncr here>"
            b"--foo--\r\n"
        ,
        "description": b"improper case of quoted-printable hex number. =5e"
    },
    "qp_no_soft_linebreak_2": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp_no_soft_linebreak_2\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=qp_att_2\r\n"
            b"Content-Disposition: attachment; filename=qp_att2\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"<qp_no_soft_linebreak wncr here>"
            b"--foo--\r\n"
        ,
        "description": b"no soft line break between continuous qp lines"
    },
}
