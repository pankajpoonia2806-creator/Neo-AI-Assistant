import webbrowser


class WebsiteLauncher:

    WEBSITES = {

        "google": "https://www.google.com",
        "gmail": "https://mail.google.com",
        "youtube": "https://www.youtube.com",
        "chatgpt": "https://chatgpt.com",
        "github": "https://github.com",
        "netflix": "https://www.netflix.com",
        "jiohotstar": "https://www.hotstar.com/in",
        "hotstar": "https://www.hotstar.com/in",
        "instagram": "https://www.instagram.com",
        "facebook": "https://www.facebook.com",
        "linkedin": "https://www.linkedin.com",
        "twitter": "https://x.com",
        "x": "https://x.com",
        "amazon": "https://www.amazon.in",
        "flipkart": "https://www.flipkart.com",
        "spotify": "https://open.spotify.com",
        "whatsapp": "https://web.whatsapp.com"

    }

    @classmethod
    def open(cls, name):

        name = name.lower().strip()

        if name in cls.WEBSITES:

            webbrowser.open(cls.WEBSITES[name])

            return f"Opening {name.title()}."

        return None