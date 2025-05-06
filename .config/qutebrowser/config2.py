config = config
c = c
config.load_autoconfig(False)
c.fonts.default_family = "Noto Sans Mono"
config.set("colors.webpage.darkmode.enabled", True)

c.window.hide_decoration = True
config.set("colors.webpage.bg", "black")
c.aliases = {"q": "quit", "w": "session-save", "wq": "quit --save"}
config.set("content.cookies.accept", "all", "chrome-devtools://*")
config.set("content.cookies.accept", "all", "devtools://*")
config.set(
    "content.headers.user_agent",
    "Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}",
    "https://web.whatsapp.com/",
)
config.set(
    "content.headers.user_agent",
    "Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0",
    "https://accounts.google.com/*",
)
config.set(
    "content.headers.user_agent",
    "Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36",
    "https://*.slack.com/*",
)
config.set(
    "content.headers.user_agent",
    "Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0",
    "https://docs.google.com/*",
)
config.set(
    "content.headers.user_agent",
    "Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0",
    "https://drive.google.com/*",
)
config.set("content.images", True, "chrome-devtools://*")


c.auto_save.session = True

c.scrolling.bar = "always"

c.tabs.new_position.unrelated = "next"
c.input.partial_timeout = 0


c.tabs.position = "right"
c.tabs.width = 160
c.tabs.padding = {"bottom": 4, "left": 4, "right": 4, "top": 4}
