""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.khelp$")
async def usit(e):
    await e.edit(
        f"      ╔════════════╗\n     ⚫𝘽𝘼𝙉𝙏𝙐𝘼𝙉⚫     \n╚════════════╝ \n"
        f"**Hai {DEFAULTUSER} Kalau Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "═⎆ Pemilik : [King Apis](t.me/PacarFerdilla) \n"
        "═⎆ Repo    : [Repo](https://github.com/apisuserbot/King-Userbot) \n"
        "═⎆ Instragam : [Instagram King Apis](Instagram.com/apis_goodboy) \n"
        "═⎆ Grup Support : [King Userbot Support](https://t.me/KingUserbotSupport)")


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"      ╔════════════╗\n  ⚫𝘿𝘼𝙁𝙏𝘼𝙍 𝙑𝘼𝙍𝙎⚫     \n╚════════════╝ \n"
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "═⎆ Daftar Vars : [DAFTAR VARS](https://raw.githubusercontent.com/apisuserbot/King-Userbot/King-Userbot/varshelper.txt)")


CMD_HELP.update(
    {
        "helper": "**✘ Plugin : **`helper`\
        \n\n  •  **Perintah :** `.khelp`\
        \n  •  **Function : **Bantuan Untuk ⚫𝐇𝐢𝐫𝐨-𝐔𝐬𝐞𝐫𝐛𝐨𝐭​⚫.\
        \n\n  •  **Perintah :** `.vars`\
        \n  •  **Function : **Melihat Daftar Vars.\
        \n\n  •  **Perintah :** `.repo`\
        \n  •  **Function : **Melihat Repo ⚫𝐇𝐢𝐫𝐨-𝐔𝐬𝐞𝐫𝐛𝐨𝐭​⚫.\
        \n\n  •  **Perintah :** `.string`\
        \n  •  **Function : **Link untuk mengambil String ⚫𝐇𝐢𝐫𝐨-𝐔𝐬𝐞𝐫𝐛𝐨𝐭​⚫.\
    "
    }
)
