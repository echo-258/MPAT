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


    "b64_6char_per_line": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64_6char_per_line\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=b64_att_6char_per_line\r\n"
            b"Content-Disposition: attachment; filename=b64_att6char_per_line\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"WrIS53\r\n"
            b"c9UC/D\r\n"
            b"SCpYJP\r\n"
            b"Q0P4WT\r\n"
            b"MPrK+W\r\n"
            b"AacWt5\r\n"
            b"K1CCNo\r\n"
            b"8=\r\n"
            b"--foo--\r\n"
        ,
        "description": b""
    },

    "b64_junk_char_dot": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64_junk_char_dot\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=b64_att_1\r\n"
            b"Content-Disposition: attachment; filename=b64_att1\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"W.D.V.P.I.V.A.l.Q.E.F.Q.W.z.R.c.U.F.p.Y.N.T.Q.o.U.F.4.p.N.0.N.D.K.T.d.\r\n"
            b"9.J.E.V.J.Q.0.F.S.L.V.N.U.Q.U.5.E.Q.V.J.E.L.U.F.O.V.E.l.W.S.V.J.V.U.y.\r\n"
            b"1.U.R.V.N.U.L.U.Z.J.T.E.U.h.J.E.g.r.S.C.o.=.\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw sample with Base 64. Add junk chars in data."
    },
    "N_b64_junk_char_dot": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64_junk_char_dot_normal\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=b64_att_1\r\n"
            b"Content-Disposition: attachment; filename=b64_att1\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"<b64_junk_char wncr1 here>"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw sample with Base 64. Add junk chars in data."
    },
    "b64_4char_eq": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64_4char_eq\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=b64_att_4char_eq\r\n"
            b"Content-Disposition: attachment; filename=b64_att4char_eq\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"WDVP=IVAl=QEFQ=WzRc=UFpY=NTQo=UF4p=N0ND=KTd9=JEVJ=Q0FS=LVNU=QU5E=QVJE=LUFO=VElW=SVJV=\r\n"
            b"Uy1U=RVNU=LUZJ=TEUh=JEgr=SCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "b64_MZ": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64_MZ\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=b64_att\r\n"
            b"Content-Disposition: attachment; filename=b64_att\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"TVqQ=\r\n"
            b"--foo--\r\n"
        ,
        "description": b""
    },
    "b64_4char_eq_wncr": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64_4char_eq_wncr\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-Type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-Type: application/octet-stream; name=b64_att_4char_eq\r\n"
            b"Content-Disposition: attachment; filename=b64_att4char_eq\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"TVqQ=AAMA=AAAE=AAAA=//8A=ALgA=AAAA=AAAA=QAAA=AAAA=AAAA=AAAA=AAAA=AAAA=AAAA=AAAA=AAAA=AAAA=AAAA=\r\n"
            b"--foo--\r\n"
        ,
        "description": b""
    },

}
