test_cases = {
    # Base 64 related
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
            b"Content-type: application/octet-stream; name=b64_eicar_1\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar1\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"V.H.d.m.d.z.c.4.M.z.Y.0.R.l.d.i.M.z.A.u.c.m.Z.l.X.W.d.h.M.W.B.6.\r\n"
            b"--foo--\r\n"
        ,
        "description": b"A meaningless Base 64 string as attachment. Add junk chars in data."
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
            b"Content-type: application/octet-stream; name=b64_eicar_2\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar2\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"W.D.V.P.I.V.A.l.Q.E.F.Q.W.z.R.c.U.F.p.Y.N.T.Q.o.U.F.4.p.N.0.N.D.K.T.d.\r\n"
            b"9.J.E.V.J.Q.0.F.S.L.V.N.U.Q.U.5.E.Q.V.J.E.L.U.F.O.V.E.l.W.S.V.J.V.U.y.\r\n"
            b"1.U.R.V.N.U.L.U.Z.J.T.E.U.h.J.E.g.r.S.C.o.=.\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Add junk chars in data."
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
            b"Content-type: text/plain; name=b64_eicar_3\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar3\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"W.D.V.P.I.V.A.l.Q.E.F.Q.W.z.R.c.U.F.p.Y.N.T.Q.o.U.F.4.p.N.0.N.D.K.T.d.\r\n"
            b"9.J.E.V.J.Q.0.F.S.L.V.N.U.Q.U.5.E.Q.V.J.E.L.U.F.O.V.E.l.W.S.V.J.V.U.y.\r\n"
            b"1.U.R.V.N.U.L.U.Z.J.T.E.U.h.J.E.g.r.S.C.o.=.\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Add junk chars in data. Use text/plain header."
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
            b"Content-type: application/octet-stream; name=b64_eicar_1\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar1\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"VHc=Znc=Nzg=MzY=NEY=V2I=MzA=LnI=ZmU=XWc=YTE=YHo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"A meaningless Base 64 string as attachment. Employ split encoding."
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
            b"Content-type: application/octet-stream; name=b64_eicar_2\r\n"
            b"Content-Disposition: attachment; filename=b64_eicar2\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"WDU=TyE=UCU=QEE=UFs=NFw=UFo=WDU=NCg=UF4=KTc=Q0M=KTc=fSQ=RUk=Q0E=Ui0=\r\n"
            b"U1Q=QU4=REE=UkQ=LUE=TlQ=SVY=SVI=VVM=LVQ=RVM=VC0=Rkk=TEU=ISQ=SCs=SCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Employ split encoding."
    },
    "b64_split_encoding_3": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: b64_split_encoding_3\r\n"
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
            b"\r\n"
            b"WDU=TyE=UCU=QEE=UFs=NFw=UFo=WDU=NCg=UF4=KTc=Q0M=KTc=fSQ=RUk=Q0E=Ui0=\r\n"
            b"U1Q=QU4=REE=UkQ=LUE=TlQ=SVY=SVI=VVM=LVQ=RVM=VC0=Rkk=TEU=ISQ=SCs=SCo=\r\n"
            b"--foo--\r\n"
        ,
        "description": b"Encode raw eicar.com with Base 64. Employ split encoding."
    },
}