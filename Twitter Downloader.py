import tweepy
import wget
import tkinter as tk
from tkinter import messagebox

# Twitter API credentials
consumer_key = "your_consumer_key_here"
consumer_secret = "your_consumer_secret_here"
access_token = "your_access_token_here"
access_token_secret = "your_access_token_secret_here"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Define function to download Twitter video or image
def download_media():
    media_url = media_url_entry.get()
    try:
        media = api.get_status(media_url, tweet_mode="extended").extended_entities["media"][0]
        if "video_info" in media:
            best_bitrate = max(media.video_info["variants"], key=lambda v: v["bitrate"])
            url = best_bitrate["url"]
        else:
            url = media.media_url
        filename = wget.download(url)
        messagebox.showinfo("Download Complete", f"The media has been downloaded successfully as {filename}.")
    except:
        messagebox.showerror("Download Error", "An error occurred while downloading the media. Please check the URL and try again.")

# Create GUI window
window = tk.Tk()
window.title("Twitter Media Downloader")

# Create media URL label and entry box
media_url_label = tk.Label(window, text="Twitter Media URL:")
media_url_label.pack()
media_url_entry = tk.Entry(window, width=50)
media_url_entry.pack()

# Create download button
download_button = tk.Button(window, text="Download", command=download_media)
download_button.pack()

# Run GUI window
window.mainloop()
