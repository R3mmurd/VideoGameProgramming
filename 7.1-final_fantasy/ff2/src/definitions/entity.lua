DEFAULT_CHARACTER_FRAME = 8
ENTITY_WIDTH = 16
ENTITY_HEIGHT = 18
NUM_CHARACTERS = 4

BATTLE_WIDTH = 16
BATTLE_HEIGHT = TILE_HEIGHT - 64 / TILE_SIZE - 2
BATTLE_PADDLE = {
    x = 4, y = 1
}

PARTY_BATTLE_POSITIONS = {
    [1] = {x = BATTLE_PADDLE.x + 6, y = BATTLE_PADDLE.y + 3},
    [2] = {x = BATTLE_PADDLE.x + 6, y = BATTLE_PADDLE.y + BATTLE_HEIGHT - 1},
    [3] = {x = BATTLE_PADDLE.x + 3, y = BATTLE_PADDLE.y + 3},
    [4] = {x = BATTLE_PADDLE.x + 3, y = BATTLE_PADDLE.y + BATTLE_HEIGHT - 1}
}

ENEMIES_POSITIONS = {
    [3] = {
        {x = BATTLE_PADDLE.x + BATTLE_WIDTH - 6, y = BATTLE_PADDLE.y + 5},
        {x = BATTLE_PADDLE.x + BATTLE_WIDTH - 3, y = BATTLE_PADDLE.y + 3},
        {x = BATTLE_PADDLE.x + BATTLE_WIDTH - 3, y = BATTLE_PADDLE.y + BATTLE_HEIGHT - 1}
    },
    [4] = {
        {x = BATTLE_PADDLE.x + BATTLE_WIDTH - 6, y = BATTLE_PADDLE.y + 3},
        {x = BATTLE_PADDLE.x + BATTLE_WIDTH - 2, y = BATTLE_PADDLE.y + 3},
        {x = BATTLE_PADDLE.x + BATTLE_WIDTH - 6, y = BATTLE_PADDLE.y + BATTLE_HEIGHT - 1},
        {x = BATTLE_PADDLE.x + BATTLE_WIDTH - 2, y = BATTLE_PADDLE.y + BATTLE_HEIGHT - 1}
    },
    [5] = {
        {x = BATTLE_PADDLE.x + BATTLE_WIDTH - 6, y = BATTLE_PADDLE.y + 3},
        {x = BATTLE_PADDLE.x + BATTLE_WIDTH - 2, y = BATTLE_PADDLE.y + 3},
        {x = BATTLE_PADDLE.x + BATTLE_WIDTH - 4, y = BATTLE_PADDLE.y + 5},
        {x = BATTLE_PADDLE.x + BATTLE_WIDTH - 6, y = BATTLE_PADDLE.y + BATTLE_HEIGHT - 1},
        {x = BATTLE_PADDLE.x + BATTLE_WIDTH - 2, y = BATTLE_PADDLE.y + BATTLE_HEIGHT - 1}
    }
}

ENTITY_DEFS = {
    animations = {
        ['walk-up'] = {
            frames = {1, 2, 3},
            interval = 0.1
        },
        ['walk-right'] = {
            frames = {4, 5, 6},
            interval = 0.1
        },
        ['walk-down'] = {
            frames = {7, 8, 9},
            interval = 0.1
        },
        ['walk-left'] = {
            frames = {10, 11, 12},
            interval = 0.1
        },
        ['idle-up'] = {
            frames = {2}
        },
        ['idle-right'] = {
            frames = {5}
        },
        ['idle-down'] = {
            frames = {8}
        },
        ['idle-left'] = {
            frames = {11}
        }
    },
    characters = {
        [1] = {
            type = 'warrior',
            female = {
                name  = 'Celes',
                texture = 'warrior-female',
            },
            male = {
                name  = 'Squall',
                texture = 'warrior-male',
            },
            properties = {
                level = 1,
                baseHP = 40,
                baseAttack = 10,
                baseDefense = 10,
                baseMagic = 0,
                HPIV = 4,
                attackIV = 5,
                defenseIV = 5,
                magicIV = 0,
                level = 1
            },
            actions = {
                {
                    name = 'Attack',
                    target_type = 'enemy',
                    sound_effect = 'hit',
                    strength = 1.5,
                    require_target = true,
                    func = function(entity, target, strength)
                        local amount = math.max(0, math.floor(entity:computeAttack()*strength) - target:computeDefense())
                        target:damage(amount)
                        return amount
                    end
                }
            }
        },
        [2] = {
            type = 'ranger', 
            female = {
                name = 'Terra',
                texture = 'ranger-female',
            },
            male = {
                name = 'Cloud',
                texture = 'ranger-male',
            },
            properties = {
                level = 1,
                baseHP = 35,
                baseAttack = 12,
                baseDefense = 8,
                baseMagic = 1,
                HPIV = 2,
                attackIV = 7,
                defenseIV = 4,
                magicIV = 1,
                level = 1
            },
            actions = {
                {
                    name = 'Attack',
                    target_type = 'enemy',
                    sound_effect = 'hit',
                    strength = 1.3,
                    require_target = true,
                    func = function(entity, target, strength)
                        local amount = math.max(0, math.floor(entity:computeAttack()*strength) - target:computeDefense())
                        target:damage(amount)
                        return amount
                    end
                },
                {
                    name = 'Arrows',
                    target_type = 'enemy',
                    sound_effect = 'arrows',
                    require_target = false,
                    strength = 10,
                    func = function(entity, targets, strength)
                        local amount = math.floor(entity:computeAttack()*strength)
                        local actual_amount = math.floor(amount / #targets)
                        for k, target in pairs(targets) do
                            target:damage(actual_amount)
                        end
                        return actual_amount
                    end
                }
            }
        },
        [3] = {
            type = 'healer',
            female = {
                name = 'Tifa',
                texture = 'healer-female',
            },
            male = {
                name = 'Kimahri',
                texture = 'healer-male',
            },
            properties = {
                level = 1,
                baseHP = 25,
                baseAttack = 2,
                baseDefense = 5,
                baseMagic = 10,
                HPIV = 2,
                attackIV = 2,
                defenseIV = 2,
                magicIV = 7,
                level = 1
            },
            actions = {
                {
                    name = 'Heal',
                    target_type = 'character',
                    strength = 5,
                    require_target = true,
                    sound_effect = 'powerup',
                    func = function(entity, target, strength)
                        local amount = math.floor(entity:computeHealing()*strength)
                        target:heal(amount)
                        return amount
                    end
                },
                {
                    name = 'Global Heal',
                    target_type = 'character',
                    require_target = false,
                    strength = 8,
                    sound_effect = 'powerup',
                    func = function(entity, targets, strength)
                        local amount = math.floor(entity:computeHealing()*strength)
                        local actual_amount = math.floor(amount / #targets)
                        for k, target in pairs(targets) do
                            target:heal(actual_amount)
                        end
                        return actual_amount
                    end
                }
            }
        },
        [4] = {
            type = 'mage',
            female = {
                name = 'Rinoa',
                texture = 'mage-female',
            },
            male = {
                name = 'Sephiroth',
                texture = 'mage-male',
            },
            properties = {
                level = 1,
                baseHP = 30,
                baseAttack = 5,
                baseDefense = 5,
                baseMagic = 12,
                HPIV = 2,
                attackIV = 3,
                defenseIV = 2,
                magicIV = 8,
                level = 1
            },
            actions = {
                {
                    name = 'Flame',
                    target_type = 'enemy',
                    require_target = false,
                    strength = 10,
                    sound_effect = 'flame',
                    func = function(entity, targets, strength)
                        local amount = math.floor(entity:computeAttack()*strength)
                        local actual_amount = math.floor(amount / #targets)
                        for k, target in pairs(targets) do
                            target:damage(actual_amount)
                        end
                        return actual_amount
                    end
                }
            }
        }
    },
    npcs = {
        female = {
            texture = 'npc-female',
            names = {
                'Alice', 'Fiona', 'Beth', 'Cami', 'Rose'
            }
        },
        male = {
            texture = 'npc-male',
            names = {
                'Albert', 'Leon', 'Nick', 'Alex', 'Sam'
            }
        },
        texts = {
            'Good luck in your journey!',
            'You, little guys! Go to defeat the west monster and break the curse!',
            'All of you are so nice!',
            'Thank you for taking such a risk! I love you all!'
        }
    },
    enemies = {
        north = {
            {
                level = 1,
                type = 'slime',
                texture = 'slime',
                width = 16,
                height = 16,
                baseHP = 15,
                baseAttack = 20,
                baseDefense = 5,
                baseMagic = 0,
                animations = {
                    ['default'] = {
                        frames = {4, 5, 6},
                        interval = 0.3
                    }
                },
                actions = {
                    {
                        name = 'Attack',
                        target_type = 'enemy',
                        sound_effect = 'hit',
                        require_target = true,
                        func = function(entity, target)
                            local amount = math.max(0, entity:computeAttack() - target:computeDefense())
                            target:damage(amount)
                            return amount
                        end
                    }
                }
            }
        },
        south = {
            {
                level = 2,
                type = 'worm',
                texture = 'small-worm',
                width = 16,
                height = 16,
                baseHP = 30,
                baseAttack = 30,
                baseDefense = 7,
                baseMagic = 0,
                animations = {
                    ['default'] = {
                        frames = {4, 5, 6},
                        interval = 0.15
                    }
                },
                actions = {
                    {
                        name = 'Attack',
                        target_type = 'enemy',
                        sound_effect = 'hit',
                        require_target = true,
                        func = function(entity, target)
                            local amount = math.max(0, entity:computeAttack() - target:computeDefense())
                            target:damage(amount)
                            return amount
                        end
                    }
                }
            }
        },
        east = {
            {
                level = 3,
                type = 'snake',
                texture = 'snake',
                width = 16,
                height = 16,
                baseHP = 40,
                baseAttack = 40,
                baseDefense = 15,
                baseMagic = 2,
                animations = {
                    ['default'] = {
                        frames = {4, 5, 6},
                        interval = 0.15
                    }
                },
                actions = {
                    {
                        name = 'Attack',
                        target_type = 'enemy',
                        sound_effect = 'hit',
                        require_target = true,
                        func = function(entity, target)
                            local amount = math.max(0, entity:computeAttack() - target:computeDefense())
                            target:damage(amount)
                            return amount
                        end
                    }
                }
            }
        },
        west = {
            {
                level = 4,
                type = 'pumpking',
                texture = 'pumpking',
                width = 23,
                height = 23,
                baseHP = 55,
                baseAttack = 60,
                baseDefense = 18,
                baseMagic = 5,
                animations = {
                    ['default'] = {
                        frames = {4, 5, 6},
                        interval = 0.15
                    }
                },
                actions = {
                    {
                        name = 'Attack',
                        target_type = 'enemy',
                        sound_effect = 'hit',
                        require_target = true,
                        func = function(entity, target)
                            local amount = math.max(0, entity:computeAttack() - target:computeDefense())
                            target:damage(amount)
                            return amount
                        end
                    }
                }
            }
        },
        boss = {
            level = 10,
            type = 'boss',
            name = 'Man-Eater Flower',
            texture = 'man-eater-flower',
            width = 30,
            height = 38,
            baseHP = 100,
            baseAttack = 100,
            baseDefense = 30,
            baseMagic = 30,
            animations = {
                ['default'] = {
                    frames = {4, 5, 6},
                    interval = 0.15
                }
            },
            actions = {
                {
                    name = 'Attack',
                    target_type = 'enemy',
                    sound_effect = 'hit',
                    require_target = true,
                    func = function(entity, target)
                        local amount = math.max(0, entity:computeAttack() - target:computeDefense())
                        target:damage(amount)
                        return amount
                    end
                },
                {
                    name = 'Flame',
                    target_type = 'enemy',
                    require_target = false,
                    sound_effect = 'flame',
                    func = function(entity, targets)
                        local amount = entity:computeAttack()
                        local actual_amount = math.floor(amount / #targets)
                        for k, target in pairs(targets) do
                            target:damage(actual_amount)
                        end
                        return actual_amount
                    end
                },
                {
                    name = 'Global Heal',
                    target_type = 'character',
                    require_target = false,
                    sound_effect = 'powerup',
                    func = function(entity, targets)
                        local amount = entity:computeHealing()
                        local actual_amount = math.floor(amount / #targets)
                        for k, target in pairs(targets) do
                            target:heal(actual_amount)
                        end
                        return actual_amount
                    end
                }
            }
        }
    }
}