import yt_dlp

def get_info(url):
    ydl_opts = {
        'quiet': True,
        'extract_flat': False,
        'noplaylist': True,
        'skip_download': True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            video = ydl.extract_info(url, download=False)

        return {
            "video_id": video.get("id"),
            "title": video.get("title"),
            "channel": video.get("uploader", "Unknown"),
            "duration": video.get("duration", 0)
        }

    except Exception as e:
        print("YouTube Error:", e)
        return None