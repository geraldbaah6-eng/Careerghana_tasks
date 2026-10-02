import random 
import smtplib
from email.mime.text import MIMEText


def generate_daily_tip(): 
    # List of 15 career tips
    tips = [ 
        "Do the hard Things as they are easy now.", 
        "Comfort breeds complacency; challenge yourself to grow.", 
        "Motivation is fleeting; discipline and habit sustain long term growth.", 
        "Document your wins and project accomplishments weekly for your resume.", 
        "Fail fast, learn faster. Reframe mistakes as valuable diagnostic data.", 
        "Embrace feedback as a tool for rapid professional growth, not personal critique.", 
        "Consistency always beats intensity when building new technical skills.", 
        "Your resume doesn't have to be perfect; it has to be honest and reflective of your skills.", 
        "Your portfolio projects show what you can build; your documentation shows how you think.", 
        "One code a day for a year keeps the bugs away — practice makes perfect.", 
        "AI won't replace humans; humans with AI will replace humans without AI.",
        "Read official documentation — it is often the most accurate source of truth.", 
        "You Don't have to be great to start; you have to start to be great.", 
        "Focus on understanding core concepts rather than memorizing exact syntax.", 
        "Network before you need it; relationships built on genuine connection yield the best opportunities." 
    ] 
    return random.choice(tips)

def sendemailtip(tip):
    # configuration for sending email
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # TLS port

    sender_email = "geraldbaah11@gmail.com"
    receiver_emails = [
        "geraldbaah3@gmail.com",
        "giroud2331@gmail.com",
        "geraldbaah6@gmail.com"
    ]
    app_password = "ihnr mkjm xjyb pzjm" 

    #Creating an email message object 
    message = MIMEText(f"Hello!\n\nHere is your daily career tip:\n\n\"{tip}\"\n\nHave a productive day!")
    message['Subject'] = "Daily Career Tip"
    message['From'] = sender_email
    message['To'] = ", ".join(receiver_emails)  # Join multiple recipients with commas

    try:
        # Establishing a secure TLS connection to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  

        server.login(sender_email, app_password)  # Log in to the SMTP server
        server.sendmail(sender_email, receiver_emails, message.as_string())  # Sending the email
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")


if __name__ == "__main__": 
    tip = generate_daily_tip()
    Selected_tip = generate_daily_tip()
    print(f"Today's Career Tip: {Selected_tip}")
    
    sendemailtip(Selected_tip)