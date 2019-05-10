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
        
        if message.content.startswith('統計'):
            await message.channel.send(
                    'こちらを見てくだしあ ..!!!\n' +
                    'ユーザ名 : nakama \n' +
                    'パスワード : naka-ma \n' +
                    'http://124.41.86.100:23001/d/uWfWtAmZk/division2?orgId=1&from=now%2Fd&to=now%2Fd'
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
