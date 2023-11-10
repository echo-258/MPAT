test_cases = {
    # cases aimed at affecting structure of the message
    "irregular_header&body_delimit_1": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: irregular_header&body_delimit_1\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=b64_eicar_1\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar1\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n"
            b"1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"b64. app. CTE-body."
    },
    "irregular_header&body_delimit_2": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: irregular_header&body_delimit_2\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=b64_eicar_2\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar2\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n"
            b"1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"b64. text. CTE-body."
    },
    "irregular_header&body_delimit_3": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: irregular_header&body_delimit_3\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=qp_eicar_3\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar3\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\n"
            b"TEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"qp. text. CTE-body."
    },
    "irregular_header&body_delimit_4": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: irregular_header&body_delimit_4\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=b64_eicar_4\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar4\r\n"
            b"\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n"
            b"1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"b64. app. CRLF-CTE-CRLF-body."
    },
    "irregular_header&body_delimit_5": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: irregular_header&body_delimit_5\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=b64_eicar_5\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar5\r\n"
            b"\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n"
            b"1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"b64. text. CRLF-CTE-CRLF-body."
    },
    "irregular_header&body_delimit_6": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: irregular_header&body_delimit_6\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=qp_eicar_6\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar6\r\n"
            b"\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\n"
            b"TEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"qp. text. CRLF-CTE-CRLF-body."
    },
    "irregular_header&body_delimit_7": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: irregular_header&body_delimit_7\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=qp_eicar_7\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar7\r\n"
            b"\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\n"
            b"TEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"qp. text. CRLF-CTE-body."
    },
    "irregular_header&body_delimit_8": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: irregular_header&body_delimit_8\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=qp_eicar_8\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar8\r\n"
            b"\r\n"
            b"A meaningless sentence.\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\n"
            b"TEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"qp. text. CRLF-meaningless-CTE-CRLF-body."
    },
    "irregular_header&body_delimit_9": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: irregular_header&body_delimit_9\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=qp_eicar_9\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar9\r\n"
            b"\r\n"
            b"A meaningless sentence.\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"Another meaningless sentence.\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\n"
            b"TEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"qp. text. CRLF-meaningless-CTE-meaningless-CRLF-body."
    },
    "irregular_header&body_delimit_10": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: irregular_header&body_delimit_10\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=qp_eicar_10\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar10\r\n"
            b"\r\n"
            b"A meaningless sentence.\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\n"
            b"TEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"qp. text. CRLF-meaningless-CTE-body."
    },
    "irregular_header&body_delimit_11": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: irregular_header&body_delimit_11\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=qp_eicar_11\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar11\r\n"
            b"\r\n"
            b" Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\n"
            b"TEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"qp. text. CRLF-space-CTE-CRLF-body."
    },
    "irregular_header&body_delimit_12": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: irregular_header&body_delimit_12\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=qp_eicar_12\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar12\r\n"
            b"A meaningless sentence.\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\n"
            b"TEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"qp. text. meaningless-CTE-body."
    },
    # To Do: insert fake "Content-" header before CTE header.
}