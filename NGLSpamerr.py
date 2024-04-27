import os  
import requests
import time
import textwrap

def sendSpam(user, message):
    url = 'https://ngl.link/api/submit'
    payload = {'username': user, 'question': message, 'deviceId': ""}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=payload, headers=headers)
    return response.status_code

def main():
    while True:
        banner_text = """

░█████╗░██╗░░░██╗██████╗░██╗██╗░░░░░
██╔══██╗╚██╗░██╔╝██╔══██╗██║██║░░░░░
██║░░╚═╝░╚████╔╝░██████╔╝██║██║░░░░░
██║░░██╗░░╚██╔╝░░██╔══██╗██║██║░░░░░
╚█████╔╝░░░██║░░░██║░░██║██║███████╗
░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚══════╝
        Dont abuse this tool. 
        """
        github_link = "https://github.com/Atsushinakajima14"
        facebook_link = "Cyril Matt O. Encenso"


        banner_text_wrapped = textwrap.fill(banner_text, width=40)
        github_link_wrapped = textwrap.fill(github_link, width=40)
        facebook_link_wrapped = textwrap.fill(facebook_link, width=100)

        box_ui = f"\033[36m{'-'*54}\n" + \
                 f"{banner_text_wrapped}\n" + \
                 f"{'-'*54}\n" + \
                 f"GitHub: {github_link_wrapped}\n" + \
                 f"Facebook: {facebook_link_wrapped}\n" + \
                 f"{'-'*54}\n"

        print(box_ui)

        user = input("\033[36mEnter username:~ \033[1;36m")
        message = input("\033[36mEnter message:~ \033[1;36m")
        amount = int(input("\033[36mEnter amount:~ \033[1;36m"))

        if amount > 100:
            print("Sorry, the limit is 100.")
        else:
            for i in range(1, amount + 1):
                status_code = sendSpam(user, message)
                text = f"\033[33m[ NGL ] \033[36m[\033[1;36m{i}\033[36m][{'success' if status_code == 200 else 'error'}]: Message sent to target: {user}\033[0m"
                print(text)
                time.sleep(2)

            print('\n\033[36mYou are loved by God. ♡\033[0m')

        time.sleep(3) 
        os.system('clear' if os.name == 'posix' else 'cls') 

if __name__ == "__main__":
    main()
