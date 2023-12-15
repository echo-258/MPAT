import os
import re
import time
import json
# import simplejson as json
import argparse

import config
import targets
import utils
# import test_cases.demo as cases
import bhv_test_cases.behave_test as cases
import bhv_test_cases.specific_payload as payload_cases
from mail_sender import MailSender


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-port', '--port', default=None, help="Set mail server port manually. Effective in manual mode only.")

    parser.add_argument('-s', '--sender', default="vps3")
    parser.add_argument('-r', '--receiver', required=True, nargs='*')

    parser.add_argument('-m', '--msg_source', choices=["py", "eml", "payload"], default="py")
    parser.add_argument('-c', '--cases', default=["normal_msg"], nargs='*')
    parser.add_argument('-p', '--payload', default=[], nargs='*')
    parser.add_argument('-j', '--subject', default=None)
    parser.add_argument('-e', '--encoding', type=json.loads, default={}, help='Example: "{"<valid_CTE_here>": "quoted-printable", "<invalid_CTE_here>": "base64"}"')

    parser.add_argument('-d', '--display_data', type=int, default=-1)
    parser.add_argument('-l', '--log', default=False, action='store_true', help="Enable logging")

    args = parser.parse_args()
    return args


def execute_sending(sender_token, target_token, msg_main_content):
    mail_server = targets.target_mailbox[target_token]["mx"]
    mail_server_port = config.mail_server_port
    smtp_header_hl = targets.helo_content[sender_token]
    smtp_header_mf = targets.sender[sender_token]
    smtp_header_rt = targets.target_mailbox[target_token]["receiver"]
    # starttls = args.starttls if args.starttls else config['server_mode']['starttls']

    # exploits_builder = ExploitsBuilder(testcases.test_cases, config)
    # smtp_seqs = exploits_builder.generate_smtp_seqs()

    from_header = b"From: " + smtp_header_mf + b"\r\n"
    to_header = b"To: " + smtp_header_rt + b"\r\n"
    date_header = b"Date: " + utils.get_date() + b"\r\n"
    msg_content = from_header + to_header + date_header + msg_main_content

    # msg_with_payload = utils.insert_payload(msg_content, specified_payload)
    mail_sender = MailSender()
    mail_sender.set_param((mail_server, mail_server_port), helo=smtp_header_hl, mail_from=smtp_header_mf,
                          rcpt_to=smtp_header_rt, email_data=msg_content)
    err_msg, unfinished = mail_sender.send_email()
    if unfinished:
        # execute sending once and only once
        utils.print_warning("sending unfinished, will retry after 2 minutes...\n")
        time.sleep(120)
        mail_sender.unfinished_flag = False     # reset unfinished flag
        err_msg, unfinished = mail_sender.send_email()
    if config.log_flag:
        subject = re.findall(b"Subject: (.*)\r\n", msg_content)[0]  # get subject from main_content
        with open(config.log_path, "a") as fp:
            fp.write(time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime()))
            fp.write("[" + smtp_header_mf.decode("utf-8") + " -> " + smtp_header_rt.decode("utf-8") + " " + subject.decode("utf-8") + "] ")
            if unfinished:
                fp.write("TIMEOUT\n")
            elif err_msg == "":
                fp.write("success\n")
            else:
                fp.write(err_msg + "\n")
    time.sleep(0.5)


def main():
    args = parse_args()

    if config.args_mode:
        sender_token = args.sender
        target_list = args.receiver
        msg_source = args.msg_source
        case_id_list = args.cases
        specified_payload = args.payload
        specified_subject = args.subject
        specified_encoding = args.encoding
        config.disp_lim = args.display_data
        config.log_flag = args.log
    else:
        sender_token = "vps3"
        target_list = ["icloud"]
        msg_source = "payload"      # to test specific payloads, set this to "payload"
        # case_id_list = list(cases.test_cases.keys())[2:]
        # case_id_list = utils.get_cases_span(list(cases.test_cases.keys()), "bound_begin_blank_char_quo_sta_app", "ecdw_CTE_part_qp")
        case_id_list = ["generic_structure"]
        # specified_payload = ["eicar_eicar"]
        specified_payload = payload_cases.specific_payload["b64_related"]["wncr"]  # test a batch of specific payloads
        specified_subject = None
        # example: specified_encoding = {"<valid_CTE_here>": "quoted-printable", "<invalid_CTE_here>": "base64"}
        specified_encoding = {"<valid_CTE_here>": "base64", "<invalid_CTE_here>": "quoted-printable"}
        config.disp_lim = 20       # recommend: 20 for long payload. See config.py for more details
        config.log_flag = False

    if config.log_flag and config.log_name == "":
        config.log_path = os.path.join(config.log_dir, "sender_log_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".log")
    start_time = time.time()

    print("Start sending emails...")

    # first traverse all cases; then, for each case, test each target
    if msg_source == "py":
        for case in case_id_list:
            if "data" not in cases.test_cases[case].keys():
                continue
            print("\033[94mtesting case: %s ...\n\033[0m" % case)
            msg_main_content = cases.test_cases[case]["data"]
            msg_main_content = utils.construct_msg_content(case, msg_main_content, specified_payload, encoding=specified_encoding)
            # msg_main_content_with_payload = utils.insert_payload(msg_main_content, specified_payload)
            for target in target_list:
                print("\033[94mtesting target mailbox: %s ...\n\033[0m" % target)
                execute_sending(sender_token, target, msg_main_content)
            time.sleep(config.interval)
    elif msg_source == "payload":
        for pld in specified_payload:
            print("\033[94mtesting payload: %s ...\n\033[0m" % pld)
            msg_main_content = cases.test_cases["generic_structure"]["data"]
            msg_main_content = utils.construct_msg_content(pld, msg_main_content, [pld], pld, specified_encoding)
            for target in target_list:
                print("\033[94mtesting target mailbox: %s ...\n\033[0m" % target)
                execute_sending(sender_token, target, msg_main_content)
            time.sleep(config.interval)
    elif msg_source == "eml":   # currently not well-developed
        eml_path = ""
        msg_main_content = utils.get_main_content(eml_path)
        msg_main_content = utils.construct_msg_content("att_name", msg_main_content, specified_payload)
        # msg_main_content_with_payload = utils.insert_payload(msg_main_content, specified_payload)
        for target in target_list:
            print("\033[94mtesting target mailbox: %s ...\n\033[0m" % target)
            execute_sending(sender_token, target, msg_main_content)

    end_time = time.time()
    print("Finished.", end_time - start_time, "s")
    if config.log_flag:
        with open(config.log_path, "a") as fp:
            fp.write("\nTime cost: " + str(end_time - start_time) + " s\n")


if __name__ == '__main__':
    main()
