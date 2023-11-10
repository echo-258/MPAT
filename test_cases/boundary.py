test_cases = {
    # data content as boundary
    "special_boundary_1": {
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
            b"Content-type: text/plain; name=b64_eicar_1\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar1\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"VHdmdzc4MzY0RldiMzAucmZlXWdhMWB6\r\n"
            b"--1URVNULUZJTEUhJEgrSCo=--\r\n"
        ,
        "description": b"Special boundary extracted from eicar content. Use Base 64 encoding."
    },
    "special_boundary_2": {
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
            b"Content-type: text/plain; name=b64_eicar_2\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar2\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"VHdmdzc4MzY0RldiMzAucmZlXWdhMWB6--\r\n"
            b"--1URVNULUZJTEUhJEgrSCo=--\r\n"
        ,
        "description": b"Special boundary extracted from eicar content. Use Base 64 encoding."
    },
    "special_boundary_3": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp eicar test case with special boundary\r\n"
            b"Content-Type: multipart/mixed; boundary=TEST-FILE=21=24H=2BH=2A\r\n"
            b"\r\n"
            b"--TEST-FILE=21=24H=2BH=2A\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--TEST-FILE=21=24H=2BH=2A\r\n"
            b"Content-type: text/plain; name=qp_eicar_3\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar3\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"Twfw78364FWb30.rfe=5Dga1=60z\r\n"
            b"--TEST-FILE=21=24H=2BH=2A--\r\n"
        ,
        "description": b"Special boundary extracted from eicar content. Use Quoted-printable encoding."
    },
    "special_boundary_4": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp eicar test case with special boundary\r\n"
            b"Content-Type: multipart/mixed; boundary=TEST-FILE=21=24H=2BH=2A\r\n"
            b"\r\n"
            b"--TEST-FILE=21=24H=2BH=2A\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--TEST-FILE=21=24H=2BH=2A\r\n"
            b"Content-type: text/plain; name=qp_eicar_4\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar4\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"Twfw78364FWb30.rfe=5Dga1=60z--\r\n"
            b"--TEST-FILE=21=24H=2BH=2A--\r\n"
        ,
        "description": b"Special boundary extracted from eicar content. Use Quoted-printable encoding."
    },
    "special_boundary_5": {
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
            b"Content-type: text/plain; name=b64_eicar_5\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar5\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n"
            b"--1URVNULUZJTEUhJEgrSCo=--\r\n"
        ,
        "description": b"Special boundary extracted from eicar content. Use Base 64 encoding."
    },
    "special_boundary_6": {
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
            b"Content-type: text/plain; name=b64_eicar_6\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar6\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy--1URVNULUZJTEUhJEgrSCo=--\r\n"
        ,
        "description": b"Special boundary extracted from eicar content. Use Base 64 encoding."
    },
    "special_boundary_7": {
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
            b"Content-type: text/plain; name=b64_eicar_7\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar7\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r"
            b"--1URVNULUZJTEUhJEgrSCo=--\r\n"
        ,
        "description": b"Special boundary extracted from eicar content. Use Base 64 encoding."
    },
    "special_boundary_8": {
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
            b"Content-type: text/plain; name=b64_eicar_8\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar8\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\n"
            b"--1URVNULUZJTEUhJEgrSCo=--\r\n"
        ,
        "description": b"Special boundary extracted from eicar content. Use Base 64 encoding."
    },

    # duplicated boundary statement
    "mul_bound_statement_1": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: mul_bound_statement_1\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"Content-Type: multipart/mixed; boundary=faa\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=eicar_1\r\n"
            b"Content-Disposition: attachment; filename=eicar1\r\n"
            b"\r\n"
            b"X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Raw eicar as attachment. Without other encoding. Use app/octet type header. Boundary is wrong."
    },
    "mul_bound_statement_2": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: mul_bound_statement_2\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"Content-Type: multipart/mixed; boundary=faa\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=b64_eicar_2.txt\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar2.txt\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n"
            b"1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Use app/octet type header. Use .txt filename."
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
            b"Content-type: text/plain; name=b64_eicar_3\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar3\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n"
            b"1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Use app/octet type header. Use .txt filename."
    },
    "mul_bound_statement_4": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: mul_bound_statement_4\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"Content-Type: multipart/mixed; boundary=faa\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=qp_eicar_4.txt\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar4.txt\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\n"
            b"TEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Use text/plain type header."
    },
    "mul_bound_statement_5": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: mul_bound_statement_5\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"Content-Type: multipart/mixed; boundary=faa\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=qp_eicar_5\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar5\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\n"
            b"TEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Use app/octet type header."
    },
    "mul_bound_statement_6": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: mul_bound_statement_6\r\n"
            b"Content-Type: multipart/mixed; boundary=faa\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=b64_eicar_6.txt\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar6.txt\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n"
            b"1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Use app/octet type header. Use .txt filename."
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
            b"Content-type: text/plain; name=b64_eicar_7\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar7\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n"
            b"1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Use app/octet type header. Use .txt filename."
    },
    "mul_bound_statement_8": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: mul_bound_statement_8\r\n"
            b"Content-Type: multipart/mixed; boundary=faa\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=qp_eicar_8.txt\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar8.txt\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\n"
            b"TEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Use app/octet type header."
    },
    "mul_bound_statement_9": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: mul_bound_statement_9\r\n"
            b"Content-Type: multipart/mixed; boundary=faa\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=qp_eicar_9\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar9\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\n"
            b"TEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Use text/plain type header."
    },
    "mul_bound_statement_10": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: mul_bound_statement_10\r\n"
            b"Content-Type: multipart/mixed; boundary=faa\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=b64_eicar_10.txt\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar10.txt\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n"
            b"1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Use app/octet type header. Use .txt filename."
    },
    "mul_bound_statement_11": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: mul_bound_statement_11\r\n"
            b"Content-Type: multipart/mixed; boundary=faa\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=qp_eicar_11.txt\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar11.txt\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\n"
            b"TEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Use text/plain type header."
    },
    "mul_bound_statement_12": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: mul_bound_statement_12\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"Content-Type: multipart/mixed; boundary=faa\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=b64_eicar_12.txt\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar12.txt\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n"
            b"1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Use app/octet type header. Use .txt filename."
    },
    "mul_bound_statement_13": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: mul_bound_statement_13\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"Content-Type: multipart/mixed; boundary=faa\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=qp_eicar_13.txt\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar13.txt\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\n"
            b"TEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Use text/plain type header."
    },
}