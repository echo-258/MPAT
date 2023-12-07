import os
import re
import time
# import simplejson as json
import argparse

import targets
import utils
# import test_cases.demo as cases
import bhv_test_cases.behave_test as cases
import bhv_test_cases.specific_payload as payload_cases
import config
from mail_sender import MailSender

# from common.common import *
# test_cases = testcases.test_cases
# from exploits_builder import ExploitsBuilder


# def parser_error(errmsg):
#     banner()
#     print(("Usage: python " + sys.argv[0] + " [Options] use -h for help"))
#     print(("Error: " + errmsg))
#     sys.exit()


# def parse_args():
#     # parse the arguments
#     parser = argparse.ArgumentParser(
#         epilog='\tExample: \r\npython ' + sys.argv[0] + " -m s -id case_a1")
#     parser.error = parser_error
#     parser._optionals.title = "OPTIONS"
#     parser.add_argument(
#         '-m', '--mode', choices=['s', 'c', 'm'], default='s',
#         help="Select mode: 's' (default) means server mode; 'c' means clien mode; 'm' means manually setting fields;")
#     parser.add_argument(
#         '-l', '--list', action='store', default=-1, const=None, nargs='?',
#         help="List all test cases number and short description. `-l case_id' to see details of a specific case.")
#     parser.add_argument(
#         '-id', '--caseid', default=None,
#         help="Select a specific test case to send email. Effective in server and client mode.")
#     parser.add_argument(
#         '-tls', '--starttls', action='store_true', help="Enable STARTTLS command.")
#
#     parser.add_argument(
#         '-helo', '--helo', default=None, help="Set HELO domain manually. Effective in manual mode only.")
#     parser.add_argument(
#         '-mfrom', '--mfrom', default=None, help="Set MAIL FROM address manually. Effective in manual mode only.")
#     parser.add_argument(
#         '-rcptto', '--rcptto', default=None, help="Set RCPT TO address manually. Effective in manual mode only.")
#     parser.add_argument(
#         '-data', '--data', default=None, help="Set raw email in DATA command. Effective in manual mode only.")
#     parser.add_argument(
#         '-ip', '--ip', default=None, help="Set mail server ip manually. Effective in manual mode only.")
#     parser.add_argument(
#         '-port', '--port', default=None, help="Set mail server port manually. Effective in manual mode only.")
#
#     args = parser.parse_args()
#     return args

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-port', '--port', default=None, help="Set mail server port manually. Effective in manual mode only.")

    parser.add_argument('-s', '--sender', default="vps3")
    parser.add_argument('-r', '--receiver', required=True, nargs='*')

    parser.add_argument('-m', '--msg_source', choices=["py", "eml", "payload"], default="py")
    parser.add_argument('-c', '--cases', default=["normal_msg"], nargs='*')
    parser.add_argument('-p', '--payload', default=[], nargs='*')
    parser.add_argument('-j', '--subject', default=None)
    parser.add_argument('-e', '--encoding', default=[], nargs='*')

    parser.add_argument('-d', '--display_data', action='store_true', default=False)

    args = parser.parse_args()
    return args

# def check_configs():
#     if config["case_id"].decode("utf-8") not in test_cases:
#         print("Error: case_id not found in testcases!")
#         return -1
#
#     if config["mode"] == 'c' and "client" not in config["case_id"].decode("utf-8"):
#         print("Error: case_id should start with 'client_' in client mode!")
#         return -1
#     if config["mode"] == 's' and "server" not in config["case_id"].decode("utf-8"):
#         print("Error: case_id should start with 'server_' in server mode!")
#         return -1
#     return 0


# def list_test_cases(case_id):
#     if case_id == None:
#         case_ids = test_cases.keys()
#         print("%s     %s" % ("Case_id", "Description"))
#         print("-------------------------------------")
#         for id in case_ids:
#             print("%s  %s" % (id, test_cases[id].get("description").decode("utf-8")))
#
#         print("\r\nYou can use '-l case_id' options to list details of a specific case.")
#     else:
#         if case_id in test_cases:
#             print("Here is the details of " + case_id + ":")
#             print(json.dumps(test_cases[case_id], indent=4))
#         else:
#             print("Sorry, case_id not found in testcases.")

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
    err_msg = mail_sender.send_email()
    if config.log_flag:
        # get subject from main_content
        subject = re.findall(b"Subject: (.*)\r\n", msg_content)[0]
        with open(config.log_path, "a") as fp:
            # write time
            fp.write(time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime()))
            # write mf, rt, subject
            fp.write("[" + smtp_header_mf.decode("utf-8") + " -> " + smtp_header_rt.decode("utf-8") + " " + subject.decode("utf-8") + "] ")
            if err_msg == "":
                fp.write("success\n")
            else:
                fp.write(err_msg + "\n")
    time.sleep(0.5)


def main():
    args_mode = False
    args = parse_args()
    # config['mode'] = args.mode
    # if args.list != -1:
    #     list_test_cases(args.list)
    #     return 0
    # if args.caseid:
    #     config['case_id'] = args.caseid.encode("utf-8")
    # if check_configs() == -1:
    #     return -1

    print("Start sending emails...")

    sender_token = "vps3"

    if args_mode:
        msg_source = args.msg_source
        disp_flag = args.display_data
        target_list = args.receiver
        case_id_list = args.cases
        specified_payload = args.payload
        specified_subject = args.subject
        specified_encoding = args.encoding
    else:
        msg_source = "payload"
        disp_flag = True
        # target_list = ["gmail", "whu_email", "icloud", "mail_ru", "outlook", "mail_com", "protonmail", "netease_mail",
        #                "qq_mail", "sina_mail"]
        target_list = ["gmail"]
        case_id_list = ["normal_msg"]
        # specified_payload = ["b64_normal_data", "b64_eicar"]
        specified_payload = payload_cases.specific_payload["b64_related"]["eicar"]

        specified_subject = None
        specified_encoding = ["base64"]

    if disp_flag:
        config.disp_flag = True
    if config.log_flag:
        config.log_path = os.path.join(config.cur_path, "sender_log_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".log")

    # first traverse all cases; then, for each case, test each target
    if msg_source == "py":
        for case in case_id_list:
            if "data" not in cases.test_cases[case].keys():
                continue
            print("\033[94mtesting case: %s ...\n\033[0m" % case)
            msg_main_content = cases.test_cases[case]["data"]
            msg_main_content = utils.construct_msg_content(msg_main_content, specified_payload)
            # msg_main_content_with_payload = utils.insert_payload(msg_main_content, specified_payload)
            for target in target_list:
                print("\033[94mtesting target mailbox: %s ...\n\033[0m" % target)
                execute_sending(sender_token, target, msg_main_content)
            time.sleep(1.5)
    elif msg_source == "payload":
        for pld in specified_payload:
            print("\033[94mtesting payload: %s ...\n\033[0m" % pld)
            msg_main_content = cases.test_cases["generic_structure"]["data"]
            msg_main_content = utils.construct_msg_content(msg_main_content, [pld], pld, specified_encoding)
            for target in target_list:
                print("\033[94mtesting target mailbox: %s ...\n\033[0m" % target)
                execute_sending(sender_token, target, msg_main_content)
            time.sleep(1.5)
    elif msg_source == "eml":
        eml_path = ""
        msg_main_content = utils.get_main_content(eml_path)
        msg_main_content = utils.construct_msg_content(msg_main_content, specified_payload)
        # msg_main_content_with_payload = utils.insert_payload(msg_main_content, specified_payload)
        for target in target_list:
            print("\033[94mtesting target mailbox: %s ...\n\033[0m" % target)
            execute_sending(sender_token, target, msg_main_content)

    print("Finished.")


if __name__ == '__main__':
    main()
