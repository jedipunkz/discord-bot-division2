#!/usr/bin/env python
# -*- coding: utf-8 -*-

import discord
from discord.ext import commands
import requests
import os

token = os.getenv('token')


class D2():

    """ Division2 class which get user information. """

    def __init__(self, bot):
        self.bot = bot

    def get_user_id(self, uplay_name):
        params = (
            ('name', uplay_name),
            ('platform', 'uplay'),
        )
        r = requests.get(
                'https://thedivisiontab.com/api/search.php',
                params=params
        )
        if 'results' in r.json():
            return r.json()['results'][0]['user']
        else:
            return False

    def get_user_info(self, user_id):
        params = (
            ('pid', user_id),
        )
        r = requests.get(
                'https://thedivisiontab.com/api/player.php',
                params=params
        )
        timeplayed_total = int(r.json()['timeplayed_total'] / 3600)
        timeplayed_dz = int(r.json()['timeplayed_dz'] / 3600)
        timeplayed_pve = int(r.json()['timeplayed_pve'] / 3600)
        timeplayed_pvp = int(r.json()['timeplayed_pvp'] / 3600)
        timeplayed_rogue = int(r.json()['timeplayed_rogue'] / 3600)
        level_pve = r.json()['level_pve']
        level_dz = r.json()['level_dz']
        kills_npc = r.json()['kills_npc']
        kills_pvp = r.json()['kills_pvp']
        kills_pve_hyenas = r.json()['kills_pve_hyenas']
        kills_pve_outcasts = r.json()['kills_pve_outcasts']
        kills_pve_blacktusk = r.json()['kills_pve_blacktusk']
        kills_pve_truesons = r.json()['kills_pve_truesons']
        kills_pve_dz_hyenas = r.json()['kills_pve_dz_hyenas']
        kills_pve_dz_outcasts = r.json()['kills_pve_dz_outcasts']
        kills_pve_dz_blacktusk = r.json()['kills_pve_dz_blacktusk']
        kills_pve_dz_truesons = r.json()['kills_pve_dz_truesons']
        return timeplayed_total, timeplayed_dz, timeplayed_pve, timeplayed_pvp, timeplayed_rogue, level_pve, level_dz, kills_npc, kills_pvp, kills_pve_hyenas, kills_pve_outcasts, kills_pve_blacktusk, kills_pve_truesons, kills_pve_dz_hyenas, kills_pve_dz_outcasts, kills_pve_dz_blacktusk, kills_pve_dz_truesons


def main():
    bot = commands.Bot(
            command_prefix='/',
            description='a division2 bot get user information.'
    )

    @bot.command()
    async def d2user(ctx, uplay_name):
        user_id = D2(bot).get_user_id(uplay_name)
        if user_id:
            timeplayed_total, timeplayed_dz, timeplayed_pve, timeplayed_pvp, timeplayed_rogue, level_pve, level_dz, kills_npc, kills_pvp, kills_pve_hyenas, kills_pve_outcasts, kills_pve_blacktusk, kills_pve_truesons, kills_pve_dz_hyenas, kills_pve_dz_outcasts, kills_pve_dz_blacktusk, kills_pve_dz_truesons = D2(bot).get_user_info(user_id)
            await ctx.send(
                    uplay_name + ' さんの情報ですぉ ..!' +
                    '```' +
                    '--- プレイ時間 ---\n' +
                    'トータルプレイ時間:' + str(timeplayed_total) + '\n' +
                    'DZ プレイ時間:' + str(timeplayed_dz) + '\n' +
                    'PVE プレイ時間:' + str(timeplayed_pve) + '\n' +
                    'PVP プレイ時間:' + str(timeplayed_pvp) + '\n' +
                    'Rogue プレイ時間:' + str(timeplayed_rogue) + '\n' +
                    '--- レベル ---\n' +
                    'PVE レベル:' + str(level_pve) + '\n' +
                    'DZ レベル:' + str(level_dz) + '\n' +
                    '--- キルした数 ---\n' +
                    'キルした NPC 数:' + str(kills_npc) + '\n' +
                    'キルした Player 数:' + str(kills_pvp) + '\n' +
                    '--- PVE の属性毎のキルした数 ---\n' +
                    'キルしたハイエナの数:' + str(kills_pve_hyenas) + '\n' +
                    'キルしたアウトキャストの数:' + str(kills_pve_outcasts) + '\n' +
                    'キルしたトゥルーサンズの数:' + str(kills_pve_truesons) + '\n' +
                    'キルしたブラックタスクの数:' + str(kills_pve_blacktusk) + '\n' +
                    '--- PVE DZ の属性毎のキルした数 ---\n' +
                    'DZ でキルしたハイエナの数:' + str(kills_pve_dz_hyenas) + '\n' +
                    'DZ でキルしたアウトキャストの数:' + str(kills_pve_dz_outcasts) + '\n' +
                    'DZ でキルしたトゥルーサンズの数:' + str(kills_pve_dz_truesons) + '\n' +
                    'DZ でキルしたブラックタスクの数:' + str(kills_pve_dz_blacktusk) + '\n' +
                    '```'
                    )
        else:
            await ctx.send('ユーザーが見つかりませんでしたよぉ...')

    bot.run(token)


if __name__ == "__main__":
    main()
