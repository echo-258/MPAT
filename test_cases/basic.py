test_cases = {
    # basic test cases
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
    "normal_att_1": {
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
            b"Content-type: text/plain; name=a.txt\r\n"
            b"Content-Disposition: attachment; filename=b.txt\r\n"
            b"\r\n"
            b"Content of a text attachment.\r\nJust for testing sending function.\r\n"
            b"--foo--\r\n"
        ,
        "description": b"A textual attachment. Add Content-Disposition header."
    },
    "normal_att_2": {
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
            b"Content-type: text/plain; name=a.txt\r\n"
            b"\r\n"
            b"Content of a text attachment.\r\nJust for testing sending function.\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Add a textual attachment with simple content. No Content-Disposition header"
    },
    "normal_att_3": {
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
            b"Content-type: text/plain; name=a.txt\r\n"
            b"Content-Disposition: attachment; filename=b.txt\r\n"
            b"\r\n"
            b"Content of a text attachment.\r\nJust for testing sending function."
            b"--foo--\r\n"
        ,
        "description": b"A textual attachment. Lack CRLF after attachment part."
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
            b"Content-type: text/plain; name=a.txt\r\n"
            b"Content-Disposition: attachment; filename=b.txt\r\n"
            b"Content of a text attachment.\r\nJust for testing sending function.\r\n"
            b"--foo--\r\n"
        ,
        "description": b"A textual attachment. Lack blank line within attachment part."
    },
    "null_com_test_1": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: meaningless .com file as attachment\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=b64_eicar_1.com\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar1.com\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"VHdmdzc4MzY0RldiMzAucmZlXWdhMWB6\r\n"
            b"--foo--\r\n"
        ,
        "description": b"A meaningless Base 64 string as attachment. Just to test permission for .com file.",
        "origin_string": "Twfw78364FWb30.rfe]ga1`z"
    },
    "null_com_test_2": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: meaningless .com file as attachment\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=b64_eicar_2\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar2\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"VHdmdzc4MzY0RldiMzAucmZlXWdhMWB6\r\n"
            b"--foo--\r\n"
        ,
        "description": b"A meaningless Base 64 string as attachment. Just to test permission for .com file. No extension."
    },
    "null_com_test_3": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: meaningless .com file as attachment\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=b64_eicar_3.com\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar3.com\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"VHdmdzc4MzY0RldiMzAucmZlXWdhMWB6\r\n"
            b"--foo--\r\n"
        ,
        "description": b"A meaningless Base 64 string as attachment. Use text/plain header."
    },
    "null_com_test_4": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: meaningless .com file as attachment\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
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
            b"VHdmdzc4MzY0RldiMzAucmZlXWdhMWB6\r\n"
            b"--foo--\r\n"
        ,
        "description": b"A meaningless Base 64 string as attachment. Use text/plain header. No extension."
    },
    "null_com_test_5": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: meaningless .com file as attachment\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
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
            b"Twfw78364FWb30.rfe=5Dga1=60z\r\n"
            b"--foo--\r\n"
        ,
        "description": b"A meaningless quoted-printable string as attachment. Use text/plain header. No extension."
    },

    # cases about simple EICAR
    "raw_eicar_1": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: raw eicar test case\r\n"
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
        "description": b"Raw eicar.com as attachment. Without other encoding. Use app/octet type header."
    },
    "raw_eicar_2": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: raw eicar test case\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/octet-stream; name=eicar_2\r\n"
            b"Content-Disposition: attachment; filename=eicar2\r\n"
            b"\r\n"
            b"X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Raw eicar.com as attachment. Without other encoding. Use app/octet type header."
    },
    "raw_eicar_3": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: raw eicar test case\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=eicar_3.com\r\n"
            b"Content-Disposition: attachment; filename=eicar3.com\r\n"
            b"\r\n"
            b"X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Raw eicar.com as attachment. Without other encoding. Use text/plain type header."
    },
    "raw_eicar_4": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: raw eicar test case\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=eicar_4\r\n"
            b"Content-Disposition: attachment; filename=eicar4\r\n"
            b"\r\n"
            b"X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Raw eicar.com as attachment. Without other encoding. Use text/plain type header."
    },
    "b64_eicar_1": {
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
            b"Content-type: application/octet-stream; name=b64_eicar_1.com\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar1.com\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Use app/octet type header."
    },
    "b64_eicar_2": {
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
            b"Content-type: application/octet-stream; name=b64_eicar_2.txt\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar2.txt\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Use app/octet type header. Use .txt filename."
    },
    "b64_eicar_3": {
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
            b"Content-type: text/plain; name=b64_eicar_3.com\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar3.com\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Use app/octet type header. Use .txt filename."
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
            b"Content-type: text/plain; name=b64_eicar_4\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar4\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Use app/octet type header. Use .txt filename."
    },
    "qp_eicar_2": {
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
            b"Content-type: application/octet-stream; name=qp_eicar_2\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar2\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\n"
            b"TEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Use app/octet type header."
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
            b"X5O=21P=25=40AP=5B4=5CPZX54=28P=5E=297CC=297=7D=24EICAR-STANDARD-ANTIVIRUS-=\r\nTEST-FILE=21=24H=2BH=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Use text/plain type header."
    },
    "eicar_zip_1": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: zipped eicar test case\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/zip; name=eicar_zip_1.zip\r\n"
            b"Content-Disposition: attachment; filename=eicar_zip1.zip\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"UEsDBAoAAAAAAOCYuCg8z1FoRAAAAEQAAAAJAAAAZWljYXIuY29tWDVPIVAlQEFQWzRcUF\r\npYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy1URVNULUZJTEUhJEgr\r\n"
            b"SCpQSwECFAAKAAAAAADgmLgoPM9RaEQAAABEAAAACQAAAAAAAAABACAA/4EAAAAAZWljYX\r\nIuY29tUEsFBgAAAAABAAEANwAAAGsAAAAAAA==\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Use app/octet type header."
    },
    "eicar_zip_2": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: zipped eicar test case\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/zip; name=eicar_zip_2.txt\r\n"
            b"Content-Disposition: attachment; filename=eicar_zip2.txt\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"UEsDBAoAAAAAAOCYuCg8z1FoRAAAAEQAAAAJAAAAZWljYXIuY29tWDVPIVAlQEFQWzRcUF\r\npYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy1URVNULUZJTEUhJEgr\r\n"
            b"SCpQSwECFAAKAAAAAADgmLgoPM9RaEQAAABEAAAACQAAAAAAAAABACAA/4EAAAAAZWljYX\r\nIuY29tUEsFBgAAAAABAAEANwAAAGsAAAAAAA==\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Use app/octet type header."
    },
    "eicar_zip_3": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: zipped eicar test case\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=eicar_zip_3.zip\r\n"
            b"Content-Disposition: attachment; filename=eicar_zip3.zip\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"UEsDBAoAAAAAAOCYuCg8z1FoRAAAAEQAAAAJAAAAZWljYXIuY29tWDVPIVAlQEFQWzRcUF\r\npYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy1URVNULUZJTEUhJEgr\r\n"
            b"SCpQSwECFAAKAAAAAADgmLgoPM9RaEQAAABEAAAACQAAAAAAAAABACAA/4EAAAAAZWljYX\r\nIuY29tUEsFBgAAAAABAAEANwAAAGsAAAAAAA==\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Use app/octet type header."
    },
    "eicar_zip_4": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: zipped eicar test case\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=eicar_zip_4\r\n"
            b"Content-Disposition: attachment; filename=eicar_zip4\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"UEsDBAoAAAAAAOCYuCg8z1FoRAAAAEQAAAAJAAAAZWljYXIuY29tWDVPIVAlQEFQWzRcUF\r\npYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy1URVNULUZJTEUhJEgr\r\n"
            b"SCpQSwECFAAKAAAAAADgmLgoPM9RaEQAAABEAAAACQAAAAAAAAABACAA/4EAAAAAZWljYX\r\nIuY29tUEsFBgAAAAABAAEANwAAAGsAAAAAAA==\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Use app/octet type header."
    },
}