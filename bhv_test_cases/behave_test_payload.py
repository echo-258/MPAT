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
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=b64_eicar_4\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar4\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n"
            b"1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Use app/octet type header."
    },
    "b64_eicar_noCTE": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64_eicar_noCTE\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=b64_eicar_4\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar4\r\n"
            b"\r\n"
            b"WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy\r\n"
            b"1URVNULUZJTEUhJEgrSCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Use app/octet type header."
    },
    "basic_qp_eicar": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: basic_qp_eicar\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain; name=qp_eicar_4\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar4\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"=58=35=4F=21=50=25=40=41=50=5B=34=5C=50=5A=58=35=34=28=50=5E=29=37=43=43=29=\r\n"
            b"=37=7D=24=45=49=43=41=52=2D=53=54=41=4E=44=41=52=44=2D=41=4E=54=49=56=49=52=\r\n"
            b"=55=53=2D=54=45=53=54=2D=46=49=4C=45=21=24=48=2B=48=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Use text/plain type header."
    },
    "basic_qp_eicar_no_CTE": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: basic_qp_eicar\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain; name=qp_eicar_4\r\n"
            b"Content-Disposition: attachment; filename=qp_eicar4\r\n"
            b"\r\n"
            b"=58=35=4F=21=50=25=40=41=50=5B=34=5C=50=5A=58=35=34=28=50=5E=29=37=43=43=29=\r\n"
            b"=37=7D=24=45=49=43=41=52=2D=53=54=41=4E=44=41=52=44=2D=41=4E=54=49=56=49=52=\r\n"
            b"=55=53=2D=54=45=53=54=2D=46=49=4C=45=21=24=48=2B=48=2A\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Quoted-printable. Use text/plain type header."
    },
}
