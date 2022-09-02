import os

from dotenv import dotenv_values
from genshin.settings import log, CONFIG
from genshin.sign import Sign
from genshin.notify import Notify

if __name__ == '__main__':

    notify = Notify()
    msg_list = []
    ret = success_num = fail_num = 0
    """
    HoYoLAB Community's COOKIE
    :param OS_COOKIE: HoYoLAB cookie(s) for one or more accounts.
        Separate cookies for multiple accounts with the hash symbol #
        e.g. cookie1text#cookie2text
        Do not surround cookies with quotes "" if using Github Secrets.
    """
    # Github Actions -> Settings -> Secrets
    # Ensure that the Name is exactly: OS_COOKIE
    # Value should look like: login_ticket=xxx; account_id=696969; cookie_token=xxxxx; ltoken=xxxx; ltuid=696969; mi18nLang=en-us; _MHYUUID=xxx
    #         Separate cookies for multiple accounts with the hash symbol #
    #         e.g. cookie1text#cookie2text
    OS_COOKIE = ''
    token = ''
    env_config = dotenv_values(".env")

    if OS_COOKIE == '':
        OS_COOKIE = os.environ.get('OS_COOKIE', env_config['OS_COOKIE'])
    if OS_COOKIE == '':
        log.error("Cookie not set properly, please read the documentation on how to set and format your cookie in Github Secrets.")
        raise Exception("Cookie failure")

    cookie_list = OS_COOKIE.split('#')
    log.info(f'Number of account cookies read: {len(cookie_list)}')
    succes_num = 0
    fail_num = 0
    already_checked_in_num = 0
    for i in range(len(cookie_list)):
        log.info(f'Preparing NO.{i + 1} Account Check-In...')
        try:
            #ltoken = cookie_list[i].split('ltoken=')[1].split(';')[0]
            token = cookie_list[i].split('cookie_token=')[1].split(';')[0]
            msg = f'	NO.{i + 1} Account:{Sign(cookie_list[i]).run()}'
            msg_list.append(msg)
            success_num = success_num + 1
        except IndexError:
            cookie_values = ["login_ticket","account_id","cookie_token","ltoken","ltuid","mi18nLang","_MHYUUID"]
            for j in cookie_values:
                if not(j in cookie_list[i]):
                    log.error(f'{j} not found')
            fail_num = fail_num + 1
            ret = -1
            log.info(f"\n\nTry these troubleshooting steps and grab the cookie again:\n -Log out and log back in\n -Ensure you are on the Daily Rewards page and not the HoyoLab Forums page\n -Try incognito mode\n -Try clearing your browser history/cache\n -Try using another browser\n")
        except Exception as e:
            if not token:
                log.error("Cookie token not found, please try to relog on the check-in page.")

            msg = f'	NO.{i + 1} Account:\n    {e}'
            msg_list.append(msg)
            fail_num = fail_num + 1
            log.error(msg)
            ret = -1
        continue
    notify.send(status= f'\n-Number of successful sign-ins: {success_num} \n-Number of failed sign-ins: {fail_num} ', msg=msg_list)
    if ret != 0:
        log.error('program terminated with errors')
        exit(ret)
    log.info('exit success')