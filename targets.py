helo_content = {
    "vps3": b"vps3.hostoftroubles.com",
    "qq": b"qq.com",
    "vivo": b"vivo.com.cn",
    "yximgs": b"yximgs.com",
    "huawei": b"huawei.com",
    "nflxso": b"nflxso.net",
    "salesforce": b"salesforce.com",
    "meeting": b"meeting.tencent.com",
    "dbg": b"@debug_sender_acl",
}

sender = {
    "vps3": b"<echo@vps3.hostoftroubles.com>",
    "qq": b"<110110110@qq.com>",
    "vivo": b"<110110110@vivo.com.cn>",
    "yximgs": b"<110110110@yximgs.com>",
    "huawei": b"<110110110@huawei.com>",
    "nflxso": b"<110110110@nflxso.net>",
    "salesforce": b"<110110110@salesforce.com>",
    "meeting": b"<110110110@meeting.tencent.com>",
    "dbg": b"echo@debug_sender_acl",
}

target_mailbox = {
    "whu_email": {
        "mx": "mx-whu-edu-cn.icoremail.net",
        "receiver": b"<cse2019echo@whu.edu.cn>",
    },
    "thu_email": {
        "mx": "mta0.tsinghua.edu.cn",
        "receiver": b"<zhangjia23@mails.tsinghua.edu.cn>"
    },
    "gmail": {
        "mx": "gmail-smtp-in.l.google.com",
        "receiver": b"<echozhang258@gmail.com>",
    },
    "icloud": {
        "mx": "mx01.mail.icloud.com",
        "receiver": b"<echozhang258@icloud.com>",
    },
    "mail_ru": {
        "mx": "mxs.mail.ru",
    "receiver": b"<echozhang258@mail.ru>",
    },
    "outlook": {
        "mx": "outlook-com.olc.protection.outlook.com",
        "receiver": b"<echozhang258@outlook.com>",
    },
    "mail_com": {
        "mx": "mx00.mail.com",
        "receiver": b"<echozhang256@mail.com>",
    },
    "gmx": {
        "mx": "mx00.gmx.net",
        "receiver": b"<echozhang256@gmx.com>",
    },
    "protonmail": {
        "mx": "mail.protonmail.ch",
        "receiver": b"<echozhang258@protonmail.com>",
    },
    "netease_mail": {
        "mx": "163mx01.mxmail.netease.com",
        "receiver": b"<maxwellkang@163.com>",
    },
    "qq_mail": {
        "mx": "mx2.qq.com",
        "receiver": b"<1379664023@qq.com>",
    },
    "sina_mail": {
        "mx": "freemx1.sinamail.sina.com.cn",
        "receiver": b"<echozhang258@sina.com>",
    },
    "zoho": {
        "mx": "smtpin.zoho.com",
        "receiver": b"<echozhang258@zohomail.com>"
    },
    "zoho_cn": {
        "mx": "mx.zoho.com.cn",
        "receiver": b"<pengaw666666@zohomail.cn>"
    },
    "sohu": {
        "mx": "sohumx.h.a.sohu.com",
        "receiver": b"<pengaw666666@sohu.com>"
    },
    "sapo": {
        "mx": "mx.ptmail.sapo.pt",
        "receiver": b"<pengaw666666@sapo.pt>"
    },
    "inbox_lv": {
        "mx": "mx1.inbox.lv",
        "receiver": b"<pengaw666666@inbox.lv>"
    },
    "fastmail": {
        "mx": "in1-smtp.messagingengine.com",
        # "receiver": b"<echozhang@fastmail.com>",
        "receiver": b"<echozhang_00@fastmail.com>",
        "paid": "True"
    },
    "gmail_inbox": {},
    "yeah_net": {},
    "yahoo_com": {},
    "aol_com": {},
    "hotmail_com": {},
    "runbox_com": {},
    "hushmail": {},
    "yandex_mail": {},
    "mailjet": {},
    "rediffmail_com": {},
    "seznam_cz": {},
    "lycos": {},
    "juno_com": {},
    "titan": {},
    "hubspot": {},
    "mailfence": {},
    "disroot": {},
    "rackspace": {},

    "op_pl": {},
    "mynet_com": {},
    "daum_net": {},
    "interia_pl": {},
    "o2_pl": {},
    "wp_pl": {},
    "t-online_de": {},
    "excite_com": {},
    "freemail_hu": {},

    "hey_com": {},
    "lockbin": {},
    "net-c": {},
    "openmailbox": {},
    "arvixe": {},
    "safemail_net": {},
    "thunderbird": {},
    "1&1": {},
    "fasthosts": {},
    "amazon_workmail": {},
    "hostinger": {},
    "hostpapa": {},
    "bluehost": {},
    "a2hosting": {},
    "mail2world": {},
    "trustify": {},
    "countermail": {},
    "everymail": {},
    "kolabnow": {},
    "msgsafe_io": {},
    "mailbox_org": {},
    "posteo": {},
    "scryptmail": {},

    # one-time service
    "10minute_mail_com": {},
    "trashmail": {},

    # "126.com": {},
    "zhangjh": {
        # "mx": "mail.zhangjh.xyz",
        "mx": "mx-01-us-west-2.prod.hydra.sophos.com",
        # "mx": "cloud15.spamtitan.com",
        # "mx": "ec2-54-86-71-228.compute-1.amazonaws.com",
        "receiver": b"<jiahe@zhangjh.xyz>"
    },
    "nisl_lol": {
        "mx": "mail.nisl.lol",
        "receiver": b"<jiahe@nisl.lol>"
    },
    "DC_test_target": {
        "mx": "120.24.255.190",
        "receiver": b"<security44@mail10.nospoofing.cn>"
    },
    "sectest": {
        "mx": "120.24.255.190",
        "receiver": b"<test@mail10.nospoofing.cn>"
    },
}

c_type_choices = {
    "null": b"",
    "text_plain": b"text/plain",
    "text_html": b"text/html",
    "app_oct_stream": b"application/octet-stream",
    "multi_mix": b"multipart/mixed"
}

target_list = [
    "whu_email",
    "gmail",
    "icloud_mail",
    "mail_ru",
    "outlook",
    "mail_com",
    "gmx",
    "protonmail",
    "netease_mail",
    "qq_mail",
    "sina_mail",
]
