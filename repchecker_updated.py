import requests
import tkinter as tk
from tkinter import messagebox

def check_ip():
    ip = ip_entry.get()
    if not ip:
        messagebox.showwarning("Input Error", "Please enter an IP address.")
        return

    url = "https://api.abuseipdb.com/api/v2/check"
    querystring = {
        'ipAddress': ip,
        'maxAgeInDays': '90'
    }
    headers = {
        'Accept': 'application/json',
        'Key': '3f66dd68273c3981daf1c9bd3143f01020cc82f6f855badf018070814b8d0e9a2f089c8095824498'
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()

        if 'data' in data:
            rep = data['data']
            result = (
                f"IP: {rep['ipAddress']}\n"
                f"Is Public: {rep['isPublic']}\n"
                f"Abuse Score: {rep['abuseConfidenceScore']}\n"
                f"Country: {rep['countryCode']}\n"
                f"Usage Type: {rep['usageType']}\n"
                f"ISP: {rep['isp']}\n"
                f"Domain: {rep['domain']}\n"
                f"Total Reports: {rep['totalReports']}\n"
                f"Last Reported At: {rep['lastReportedAt']}"
            )
        else:
            result = "No data found or invalid IP."

        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, result)

    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("IP Reputation Checker")

tk.Label(root, text="Enter IP address:").pack(pady=5)
ip_entry = tk.Entry(root, width=30)
ip_entry.pack()

tk.Button(root, text="Check IP", command=check_ip).pack(pady=10)

result_text = tk.Text(root, height=15, width=60)
result_text.pack(pady=10)

root.mainloop()
