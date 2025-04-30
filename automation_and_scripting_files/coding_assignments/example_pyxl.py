import openpyxl
import datetime


def send_notification():
    match_score = fetch_scores()
    notification.notify(
        title='Live Sports Score Update',
        message=match_score,
        app_icon=None,  # Path to an app icon
        timeout=10,  # Duration in seconds
    )
    # Call record_to_excel here, after sending the notification
    record_to_excel(match_score) 

def record_to_excel(match_data):
    """Records the match data to an Excel spreadsheet."""
    try:
        workbook = openpyxl.load_workbook('sports_data.xlsx')
        sheet = workbook.active
    except FileNotFoundError:
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.append(["Home Team", "Score", "Away Team", "Date"])

    # Extract data (assuming match_data is in the format "HomeTeam Score - Score AwayTeam")
    try:
        home_team, score, away_team = match_data.split(' ')
        today = datetime.date.today().strftime("%Y-%m-%d")
        # Corrected line: Appending the complete date string
        sheet.append([home_team, score, away_team, today])  
    except ValueError:
        sheet.append(["Error processing data", "", "", today])

    workbook.save('sports_data.xlsx')

# Test sending a notification
send_notification()

schedule.every().day.at("08:00").do(send_notification)

# Test the scheduling of notifications (this will run until you stop it)
while True:
    schedule.run_pending()
    time.sleep(1)