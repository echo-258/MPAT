test_cases = {
    # untested cases
    "att_with_ctl_char_1": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp eicar test case with control character\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=qp_att_1\r\n"
            b"Content-Disposition: attachment; filename=qp_att1\r\n"
            b"\r\n"
            b"abcd\x01\x02\x03\x04efgh\x11\x12\x13\x14\x21ijkl\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Add control chars (0x01 ~ 0x19, not printable) in content."
    },
    "att_with_ctl_char_2": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp eicar test case with control character\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=qp_att_2\r\n"
            b"Content-Disposition: attachment; filename=qp_att2\r\n"
            b"\r\n"
            b"abcd\x01\x02\x03\x04efgh\x11\x12\x13\x14\x00ijkl\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Add control chars (0x00 ~ 0x19, not printable) in content."
    },
    "att_with_non_ascii": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: qp eicar test case with non-ascii character\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain; name=qp_att_3\r\n"
            b"Content-Disposition: attachment; filename=qp_att3\r\n"
            b"\r\n"
            b"abcd\xe1\xe2\xe3\xe4efgh\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Add non-ascii chars (0x80 ~ 0xff, with 1 as the highest bit) in content."
    },
}