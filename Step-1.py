# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 12:04:02 2018

@author: Tejas
"""
import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer



class Er0rBot(sc2.BotAI):
    async def on_step(self,iteration):
        #What to do each step
        await self.distribute_workers()

run_game(maps.get("AbyssalReefLE"), [
    Bot(Race.Protoss, Er0rBot()),
    Computer(Race.Terran, Difficulty.Easy)
], realtime=True)