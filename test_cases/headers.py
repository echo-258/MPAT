test_cases = {
    # cases about the appearance headers

    # lack of headers
    "normal_att_no_mimeV": {
        "data":
            b"Subject: normal attachment test case without MIME-Version header\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=a.txt\r\n"
            b"Content-Disposition: attachment; filename=b.txt\r\n"
            b"\r\n"
            b"Content of a text attachment.\r\nJust for testing sending function.\r\n"
            b"--foo--\r\n"
        ,
        "description": b"A textual attachment. Lack MIME-Version header."
    },
    "raw_eicar_no_mimeV_1": {
        "data":
            b"Subject: raw eicar test case without MIME-Version header\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=eicar_1.com\r\n"
            b"Content-Disposition: attachment; filename=eicar1.com\r\n"
            b"\r\n"
            b"X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Raw eicar.com as attachment. Lack MIME-Version header."
    },
    "raw_eicar_no_mimeV_2": {
        "data":
            b"Subject: raw eicar test case without MIME-Version header\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=eicar_2.txt\r\n"
            b"Content-Disposition: attachment; filename=eicar2.txt\r\n"
            b"\r\n"
            b"X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Raw eicar.com as attachment. Lack MIME-Version header. Use .txt filename."
    },

    "normal_att_no_type": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: normal attachment test case without Content-Type header\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-Disposition: attachment; filename=b.txt\r\n"
            b"\r\n"
            b"Content of a text attachment.\r\nJust for testing sending function.\r\n"
            b"--foo--\r\n"
        ,
        "description": b"A textual attachment. Lack Content-Type header."
    },
    "raw_eicar_no_type_1": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: raw eicar test case without Content-Type header\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-Disposition: attachment; filename=eicar1.com\r\n"
            b"\r\n"
            b"X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Raw eicar.com as attachment. Lack Content-Type header."
    },
    "raw_eicar_no_type_2": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: raw eicar test case without Content-Type header\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-Disposition: attachment; filename=eicar2\r\n"
            b"\r\n"
            b"X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Raw eicar.com as attachment. Lack Content-Type header. No extension."
    },
    "b64_eicar_no_type_1": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64 eicar test case without Content-Type header\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar1.com\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Use app/octet type header."
    },
    "b64_eicar_no_type_2": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64 eicar test case without Content-Type header\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar2\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Use app/octet type header. No extension."
    },

    "normal_att_no_encoding_1": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: normal attachment test case without Content-Transfer-Encoding header\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=normal_1\r\n"
            b"Content-Disposition: attachment; filename=normal1\r\n"
            b"\r\n"
            b"VHdmdzc4MzY0RldiMzAucmZlXWdhMWB6\r\n"
            b"--foo--\r\n"
        ,
        "description": b"A textual attachment with Base64 encoding. Lack Content-Transfer-Encoding header."
    },
    "normal_att_no_encoding_2": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: normal attachment test case without Content-Transfer-Encoding header\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=normal_2\r\n"
            b"Content-Disposition: attachment; filename=normal2\r\n"
            b"\r\n"
            b"Twfw78364FWb30.rfe=5Dga1=60z\r\n"
            b"--foo--\r\n"
        ,
        "description": b"A textual attachment with Quoted-printable. Lack Content-Transfer-Encoding header."
    },

    "b64_eicar_no_encoding_1": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64 eicar test case without Content-Transfer-Encoding header\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=b64_eicar_1.com\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar1.com\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Lack Content-Transfer-Encoding header."
    },
    "b64_eicar_no_encoding_2": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64 eicar test case without Content-Transfer-Encoding header\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=b64_eicar_2\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar2\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Lack Content-Transfer-Encoding header."
    },
    "b64_eicar_no_encoding_3": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64 eicar test case without Content-Transfer-Encoding header\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=b64_eicar_3\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar3\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Use text/plain type header. Lack Content-Transfer-Encoding header."
    },
    "b64_eicar_no_encoding_g1": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64 eicar test case without Content-Transfer-Encoding header\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=b64_eicar_g1\r\n"
            b"Content-Disposition: attachment; filename=b64_eicarg1\r\n"
            b"\r\n"
            b"VHdmdzc4MzY0RldiMzAucmZlXWdhMWB6\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode normal message with Base 64. Lack Content-Transfer-Encoding header."
    },
    "b64_eicar_no_encoding_g2": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64 eicar test case without Content-Transfer-Encoding header\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=b64_eicar_g2\r\n"
            b"Content-Disposition: attachment; filename=b64_eicarg2\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n1URVNULUZJTEUhJEgr\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Lack Content-Transfer-Encoding header."
    },
    "b64_eicar_no_encoding_g3": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64 eicar test case without Content-Transfer-Encoding header\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=b64_eicar_g2\r\n"
            b"Content-Disposition: attachment; filename=b64_eicarg2\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\nTEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-Printable. Lack Content-Transfer-Encoding header."
    },

    "qp_eicar_no_encoding_1": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64 eicar test case without Content-Transfer-Encoding header\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=qp_eicar_1\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar1\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\n"
            b"TEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Lack Content-Transfer-Encoding header."
    },
    "qp_eicar_no_encoding_2": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64 eicar test case without Content-Transfer-Encoding header\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=qp_eicar_2\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar2\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\n"
            b"TEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Lack Content-Transfer-Encoding header."
    },

    # duplication of headers
    "multiple_encoding_1": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64 eicar test case with multiple encoding\r\n"
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
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Multiple CTE header."
    },
    "multiple_encoding_2": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64 eicar test case with multiple encoding\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=b64_eicar_2\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar2\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Multiple CTE header."
    },
    "multiple_encoding_3": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64 eicar test case with multiple encoding\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=b64_eicar_3\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar3\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Multiple CTE header. Use text/plain header."
    },
    "multiple_encoding_4": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64 eicar test case with multiple encoding\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=b64_eicar_4\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar4\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Multiple CTE header. Use text/plain header."
    },
    "multiple_encoding_5": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64 eicar test case with multiple encoding\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=qp_eicar_5\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar5\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\n"
            b"TEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Multiple CTE header."
    },
    "multiple_encoding_6": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64 eicar test case with multiple encoding\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=me_qp_eicar_6\r\n"
            b"Content-Disposition: attachment; filename=me_qp_eicar6\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\n"
            b"TEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Multiple CTE header."
    },
    "multiple_encoding_7": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64 eicar test case with multiple encoding\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=eicar_7\r\n"
            b"Content-Disposition: attachment; filename=eicar7\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\n"
            b"TEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Multiple CTE header. Use text/plain header."
    },
    "multiple_encoding_8": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64 eicar test case with multiple encoding\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=eicar_8\r\n"
            b"Content-Disposition: attachment; filename=eicar8\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\n"
            b"TEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Multiple CTE header. Use text/plain header."
    },
    "multiple_encoding_9": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: normal attachment test case with multiple encoding\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=normal_9\r\n"
            b"Content-Disposition: attachment; filename=normal9\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"VHdmdzc4MzY0RldiMzAucmZlXWdhMWB6\r\n"
            b"--foo--\r\n"
        ,
        "description": b"A textual attachment with Base64 encoding. Multiple CTE header."
    },
    "multiple_encoding_10": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: normal attachment test case with multiple encoding\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=normal_10\r\n"
            b"Content-Disposition: attachment; filename=normal10\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"VHdmdzc4MzY0RldiMzAucmZlXWdhMWB6\r\n"
            b"--foo--\r\n"
        ,
        "description": b"A textual attachment with Base64 encoding. Multiple CTE header."
    },
    "multiple_encoding_11": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: normal attachment test case with multiple encoding\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=normal_11\r\n"
            b"Content-Disposition: attachment; filename=normal11\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"Twfw78364FWb30.rfe=5Dga1=60z\r\n"
            b"--foo--\r\n"
        ,
        "description": b"A textual attachment with Quoted-printable encoding. Multiple CTE header."
    },
    "multiple_encoding_12": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: normal attachment test case with multiple encoding\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=normal_12\r\n"
            b"Content-Disposition: attachment; filename=normal12\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"Twfw78364FWb30.rfe=5Dga1=60z\r\n"
            b"--foo--\r\n"
        ,
        "description": b"A textual attachment with Quoted-printable encoding. Multiple CTE header."
    },

    "multiple_type_1": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp eicar test case with multiple Content-Type\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=qp_eicar_1\r\n"
            b"Content-type: text/plain; name=qp_eicar_1\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar1\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\n"
            b"TEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Multiple Content-Type header."
    },
    "multiple_type_2": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp eicar test case with multiple Content-Type\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=qp_eicar_2\r\n"
            b"Content-type: application/octet-stream; name=qp_eicar_2\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar2\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\n"
            b"TEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Multiple Content-Type header."
    },

    # cases about the order of headers. no valid result found yet.
    "abnormal_header_order_1": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp eicar test case with abnormal order of headers\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"Content-Type: text/plain; name=qp_eicar_1\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar1\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\nTEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Abnormal order of headers."
    },
    "abnormal_header_order_2": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp eicar test case with abnormal order of headers\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar2\r\n"
            b"Content-Type: text/plain; name=qp_eicar_2\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\nTEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Abnormal order of headers."
    },
    "abnormal_header_order_3": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp eicar test case with abnormal order of headers\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar3\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"Content-Type: text/plain; name=qp_eicar_3\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\nTEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Abnormal order of headers."
    },
    "abnormal_header_order_4": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp eicar test case with abnormal order of headers\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar4\r\n"
            b"Content-Type: text/plain; name=qp_eicar_4\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\nTEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Abnormal order of headers."
    },

    # Content-Type related
    "unmatched_type_1": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64 eicar test case with unmatched C-type\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: ; name=b64_eicar_1\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar1\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Further research on C-type header."
    },
    "unmatched_type_2": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64 eicar test case with unmatched C-type\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: image/jpeg; name=b64_eicar_2\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar2\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Further research on C-type header."
    },
    "unmatched_type_3": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64 eicar test case with unmatched C-type\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application; name=b64_eicar_3\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar3\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Further research on C-type header."
    },
    "unmatched_type_4": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64 eicar test case with unmatched C-type\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: myctype/mysubtype; name=b64_eicar_4\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar4\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Further research on C-type header."
    },
    "unmatched_type_5": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64 eicar test case with unmatched C-type\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: image/jpeg; name=b64_eicar_5.com\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar5.com\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Further research on C-type header."
    },

    # Content-Length related
    "C-length_test_1": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: meaningless .com file as attachment with C-length header\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=b64_eicar_1\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar1\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"Content-Length: 10\r\n"
            b"\r\n"
            b"VHdmdzc4MzY0RldiMzAucmZlXWdhMWB6\r\n"
            b"--foo--\r\n"
        ,
        "description": b"A meaningless Base 64 string as attachment. Test the effect of C-length header."
    },
    "C-length_test_2": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: meaningless .com file as attachment with C-length header\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"Content-Length: 10\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=b64_eicar_2\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar2\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"VHdmdzc4MzY0RldiMzAucmZlXWdhMWB6\r\n"
            b"--foo--\r\n"
        ,
        "description": b"A meaningless Base 64 string as attachment. Test the effect of C-length header."
    },
    "C-length_test_3": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64 eicar test case with C-length header\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=b64_eicar_3\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar3\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"Content-Length: 10\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Test the effect of C-length header."
    },
    "C-length_test_4": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64 eicar test case with C-length header\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"Content-Length: 10\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=b64_eicar_4\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar4\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Test the effect of C-length header."
    },

    "C-type_abnormal_case_1": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64 eicar test case with abnormal C-type\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"coNTeNt-tYPe: application/octet-stream; name=b64_eicar_1.com\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar1.com\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Abnormal case in Content-type header."
    },
    "C-type_abnormal_case_2": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64 eicar test case with abnormal C-type\r\n"
            b"coNTeNt-tYPe: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=b64_eicar_2.com\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar2.com\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Abnormal case in Content-type header."
    },

    # Content-Transfer-Encoding related
    "C-encoding_abnormal_case": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64 eicar test case with abnormal C-encoding\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=b64_eicar_3.com\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar3.com\r\n"
            b"CoNtent-TrAnsFer-ENcodIng: base64\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Abnormal case in Content-Transfer-Encoding header."
    },
    "space_before_colon": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp eicar test case with extra space before colon in CTE header\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=qp_eicar_1\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar1\r\n"
            b"Content-Transfer-Encoding : quoted-printable\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\nTEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Add extra space in CTE header before colon."
    },
    "0_before_colon": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp eicar test case with extra \\0 before colon in CTE header\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=qp_eicar_2\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar2\r\n"
            b"Content-Transfer-Encoding\0: quoted-printable\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\nTEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Add \\0 in CTE header before colon."
    },
    "space_before_CTE": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp eicar test case with extra space before CTE header\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=qp_eicar_3\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar3\r\n"
            b" Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\nTEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Add extra space before CTE header."
    },
    "0_before_CTE": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp eicar test case with extra \\0 before CTE header\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=qp_eicar_4\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar4\r\n"
            b"\0Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\nTEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Add extra \\0 before CTE header."
    },

    "CTE_value_abnormal_case": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp eicar test case with abnormal encoding of CTE value\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=qp_eicar_1\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar1\r\n"
            b"Content-Transfer-Encoding: quoTeD-pRIntAblE\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\nTEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Abnormal case in CTE value."
    },
    "CTE_value_with_0_1": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp eicar test case with \\0 after CTE value\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=qp_eicar_1\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar1\r\n"
            b"Content-Transfer-Encoding: quoted-printable\0\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\nTEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Add extra \\0 after CTE value."
    },
    "CTE_value_with_0_2": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp eicar test case with \\0 in CTE value\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=qp_eicar_2\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar2\r\n"
            b"Content-Transfer-Encoding: quoted-\0printable\0\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\nTEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Add extra \\0 within CTE value."
    },

    # separation between headers
    "abnormal_line_break_between_headers_1": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp eicar test case with abnormal line break between headers\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=qp_eicar_1\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar1\r"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\nTEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Abnormal line break between headers."
    },
    "abnormal_line_break_between_headers_1_": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp eicar test case with abnormal line break between headers\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=qp_eicar_8\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar8\r"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\nTEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Abnormal line break between headers."
    },
    "abnormal_line_break_between_headers_2": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp eicar test case with abnormal line break between headers\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=qp_eicar_2\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar2\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\n"
            b"TEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Abnormal line break between headers."
    },
    "abnormal_line_break_between_headers_2_": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp eicar test case with abnormal line break between headers\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=qp_eicar_9\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar9\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\nTEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Abnormal line break between headers."
    },
    "abnormal_line_break_between_headers_3": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp eicar test case with abnormal line break between headers\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=qp_eicar_3\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar3\n\r"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\nTEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Abnormal line break between headers."
    },
    "abnormal_line_break_between_headers_3_": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp eicar test case with abnormal line break between headers\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=qp_eicar_10\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar10\n\r"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\nTEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Abnormal line break between headers."
    },
    "abnormal_line_break_between_headers_4": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp eicar test case with abnormal line break between headers\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=qp_eicar_4\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar4\r\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\nTEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Abnormal line break between headers."
    },
    "abnormal_line_break_between_headers_4_": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp eicar test case with abnormal line break between headers\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=qp_eicar_11\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar11\r\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\nTEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Abnormal line break between headers."
    },
    "abnormal_line_break_between_headers_5": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp eicar test case with abnormal line break between headers\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=qp_eicar_5\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar5\r\n\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\nTEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Abnormal line break between headers."
    },
    "abnormal_line_break_between_headers_5_": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp eicar test case with abnormal line break between headers\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=qp_eicar_12\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar12\r\n\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\nTEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Abnormal line break between headers."
    },
    "abnormal_line_break_between_headers_6": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp eicar test case with abnormal line break between headers\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=qp_eicar_6\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar6\r\n\r"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\nTEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Abnormal line break between headers."
    },
    "abnormal_line_break_between_headers_6_": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp eicar test case with abnormal line break between headers\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=qp_eicar_13\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar13\r\n\r"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\nTEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Abnormal line break between headers."
    },
    "abnormal_line_break_between_headers_7": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp eicar test case with abnormal line break between headers\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=qp_eicar_7\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar7\n\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\nTEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Abnormal line break between headers."
    },
    "abnormal_line_break_between_headers_7_": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp eicar test case with abnormal line break between headers\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=qp_eicar_14\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar14\n\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\nTEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Abnormal line break between headers."
    },
}