#!/usr/bin/env python
# -*- coding: utf-8 -*-

import discord
import os


class Isac(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('メンテ'):
            await message.channel.send(
                    'こちらを見てくだしあ..!!!' +
                    'https://twitter.com/thedivisiongame'
            )
        if message.content == "眠たい" \
                or message.content == "眠い" \
                or message.content == "ねむい":
            await message.channel.send(
                    f"{message.author.mention}さん、寝ましょう"
            )


def main():
    token = os.getenv('token')
    client = Isac()
    client.run(token)


if __name__ == "__main__":
    main()
