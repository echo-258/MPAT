test_cases = {
    "case_1": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: plain\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/zip; name=whatever.zip\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"\r\n"
            b"UEsDBBQAAgAIABFKjkk8z1FoRgAAAEQAAAAJAAAAZWljYXIuY29tizD1VwxQdXAMiDaJCYiKMDXR\r\nCIjTNHd21jSvVXH1dHYM0g0OcfRzcQxy0XX0C/EM8wwKDdYNcQ0O0XXz9HFVVPHQ9tACAFBLAQIU\r\nAxQAAgAIABFKjkk8z1FoRgAAAEQAAAAJAAAAAAAAAAAAAAC2gQAAAABlaWNhci5jb21QSwUGAAAA\r\nAAEAAQA3AAAAbQAAAAAA\r\n"
            b"--foo--\r\n"
        ,
    },
    "case_2": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: plain\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/zip; name=whatever.zip\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"UEsDBBQAAgAIABFKjkk8z1FoRgAAAEQAAAAJAAAAZWljYXIuY29tizD1VwxQdXAMiDaJCYiKMDXR\r\nCIjTNHd21jSvVXH1dHYM0g0OcfRzcQxy0XX0C/EM8wwKDdYNcQ0O0XXz9HFVVPHQ9tACAFBLAQIU\r\nAxQAAgAIABFKjkk8z1FoRgAAAEQAAAAJAAAAAAAAAAAAAAC2gQAAAABlaWNhci5jb21QSwUGAAAA\r\nAAEAAQA3AAAAbQAAAAAA\r\n"
            b"--foo--\r\n"
        ,
    },
    "case_3": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: plain\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/zip; name=whatever.zip\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"U.E.s.D.B.B.Q.A.A.g.A.I.A.B.F.K.j.k.k.8.z.1.F.o.R.g.A.A.A.E.Q.\r\nA.A.A.A.J.A.A.A.A.Z.W.l.j.Y.X.I.u.Y.2.9.t.i.z.D.1.V.w.x.Q.d.X.\r\nA.M.i.D.a.J.C.Y.i.K.M.D.X.R.C.I.j.T.N.H.d.2.1.\r\nj.S.v.V.X.H.1.d.H.Y.M.0.g.0.O.c.f\r\n.R.z.c.Q.x.y.0.X.X.0.C./.E.M.8.w.w.K.D.d.Y.N.c.Q.0.O.0.X.X.z.\r\n9.H.F.V.V.P.H.Q.9.t.A.C.A.F.B.L.A.Q.I.U.\r\nA.x.Q.A.A.g.A.I.A.B.F.K.j.k.k.8.z.1.F.o.R.g.A.A.A.E.Q.\r\nA.A.A.A.J.A.A.A.A.A.A.A.A.A.A.A.A.A.A.C.2.g.Q.A.A.A.A.B.l.a.\r\nW.N.h.c.i.5.j.b.2.1.Q.S.w.U.G.A.A.A.A.\r\nA.A.E.A.A.Q.A.3.A.A.A.A.b.Q.A.A.A.A.A.A.\r\n"
            b"--foo--\r\n"
        ,
    },
    "case_4": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: plain\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/zip; name=whatever.zip\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"UEs=AwQ=FAA=AgA=CAA=EUo=jkk=PM8=UWg=RgA=AAA=RAA=AAA=CQA=AAA=ZWk=Y2E=ci4=\r\nY28=bYs=MPU=Vww=UHU=cAw=iDY=iQk=iIo=MDU=0Qg=iNM=NHc=dtY=NK8=VXE=9XQ=dgw=\r\n0g0=DnE=9HM=cQw=ctE=dfQ=C/E=DPM=DAo=DdY=DXE=DQ4=0XU=8/Q=cVU=VPE=0PY=0AI=\r\nAFA=SwE=AhQ=AxQ=AAI=AAg=ABE=So4=STw=z1E=aEY=AAA=AEQ=AAA=AAk=AAA=AAA=AAA=\r\nAAA=AAA=ALY=gQA=AAA=AGU=aWM=YXI=LmM=b20=UEs=BQY=AAA=AAA=AQA=AQA=NwA=AAA=\r\nbQA=AAA=AAA="
            b"--foo--\r\n"
        ,
    },
    "case_5": {
        "data":
            b"MIME-Version: 1.0\r\n"
            b"Subject: plain\r\n"
            b"Content-Type: multipart/mixed; boundary=foo\r\n"
            b"\r\n"
            b"--foo\r\n"
            b"Content-type: text/plain\r\n"
            b"\r\n"
            b"Email with an attachment.\r\nThis is the main body text part.\r\n"
            b"--foo\r\n"
            b"Content-type: application/zip; name=whatever.zip\r\n"
            b"Content-Transfer-Encoding: base64\r\n"
            b"Content-Transfer-Encoding: quoted-printable\r\n"
            b"\r\n"
            b"UEs=.AwQ=.FAA=.AgA=.CAA=.EUo=.jkk=.PM8=.UWg=.RgA=.AAA=.RAA=.AAA=.CQA=.AAA=.\r\nZWk=.Y2E=.ci4=.Y28=.bYs=.MPU=.Vww=.UHU=.cAw=.iDY=.iQk=.iIo=.MDU=.0Qg=.iNM=.\r\nNHc=.dtY=.NK8=.VXE=.9XQ=.dgw=.0g0=.DnE=.9HM=.cQw=.ctE=.dfQ=.C/E=.DPM=.DAo=.\r\nDdY=.DXE=.DQ4=.0XU=.8/Q=.cVU=.VPE=.0PY=.0AI=.AFA=.SwE=.AhQ=.AxQ=.AAI=.AAg=.\r\nABE=.So4=.STw=.z1E=.aEY=.AAA=.AEQ=.AAA=.AAk=.AAA=.AAA=.AAA=.AAA=.AAA=.ALY=.\r\ngQA=.AAA=.AGU=.aWM=.YXI=.LmM=.b20=.UEs=.BQY=.AAA=.AAA=.AQA=.AQA=.NwA=.AAA=.\r\nbQA=.AAA=.AAA=."
            b"--foo--\r\n"
        ,
    },
}