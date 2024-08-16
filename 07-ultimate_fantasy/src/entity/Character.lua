--[[
    ISPPV1 2023
    Study Case: Ultimate Fantasy (RPG)

    Author: Colton Ogden
    cogden@cs50.harvard.edu

    Modified by Alejandro Mujica (alejandro.j.mujic4@gmail.com)

    This class contains the class Character.
]]
Character = Class{__includes = BattleEntity}

function Character:init(def)
    BattleEntity.init(self, def)

    self.HPIV = def.HPIV
    self.attackIV = def.attackIV
    self.defenseIV = def.defenseIV
    self.magicIV = def.magicIV
    self.currentExp = 0
    self:nextExpToLevel()
end

function Character:calculateStats()
    for i = 1, self.level do
        self:statsLevelUp()
    end
end

function Character:statsLevelUp()
    local HPIncrease = 0

    for j = 1, 3 do
        if math.random(6) <= self.HPIV then
            self.HP = self.HP + 1
            HPIncrease = HPIncrease + 1
        end
    end

    self.currentHP = self.HP

    local attackIncrease = 0

    for j = 1, 3 do
        if math.random(6) <= self.attackIV then
            self.attack = self.attack + 1
            attackIncrease = attackIncrease + 1
        end
    end

    local defenseIncrease = 0

    for j = 1, 3 do
        if math.random(6) <= self.defenseIV then
            self.defense = self.defense + 1
            defenseIncrease = defenseIncrease + 1
        end
    end

    local magicIncrease = 0

    for j = 1, 3 do
        if math.random(6) <= self.magicIV then
            self.magic = self.magic + 1
            magicIncrease = magicIncrease + 1
        end
    end

    return HPIncrease, attackIncrease, defenseIncrease, magicIncrease
end

function Character:levelUp()
    self.level = self.level + 1
    self:nextExpToLevel()
    return self:statsLevelUp()
end

function Character:nextExpToLevel()
    self.expToLevel = self.level * self.level * 10 * 1.1
end
