namespace SpriteKind {
    export const Platform = SpriteKind.create()
    export const plattform2 = SpriteKind.create()
    export const NPC_A = SpriteKind.create()
    export const Press = SpriteKind.create()
    export const ITEM_I = SpriteKind.create()
    export const Sandwich = SpriteKind.create()
    export const NPC_B = SpriteKind.create()
    export const ITEM_II = SpriteKind.create()
    export const SANDWICH_ITEM = SpriteKind.create()
    export const Platfor_3 = SpriteKind.create()
    export const Item_III = SpriteKind.create()
    export const NPC_C = SpriteKind.create()
    export const Boss_II = SpriteKind.create()
}
namespace StatusBarKind {
    export const Lvl = StatusBarKind.create()
    export const Player_Fight_Health = StatusBarKind.create()
    export const Level_BAR = StatusBarKind.create()
    export const Enemy_Health = StatusBarKind.create()
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile38`, function (sprite, location) {
    Player_A1.vy += 200
    Player_A1.vx = 0
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile72`, function (sprite, location) {
    tiles.placeOnRandomTile(Player_A1, assets.tile`myTile18`)
})
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Fight_Toggle == 1) {
        if (Animation_finished == 1 && turn_toggle == 1) {
            if (METTALL_PIPE_ITEM == 0) {
                Damage = randint(0, -25)
            } else if (timewastermedal_ITEM == 1) {
                Damage = randint(0, -35)
            } else {
                Damage = randint(-2, -20)
            }
            Enemy_Health.value += Damage
            animation.runImageAnimation(
            radioactive_Sandwich,
            [img`
                ......ec.........
                ...33ebbc........
                ...3e4dbbc.......
                ...e4dddbbc......
                33e4dddddbbc.....
                3eddddddddbbc....
                e4ddc6dc6ddbbc...
                2224744744222bc..
                e4dd5dd5ddddc2c..
                6edb7dddd6bd42...
                67edb7666bf222...
                .77edb6bbf42.....
                ...6e4bdc222.....
                ...67e4c42.......
                ....76c422.......
                ......cc.........
                .................
                .................
                .................
                `,img`
                .................
                .......ec........
                ....33ebbc.......
                ....314dbbc......
                ....e1dddbbc.....
                .3311111ddbbc....
                .3edd1dddddbbc...
                .e4dd1ddddddbbc..
                .2224c64c64222bc.
                .e4ddddddddddc2c.
                .6edbddddd6b142..
                .67edb7666bf122..
                ..77edb6bb11111..
                ....6e4bdc221....
                ....67e4c42.1....
                .....76c422......
                .......cc........
                .................
                .................
                `,img`
                .................
                .......ec........
                ....33ebbc.......
                ....3e41bbc......
                ....e4d1dbbc.....
                .33e411111bbc....
                .3edddd1dddbbc...
                .e4ddc61c6ddbbc..
                .2224744744222bc.
                .e4d15dd5dddd12c.
                .6ed17dddd6bd12..
                .611111666b11111.
                ..771db6bbf421...
                ....1e4bdc2221...
                ....67e4c42......
                .....76c422......
                .......cc........
                .................
                .................
                `,img`
                ......ec.........
                ...33ebbc........
                ...3e4dbbc.......
                ...e4dddbbc......
                33e4dddddbbc.....
                3eddddddddbbc....
                e4ddc6dc6ddbbc...
                2224744744222bc..
                e4dd5dd5ddddc2c..
                6edb7dddd6bd42...
                67edb7666bf222...
                .77edb6bbf42.....
                ...6e4bdc222.....
                ...67e4c42.......
                ....76c422.......
                ......cc.........
                .................
                .................
                .................
                `],
            200,
            false
            )
            Animation_finished = 0
            pause(500)
            turn_toggle = 0
            if (turn_toggle == 0) {
                Player_Damage = randint(0, -10)
                animation.runImageAnimation(
                Player_A1,
                [img`
                    . . . . . . . f f f f f . . . . 
                    . . . . . . f b 1 e e e f . . . 
                    . . . . . f b 1 e d d d d f . . 
                    . . . . f f 1 e d f d d f d c . 
                    . . . f 1 1 1 e d f d d f d c . 
                    . . . c 1 b 1 e d d d d e e d c 
                    f f . c 1 b 1 e d d c d d d d c 
                    f 1 f . c f 1 e d d d c c c c c 
                    f 1 f . 5 f f b e d d d d b f . 
                    f 1 f 5 f b b 1 b f f f f f . . 
                    f 1 f f b 1 1 2 8 1 1 f . . . . 
                    . f f b 1 1 1 f 1 f f 1 f . . . 
                    . . f b 1 1 1 f 1 f f 1 f . . . 
                    . . . f 1 f f b c f b c f . . . 
                    . . . f c b b c c c c c f . . . 
                    . . . f f f f f f f f f . . . . 
                    `,img`
                    . . . . . . . f f f f f . . . . 
                    . . 7 . . . f b 1 e e 7 f . . . 
                    . . 7 . . f b 1 e d d 7 d f . . 
                    7 7 7 5 5 f 1 e d 7 7 7 5 5 c . 
                    . . 5 f 1 1 1 e d f d 5 f d c . 
                    . . 5 c 1 b 1 e d d d 5 e e d c 
                    f f . c 1 b 1 e d d c d d d d c 
                    f 1 f . c f 1 e d d d c c c c c 
                    f 1 f . 5 f f b e d d d d b f . 
                    f 1 f 5 f b b 1 b f f f f f 7 . 
                    f 1 f f b 1 1 2 8 1 1 f . . 7 . 
                    . f f b 1 7 1 f 1 f f 1 7 7 7 5 
                    . . f b 1 7 1 f 1 f f 1 f . 5 . 
                    . . . 7 7 7 5 5 c f b c f . 5 . 
                    . . . f c 5 b c c c c c f . . . 
                    . . . f f 5 f f f f f f . . . . 
                    `,img`
                    . . . . . . . f f f f f . . . . 
                    . . . . . . f b 7 e e e f . . . 
                    . . . . . f b 1 7 d d d d f . . 
                    . . . . f f 7 7 7 5 5 d f d c . 
                    . . . f 1 1 1 e 5 f d d f d c . 
                    . . . c 1 b 1 e 5 d d d e e d c 
                    f f . c 1 b 1 e d d c d d d d c 
                    f 1 f . c f 1 e d d d c c c 7 c 
                    f 1 f . 5 f f b e d d d d b 7 . 
                    f 1 f 5 f b b 1 b f f f 7 7 7 5 
                    f 1 f f b 1 1 2 8 7 1 f . . 5 . 
                    . f f b 1 1 1 f 1 7 f 1 f . 5 . 
                    . . f b 1 1 1 7 7 7 5 5 f . . . 
                    . . . f 1 f f b c 5 b c f . . . 
                    . . . f c b b c c 5 c c f . . . 
                    . . . f f f f f f f f f . . . . 
                    `,img`
                    . . . . . . . f f f f f . . . . 
                    . . . . . . f b 1 e e e f . . . 
                    . . . . . f b 1 e d d d d f . . 
                    . . . . f f 1 e d f d d f d c . 
                    . . . f 1 1 1 e d f d d f d c . 
                    . . . c 1 b 1 e d d d d e e d c 
                    f f . c 1 b 1 e d d c d d d d c 
                    f 1 f . c f 1 e d d d c c c c c 
                    f 1 f . 5 f f b e d d d d b f . 
                    f 1 f 5 f b b 1 b f f f f f . . 
                    f 1 f f b 1 1 2 8 1 1 f . . . . 
                    . f f b 1 1 1 f 1 f f 1 f . . . 
                    . . f b 1 1 1 f 1 f f 1 f . . . 
                    . . . f 1 f f b c f b c f . . . 
                    . . . f c b b c c c c c f . . . 
                    . . . f f f f f f f f f . . . . 
                    `],
                200,
                false
                )
                turn_toggle = 1
                Player_health_in_fight.value += Player_Damage
                Animation_finished = 1
            }
        }
    }
})
scene.onOverlapTile(SpriteKind.Press, assets.tile`myTile28`, function (sprite, location) {
    Press_A1.ay = 200
})
controller.combos.attachCombo("ABAB", function () {
    Zahl += 1
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Platfor_3, function (sprite, otherSprite) {
    if (Level.value == 0) {
        if (info.life() == 1) {
            Dead_1()
        } else {
            pause(100)
            Player_A1.y += -30
            Player_A1.vx += -30
            info.changeLifeBy(-1)
        }
    } else {
        if (info.life() == 1) {
            Dead_1()
        } else {
            pause(100)
            Player_A1.y += -30
            Player_A1.vx += -30
            info.changeLifeBy(-1)
        }
    }
})
function Statusbar_changes_for_fight () {
    Enemy_Health = statusbars.create(20, 4, StatusBarKind.Enemy_Health)
    Enemy_Health.setColor(7, 6)
    Enemy_Health.setBarBorder(1, 8)
    Player_health_in_fight = statusbars.create(4, 50, StatusBarKind.Player_Fight_Health)
    Player_health_in_fight.setColor(2, 4)
    Player_health_in_fight.setBarBorder(1, 14)
    Save_for_statusbar_LIFE_BARRRR = LIFE_BARRRRR.value
    save_for_Level = Level.value
    Level.setColor(0, 0)
    LIFE_BARRRRR.setColor(0, 0)
    Level.setBarBorder(1, 0)
    LIFE_BARRRRR.setBarBorder(1, 0)
}
function Item_menu_page_II () {
	
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile60`, function (sprite, location) {
    game.showLongText("Congrats you waisted time!", DialogLayout.Bottom)
    timewastermedal = sprites.create(img`
        .......111.......
        ....111222111....
        ...12228882221...
        ..12888...88821..
        .128.........821.
        .128.........821.
        .128.........821.
        .128.........821.
        ..128.......821..
        ..128.......821..
        ...1288.4.8821...
        ....12dd54421....
        .....d555554.....
        .....d554554.....
        ....d55545552....
        .....4554452.....
        .....4555552.....
        ......44522......
        ........2........
        `, SpriteKind.ITEM_II)
    tiles.placeOnTile(timewastermedal, location)
    tiles.setTileAt(location, assets.tile`myTile41`)
    timewastermedal.follow(Player_A1)
    timewastermedal_ITEM = 1
    Item = 1
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile34`, function (sprite, location) {
    Player_A1.vx += 10
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.ITEM_I, function (sprite, otherSprite) {
    Get_item()
    sprites.destroy(otherSprite)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile15`, function (sprite, location) {
    Dead_1()
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile22`, function (sprite, location) {
    tiles.placeOnRandomTile(Player_A1, assets.tile`myTile23`)
})
function MENU_end () {
    Player_A1 = sprites.create(img`
        . . . . . . . f f f f f . . . . 
        . . . . . . f b 1 e e e f . . . 
        . . . . . f b 1 e d d d d f . . 
        . . . . f f b e d f d d f d c . 
        . . . f 1 1 1 e d f d d f d c . 
        . . . c 1 b 1 e d d d d e e d c 
        . . . c 1 b 1 e d d c d d d d c 
        . . . . c f 1 1 e d d c c c c c 
        . . . . 5 f f b b e d d d b f . 
        . . . 5 f b b 1 1 f f f f f . . 
        f f 4 f b 1 1 1 8 2 f f . . . . 
        f 1 4 f 1 1 f 1 1 f 1 1 f . . . 
        f 1 4 f 1 1 1 f 1 1 f 1 1 f . . 
        f 1 f f 1 f b b f b c f c b f . 
        f f f f 1 b c c f c c f c c f . 
        . f f f f f f f f f f f f f . . 
        `, SpriteKind.Player)
    if (Level.value == 2) {
        Start()
        tiles.placeOnTile(Player_A1, Player_POS)
    } else if (Level.value == 3) {
        platform = sprites.create(img`
            ffffffffff
            f86919191f
            f86911911f
            f86919191f
            f86991191f
            f86919911f
            f86991191f
            f86911191f
            f86911191f
            f86991191f
            f86919911f
            f86991191f
            f86919191f
            f86911911f
            f86919191f
            f86991191f
            f86991191f
            f86919191f
            f86911911f
            f86919191f
            f86991191f
            f86919911f
            f86991191f
            f86911191f
            f86911191f
            f86991191f
            f86919911f
            f86991191f
            f86919191f
            f86911911f
            f86919191f
            f86991191f
            f86991191f
            f86919191f
            f86911911f
            f86919191f
            f86991191f
            f86919911f
            f86991191f
            f86911191f
            f86911191f
            f86991191f
            f86919911f
            f86991191f
            f86919191f
            f86911911f
            f86919191f
            ffffffffff
            `, SpriteKind.Platform)
        platform_2 = sprites.create(img`
            ffffffffffffffffffffffffffffffffffffffffffffffff
            f8888888888888888888888888888888888888888888888f
            f6666666666666666666666666666666666666666666666f
            f9999999999999999999999999999999999999999999999f
            f1119191191911199111919119191119911191911919111f
            f9191911119191911919191111919191191919111191919f
            f1911911119119111191191111911911119119111191191f
            f9199199991991999919919999199199991991999919919f
            f1111111111111111111111111111111111111111111111f
            ffffffffffffffffffffffffffffffffffffffffffffffff
            `, SpriteKind.plattform2)
        Start_2()
        tiles.placeOnTile(Player_A1, Player_POS)
    } else if (Level.value == 4) {
        platform = sprites.create(img`
            ffffffffff
            f86919191f
            f86911911f
            f86919191f
            f86991191f
            f86919911f
            f86991191f
            f86911191f
            f86911191f
            f86991191f
            f86919911f
            f86991191f
            f86919191f
            f86911911f
            f86919191f
            f86991191f
            f86991191f
            f86919191f
            f86911911f
            f86919191f
            f86991191f
            f86919911f
            f86991191f
            f86911191f
            f86911191f
            f86991191f
            f86919911f
            f86991191f
            f86919191f
            f86911911f
            f86919191f
            f86991191f
            f86991191f
            f86919191f
            f86911911f
            f86919191f
            f86991191f
            f86919911f
            f86991191f
            f86911191f
            f86911191f
            f86991191f
            f86919911f
            f86991191f
            f86919191f
            f86911911f
            f86919191f
            ffffffffff
            `, SpriteKind.Platform)
        platform_2 = sprites.create(img`
            ffffffffffffffffffffffffffffffffffffffffffffffff
            f8888888888888888888888888888888888888888888888f
            f6666666666666666666666666666666666666666666666f
            f9999999999999999999999999999999999999999999999f
            f1119191191911199111919119191119911191911919111f
            f9191911119191911919191111919191191919111191919f
            f1911911119119111191191111911911119119111191191f
            f9199199991991999919919999199199991991999919919f
            f1111111111111111111111111111111111111111111111f
            ffffffffffffffffffffffffffffffffffffffffffffffff
            `, SpriteKind.plattform2)
        Start_3()
        tiles.placeOnTile(Player_A1, Player_POS)
    } else {
    	
    }
    scene.setBackgroundImage(img`
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffcffffffffffcffffffffffffffffffffffffffffcffffffffffcffffffffffffffffffffffffffffcffffffffffcffffffffffffffffffffffffffffcffffffffffcffffffffffffffffffffff
        ffffffffffffffffcbcffffffffffffffffffffcffffffffffffffffcbcffffffffffffffffffffcffffffffffffffffcbcffffffffffffffffffffcffffffffffffffffcbcffffffffffffffffffffc
        fffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffff
        fffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcffffffffffff
        fff3fffffffffffffffffffffbbbfffffffffffffff3fffffffffffffffffffffbbbfffffffffffffff3fffffffffffffffffffffbbbfffffffffffffff3fffffffffffffffffffffbbbffffffffffff
        ffb3bffffffffffffffffffffcbcffffffffffffffb3bffffffffffffffffffffcbcffffffffffffffb3bffffffffffffffffffffcbcffffffffffffffb3bffffffffffffffffffffcbcffffffffffff
        f33333ffffffffffffccfffffffffffffffffffff33333ffffffffffffccfffffffffffffffffffff33333ffffffffffffccfffffffffffffffffffff33333ffffffffffffccffffffffffffffffffff
        ff3b3fffffffffffffccffffffffffffffffffffff3b3fffffffffffffccffffffffffffffffffffff3b3fffffffffffffccffffffffffffffffffffff3b3fffffffffffffccffffffffffffffffffff
        ffbfbfffffffffffffffffffffffffffffcfffffffbfbfffffffffffffffffffffffffffffcfffffffbfbfffffffffffffffffffffffffffffcfffffffbfbfffffffffffffffffffffffffffffcfffff
        fffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcffff
        fffffffffffcffffffffffffffffffffffcffffffffffffffffcffffffffffffffffffffffcffffffffffffffffcffffffffffffffffffffffcffffffffffffffffcffffffffffffffffffffffcfffff
        ffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffff
        fffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fcfffffffffffffffffffffffffcfffffffffffffcfffffffffffffffffffffffffcfffffffffffffcfffffffffffffffffffffffffcfffffffffffffcfffffffffffffffffffffffffcffffffffffff
        fffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffccfffffcffffffffffffffffffffffffffffffffccfffffcffffffffffffffffffffffffffffffffccfffffcffffffffffffffffffffffffffffffffccfffffcffffffffffffffffffffffffff
        ffffffccfffffffffffffcccccccccccffffffffffffffccfffffffffffffcccccccccccffffffffffffffccfffffffffffffcccccccccccffffffffffffffccfffffffffffffcccccccccccffffffff
        ffffffffffffffffccccccccccccccccccccffffffffffffffffffffccccccccccccccccccccffffffffffffffffffffccccccccccccccccccccffffffffffffffffffffccccccccccccccccccccffff
        fffffffffffffccccccccccccccccccccccccccffffffffffffffccccccccccccccccccccccccccffffffffffffffccccccccccccccccccccccccccffffffffffffffccccccccccccccccccccccccccf
        ccfffffffffcccccccccccccccccccccccccccccccfffffffffcccccccccccccccccccccccccccccccfffffffffcccccccccccccccccccccccccccccccfffffffffccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        bbbbbbbbbbbbccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccbbbbbbbb
        bbbbbbbbbbbbbbbbbccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbb3333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb3333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb3333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb3333bbbbbbbbbb
        bbbbbbbbb3333333bbbbbbbbb33cbbbbbbbbbbbbbbbbbbbbb3333333bbbbbbbbb33cbbbbbbbbbbbbbbbbbbbbb3333333bbbbbbbbb33cbbbbbbbbbbbbbbbbbbbbb3333333bbbbbbbbb33cbbbbbbbbbbbb
        bbbbbbb33cccccbb33bbbbbbbccbbccbbbbbbbbbbbbbbbb33cccccbb33bbbbbbbccbbccbbbbbbbbbbbbbbbb33cccccbb33bbbbbbbccbbccbbbbbbbbbbbbbbbb33cccccbb33bbbbbbbccbbccbbbbbbbbb
        bbbbbbbcccbbbbbcccbbbbbbbbccccbbbbbbbbbbbbbbbbbcccbbbbbcccbbbbbbbbccccbbbbbbbbbbbbbbbbbcccbbbbbcccbbbbbbbbccccbbbbbbbbbbbbbbbbbcccbbbbbcccbbbbbbbbccccbbbbbbbbbb
        3bbbbbbbcccccccccbbbbbbbbbbbbbbb333333333bbbbbbbcccccccccbbbbbbbbbbbbbbb333333333bbbbbbbcccccccccbbbbbbbbbbbbbbb333333333bbbbbbbcccccccccbbbbbbbbbbbbbbb33333333
        333bbbbbbbcccccbbbbbbbbbbbbbbb333ccbbbbb333bbbbbbbcccccbbbbbbbbbbbbbbb333ccbbbbb333bbbbbbbcccccbbbbbbbbbbbbbbb333ccbbbbb333bbbbbbbcccccbbbbbbbbbbbbbbb333ccbbbbb
        cc3bbbbbbbbbbbbbbbbbbbbbbbbbbb3cccbbbccccc3bbbbbbbbbbbbbbbbbbbbbbbbbbb3cccbbbccccc3bbbbbbbbbbbbbbbbbbbbbbbbbbb3cccbbbccccc3bbbbbbbbbbbbbbbbbbbbbbbbbbb3cccbbbccc
        cccbbbbbbbbbbbb333bbbbbb3bbbbbcccbbbbbcccccbbbbbbbbbbbb333bbbbbb3bbbbbcccbbbbbcccccbbbbbbbbbbbb333bbbbbb3bbbbbcccbbbbbcccccbbbbbbbbbbbb333bbbbbb3bbbbbcccbbbbbcc
        cccbbbbbbbbbbbb333bbbbbbbbbbbbcccccccccccccbbbbbbbbbbbb333bbbbbbbbbbbbcccccccccccccbbbbbbbbbbbb333bbbbbbbbbbbbcccccccccccccbbbbbbbbbbbb333bbbbbbbbbbbbcccccccccc
        cbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccc
        bbbb3333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb3333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb3333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb3333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbb333333bbb33ddddddddddddddddd33bbbbbbbbbb333333bbb33ddddddddddddddddd33bbbbbbbbbb333333bbb33ddddddddddddddddd33bbbbbbbbbb333333bbb33ddddddddddddddddd33bbbbbbb
        bbb33333ddddddddddddddddddddddddddddd3bbbbb33333ddddddddddddddddddddddddddddd3bbbbb33333ddddddddddddddddddddddddddddd3bbbbb33333ddddddddddddddddddddddddddddd3bb
        dddddddddddddddddddddddddddddddd33333ddddddddddddddddddddddddddddddddddd33333ddddddddddddddddddddddddddddddddddd33333ddddddddddddddddddddddddddddddddddd33333ddd
        dddddddddddddd3333333333ddddddd33dddd33ddddddddddddddd3333333333ddddddd33dddd33ddddddddddddddd3333333333ddddddd33dddd33ddddddddddddddd3333333333ddddddd33dddd33d
        dddddddddddd333ddddddddd33dddddbbbbbbbbddddddddddddd333ddddddddd33dddddbbbbbbbbddddddddddddd333ddddddddd33dddddbbbbbbbbddddddddddddd333ddddddddd33dddddbbbbbbbbd
        ddddddddddd333d3bbbbbbbbd33dddddbbbbbbddddddddddddd333d3bbbbbbbbd33dddddbbbbbbddddddddddddd333d3bbbbbbbbd33dddddbbbbbbddddddddddddd333d3bbbbbbbbd33dddddbbbbbbdd
        ddddddddddd33bbbbbbbbbbbb33dddddddddddddddddddddddd33bbbbbbbbbbbb33dddddddddddddddddddddddd33bbbbbbbbbbbb33dddddddddddddddddddddddd33bbbbbbbbbbbb33ddddddddddddd
        ddddddddddddbbbbbbbbbbbbbbddddddddddddddddddddddddddbbbbbbbbbbbbbbddddddddddddddddddddddddddbbbbbbbbbbbbbbddddddddddddddddddddddddddbbbbbbbbbbbbbbdddddddddddddd
        ddddddddddddd3bbbbbbbbbb3dddddddddddddddddddddddddddd3bbbbbbbbbb3dddddddddddddddddddddddddddd3bbbbbbbbbb3dddddddddddddddddddddddddddd3bbbbbbbbbb3ddddddddddddddd
        d333333ddddddddd333333ddddddddddddddddddd333333ddddddddd333333ddddddddddddddddddd333333ddddddddd333333ddddddddddddddddddd333333ddddddddd333333dddddddddddddddddd
        333333333dddddddddddddddddddddddddddddd3333333333dddddddddddddddddddddddddddddd3333333333dddddddddddddddddddddddddddddd3333333333dddddddddddddddddddddddddddddd3
        33333333dddddddddddddddddddddddddddddddd33333333dddddddddddddddddddddddddddddddd33333333dddddddddddddddddddddddddddddddd33333333dddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddd3333333333333ddddddddddddddddddddddddddd3333333333333ddddddddddddddddddddddddddd3333333333333ddddddddddddddddddddddddddd3333333333333d
        33ddddddddddddddddddddd333dddddddddddd3333ddddddddddddddddddddd333dddddddddddd3333ddddddddddddddddddddd333dddddddddddd3333ddddddddddddddddddddd333dddddddddddd33
        d333ddddddddddddddddd333ddddddddddddddddd333ddddddddddddddddd333ddddddddddddddddd333ddddddddddddddddd333ddddddddddddddddd333ddddddddddddddddd333dddddddddddddddd
        ddd33ddddddddddddddd33dddd3bbbbbbbbbbb3dddd33ddddddddddddddd33dddd3bbbbbbbbbbb3dddd33ddddddddddddddd33dddd3bbbbbbbbbbb3dddd33ddddddddddddddd33dddd3bbbbbbbbbbb3d
        b3dd3ddddddddddddddd3dd3bbbbbbbbbbbbbbbbb3dd3ddddddddddddddd3dd3bbbbbbbbbbbbbbbbb3dd3ddddddddddddddd3dd3bbbbbbbbbbbbbbbbb3dd3ddddddddddddddd3dd3bbbbbbbbbbbbbbbb
        bb333ddddddddddddddd33bbbbbbbbbbbbbbbbbbbb333ddddddddddddddd33bbbbbbbbbbbbbbbbbbbb333ddddddddddddddd33bbbbbbbbbbbbbbbbbbbb333ddddddddddddddd33bbbbbbbbbbbbbbbbbb
        bbb3dddddddddddddddd3bbbbbbbbbbbbbbbbbbbbbb3dddddddddddddddd3bbbbbbbbbbbbbbbbbbbbbb3dddddddddddddddd3bbbbbbbbbbbbbbbbbbbbbb3dddddddddddddddd3bbbbbbbbbbbbbbbbbbb
        b3ddddddddddddddddddd3bbbbbbbbbbbbbbbbbbb3ddddddddddddddddddd3bbbbbbbbbbbbbbbbbbb3ddddddddddddddddddd3bbbbbbbbbbbbbbbbbbb3ddddddddddddddddddd3bbbbbbbbbbbbbbbbbb
        dddddddddddddddddddddddd3bbbbbbbbbbbbb33dddddddddddddddddddddddd3bbbbbbbbbbbbb33dddddddddddddddddddddddd3bbbbbbbbbbbbb33dddddddddddddddddddddddd3bbbbbbbbbbbbb33
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddd3333333333333ddddddddddddddddddddddddddd3333333333333ddddddddddddddddddddddddddd3333333333333ddddddddddddddddddddddddddd3333333333333ddddddddddddddddd
        dddddd333333333333333333333ddddddddddddddddddd333333333333333333333ddddddddddddddddddd333333333333333333333ddddddddddddddddddd333333333333333333333ddddddddddddd
        dddd3333333333333333ddd3333333dddddddddddddd3333333333333333ddd3333333dddddddddddddd3333333333333333ddd3333333dddddddddddddd3333333333333333ddd3333333dddddddddd
        dd3333333333333333333dddddd333333ddddddddd3333333333333333333dddddd333333ddddddddd3333333333333333333dddddd333333ddddddddd3333333333333333333dddddd333333ddddddd
        3333333333333333333333ddddddddddddddd3333333333333333333333333ddddddddddddddd3333333333333333333333333ddddddddddddddd3333333333333333333333333ddddddddddddddd333
        33333333333333333333333333dddddddd33333333333333333333333333333333dddddddd33333333333333333333333333333333dddddddd33333333333333333333333333333333dddddddd333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        `)
    scene.cameraFollowSprite(Player_A1)
    Status_bar_menu_end()
    controller.moveSprite(Player_A1, 70, 0)
    sprites.destroy(Text_v_VI)
    sprites.destroy(TEXT_V_II)
    sprites.destroy(Text_V1)
    sprites.destroy(Text_v_VI)
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile46`, function (sprite, location) {
    game.showLongText("What in the name of god is this, is it a radioactive sandwich! One of the workers must have left his lunch out and the radioactivity of the reactor made it be like this! Fight it by Overlaping with it", DialogLayout.Bottom)
    tiles.setTileAt(location, assets.tile`transparency16`)
    ZAHL_2 = 1
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    Player_A1.vy = -180
    pause(1000)
    Player_A1.ay = 350
    pause(200)
})
function Get_item () {
    if (Zahl == 0) {
        game.showLongText("Congrats to youre 1st item", DialogLayout.Bottom)
    } else if (Zahl == 1) {
        game.showLongText("Congrats to youre 2nd item", DialogLayout.Bottom)
    } else if (Zahl == 2) {
        game.showLongText("Three times the charm congrats to youre third item", DialogLayout.Bottom)
    } else if (Zahl == 3) {
        game.showLongText("Wow 4 items already!", DialogLayout.Bottom)
    } else if (Zahl == 4) {
        game.showLongText("You now have one item for every finger of youre hand, unless you have a mutant hand!", DialogLayout.Bottom)
    } else if (Zahl == 5) {
        game.showLongText("Ok you can stop now, what do you even wnna do with 6 items", DialogLayout.Bottom)
    } else {
        game.showLongText("Congrats you got every item in the game, seems like it was way to easy for you :(", DialogLayout.Bottom)
    }
    pause(100)
    Zahl += 1
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Platform, function (sprite, otherSprite) {
    if (info.life() == 1) {
        Dead_1()
    } else {
        Player_A1.x += -30
        info.changeLifeBy(-1)
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile7`, function (sprite, location) {
    Dead_1()
})
statusbars.onZero(StatusBarKind.Enemy_Health, function (status) {
    End_fight()
})
function Start () {
    Level.value += 1
    tiles.setCurrentTilemap(tilemap`Level1`)
    NPC_1_Mamfred_Monk = sprites.create(img`
        . . . . f f f f f . . . . . . . 
        . . . f b b b 1 1 f . . . . . . 
        . . f d d d d b 1 1 f . . . . . 
        . c d f d d f d b 1 f f . . . . 
        . c d f d d f d b 1 1 1 f . . . 
        c d b b d d d d b 1 b 1 c . . . 
        c d d d d d d d b 1 b 1 c . . . 
        c d c c c d d b 1 1 f c . . . . 
        . f d d d d b c c f f . . . . . 
        . . f f f f f 4 2 8 b f . . . . 
        . . . . f f 1 1 1 1 1 b f . f f 
        . . . f b 1 f 1 1 f 1 b f . 1 f 
        . . f b 1 f 1 1 f 1 1 b f . 1 f 
        . f b c f c b f b b f 1 f f 1 f 
        . f c c f c c f c c b 1 f f f f 
        . . f f f f f f f f f f f f f . 
        `, SpriteKind.NPC_A)
    platform = sprites.create(img`
        ffffffffff
        f86919191f
        f86911911f
        f86919191f
        f86991191f
        f86919911f
        f86991191f
        f86911191f
        f86911191f
        f86991191f
        f86919911f
        f86991191f
        f86919191f
        f86911911f
        f86919191f
        f86991191f
        f86991191f
        f86919191f
        f86911911f
        f86919191f
        f86991191f
        f86919911f
        f86991191f
        f86911191f
        f86911191f
        f86991191f
        f86919911f
        f86991191f
        f86919191f
        f86911911f
        f86919191f
        f86991191f
        f86991191f
        f86919191f
        f86911911f
        f86919191f
        f86991191f
        f86919911f
        f86991191f
        f86911191f
        f86911191f
        f86991191f
        f86919911f
        f86991191f
        f86919191f
        f86911911f
        f86919191f
        ffffffffff
        `, SpriteKind.Platform)
    platform_2 = sprites.create(img`
        ffffffffffffffffffffffffffffffffffffffffffffffff
        f8888888888888888888888888888888888888888888888f
        f6666666666666666666666666666666666666666666666f
        f9999999999999999999999999999999999999999999999f
        f1119191191911199111919119191119911191911919111f
        f9191911119191911919191111919191191919111191919f
        f1911911119119111191191111911911119119111191191f
        f9199199991991999919919999199199991991999919919f
        f1111111111111111111111111111111111111111111111f
        ffffffffffffffffffffffffffffffffffffffffffffffff
        `, SpriteKind.plattform2)
    tiles.placeOnRandomTile(platform_2, assets.tile`myTile13`)
    tiles.placeOnRandomTile(platform, assets.tile`myTile4`)
    tiles.placeOnRandomTile(NPC_1_Mamfred_Monk, assets.tile`myTile16`)
    Player_A1.setImage(img`
        . . . . . . . f f f f f . . . . 
        . . . . . . f b 1 e e e f . . . 
        . . . . . f b 1 e d d d d f . . 
        . . . . f f b e d f d d f d c . 
        . . . f 1 1 1 e d f d d f d c . 
        . . . c 1 b 1 e d d d d e e d c 
        . . . c 1 b 1 e d d c d d d d c 
        . . . . c f 1 1 e d d c c c c c 
        . . . . 5 f f b b e d d d b f . 
        . . . 5 f b b 1 1 f f f f f . . 
        f f 4 f b 1 1 1 8 2 f f . . . . 
        f 1 4 f 1 1 f 1 1 f 1 1 f . . . 
        f 1 4 f 1 1 1 f 1 1 f 1 1 f . . 
        f 1 f f 1 f b b f b c f c b f . 
        f f f f 1 b c c f c c f c c f . 
        . f f f f f f f f f f f f f . . 
        `)
    info.setLife(5)
    scene.setBackgroundImage(img`
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffcffffffffffcffffffffffffffffffffffffffffcffffffffffcffffffffffffffffffffffffffffcffffffffffcffffffffffffffffffffffffffffcffffffffffcffffffffffffffffffffff
        ffffffffffffffffcbcffffffffffffffffffffcffffffffffffffffcbcffffffffffffffffffffcffffffffffffffffcbcffffffffffffffffffffcffffffffffffffffcbcffffffffffffffffffffc
        fffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffff
        fffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcffffffffffff
        fff3fffffffffffffffffffffbbbfffffffffffffff3fffffffffffffffffffffbbbfffffffffffffff3fffffffffffffffffffffbbbfffffffffffffff3fffffffffffffffffffffbbbffffffffffff
        ffb3bffffffffffffffffffffcbcffffffffffffffb3bffffffffffffffffffffcbcffffffffffffffb3bffffffffffffffffffffcbcffffffffffffffb3bffffffffffffffffffffcbcffffffffffff
        f33333ffffffffffffccfffffffffffffffffffff33333ffffffffffffccfffffffffffffffffffff33333ffffffffffffccfffffffffffffffffffff33333ffffffffffffccffffffffffffffffffff
        ff3b3fffffffffffffccffffffffffffffffffffff3b3fffffffffffffccffffffffffffffffffffff3b3fffffffffffffccffffffffffffffffffffff3b3fffffffffffffccffffffffffffffffffff
        ffbfbfffffffffffffffffffffffffffffcfffffffbfbfffffffffffffffffffffffffffffcfffffffbfbfffffffffffffffffffffffffffffcfffffffbfbfffffffffffffffffffffffffffffcfffff
        fffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcffff
        fffffffffffcffffffffffffffffffffffcffffffffffffffffcffffffffffffffffffffffcffffffffffffffffcffffffffffffffffffffffcffffffffffffffffcffffffffffffffffffffffcfffff
        ffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffff
        fffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fcfffffffffffffffffffffffffcfffffffffffffcfffffffffffffffffffffffffcfffffffffffffcfffffffffffffffffffffffffcfffffffffffffcfffffffffffffffffffffffffcffffffffffff
        fffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffccfffffcffffffffffffffffffffffffffffffffccfffffcffffffffffffffffffffffffffffffffccfffffcffffffffffffffffffffffffffffffffccfffffcffffffffffffffffffffffffff
        ffffffccfffffffffffffcccccccccccffffffffffffffccfffffffffffffcccccccccccffffffffffffffccfffffffffffffcccccccccccffffffffffffffccfffffffffffffcccccccccccffffffff
        ffffffffffffffffccccccccccccccccccccffffffffffffffffffffccccccccccccccccccccffffffffffffffffffffccccccccccccccccccccffffffffffffffffffffccccccccccccccccccccffff
        fffffffffffffccccccccccccccccccccccccccffffffffffffffccccccccccccccccccccccccccffffffffffffffccccccccccccccccccccccccccffffffffffffffccccccccccccccccccccccccccf
        ccfffffffffcccccccccccccccccccccccccccccccfffffffffcccccccccccccccccccccccccccccccfffffffffcccccccccccccccccccccccccccccccfffffffffccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        bbbbbbbbbbbbccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccbbbbbbbb
        bbbbbbbbbbbbbbbbbccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbb3333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb3333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb3333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb3333bbbbbbbbbb
        bbbbbbbbb3333333bbbbbbbbb33cbbbbbbbbbbbbbbbbbbbbb3333333bbbbbbbbb33cbbbbbbbbbbbbbbbbbbbbb3333333bbbbbbbbb33cbbbbbbbbbbbbbbbbbbbbb3333333bbbbbbbbb33cbbbbbbbbbbbb
        bbbbbbb33cccccbb33bbbbbbbccbbccbbbbbbbbbbbbbbbb33cccccbb33bbbbbbbccbbccbbbbbbbbbbbbbbbb33cccccbb33bbbbbbbccbbccbbbbbbbbbbbbbbbb33cccccbb33bbbbbbbccbbccbbbbbbbbb
        bbbbbbbcccbbbbbcccbbbbbbbbccccbbbbbbbbbbbbbbbbbcccbbbbbcccbbbbbbbbccccbbbbbbbbbbbbbbbbbcccbbbbbcccbbbbbbbbccccbbbbbbbbbbbbbbbbbcccbbbbbcccbbbbbbbbccccbbbbbbbbbb
        3bbbbbbbcccccccccbbbbbbbbbbbbbbb333333333bbbbbbbcccccccccbbbbbbbbbbbbbbb333333333bbbbbbbcccccccccbbbbbbbbbbbbbbb333333333bbbbbbbcccccccccbbbbbbbbbbbbbbb33333333
        333bbbbbbbcccccbbbbbbbbbbbbbbb333ccbbbbb333bbbbbbbcccccbbbbbbbbbbbbbbb333ccbbbbb333bbbbbbbcccccbbbbbbbbbbbbbbb333ccbbbbb333bbbbbbbcccccbbbbbbbbbbbbbbb333ccbbbbb
        cc3bbbbbbbbbbbbbbbbbbbbbbbbbbb3cccbbbccccc3bbbbbbbbbbbbbbbbbbbbbbbbbbb3cccbbbccccc3bbbbbbbbbbbbbbbbbbbbbbbbbbb3cccbbbccccc3bbbbbbbbbbbbbbbbbbbbbbbbbbb3cccbbbccc
        cccbbbbbbbbbbbb333bbbbbb3bbbbbcccbbbbbcccccbbbbbbbbbbbb333bbbbbb3bbbbbcccbbbbbcccccbbbbbbbbbbbb333bbbbbb3bbbbbcccbbbbbcccccbbbbbbbbbbbb333bbbbbb3bbbbbcccbbbbbcc
        cccbbbbbbbbbbbb333bbbbbbbbbbbbcccccccccccccbbbbbbbbbbbb333bbbbbbbbbbbbcccccccccccccbbbbbbbbbbbb333bbbbbbbbbbbbcccccccccccccbbbbbbbbbbbb333bbbbbbbbbbbbcccccccccc
        cbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccc
        bbbb3333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb3333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb3333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb3333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbb333333bbb33ddddddddddddddddd33bbbbbbbbbb333333bbb33ddddddddddddddddd33bbbbbbbbbb333333bbb33ddddddddddddddddd33bbbbbbbbbb333333bbb33ddddddddddddddddd33bbbbbbb
        bbb33333ddddddddddddddddddddddddddddd3bbbbb33333ddddddddddddddddddddddddddddd3bbbbb33333ddddddddddddddddddddddddddddd3bbbbb33333ddddddddddddddddddddddddddddd3bb
        dddddddddddddddddddddddddddddddd33333ddddddddddddddddddddddddddddddddddd33333ddddddddddddddddddddddddddddddddddd33333ddddddddddddddddddddddddddddddddddd33333ddd
        dddddddddddddd3333333333ddddddd33dddd33ddddddddddddddd3333333333ddddddd33dddd33ddddddddddddddd3333333333ddddddd33dddd33ddddddddddddddd3333333333ddddddd33dddd33d
        dddddddddddd333ddddddddd33dddddbbbbbbbbddddddddddddd333ddddddddd33dddddbbbbbbbbddddddddddddd333ddddddddd33dddddbbbbbbbbddddddddddddd333ddddddddd33dddddbbbbbbbbd
        ddddddddddd333d3bbbbbbbbd33dddddbbbbbbddddddddddddd333d3bbbbbbbbd33dddddbbbbbbddddddddddddd333d3bbbbbbbbd33dddddbbbbbbddddddddddddd333d3bbbbbbbbd33dddddbbbbbbdd
        ddddddddddd33bbbbbbbbbbbb33dddddddddddddddddddddddd33bbbbbbbbbbbb33dddddddddddddddddddddddd33bbbbbbbbbbbb33dddddddddddddddddddddddd33bbbbbbbbbbbb33ddddddddddddd
        ddddddddddddbbbbbbbbbbbbbbddddddddddddddddddddddddddbbbbbbbbbbbbbbddddddddddddddddddddddddddbbbbbbbbbbbbbbddddddddddddddddddddddddddbbbbbbbbbbbbbbdddddddddddddd
        ddddddddddddd3bbbbbbbbbb3dddddddddddddddddddddddddddd3bbbbbbbbbb3dddddddddddddddddddddddddddd3bbbbbbbbbb3dddddddddddddddddddddddddddd3bbbbbbbbbb3ddddddddddddddd
        d333333ddddddddd333333ddddddddddddddddddd333333ddddddddd333333ddddddddddddddddddd333333ddddddddd333333ddddddddddddddddddd333333ddddddddd333333dddddddddddddddddd
        333333333dddddddddddddddddddddddddddddd3333333333dddddddddddddddddddddddddddddd3333333333dddddddddddddddddddddddddddddd3333333333dddddddddddddddddddddddddddddd3
        33333333dddddddddddddddddddddddddddddddd33333333dddddddddddddddddddddddddddddddd33333333dddddddddddddddddddddddddddddddd33333333dddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddd3333333333333ddddddddddddddddddddddddddd3333333333333ddddddddddddddddddddddddddd3333333333333ddddddddddddddddddddddddddd3333333333333d
        33ddddddddddddddddddddd333dddddddddddd3333ddddddddddddddddddddd333dddddddddddd3333ddddddddddddddddddddd333dddddddddddd3333ddddddddddddddddddddd333dddddddddddd33
        d333ddddddddddddddddd333ddddddddddddddddd333ddddddddddddddddd333ddddddddddddddddd333ddddddddddddddddd333ddddddddddddddddd333ddddddddddddddddd333dddddddddddddddd
        ddd33ddddddddddddddd33dddd3bbbbbbbbbbb3dddd33ddddddddddddddd33dddd3bbbbbbbbbbb3dddd33ddddddddddddddd33dddd3bbbbbbbbbbb3dddd33ddddddddddddddd33dddd3bbbbbbbbbbb3d
        b3dd3ddddddddddddddd3dd3bbbbbbbbbbbbbbbbb3dd3ddddddddddddddd3dd3bbbbbbbbbbbbbbbbb3dd3ddddddddddddddd3dd3bbbbbbbbbbbbbbbbb3dd3ddddddddddddddd3dd3bbbbbbbbbbbbbbbb
        bb333ddddddddddddddd33bbbbbbbbbbbbbbbbbbbb333ddddddddddddddd33bbbbbbbbbbbbbbbbbbbb333ddddddddddddddd33bbbbbbbbbbbbbbbbbbbb333ddddddddddddddd33bbbbbbbbbbbbbbbbbb
        bbb3dddddddddddddddd3bbbbbbbbbbbbbbbbbbbbbb3dddddddddddddddd3bbbbbbbbbbbbbbbbbbbbbb3dddddddddddddddd3bbbbbbbbbbbbbbbbbbbbbb3dddddddddddddddd3bbbbbbbbbbbbbbbbbbb
        b3ddddddddddddddddddd3bbbbbbbbbbbbbbbbbbb3ddddddddddddddddddd3bbbbbbbbbbbbbbbbbbb3ddddddddddddddddddd3bbbbbbbbbbbbbbbbbbb3ddddddddddddddddddd3bbbbbbbbbbbbbbbbbb
        dddddddddddddddddddddddd3bbbbbbbbbbbbb33dddddddddddddddddddddddd3bbbbbbbbbbbbb33dddddddddddddddddddddddd3bbbbbbbbbbbbb33dddddddddddddddddddddddd3bbbbbbbbbbbbb33
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddd3333333333333ddddddddddddddddddddddddddd3333333333333ddddddddddddddddddddddddddd3333333333333ddddddddddddddddddddddddddd3333333333333ddddddddddddddddd
        dddddd333333333333333333333ddddddddddddddddddd333333333333333333333ddddddddddddddddddd333333333333333333333ddddddddddddddddddd333333333333333333333ddddddddddddd
        dddd3333333333333333ddd3333333dddddddddddddd3333333333333333ddd3333333dddddddddddddd3333333333333333ddd3333333dddddddddddddd3333333333333333ddd3333333dddddddddd
        dd3333333333333333333dddddd333333ddddddddd3333333333333333333dddddd333333ddddddddd3333333333333333333dddddd333333ddddddddd3333333333333333333dddddd333333ddddddd
        3333333333333333333333ddddddddddddddd3333333333333333333333333ddddddddddddddd3333333333333333333333333ddddddddddddddd3333333333333333333333333ddddddddddddddd333
        33333333333333333333333333dddddddd33333333333333333333333333333333dddddddd33333333333333333333333333333333dddddddd33333333333333333333333333333333dddddddd333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        `)
    info.setScore(1)
    scene.cameraFollowSprite(Player_A1)
    tiles.placeOnRandomTile(Player_A1, assets.tile`myTile3`)
    controller.moveSprite(Player_A1, 70, 0)
    Player_A1.ay = 370
    LIFE_BARRRRR = statusbars.create(4, 50, StatusBarKind.Level_BAR)
    LIFE_BARRRRR.setColor(2, 3)
    LIFE_BARRRRR.setBarBorder(1, 10)
    LIFE_BARRRRR.positionDirection(CollisionDirection.Left)
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile73`, function (sprite, location) {
    Dead_1()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.NPC_B, function (sprite, otherSprite) {
    if (true && Boss_1_dead_yesno == 1) {
        Start_3()
    }
})
controller.combos.attachCombo("AUDB", function () {
    Start_2()
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Level.value + 1 > 2) {
        animation.runImageAnimation(
        Player_A1,
        [img`
            . . . . f f f f f . . . . . . . 
            . . . f e e e 1 b f . . . . . . 
            . . f d d d d e 1 b f . . . . . 
            . c d f d d f d e 1 f f . . . . 
            . c d f d d f d e 1 1 1 f . . . 
            c d e e d d d d e 1 b 1 c . . . 
            c d d d d c d d e 1 b 1 c . f f 
            c c c c c d d d e 1 f c . f 1 f 
            . f b d d d d e b f f 5 . f 1 f 
            . . f f f f f b 1 b b f 5 f 1 f 
            . . . . f 1 1 8 2 1 1 b f f 1 f 
            . . . f 1 f f 1 f 1 1 1 b f f . 
            . . . f 1 f f 1 f 1 1 1 b f . . 
            . . . f c b f c b f f 1 f . . . 
            . . . f c c c c c b b c f . . . 
            . . . . f f f f f f f f f . . . 
            `,img`
            . . . . f f f f f . . . . . . . 
            . . . f e e e 1 b f . . . . . . 
            . . f d d d d e 1 b f . . . . . 
            . c d f d d f d e 1 f . . . . . 
            . c d f d d f d e 1 f f . . . . 
            c d e e d d d d e 1 1 1 f . . . 
            c d d d d c d d e 1 b 1 c . . . 
            c c c c c d d e 1 1 b 1 c . f f 
            . f b d d d e 1 1 f f c . f 1 f 
            . f f f f f f b b b b f 5 f 1 f 
            . f f f f 1 1 1 1 1 1 b f f 1 f 
            f c c f c c f 1 f 1 1 1 b f f . 
            f c b f c b f 1 f 1 1 1 1 f . . 
            f f f f f f f f f f f f 1 f . . 
            . . . . . . . . . f c c c f . . 
            . . . . . . . . . . f f f f . . 
            `,img`
            . . . . f f f f f . . . . . . . 
            . . . f e e e 1 b f . . . . . . 
            . . f d d d d e 1 b f f . . . . 
            . c d d d d d d e 1 1 1 f . . . 
            . c d f d d f d e 1 b 1 c . . . 
            c d d f d d f d e 1 b 1 c . f f 
            c d e e d d d d e 1 f c . f 1 f 
            c d d d d c d e 1 1 f . . f 1 f 
            . f c c c d e 1 1 f f 5 . f 1 f 
            . . f f f f f b b b b f 5 f 1 f 
            . . . . f 1 2 8 1 1 1 b f f f . 
            . . f f 1 f 1 1 f 1 1 1 b f . . 
            . f 1 f f 1 1 f f f 1 1 1 f . . 
            f c b f c c b f f f f f f b f . 
            f c c f c c c f . . f c c c f . 
            . f f f f f f f . . . f f f . . 
            `,img`
            . . . . f f f f f . . . . . . . 
            . . . f e e 1 b b f f f . . . . 
            . . f d d d e 1 1 1 1 1 f . . . 
            . c d d d d d e 1 1 b 1 c . . . 
            . c d d d d d d e 1 b 1 c . . . 
            c d d f d d f d e 1 f c . f f . 
            c d d f d d f d e 1 f . . f 1 f 
            c d e e d d d d e 1 f . . f 1 f 
            . f b d d c d e 1 f f 5 . f 1 f 
            . . f f f d e 1 1 1 1 f 5 f 1 f 
            . . . . f e 1 1 1 1 1 1 f f f . 
            . . . . f f 1 1 1 1 1 b f f . . 
            . . . f 1 f f 1 1 c c c f f . . 
            . . f c b f c c b f f f . . . . 
            . . f c c f c c c f f . . . . . 
            . . . f f f f f f f . . . . . . 
            `,img`
            . . . . f f f f f . . . . . . . 
            . . . f e e e 1 b f . . . . . . 
            . . f d d d d e 1 b f . . . . . 
            . c d f d d f d e b f f . . . . 
            . c d f d d f d e 1 1 1 f . . . 
            c d e e d d d d e 1 b 1 c . . . 
            c d d d d c d d e 1 b 1 c . . . 
            c c c c c d d e 1 1 f c . . . . 
            . f b d d d e b b f f 5 . . . . 
            . . f f f f f 1 1 b b f 5 . . . 
            . . . . f f 2 8 1 1 1 b f 4 f f 
            . . . f 1 1 f 1 1 f 1 1 f 4 1 f 
            . . f 1 1 f 1 1 f 1 1 1 f 4 1 f 
            . f b c f c b f b b f 1 f f 1 f 
            . f c c f c c f c c b 1 f f f f 
            . . f f f f f f f f f f f f f . 
            `],
        200,
        true
        )
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Sandwich, function (sprite, otherSprite) {
    if (ZAHL_2 == 1) {
        fight_count = 1
        Boss_fight_I()
        Enemy_Health.attachToSprite(otherSprite)
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile9`, function (sprite, location) {
    Dead_1()
})
controller.right.onEvent(ControllerButtonEvent.Released, function () {
    if (Level.value + 1 > 2) {
        animation.stopAnimation(animation.AnimationTypes.All, Player_A1)
        Player_A1.setImage(img`
            . . . . . . . f f f f f . . . . 
            . . . . . . f b 1 e e e f . . . 
            . . . . . f b 1 e d d d d f . . 
            . . . . f f b e d f d d f d c . 
            . . . f 1 1 1 e d f d d f d c . 
            . . . c 1 b 1 e d d d d e e d c 
            . . . c 1 b 1 e d d c d d d d c 
            . . . . c f 1 1 e d d c c c c c 
            . . . . 5 f f b b e d d d b f . 
            . . . 5 f b b 1 1 f f f f f . . 
            f f 4 f b 1 1 1 8 2 f f . . . . 
            f 1 4 f 1 1 f 1 1 f 1 1 f . . . 
            f 1 4 f 1 1 1 f 1 1 f 1 1 f . . 
            f 1 f f 1 f b b f b c f c b f . 
            f f f f 1 b c c f c c f c c f . 
            . f f f f f f f f f f f f f . . 
            `)
    }
})
controller.left.onEvent(ControllerButtonEvent.Released, function () {
    if (Level.value + 1 > 2) {
        animation.stopAnimation(animation.AnimationTypes.All, Player_A1)
        Player_A1.setImage(img`
            . . . . f f f f f . . . . . . . 
            . . . f e e e 1 b f . . . . . . 
            . . f d d d d e 1 b f . . . . . 
            . c d f d d f d e b f f . . . . 
            . c d f d d f d e 1 1 1 f . . . 
            c d e e d d d d e 1 b 1 c . . . 
            c d d d d c d d e 1 b 1 c . . . 
            c c c c c d d e 1 1 f c . . . . 
            . f b d d d e b b f f 5 . . . . 
            . . f f f f f 1 1 b b f 5 . . . 
            . . . . f f 2 8 1 1 1 b f 4 f f 
            . . . f 1 1 f 1 1 f 1 1 f 4 1 f 
            . . f 1 1 f 1 1 f 1 1 1 f 4 1 f 
            . f b c f c b f b b f 1 f f 1 f 
            . f c c f c c f c c b 1 f f f f 
            . . f f f f f f f f f f f f f . 
            `)
    }
})
function THE_REAL_START () {
    scene.setBackgroundImage(img`
        eeeee2222222222222222222222222222222222ee2222ee2222ee2222222eeeee2222222222222222222222222222222222ee22222eeee222ee2eeeee2222222222222222222222222222222222ee222
        222eeeee22222222222222222222222222222eee2222eeee2222ee222222222eeeee22222222222222222222222222222eee2222eeeee222ee22222eeeee22222222222222222222222222222eee2222
        222222eeeeeee222222222222222222222eeee22222eeeeee2222eee2222222222eeeeeee222222222222222222222eeee22222eeee2222ee222222222eeeeeee222222222222222222222eeee22222e
        222222222eeeeeeeeeeeeee2222222eeeee222222eeee22eee2222eeee22222222222eeeeeeeeeeeeee2222222eeeee222223eeee22222eeee22222222222eeeeeeeeeeeeee2222222eeeee222222eee
        e222222222222222222222222222eeee2222222eeee22222eef22222eeeee222222222222222222222222222eeee2333333eeee22222efe2eeeee222222222222222222222222222eeee2222222eeee2
        eeeeeeee22222222222222222222222222222eee2222222eeeefe222222eeeeeeeee22222222222222333333333333322eee2222222efe22222eeeeeeeee22222222222222222222222222222eee2222
        2222eeeeeeeee222222222222222222222eeee2222222eeeeeeeffe222222222eeeeeeeee222223333333333322222eeee2223322effeee222322222eeeeeeeee222222222222222222222eeee222222
        2223322222222222222222222222222eeee2222222eeeeeeee222efffe222222222222222222222222222222222eeee2233332efffe22eeeee233333222222222222222222222222222eeee2222222ee
        2222233332222222222222222222222222222222eeeeeeeee22222eefffe2222222222222222222222222222222233333332efffee22222eeeee2233333333333333333332222222222222222222eeee
        eeee22233333333333333332222222222222eeeeee222222222eeeee22ffffee22222222223333333333333333333332eeffff22eeeee22222eeeeee23333333333333222222222222222222eeeeeeee
        eeeeeeeeee233333333332222222222eeeeeee2222222222eeeee2222ffeefffffffee2222222222223333333332fffffffeeff2222eeeee222222eeeeeeee222222222222222222222eeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee22eeeeeeee2222eee222222ffeeeeeeeeeeffffffffffffffffffffffffeeeeeeeeeeff222222eee2222eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeee22222222222222ee22222222222222222222222222effeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffe22222222222222222222222222ee22222222222222eeeeeeeeeee
        eeeeeeeeee22222222222222222eeee2222222222222222222efffeeeeeeeeeeeeeeeeee2eeeeeeeeeeeeeeeeee2eeeeeeeeeeeeeefffe2222222222222222222eeee22222222222222222eeeeeeeeee
        eeeeeeeeee222222222222222222eeeeeeee222222222eeefffeeeeeeeeeeeeeeeeeeeee222222eeeeeeeeee2222eeeeeeeeeeeeeeeeefffeee222222222eeeeeeee222222222222222222eeeeeeeeee
        eeeeeeeee2222222222222222222eeeeeeeeeeeeeeeeffffeeeeeeeeeeeeeeeeeeeeeeee22222222222222222222ee2eeeeeeeeeeeeeeeeeffffeeeeeeeeeeeeeeee2222222222222222222eeeeeeeee
        eeeeeeeee2222222222222222222ee2222effffffffffffeeeeeeeeeeeeeeeeeeeeeeeee22222222222222222222ee22eeeeeeeeeeeeeeeefffffffffffffe2222ee2222222222222222222eeeeeeeee
        eeeeeeee22e22222222222222222ee2222eeee2efffffffeeeeeeeeeeeeeeeeeeeee22ee22222222222222222222e222eeeeeeeeeeeeeeeeffffffffe2eeee2222ee22222222222222222e22eeeeeeee
        eeeeeeee2222222222222222222ee22222ee22eeffffffeeeeeeeeeeeeeeeeeeeeee22ee22222222222222222222e222eeeeeeeeeeeeeeeeffffffffee22ee22222ee2222222222222222222eeeeeeee
        eeeeeeee2e2222222222222222eee22222ee22efffffffeeeeeeeeeeeeeeeeeeeeee22ee22222222222222222222e222eeeeeeeeeeeeeeeefffffffffe22ee22222eee2222222222222222e2eeeeeeee
        eeeeeee22e2222222222222222ee222222e22eefffffffeeeeeeeeeeeeeeeeeeeeee22ee22222222222222222222e222eeeeeeeeeeeeeeeefffffffffee22e222222ee2222222222222222e22eeeeeee
        eeeeeee22e222222222222222ee222222ee22effffffffeeeeeeeeeeeeeeeeee2eee22ee22222222222222222222e222eeee2eeeeeeeeeeeefffffffffe22ee222222ee222222222222222e22eeeeeee
        eeeeee22e2222222222222222ee222222e22eeffffffffeeeeeeeeeeeeeeeeee2eee22ee22222222222222222222e2222eee2eeeeeeeeeeeefffffffffee22e222222ee2222222222222222e22eeeeee
        eeeeee22e222222222222222ee222222ee2eeeffffffffeeeeeeeeeeeeeeeeee2ee222e222222222222222222222e2222eee2eeeeeeeeeeeefffffffffe3e2ee222222ee222222222222222e22eeeeee
        eeeee22ee222222222222222ee22222ee22eefffffffffeeeeeeeeeeeeeeeeee2ee222e2222222222222222222222e222eee2eeeeeeeeeeeeffffffffffe322ee22222ee222222222222222ee22eeeee
        eeeee22e222222222222222ee222222ee2eeeffffffffeeeeeeeeeeeeeeeeee22ee222e2222222222222222222222e222eee2eeeeeeeeeeeeffffffffffe3e2ee222222ee222222222222222e22eeeee
        eeee22ee222222222222222e222222ee22eefffffffffeeeeeeeeeeeeeeeeee22ee222e2222222222222222222222e222eee22eeeeeeeeeeeeffffffffffe322ee222222e222222222222222ee22eeee
        eeee22ee22e22222222222ee22222ee22eeffffffffffeeeeeeeeeeeeeeeeee22ee222e2222222222222222222222e222eeee2eeeeeeeeeeeefffffffffff3322ee22222ee22222222222e22ee22eeee
        eeee2ee222222222222222e222222ee32eeffffffffffeeeeeeeeeeeeeeeeee22ee222e2222222222222222222222e2222eee2eeeeeeeeeeeefffffffffffe332ee222222e222222222222222ee2eeee
        eee22ee22e22222222222e222222ee32eeffffffeffffeeeeeeeeeeeeeeeeee22ee222e2222222222222222222222e2222eee2eeeeeeeeeeeeffffffffffff3322ee222222e22222222222e22ee22eee
        eee2ee222e22222222222e22222ee23eeeffffffeffffeeeeeeeeeeeeeeeeee22ee222e2222222222222222222222e2222eee2eeeeeeeeeeeeffffffffffffe3322ee22222e22222222222e222ee2eee
        ee22ee22e22222222222e222222ee32eefffffffefffeeeeeeeeeeeeeeeeeee22ee222e2222222222222222222222e2222eee2eeeeeeeeeeeeeffffffffffffe332ee222222e22222222222e22ee22ee
        ee2eee2ee2222222222e222222ee33eeefffffffefffeefeeeeeeeeeeeeeee222ee22ee2222222222222222222222e2222eee22eeeeeeeeeeeeffffffffffffe3322ee222222e2222222222ee2eee2ee
        eeeee22ee2222222222e22222ee33eeeffffffffffffeefeeeeeeeeeeeeeee22eee22ee2222222222222222222222e2222eee22eeeeeeeeeeeefffffffffffffe3322ee22222e2222222222ee22eeeee
        eeeee2ee2222222222222222eee33eeffffffffeffffeefeeeeeeeeeeeeeee22eee22ee2222222222222222222222e2222eee22eeeeeeeeeeeefeffffffffffffe332eee2222222222222222ee2eeeee
        eeee22ee2222222222222222ee33eeeffffffffeffffeefeeeeeeeeeeeeeee22ee222ee2222222222222222222222e2222eee22eeeeeeeeeeeefeffffefffffffe3332ee2222222222222222ee22eeee
        eeee2ee2222222222222222ee33eeefffffffffeffffeefeeeeeeeeeeeeeee22ee222e22222222222222222222222e2222eee22eeeeeeeeeeeeeeffffeffffffffe3322ee2222222222222222ee2eeee
        eeee2ee222222222222222ee333eeffffffffffefffeeeeeeeeeeeeeeeeeee22ee222e22222222222222222222222e2222eee22eeeeeeeeeeeeeeefffefffffffffe3322ee222222222222222ee2eeee
        eee2ee2222222222222222ee33eeeffffffffffefffeeeeeeeeeeeeeeeeeee22ee222e22222222222222222222222e22222ee22eeeeeeeeeeeeeeefffefffffffffee332ee2222222222222222ee2eee
        eee2ee222222222222222ee33eeefffffffffffefffeefeeeeeeeeeeeeeeee22ee222e22222222222222222222222ee2222eee2eeeeeeeeeeeeeeefffeffffffffffe3332ee222222222222222ee2eee
        ee2ee2222222222222222e33eeefffffffffffeefffeefeeeeeeeeeeeeeee222ee222e22222222222222222222222ee2222eee22eeeeeeeeeeeeeeffffeffffffffffe3322e2322222222222222ee2ee
        ee2ee222222222222232e333eeffffffffffffeefffeefeeeeeeeeeeeeeee22eee222e22222222222222222222222ee2222eee22eeeeeeeeeeeeeeefffefffffffffffe3322e322222222222222ee2ee
        e2ee2222222222222322e33eeeffffffffffffeefffeefeeeeeeeeeeeeeee22ee2222e22222222222222222222222ee2222eee22eeeeeeeeeeeeeeefffefffffffffffee332e2322222222222222ee2e
        e2ee222222222222332e33eeefffffffffffffeefffeefeeeeeeeeeeeeeee22ee2222e22222222222222222222222ee2222eee22eeeeeeeeeeeeeeefffeffffffffffffe3322e322222222222222ee2e
        eee222222222222332e33eeeffffffffffffffeeffeeeeeeeeeeeeeeeeeee22ee2222222222222222222222222222ee2222eee22eeeeeeeeeeeeeeefffefffffffffffffe3322e322222222222222eee
        eee222222222222322332eefffffffffffffffefffeefeeeeeeeeeeeeeeee22ee222222222ff22222222222ff2222ee2222eee22eeeeeeeeeeeeeeeeffeefffffffffffffe3322322222222222222eee
        ee222222222222332333eeeffffffffffffffeefffeefeeeeeeeeeeeeeee222ee222222222fdf222222222f4f22222e2222eee22eeeeeeeeeeeeeeeeffeefffffffffffffee3223322222222222222ee
        ee22222222222332233eeefffffffffffffffeefffeefeeeeeeeeee2eeee222ee222222222f5df2222222f44f22222e2222eee22eeeeeeeeeeeeeeeeffeeffffffffffffffee322322222222222222ee
        e22222222222332233eeeffffffffffffffffeefffeefeeeeeeeeee2eeee22eee222222222f55df22222f445f22222e2222eee22eeeeeeeeeeeeeeeefffefffffffffffffffe3323322222222222222e
        e22222222222332332eefffffffffffffffffeefffeefeeeeeeeeeeeeeee22eee222222222f511df222f4455f22222e2222eeee2eeeeeeeeeeeeeeeefffeefffffffffffffffe322322222222222222e
        22222e22222332232eeefffffffffffffffffeefffeefeeeeeeeee2eeeee22ee2222222222f5115df2f44555f22222e22222eee22eeeeeeeeeeeeeeeeffeefffffffffffffffeee23322222222e22222
        22222e2222332232eeeffffffffffffffffffeeffeefeeeeeeeeee2eeeee22ee2222222222f555555f445555f22222e22222eee22eeeeeeeeeeeeeeeeffeeffffffffffffffffeee2322222222e22222
        222222222332222eeeffffffffffffffffffeefffeefeeeeeeeeee2eeee222ee2222222222f5555554455554f22222e22222eee22eeeeeeeeeeeeeeeeffeefffffffffffffffffeee332222222222222
        2222e222233222eeefffffffffffffffffffeefffeefeeeeeeeeee2eeee222ee2222222222f5555555555554f22222e22222eee22eeeeeeeeeeeeeeeefffeffffffffffffffffffeee322222222e2222
        2222e222332222eeefffffffffffffffffffeefffeefeeeeeeeeee2eeee222ee2222222222f5555555555554f22222e22222eee22eeeeeeeeeeeeeeeefffeefffffffffffffffffeee332222222e2222
        222e222332222eeeffffffffffffffffffffeefffeefeeeeeeeee22eeee222ee2222222222f5555555555544f22222e22222eee22eeeeeeeeeeeeeeeefffeeffffffffffffffffffeee322222222e222
        222e22232e22eeefffffffffffffffffffffeefffeefeeeeeeeee2eeeee22eee2222222222f5555f455f5544f22222222222eee22eeeeeeeeeeeeeeeeeffeefffffffffffffffffffee332e22222e222
        222e22222e2eeeffffffffffffffffffffffeefffefeeeeeeeeee2eeeee22ee22222222222f5555ff4ff5544f22222222222eee22eeeeeeeeeeeeeeeeeffeeffffffffffffffffffffee32e22222e222
        22ee2222e2eeeffffffffffffffffffffffeeffffefeeeeeeeeee2eeee222ee22222222222f5555f2f2f5544f22222222222eee22eeeeeeeeeeeeeeeeefffefffffffffffffffffffffee32e2222ee22
        22e22222e2eeeffffffffffffffffffffffeeffffefeeeeeeeee22eeee222ee22222222222f5555f222f5544f22222222222eee222eeeeeeeeeeeeeeeefffeeffffffffffffffffffffee32e22222e22
        22e2222eeeeefffffffffffffffffffffffeefffeefeeeeeeeee22eeee222ee22222222222f5555f222f4444f22222222222eee222eeeeeeeeeeeeeeeefffeefffffffffffffffffffffeeeee2222e22
        2ee2222eeeeffffffffffffffffffffffffeefffeefeeeeeeeee22eeee222ee22222222222ffffff222ffffff22222222222eeee22e2eeeeeeeeeeeeeefffeeffffffffffffffffffffffeeee2222ee2
        2e2222eeeefffffffffffffffffffffffffeefffefeeeeeeeeef2feeee222ee22f2f22222222222222222222222222222222eeee22eeeeeeeeeeeeeeeeeffeefffffffffffffffffffffffeeee2222e2
        2e222eee2effffffffffffffffffffffffeeefffefeeeeeeeef5f5fee222eee2f5f5f2222222222222222222222222222222eeee22ee2eeeeeeeeeeeeeefffeeffffffffffffffffffffffe2eee222e2
        2e222eee2effffffffffffffffffffffffeeffffefeeeeeeeef5f5fee222ee22f5f5f2222222222222222222222222222222eeee22ee2eeeeeeeeeeeeeefffeeffffffffffffffffffffffe2eee222e2
        ee22eeee2effffffffffffffffffffffffeeffffefeeeeeeeeef2feee222ee222fef222222222222222222222222222e22222eee22ee2eeeeeeeeeeeeeefffeeffffffffffffffffffffffe2eeee22ee
        ee22eee22effffffffffffffffffffffffeeffffefeeeeeeeee22eefffffffff22e2fff222222222222ffffffffff22e22222eee22ee2eeeeeeeeeeeeeefffeeffffffffffffffffffffffe22eee22ee
        eeeeee22eefffffffff55555ffffffffffeeffffeeeeeeeeeee22eef5555555f22e2f5f222222222222f55555ff5f22e22222eee22ee2eeeeeeeeeeeeeeeffeeffffffffffffffffffffffee22eeeeee
        eeeee222effffffffff5fff5ffffffffffeeffffeeeeeeeeeee2eeef5fffff5f22e2f5f222222222222f5fff5ff5f22e22222eee222e22eeeeeeeeeeeeeefffeeffffffffffffffffffffffe222eeeee
        2222222eeffffffffff5fff5fffffffffeeefffeeeeeeeeeee22eeef5f22ef5f22e2f5f222222222222f5f2f5ff5f22e22222eee222e22eeeeeeeeeeeeeefffeeffffffffffffffffffffffee2222222
        222222eefffffffffff5fff5fffffffffeeffffeeeeeeeeeee22eeef5f22ef5f22eff5ff22222222222f5fff5ff5f22e22222eee222ee2eeeeeeeeeeeeeefffeefffffffffffffffffffffffee222222
        22222eeefffffffffff55555fffffffffffffffffffffffffff2eeef5fffff5f22ef555ffffffff2222f55555ff5f22fffffffffff2efffeeeeeeeeeeeeeeffeefffffffffffffffffffffffeee22222
        222eeeeefffffffffff55fffff555ff55555ff55555ff55555f2eeef5555555f22ef555ff55555f2222f55fffff5f22f555555ff5f2ef5feeeeeeeeeeeeeefffeeffffffffffffffffffffffeeeee222
        eeee2eeeeffffffffff55fffff5ffff5fff5ff5ffffff5fffffeeeef5fffff5f2eeff5fff5fff5f2222f55f222f5f22ffffff5ff5f2ef5feeeeeeeeeeeeeefffeefffffffffffffffffffffeeee2eeee
        222e2ee2effffffffff55fffff5ffff55555ff55555ff55555feeeef5f2eef5f2ee2f5f2f5f2f5f2222f55f222f5ffff555555ff5f2ef5feeeeeeeeeeeeeefffeefffffffffffffffffffffe2ee2e222
        222e2ee2effffffffff55fffff5ffff5ffffffffff5ffffff5feeeef5f2e2f5f2ee2f5f2f5fff5f2222f55f222f5f5ff5ffff5ff5ffff5feeeeeeeeeeeeeefffeefffffffffffffffffffffe2ee2e222
        222e2ee2effffffffff55fffff5ffff555ffff55555ff55555feeeef5f2e2f5f2ee2f5f2f55555f2222f55f222ff5fff555555ff555555feeeeeeeeeeeeeeffffeeffffffffffffffffffffe2ee2e222
        222e2ee2effffffffffffffffffffffffffffffffffffffffffeeeefff2e2fff2ee2fff2fffffff2222ffff2222fff2ffffffffffffff5feeeeeeeeeeeeefffffeeffffffffffffffffffffe2ee2e222
        222e2ee22effffffffffffffffffffffeefffffeeeeeeeee22eeee22222e22222ee2222222222222222222222222222ee2222eeee222f5feeeeeeeeeeeeeeffffeefffffffffffffffffffe22ee2e222
        222e2ee22effffffffffffffffffffffeeffffeeeeeeeeee22eeee22222e22222ee2222222222222222222222222222ee2222eeeee22f5feeeeeeeeeeeeeefffffefffffffffffffffffffe22ee2e222
        222e2eee2effffffffffffffffffffffeeffffeeeeeeeeee22efef22222e22222fef222222222222222222222222222ee2222eeefffff5f2eeeeeeeeeeeeefffffefffffffffffffffffffe2eee2e222
        222e22ee2eefffffffffffffffffffffefffffeeeeeeeee222f5f5f222ee2222f5f5f22222222222222222222222222ee2222eeef55555f2eeeeeeeeeeeeeffffffffffffffffffffffffee2ee22e222
        222e22ee22efffffffffffffffffffffefffffeeeeeeeee22ef5f5f222ee2222f5f5f22222222222222222222222222ee2222eeefffffff2eeeeeeeeeeeeeefffffffffffffffffffffffe22ee22e222
        222e22ee22efffffffffffffffffffffefffffeeeeeeeee22eefef2222ee22222f2f222222222222222222222222222ee2222eeeee22ee22eeeeeeeeeeeeeefffffffffffffffffffffffe22ee22e222
        222e22ee22efffffffffffffffffffffffffffeeeeeeeee22eee222222ee22222e22222222222222222222222222222ee22222eeee222e22eeeeeeefffeeeefffffffffffffffffffffffe22ee22e222
        222e22ee222efffffff55555ffffffffffffffeeeeeeeee22eee222fffffffff2e222ffff2222222222222222222222ee22222eeee222ee2fffeeeef5feeeeefffffffffffffffffffffe222ee22e222
        222e22eee22efffffff5fff5ffffffffffffffeeeeeeee22eeee222f5555555f2e22ff55f2222222222222222222222ee22222eeee222ee2f5ffffef5feeeeefffffffffffffffffffffe22eee22e222
        222e222ee22efffffff5fff5ffffffffffffffeeeeeeee22eeee222f5fffff5f2e22f5fff2222222222222222222222ee22222eeee222ee2f5ff5fef5feeefffffffffffffffffffffffe22ee222e222
        222e222ee22eeffffff5fff5fffffffffffffeeeeeeeee22eee2222f5fe22f5f2ee2f5f2eeee222eeee222eeee22222ee222222eeee22222f5ffffff5ffeeffffffffffffffffffffffee22ee222e222
        222e222ee222effffff55555fffffffffffffffffffffffffffee22f5fffff5feddef5fffffffffffffffeedeffffffffffffffffffffffff5fffff555ffffffffbbbffffffffbfffffe222ee222e222
        222e222ee222ebbffff55fffff555ff55555ff55555ff55555fbeeef555555feddddf555ff55555ff555fedddf55555ff555ff55555ff55555ff5ff555ff55555fbbbbfffffbbbbbfffe222ee222e222
        222ee22ee222eebbbbf55fbbbf5ffff5fff5ff5ffffff5fffffbbddf5fffff5fddddf5ffff5fff5ff5fffddddf5ffffff5ffff5fff5ff5fff5ff5fff5fff5fffffbbbbbbbbbbbbbbbbee222ee22ee222
        222ee22ee2222ebbbbf55fbbbf5ffff55555ff55555ff55555fddddf5fdddf5fddddf5fddf5fdf5ff5fddddddf5fddddf5fddf55555ff5fbf5ff5fbf5fbf55555fbbbbbbbbbbbbbbbbe2222ee22ee222
        2222e222e2222eebbbf55fbbbf5fbbf5ffffffffff5ffffff5fddddf5fffff5fddddf5fddf5fff5ff5fddddddf5ffffff5fddf5ffffff5fff5ff5fbf5fbfffff5fbbbbbbbbbbbbbbbee2222e222e2222
        2222e222ee2222ebbbf55fbbbf5fbbf555fbbf55555ff55555fddddf5555555fddddf5fddf55555ff5fddddddf55555ff5fddf555fddf55555ff5fbf5fbf55555fbbbbbbbbbbbbbbbe2222ee222e2222
        2222e222ee2222ebbbffffbbbfffbbfffffbbffffffffffffffddddfffffffffddddfffddffffffffffddddddffffffffffddfffffddffffffffffbfffbfffffffbbbbbbbbbbbbbbbe2222ee222e2222
        2222e222ee2222eebbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbee2222ee222e2222
        2222e2222e22e22ebbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbe22e22e2222e2222
        222222222e22e22eebbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbee22e22e222222222
        222222222e22e222ebbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbe222e22e222222222
        2222222222e22e22eebbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbee22e22e2222222222
        222222e222e22e222ebbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbe222e22e222e222222
        222222e222222e222eebbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbee222e222222e222222
        222222e2222222e222ebbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbe222e2222222e222222
        222222ee222222e222eebbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbee222e222222ee222222
        2222222e222222e2222ebbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbe2222e222222e2222222
        22222e2e2222222e222eebbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbee222e2222222e2e22222
        22222e2e2222222e222eebbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbee222e2222222e2e22222
        22222e2e22222222e22ebbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbe22e22222222e2e22222
        22222e2ee2222222e22ebbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbe22e2222222ee2e22222
        22222e2ee2222222eeeebbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbeeee2222222ee2e22222
        22222e22e2222222eeebbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbeee2222222e22e22222
        22222ee2e2222222eebbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbee2222222e2ee22222
        22222ee2e222222eebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbee222222e2ee22222
        222222e2ee22222ebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbe22222ee2e222222
        222222e22e2222eebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbee2222e22e222222
        222222e22e22eeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeee22e22e222222
        222222e2eeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeee2e222222
        222222e2ebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbe2e222222
        222222eeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeee222222
        `)
    Level = statusbars.create(100, 5, StatusBarKind.Lvl)
    Level.value = 1
    Level.setColor(9, 15)
    Level.positionDirection(CollisionDirection.Top)
    Player_A1 = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, SpriteKind.Player)
    Level.setBarBorder(1, 8)
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.NPC_A, function (sprite, otherSprite) {
    game.splash("Hello player, how nice you got here in time! I have a task for you, will you do it?", "Sure mr. Monk, what is it you want me to do?")
    game.splash("Bring me the Reactor-remmote-control-antigravity-starter!", "Where is it?")
    game.splash("Its 2 floors up in the technic rooms.", "*what the hell am I supposed to get*")
    Start_2()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Item_III, function (sprite, otherSprite) {
    Letter_Item = 1
    Item = 1
    Get_item()
    sprites.destroy(otherSprite)
})
statusbars.onStatusReached(StatusBarKind.Level_BAR, statusbars.StatusComparison.EQ, statusbars.ComparisonType.Percentage, 0, function (status) {
    game.gameOver(false)
})
scene.onOverlapTile(SpriteKind.Platform, assets.tile`myTile6`, function (sprite, location) {
    platform.setVelocity(0, 100)
})
scene.onOverlapTile(SpriteKind.Platfor_3, assets.tile`myTile29`, function (sprite, location) {
    Platform_3.setVelocity(100, 100)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Press, function (sprite, otherSprite) {
    if (info.life() == 1) {
        Dead_1()
    } else {
        pause(100)
        Player_A1.setImage(img`
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . f f f f f . . . . 
            . . . . . . f b 1 e e e f . . . 
            . . . . . f b 1 e d d d d f . . 
            . . . . f f b e d f d d f d c . 
            . . . f 1 1 1 e d f d d f d c c 
            . . . c 1 b 1 e d d c d d d d c 
            . . . . 5 f f b b e d d d b f . 
            f f 4 5 f b b 1 1 f f f f f . . 
            f 1 4 f 1 1 f 1 1 f 1 1 f f . . 
            f 1 f f 1 f b b f b c f c b f . 
            f f f f 1 b c c f c c f c c f . 
            . f f f f f f f f f f f f f . . 
            `)
        info.changeLifeBy(-1)
        pause(200)
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile49`, function (sprite, location) {
    Dead_1()
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile40`, function (sprite, location) {
    game.splash("So you think you're very smart, you think that this is a special secret but Ooops: METAL PIPE!!!!")
    Metall_Pipe = sprites.create(img`
        . . . . . . . . . . . . . . . . c c c c . 
        . . . . . . . . . . . . . . . c c f f c c 
        . . . . . . . . . . . . . . . c c c c d c 
        . . . . . . . . . . . . . . . c c b b d c 
        . c c c c c c c c c c c c c c c c b b d c 
        c c c c c c c c c c c c c c c c b b b 1 c 
        c f c b b b b b b b b b b b b b b b b 1 c 
        c f c b b b b b b b b b b b b b b b b 1 c 
        c c d d d d d d d d d d d d d d 1 1 1 c . 
        . c c c c c c c c c c c c c c c c c c . . 
        `, SpriteKind.ITEM_I)
    tiles.setTileAt(location, assets.tile`myTile41`)
    tiles.placeOnTile(Metall_Pipe, location)
    Metall_Pipe.follow(Player_A1)
    METTALL_PIPE_ITEM = 1
    Item = 1
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Level.value + 1 > 2) {
        animation.runImageAnimation(
        Player_A1,
        [img`
            . . . . . . . f f f f f . . . . 
            . . . . . . f b 1 e e e f . . . 
            . . . . . f b 1 e d d d d f . . 
            . . . . f f 1 e d f d d f d c . 
            . . . f 1 1 1 e d f d d f d c . 
            . . . c 1 b 1 e d d d d e e d c 
            f f . c 1 b 1 e d d c d d d d c 
            f 1 f . c f 1 e d d d c c c c c 
            f 1 f . 5 f f b e d d d d b f . 
            f 1 f 5 f b b 1 b f f f f f . . 
            f 1 f f b 1 1 2 8 1 1 f . . . . 
            . f f b 1 1 1 f 1 f f 1 f . . . 
            . . f b 1 1 1 f 1 f f 1 f . . . 
            . . . f 1 f f b c f b c f . . . 
            . . . f c b b c c c c c f . . . 
            . . . f f f f f f f f f . . . . 
            `,img`
            . . . . . . . f f f f f . . . . 
            . . . . . . f b 1 e e e f . . . 
            . . . . . f b 1 e d d d d f . . 
            . . . . . f 1 e d f d d f d c . 
            . . . . f f 1 e d f d d f d c . 
            . . . f 1 1 1 e d d d d e e d c 
            . . . c 1 b 1 e d d c d d d d c 
            f f . c 1 b 1 1 e d d c c c c c 
            f 1 f . c f f 1 1 e d d d b f . 
            f 1 f 5 f b b b b f f f f f f . 
            f 1 f f b 1 1 1 1 1 1 f f f f . 
            . f f b 1 1 1 f 1 f c c f c c f 
            . . f 1 1 1 1 f 1 f b c f b c f 
            . . f 1 f f f f f f f f f f f f 
            . . f c c c f . . . . . . . . . 
            . . f f f f . . . . . . . . . . 
            `,img`
            . . . . . . . f f f f f . . . . 
            . . . . . . f b 1 e e e f . . . 
            . . . . f f b 1 e d d d d f . . 
            . . . f 1 1 1 e d d d d d d c . 
            . . . c 1 b 1 e d f d d f d c . 
            f f . c 1 b 1 e d f d d f d d c 
            f 1 f . c f 1 e d d d d e e d c 
            f 1 f . . f 1 1 e d c d d d d c 
            f 1 f . 5 f f 1 1 e d c c c f . 
            f 1 f 5 f b b b b f f f f f . . 
            . f f f b 1 1 1 8 2 1 f . . . . 
            . . f b 1 1 1 f 1 1 f 1 f f . . 
            . . f 1 1 1 f f f 1 1 f f 1 f . 
            . f b f f f f f f b c c f b c f 
            . f c c c f . . f c c c f c c f 
            . . f f f . . . f f f f f f f . 
            `,img`
            . . . . . . . f f f f f . . . . 
            . . . . f f f b b 1 e e f . . . 
            . . . f 1 1 1 1 1 e d d d f . . 
            . . . c 1 b 1 1 e d d d d d c . 
            . . . c 1 b 1 e d d d d d d c . 
            . f f . c f 1 e d f d d f d d c 
            f 1 f . . f 1 e d f d d f d d c 
            f 1 f . . f 1 e d d d d e e d c 
            f 1 f . 5 f f 1 e d c d d b f . 
            f 1 f 5 f 1 1 1 1 e d f f f . . 
            . f f f 1 1 1 1 1 1 e f . . . . 
            . . f f b 1 1 1 1 1 f f . . . . 
            . . f f c c c 1 1 f f 1 f . . . 
            . . . . f f f b c c f b c f . . 
            . . . . . f f c c c f c c f . . 
            . . . . . . f f f f f f f . . . 
            `,img`
            . . . . . . . f f f f f . . . . 
            . . . . . . f b 1 e e e f . . . 
            . . . . . f b 1 e d d d d f . . 
            . . . . f f b e d f d d f d c . 
            . . . f 1 1 1 e d f d d f d c . 
            . . . c 1 b 1 e d d d d e e d c 
            . . . c 1 b 1 e d d c d d d d c 
            . . . . c f 1 1 e d d c c c c c 
            . . . . 5 f f b b e d d d b f . 
            . . . 5 f b b 1 1 f f f f f . . 
            f f 4 f b 1 1 1 8 2 f f . . . . 
            f 1 4 f 1 1 f 1 1 f 1 1 f . . . 
            f 1 4 f 1 1 1 f 1 1 f 1 1 f . . 
            f 1 f f 1 f b b f b c f c b f . 
            f f f f 1 b c c f c c f c c f . 
            . f f f f f f f f f f f f f . . 
            `],
        200,
        true
        )
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile36`, function (sprite, location) {
    Player_A1.vx += -10
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile50`, function (sprite, location) {
    Dead_1()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.NPC_C, function (sprite, otherSprite) {
    if (Nowhere_talkedin_with_us == 0) {
        Nowhere_talkedin_with_us = 1
        game.showLongText("'ello im Nowhere, them call me Nowhere becose Nowhere is in my brain *chuchles arwardly*", DialogLayout.Bottom)
    }
})
function NormalMENU () {
    Statusbar_changes_for_MENU()
    scene.setBackgroundImage(img`
        ccccc8888888888888888888888888888888888cc8888cc8888cc8888888ccccc8888888888888888888888888888888888cc88888cccc888cc8ccccc8888888888888888888888888888888888cc888
        888ccccc88888888888888888888888888888ccc8888cccc8888cc888888888ccccc88888888888888888888888888888ccc8888ccccc888cc88888ccccc88888888888888888888888888888ccc8888
        888888ccccccc888888888888888888888cccc88888cccccc8888ccc8888888888ccccccc888888888888888888888cccc88888cccc8888cc888888888ccccccc888888888888888888888cccc88888c
        888888888cccccccccccccc8888888ccccc888888cccc88ccc8888cccc88888888888cccccccccccccc8888888ccccc88888acccc88888cccc88888888888cccccccccccccc8888888ccccc888888ccc
        c888888888888888888888888888cccc8888888cccc88888ccf88888ccccc888888888888888888888888888cccc8aaaaaacccc88888cfc8ccccc888888888888888888888888888cccc8888888cccc8
        cccccccc88888888888888888888888888888ccc8888888ccccfc888888ccccccccc88888888888888aaaaaaaaaaaaa88ccc8888888cfc88888ccccccccc88888888888888888888888888888ccc8888
        8888ccccccccc888888888888888888888cccc8888888cccccccffc888888888ccccccccc88888aaaaaaaaaaa88888cccc888aa88cffccc888a88888ccccccccc888888888888888888888cccc888888
        888aa88888888888888888888888888cccc8888888cccccccc888cfffc888888888888888888888888888888888cccc88aaaa8cfffc88ccccc8aaaaa888888888888888888888888888cccc8888888cc
        88888aaaa8888888888888888888888888888888ccccccccc88888ccfffc88888888888888888888888888888888aaaaaaa8cfffcc88888ccccc88aaaaaaaaaaaaaaaaaaa8888888888888888888cccc
        cccc888aaaaaaaaaaaaaaaa8888888888888cccccc888888888ccccc88ffffcc8888888888aaaaaaaaaaaaaaaaaaaaa8ccffff88ccccc88888cccccc8aaaaaaaaaaaaa888888888888888888cccccccc
        ccccccccccaaaaaaaaaaa8888888888ccccccc8888888888ccccc8888fffffffffffcc888888888888aaaaaaaaa8fffffffffff8888ccccc888888cccccccc888888888888888888888ccccccccccccc
        ccccccccccccccccccccccccccccccccc88cccccccc8888ccc888888ffffffffffffffffffffffffffffffffffffffffffffffff888888ccc8888ccccccccccccccccccccccccccccccccccccccccccc
        ccccccccccc88888888888888cc88888888888888888888888888cffffffffffffffffffffffffffffffffffffffffffffffffffffc88888888888888888888888888cc88888888888888ccccccccccc
        cccccccccc88888888888888888cccc8888888888888888888cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc8888888888888888888cccc88888888888888888cccccccccc
        cccccccccc888888888888888888cccccccc888888888cccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccc888888888cccccccc888888888888888888cccccccccc
        ccccccccc8888888888888888888ccccccccccccccccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcccccccccccccccc8888888888888888888ccccccccc
        ccccccccc8888888888888888888cc8888cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc8888cc8888888888888888888ccccccccc
        cccccccc88e88888888888888888cc8888cccc8cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc8cccc8888cc88888888888888888c88cccccccc
        cccccccc8888888888888888888cc88888cc88ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc88cc88888cc8888888888888888888cccccccc
        cccccccc8e8888888888888888ccc88888cc88cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc88cc88888ccc8888888888888888c8cccccccc
        ccccccc88e8888888888888888cc888888c88ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc88c888888cc8888888888888888c88ccccccc
        ccccccc88e888888888888888cc888888cc88cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc88cc888888cc888888888888888c88ccccccc
        cccccc88c8888888888888888cc888888c88ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc88c888888cc8888888888888888c88cccccc
        cccccc88c888888888888888cc888888cc8cccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcac8cc888888cc888888888888888c88cccccc
        ccccc88cc888888888888888cc88888cc88ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffca88cc88888cc888888888888888cc88ccccc
        ccccc88c888888888888888cc888888cc8cccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcac8cc888888cc888888888888888c88ccccc
        cccc88cc888888888888888c888888cc88ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffca88cc888888c888888888888888cc88cccc
        cccc88cc88e88888888888cc88888cc88ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffaa88cc88888cc88888888888c88cc88cccc
        cccc8cc888888888888888c888888cca8ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcaa8cc888888c888888888888888cc8cccc
        ccc88cc88e88888888888e888888cca8ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffaa88cc888888c88888888888c88cc88ccc
        ccc8cc888e88888888888e88888cc8acccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcaa88cc88888c88888888888c888cc8ccc
        cc88cc88c88888888888e888888cca8ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcaa8cc888888c88888888888c88cc88cc
        cc8ccc8cc8888888888e888888ccaacccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcaa88cc888888c8888888888cc8ccc8cc
        ccccc88cc8888888888e88888ccaacccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcaa88cc88888c8888888888cc88ccccc
        ccccc8cc8888888888888888cccaaccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcaa8ccc8888888888888888cc8ccccc
        cccc88cc8888888888888888ccaacccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcaaa8cc8888888888888888cc88cccc
        cccc8cc8888888888888888ccaacccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcaa88cc8888888888888888cc8cccc
        cccc8cc888888888888888ccaaaccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcaa88cc888888888888888cc8cccc
        ccc8cc8888888888888888ccaacccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccaa8cc8888888888888888cc8ccc
        ccc8cc888888888888888ccaacccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcaaa8cc888888888888888cc8ccc
        cc8cc8888888888888888caacccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcaa88c8a88888888888888cc8cc
        cc8cc8888888888888a8eaaaccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcaa88ca88888888888888cc8cc
        c8cc8888888888888a88eaacccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccaa8c8a88888888888888cc8c
        c8cc888888888888aa8eaacccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcaa88ea88888888888888cc8c
        ccc888888888888aa8eaacccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcaa88ea88888888888888ccc
        ccc888888888888a88aaaccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcaa88a88888888888888ccc
        cc888888888888aa8aaacccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcca88aa88888888888888cc
        cc88888888888aa88aacccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcca88a88888888888888cc
        c88888888888aa88aacccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcaa8aa88888888888888c
        c88888888888aa8aaaccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffca88a88888888888888c
        88888e88888aa88aacccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccc8aa88888888c88888
        88888e8888aa88aacccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccc8a88888888c88888
        888888888aa8888cccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcccaa8888888888888
        8888e8888aa888cccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccca88888888c8888
        8888e888aa8888cccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcccaa8888888c8888
        888c888aa8888cccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccca88888888c888
        888c888a8e88cccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccaa8c88888c888
        888c88888e8cccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcca8c88888c888
        88cc8888c8cccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccaac8888cc88
        88c88888c8cccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccaac88888c88
        88c8888cccccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccccc8888c88
        8cc8888ccccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcccc8888cc8
        8c8888ccccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcccc8888c8
        8c888ccc8cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc8ccc888c8
        8c888ccc8cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc8ccc888c8
        cc88cccc8cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc8cccc88cc
        cc88ccc88cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc88ccc88cc
        cccccc88ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc88cccccc
        ccccc888cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc888ccccc
        8888888ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc8888888
        888888ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc888888
        88888cccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccc88888
        888cccccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccccc888
        cccc8ccccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcccc8cccc
        888c8cc8cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc8cc8c888
        888c8cc8cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc8cc8c888
        888c8cc8cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc8cc8c888
        888c8cc8cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc8cc8c888
        888c8cc88cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc88cc8c888
        888c8cc88cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc88cc8c888
        888c8ccc8cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc8ccc8c888
        888c88cc8ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc8cc88c888
        888c88cc88cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc88cc88c888
        888c88cc88cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc88cc88c888
        888c88cc88cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc88cc88c888
        888c88cc888cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc888cc88c888
        888c88ccc88cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc88ccc88c888
        888c888cc88cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc88cc888c888
        888c888cc88ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc88cc888c888
        888c888cc888cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc888cc888c888
        888c888cc888cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc888cc888c888
        888cc88cc888ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc888cc88cc888
        888cc88cc8888cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc8888cc88cc888
        8888c888c8888ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc8888c888c8888
        8888c888cc8888cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc8888cc888c8888
        8888c888cc8888cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc8888cc888c8888
        8888c888cc8888ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc8888cc888c8888
        8888c8888c88c88cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc88c88c8888c8888
        888888888c88c88ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc88c88c888888888
        888888888c88c888cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc888c88c888888888
        8888888888c88c88ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc88c88c8888888888
        888888c888c88c888cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc888c88c888c888888
        888888c888888c888ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc888c888888c888888
        888888c8888888c888cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc888c8888888c888888
        888888cc888888c888ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc888c888888cc888888
        8888888c888888c8888cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc8888c888888c8888888
        88888c8c8888888c888ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc888c8888888c8c88888
        88888c8c8888888c888ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc888c8888888c8c88888
        88888c8c88888888c88cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc88c88888888c8c88888
        88888c8cc8888888c88cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc88c8888888cc8c88888
        88888c8cc8888888ccccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcccc8888888cc8c88888
        88888c88c8888888cccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccc8888888c88c88888
        88888cc8c8888888ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc8888888c8cc88888
        88888cc8c888888ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc888888c8cc88888
        888888c8cc88888cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc88888cc8c888888
        888888c88c8888ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc8888c88c888888
        888888c88c88cccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccc88c88c888888
        888888c8cccccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccccc8c888888
        888888c8cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc8c888888
        888888cccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccc888888
        `)
    tiles.setCurrentTilemap(tilemap`level11`)
    Text_v_VI = textsprite.create("Space Monkey Menu", 0, 1)
    tiles.placeOnRandomTile(Text_v_VI, assets.tile`myTile3`)
    sprites.destroy(Player_A1)
    scene.cameraFollowSprite(Text_v_VI)
    scaling.scaleByPixels(Text_v_VI, 10, ScaleDirection.Horizontally, ScaleAnchor.Middle)
    scaling.scaleByPixels(Text_v_VI, 8, ScaleDirection.Vertically, ScaleAnchor.Middle)
    Item_Menu = textsprite.create("Items 'B'")
    tiles.placeOnRandomTile(Item_Menu, assets.tile`myTile4`)
    sprites.destroy(Player_A1)
    sprites.destroy(platform)
    sprites.destroy(NPC_1_Mamfred_Monk)
    sprites.destroy(platform_2)
    sprites.destroy(Press_A1)
    sprites.destroy(radioactive_Sandwich)
    Item_menu_yesno = 0
}
function Boss_fight_I () {
    Statusbar_changes_for_fight()
    ZAHL_2 += 1
    Player_health_in_fight.positionDirection(CollisionDirection.Right)
    Enemy_Health.setBarSize(20, 4)
    turn_toggle = 1
    Fight_Toggle = 1
    if (fight_count == 1) {
        game.showLongText("So this is youre very first fight, to attack you press UP and to heal you press DOWN (only possible if you have healing item), got it? The red bar on the right is youre health and the green bar ontop of youre enemy is its health, you win by getting its health down to 0!", DialogLayout.Bottom)
    } else {
        game.showLongText("I thought that this shoud be youre first fight but if you already know how to fight my entire existence is even more useless", DialogLayout.Bottom)
    }
    Animation_finished = 1
}
scene.onOverlapTile(SpriteKind.Press, assets.tile`myTile29`, function (sprite, location) {
    Press_A1.ay = -100
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile52`, function (sprite, location) {
    Dead_1()
})
function End_fight () {
    sprites.destroy(radioactive_Sandwich, effects.fire, 500)
    Fight_Toggle = 0
    turn_toggle = 0
    Boss_1_dead_yesno = 1
    Sandwich_ITEM = sprites.create(img`
        . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . 
        . 2 2 2 7 6 e 2 2 2 7 6 c c . 
        e 2 4 7 7 7 6 2 4 2 7 7 6 c c 
        2 2 2 4 4 4 4 4 4 4 2 2 2 b c 
        e 4 d d d d d d d d d d c 2 c 
        6 e d d d d d d d d d d 4 2 . 
        6 7 e d d d d d d d f 2 2 2 . 
        . 7 7 e d d d d d f 4 2 . . . 
        . . . 6 e 4 d d c 2 2 2 . . . 
        . . . 6 7 e 4 c 4 2 . . . . . 
        . . . . 7 6 c 4 2 2 . . . . . 
        . . . . . . c c . . . . . . . 
        `, SpriteKind.SANDWICH_ITEM)
    Statusbar_changes_for_normal()
    Sandwich_ITEM.follow(Player_A1)
    tiles.placeOnRandomTile(Sandwich_ITEM, assets.tile`myTile44`)
}
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Fight_Toggle == 1) {
        Health_item_yesno = 1
        Heal_Value = 15
        if (true && turn_toggle == 1) {
            if (Health_item_yesno == 1) {
                Player_health_in_fight.value += Heal_Value
                animation.runImageAnimation(
                Player_A1,
                [img`
                    . . . . . . . f f f f f . . . . 
                    . . . . . . f b 1 e e e f . . . 
                    . . . . . f b 1 e d d d d f . . 
                    . . . . f f 1 e d f d d f d c . 
                    . . . f 1 1 1 e d f d d f d c . 
                    . . . c 1 b 1 e d d d d e e d c 
                    f f . c 1 b 1 e d d c d d d d c 
                    f 1 f . c f 1 e d d d c c c c c 
                    f 1 f . 5 f f b e d d d d b f . 
                    f 1 f 5 f b b 1 b f f f f f . . 
                    f 1 f f b 1 1 2 8 1 1 f . . . . 
                    . f f b 1 1 1 f 1 f f 1 f . . . 
                    . . f b 1 1 1 f 1 f f 1 f . . . 
                    . . . f 1 f f b c f b c f . . . 
                    . . . f c b b c c c c c f . . . 
                    . . . f f f f f f f f f . . . . 
                    `,img`
                    . 2 . 2 . . . f f f f f . . . . 
                    2 2 2 2 4 . f b 1 e e e f . . . 
                    . 2 2 4 . f b 1 e d d d d f . . 
                    . . 4 . f f 1 e d f d d f d c . 
                    . . . f 1 1 1 e d f d d f d c . 
                    . . . c 1 b 1 e d d d d e e d c 
                    f f . c 1 b 1 e d d c d d d d c 
                    f 1 f . c f 1 e d d d c c c c c 
                    f 1 f . 5 f f b e d d d 2 b 2 . 
                    f 1 f 5 f b b 1 b f f 2 2 2 2 4 
                    f 1 f f b 1 1 2 8 1 1 f 2 2 4 . 
                    . 2 f 2 1 1 1 f 1 f f 1 f 4 . . 
                    2 2 2 2 4 1 1 f 1 f f 1 f . . . 
                    . 2 2 4 1 f f b c f b c f . . . 
                    . . 4 f c b b c c c c c f . . . 
                    . . . f f f f f f f f f . . . . 
                    `],
                200,
                false
                )
            }
            turn_toggle = 0
        }
        if (turn_toggle == 0) {
            Player_Damage = randint(0, -10)
            turn_toggle = 1
            Player_health_in_fight.value += Player_Damage
        }
    }
})
function Statusbar_changes_for_MENU () {
    Save_for_statusbar_LIFE_BARRRR = LIFE_BARRRRR.value
    save_for_Level = Level.value
    Level.setColor(0, 0)
    LIFE_BARRRRR.setColor(0, 0)
    Level.setBarBorder(1, 0)
    LIFE_BARRRRR.setBarBorder(1, 0)
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile2`, function (sprite, location) {
    game.showLongText("Welcome to Space Monkey II. use 'A' to jump 'left' and 'right' to move.", DialogLayout.Bottom)
    tiles.setTileAt(location, assets.tile`transparency16`)
})
controller.combos.attachCombo("AUDADU", function () {
    Start_3()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.ITEM_II, function (sprite, otherSprite) {
    Get_item()
    sprites.destroy(otherSprite)
})
controller.menu.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Level.value > 1 && MENU_yes__no == 0) {
        NormalMENU()
        Start_Menu_yesno = 1
        MENU_yes__no = 1
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile61`, function (sprite, location) {
    game.showLongText("You find a very interesting letter, written on a thing you heared of in youre History class when you were a little Monk, Its called paper you think!", DialogLayout.Bottom)
    Letter = sprites.create(img`
        3 3 3 3 3 3 3 b b b b b b b b b b b b 
        3 3 d d d d d d d d d d d d d d d b b 
        3 d 3 3 d d d d d d d d d d d b b d b 
        3 d d d 3 b b d d e d d b b b d d d b 
        3 d d d d d d b e 2 4 b d d d d d d b 
        b d d d d d d d d 2 d d d d d d d d b 
        b d d d d d d d d d d d f d f d d d e 
        b d d d d d d d d d d f d d f d f d e 
        b d d d d d d d d d d d d d d d d d e 
        b b b b b b b b b b b b e e e e e e e 
        `, SpriteKind.Item_III)
    tiles.placeOnTile(Letter, location)
    tiles.setTileAt(location, assets.tile`myTile41`)
    Letter.follow(Player_A1)
    Letter_Item = 1
    Item = 1
})
scene.onOverlapTile(SpriteKind.Platform, assets.tile`myTile4`, function (sprite, location) {
    platform.setVelocity(0, -100)
})
function Start_2 () {
    tiles.setCurrentTilemap(tilemap`Level2`)
    tiles.placeOnRandomTile(Player_A1, assets.tile`myTile18`)
    Press_A1 = sprites.create(img`
        .....ffffff.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        .....fccccf.....
        ffffffffffffffff
        fccccccccccccccf
        fbbddd5bb555555f
        fbd5555b5555554f
        fd555555b555442f
        f555555bb444422f
        fccccccccccccccf
        ffffffffffffffff
        .c.c.c.cc.c.c.c.
        `, SpriteKind.Press)
    tiles.placeOnRandomTile(Press_A1, assets.tile`myTile28`)
    tiles.placeOnRandomTile(platform, assets.tile`myTile4`)
    platform.setImage(img`
        ffffffffff
        fcbcbcbcbf
        fcbcbbcbbf
        fcbcbcbcbf
        fcbccbbcbf
        fcbcbccbbf
        fcbccbbcbf
        fcbcbbbcbf
        fcbcbbbcbf
        fcbccbbcbf
        fcbcbccbbf
        fcbccbbcbf
        fcbcbcbcbf
        fcbcbbcbbf
        fcbcbcbcbf
        fcbccbbcbf
        fcbccbbcbf
        fcbcbcbcbf
        fcbcbbcbbf
        fcbcbcbcbf
        fcbccbbcbf
        fcbcbccbbf
        fcbccbbcbf
        fcbcbbbcbf
        fcbcbbbcbf
        fcbccbbcbf
        fcbcbccbbf
        fcbccbbcbf
        fcbcbcbcbf
        fcbcbbcbbf
        fcbcbcbcbf
        fcbccbbcbf
        fcbccbbcbf
        fcbcbcbcbf
        fcbcbbcbbf
        fcbcbcbcbf
        fcbccbbcbf
        fcbcbccbbf
        fcbccbbcbf
        fcbcbbbcbf
        fcbcbbbcbf
        fcbccbbcbf
        fcbcbccbbf
        fcbccbbcbf
        fcbcbcbcbf
        fcbcbbcbbf
        fcbcbcbcbf
        ffffffffff
        `)
    info.setScore(2)
    Level.value += 1
    tiles.placeOnRandomTile(platform_2, assets.tile`myTile13`)
    platform_2.setImage(img`
        ffffffffffffffffffffffffffffffffffffffffffffffff
        fccccccccccccccccccccccccccccccccccccccccccccccf
        fbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbf
        fccccccccccccccccccccccccccccccccccccccccccccccf
        fbbbcbcbbcbcbbbccbbbcbcbbcbcbbbccbbbcbcbbcbcbbbf
        fcbcbcbbbbcbcbcbbcbcbcbbbbcbcbcbbcbcbcbbbbcbcbcf
        fbcbbcbbbbcbbcbbbbcbbcbbbbcbbcbbbbcbbcbbbbcbbcbf
        fcbccbccccbccbccccbccbccccbccbccccbccbccccbccbcf
        fbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbf
        ffffffffffffffffffffffffffffffffffffffffffffffff
        `)
    radioactive_Sandwich = sprites.create(img`
        . . . . . . e c . . . . . . . 
        . . . 3 3 e b b c . . . . . . 
        . . . 3 e 4 d b b c . . . . . 
        . . . e 4 d d d b b c . . . . 
        3 3 e 4 d d d d d b b c . . . 
        3 e d d d d d d d d b b c . . 
        e 4 d d c 6 d c 6 d d b b c . 
        2 2 2 4 7 4 4 7 4 4 2 2 2 b c 
        e 4 d d 5 d d 5 d d d d c 2 c 
        6 e d b 7 d d d d 6 b d 4 2 . 
        6 7 e d b 7 6 6 6 b f 2 2 2 . 
        . 7 7 e d b 6 b b f 4 2 . . . 
        . . . 6 e 4 b d c 2 2 2 . . . 
        . . . 6 7 e 4 c 4 2 . . . . . 
        . . . . 7 6 c 4 2 2 . . . . . 
        . . . . . . c c . . . . . . . 
        `, SpriteKind.Sandwich)
    tiles.placeOnRandomTile(radioactive_Sandwich, assets.tile`myTile44`)
    animation.runImageAnimation(
    radioactive_Sandwich,
    [img`
        . . . . . . e c . . . . . . . 
        . . . 3 3 e b b c . . . . . . 
        . . . 3 e 4 d b b c . . . . . 
        . . . e 4 d d d b b c . . . . 
        3 3 e 4 d d d d d b b c . . . 
        3 e d d d d d d d d b b c . . 
        e 4 d d c 6 d c 6 d d b b c . 
        2 2 2 4 7 4 4 7 4 4 2 2 2 b c 
        e 4 d d 5 d d 5 d d d d c 2 c 
        6 e d b 7 d d d d 6 b d 4 2 . 
        6 7 e d b 7 6 6 6 b f 2 2 2 . 
        . 7 7 e d b 6 b b f 4 2 . . . 
        . . . 6 e 4 b d c 2 2 2 . . . 
        . . . 6 7 e 4 c 4 2 . . . . . 
        . . . . 7 6 c 4 2 2 . . . . . 
        . . . . . . c c . . . . . . . 
        . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . 
        `,img`
        . . . . . . e c . . . . . . . 
        . . . 3 3 e b b c . . . . . . 
        . . . 3 e 4 d b b c . . . . . 
        . . . e 4 d d d b b c . . . . 
        3 3 e 4 d d d d d b b c . . . 
        3 e d d d d d d d d b b c . . 
        e 4 d d c 6 d c 6 d d b b c . 
        2 2 2 4 7 4 4 7 4 4 2 2 2 b c 
        e 4 d d 5 d d 5 d d d d c 2 c 
        6 e d b 7 d d d d 6 b d 4 2 . 
        6 7 e d b 7 6 6 6 b f 2 2 2 . 
        . 7 7 e d b 6 b b f 4 2 . . . 
        . . . 6 e 4 b d c 2 2 2 . . . 
        . . . 6 7 e 4 c 4 2 . . . . . 
        . . . . 7 6 c 4 2 2 . . . . . 
        . . . . . . c c . . . . . . . 
        . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . 
        `,img`
        . . . . . . e c . . . . . . . 
        . . . 3 3 e b b c . . . . . . 
        . . . 3 e 4 d b b c . . . . . 
        . . . e 4 d d d b b c . . . . 
        3 3 e 4 d d d d d b b c . . . 
        3 e d d d d d d d d b b c . . 
        e 4 d d c 6 d c 6 d d b b c . 
        2 2 2 4 7 4 4 7 4 4 2 2 2 b c 
        e 4 d d 5 d d 5 d d d d c 2 c 
        6 e d b 7 d d d d 6 b d 4 2 . 
        6 7 e d b 7 6 6 6 b f 2 2 2 . 
        . 7 7 e d b 6 b b f 4 2 . . . 
        . . . 6 e 4 b d c 2 2 2 . . . 
        . . . 6 7 e 4 c 4 2 . . . . . 
        . . . . 7 6 c 4 2 2 . . . . . 
        . . . . . . c c . . . . . . . 
        . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . 
        `,img`
        . . . . . . e c . . . . . . . 
        . . . 3 3 e b b c . . . . . . 
        . . . 3 e 4 d b b c . . . . . 
        . . . e 4 d d d b b c . . . . 
        3 3 e 4 d d d d d b b c . . . 
        3 e d d d d d d d d b b c . . 
        e 4 d d c 6 d c 6 d d b b c . 
        2 2 2 4 7 4 4 7 4 4 2 2 2 b c 
        e 4 d d 5 d d 5 d d d d c 2 c 
        6 e d b 7 d d d d 6 b d 4 2 . 
        6 7 e d b 7 6 6 6 b f 2 2 2 . 
        . 7 7 e d b 6 b b f 4 2 . . . 
        . . . 6 e 4 b d c 2 2 2 . . . 
        . . . 6 7 e 4 c 4 2 . . . . . 
        . . . . 7 6 c 4 2 2 . . . . . 
        . . . . . . c c . . . . . . . 
        . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . 
        `,img`
        . . . . . . e c . . . . . . . 
        . . . 3 3 e b b c . . . . . . 
        . . . 3 e 4 d b b c . . . . . 
        . . . e 4 d d d b b c . . . . 
        3 3 e 4 d d d d d b b c . . . 
        3 e d d d d d d d d b b c . . 
        e 4 d d c 6 d c 6 d d b b c . 
        2 2 2 4 7 4 4 7 4 4 2 2 2 b c 
        e 4 d d 5 d d 5 d d d d c 2 c 
        6 e d b 7 d d d d 6 b d 4 2 . 
        6 7 e d b 7 6 6 6 b f 2 2 2 . 
        . 7 7 e d b 6 b b f 4 2 . . . 
        . . . 6 e 4 b d c 2 2 2 . . . 
        . . . 6 7 e 4 c 4 2 . . . . . 
        . . . . 7 6 c 4 2 2 . . . . . 
        . . . . . . c c . . . . . . . 
        . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . 
        `,img`
        . . . . . . . . . . . . . . . 
        . . . . . . e c . . . . . . . 
        . . . 3 3 e b b c . . . . . . 
        . . . 3 e 4 d b b c . . . . . 
        . . . e 4 d d d b b c . . . . 
        3 3 e 4 d d d d d b b c . . . 
        3 e d d d d d d d d b b c . . 
        e 4 d d c 6 d c 6 d d b b c . 
        2 2 2 4 7 4 4 7 4 4 2 2 2 b c 
        e 4 d d 5 d d 5 d d d d c 2 c 
        6 e d b 7 d d d d 6 b d 4 2 . 
        6 7 e d b 7 6 6 6 b f 2 2 2 . 
        . 7 7 e d b 6 b b f 4 2 . . . 
        . . . 6 e 4 b d c 2 2 2 . . . 
        . . . 6 7 e 4 c 4 2 . . . . . 
        . . . . 7 6 c 4 2 2 . . . . . 
        . . . . . . c c . . . . . . . 
        . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . 
        `,img`
        . . . . . . . . . . . . . . . 
        . . . . . . e c . . . . . . . 
        . . . 3 3 e b b c . . . . . . 
        . . . 3 e 4 d b b c . . . . . 
        . . . e 4 d d d b b c . . . . 
        3 3 e 4 d d d d d b b c . . . 
        3 e d d d d d d d d b b c . . 
        e 4 d d c 6 d c 6 d d b b c . 
        2 2 2 4 7 4 4 7 4 4 2 2 2 b c 
        e 4 d d 5 d d 5 d d d d c 2 c 
        6 e d b 7 d d d d 6 b d 4 2 . 
        6 7 e d b 7 6 6 6 b f 2 2 2 . 
        . 7 7 e d b 6 b b f 4 2 . . . 
        . . . 6 e 4 b d c 2 2 2 . . . 
        . . . 6 7 e 4 c 4 2 . . . . . 
        . . . . 7 6 c 4 2 2 . . . . . 
        . . . . . . c c . . . . . . . 
        . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . 
        `,img`
        . . . . . . . . . . . . . . . 
        . . . . . . e c . . . . . . . 
        . . . 3 3 e b b c . . . . . . 
        . . . 3 e 4 d b b c . . . . . 
        . . . e 4 d d d b b c . . . . 
        3 3 e 4 d d d d d b b c . . . 
        3 e d d d d d d d d b b c . . 
        e 4 d d c 6 d c 6 d d b b c . 
        2 2 2 4 7 4 4 7 4 4 2 2 2 b c 
        e 4 d d 5 d d 5 d d d d c 2 c 
        6 e d b 7 d d d d 6 b d 4 2 . 
        6 7 e d b 7 6 6 6 b f 2 2 2 . 
        . 7 7 e d b 6 b b f 4 2 . . . 
        . . . 6 e 4 b d c 2 2 2 . . . 
        . . . 6 7 e 4 c 4 2 . . . . . 
        . . . . 7 6 c 4 2 2 . . . . . 
        . . . . . . c c . . . . . . . 
        . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . 
        `,img`
        . . . . . . . . . . . . . . . 
        . . . . . . e c . . . . . . . 
        . . . 3 3 e b b c . . . . . . 
        . . . 3 e 4 d b b c . . . . . 
        . . . e 4 d d d b b c . . . . 
        3 3 e 4 d d d d d b b c . . . 
        3 e d d d d d d d d b b c . . 
        e 4 d d c 6 d c 6 d d b b c . 
        2 2 2 4 7 4 4 7 4 4 2 2 2 b c 
        e 4 d d 5 d d 5 d d d d c 2 c 
        6 e d b 7 d d d d 6 b d 4 2 . 
        6 7 e d b 7 6 6 6 b f 2 2 2 . 
        . 7 7 e d b 6 b b f 4 2 . . . 
        . . . 6 e 4 b d c 2 2 2 . . . 
        . . . 6 7 e 4 c 4 2 . . . . . 
        . . . . 7 6 c 4 2 2 . . . . . 
        . . . . . . c c . . . . . . . 
        . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . 
        `],
    100,
    true
    )
    Entrance_sign_lvl_3_W_1 = sprites.create(img`
        ........f........
        .......fdf.......
        ......fd4bf......
        .....fd554bf.....
        ....fdff5ffbf....
        ...fdfff5fffbf...
        ..fd5fff5fff4bf..
        ..fd5555f5554bf..
        ..fd555fff554bf..
        ..fd55fffff54bf..
        ..fffffffffffff..
        ......fcccf......
        ......fcccf......
        ......fbbbf......
        ......fbbbf......
        ..fffffffffffff..
        ..fe2222222222f..
        ..fe2122112212f..
        ..fe2212121222f..
        ..fe2112111212f..
        ..feee22222222f..
        ..fffffffffffff..
        ......fcccf......
        ......fbbbf......
        ......fbbbf......
        ......fbcbf......
        ......fcbcf......
        ......fccbf......
        ......fbccf......
        ......fcbcf......
        ......fbccf......
        ......fcccf......
        `, SpriteKind.NPC_B)
    tiles.placeOnRandomTile(Entrance_sign_lvl_3_W_1, assets.tile`myTile45`)
    Entrance_sign_lvl_3_W_1.y += -2
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile62`, function (sprite, location) {
    tiles.placeOnRandomTile(Player_A1, assets.tile`myTile37`)
})
controller.combos.attachCombo("AUUDD", function () {
    Get_item()
})
scene.onOverlapTile(SpriteKind.Platfor_3, assets.tile`myTile44`, function (sprite, location) {
    Platform_3.setVelocity(-100, -100)
})
function Dead_1 () {
    Zahl = randint(1, 7)
    if (Zahl == 6) {
        game.splash("Ouch!")
    } else if (Zahl == 1) {
        game.splash("Uhh!")
    } else if (Zahl == 2) {
        game.splash("Ahhhhhhh")
    } else if (Zahl == 3) {
        game.splash("Damn it")
    } else if (Zahl == 4) {
        game.splash("Ohm!")
    } else if (Zahl == 5) {
        game.splash("Noooo")
    } else {
        game.splash("Get some skil man")
    }
    if (Level.value + 1 == 3) {
        info.setLife(5)
        tiles.placeOnRandomTile(Player_A1, assets.tile`myTile3`)
    }
    if (Level.value + 1 == 4) {
        info.setLife(5)
        tiles.placeOnRandomTile(Player_A1, assets.tile`myTile18`)
    }
    if (Level.value + 1 == 5) {
        info.setLife(5)
        tiles.placeOnRandomTile(Player_A1, assets.tile`myTile47`)
    }
    LIFE_BARRRRR.value += -10
}
function Credits () {
    scene.setBackgroundImage(img`
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        `)
    game.showLongText("Game design by Lucjan    Code by Lucjan  Inspiration from Dudewars               Idea by Konstantin", DialogLayout.Bottom)
}
function Start_3 () {
    tiles.setCurrentTilemap(tilemap`level2`)
    Level.value = 4
    Big_Sandwich = sprites.create(img`
        ....................ccceee...................
        ....................ccceee...................
        ....................ccceee...................
        .................cccbbbbbbeee333333..........
        .................cccbbbbbbeee333333..........
        .................cccbbbbbbeee333333..........
        ..............cccbbbbbbddd444eee333..........
        ..............cccbbbbbbddd444eee333..........
        ..............cccbbbbbbddd444eee333..........
        ...........cccbbbbbbddddddddd444eee..........
        ...........cccbbbbbbddddddddd444eee..........
        ...........cccbbbbbbddddddddd444eee..........
        ........cccbbbbbbddddddddddddddd444eee3333333
        ........cccbbbbbbddddddddddddddd444eee3333333
        ........cccbbbbbbddddddddddddddd444eee3333333
        .....cccbbbbbbddddddddddddddddddddddddeee3333
        .....cccbbbbbbddddddddddddddddddddddddeee3333
        .....cccbbbbbbddddddddddddddddddddddddeee3333
        ..cccbbbbbbdddddd666cccddd666cccdddddd444eeee
        ..cccbbbbbbdddddd666cccddd666cccdddddd444eeee
        ..cccbbbbbbdddddd666cccddd666cccdddddd444eeee
        ccbbb2222222224444447774444447774442222222222
        ccbbb2222222224444447774444447774442222222222
        ccbbb2222222224444447774444447774442222222222
        cc222cccdddddddddddd555dddddd555dddddd444eeee
        cc222cccdddddddddddd555dddddd555dddddd444eeee
        cc222cccdddddddddddd555dddddd555dddddd444eeee
        ..222444dddbbb666dddddddddddd777bbbdddeee6666
        ..222444dddbbb666dddddddddddd777bbbdddeee6666
        ..222444dddbbb666dddddddddddd777bbbdddeee6666
        ..222222222fffbbb666666666777bbbdddeee7776666
        ..222222222fffbbb666666666777bbbdddeee7776666
        ..222222222fffbbb666666666777bbbdddeee7776666
        ........222444fffbbbbbb666bbbdddeee777777....
        ........222444fffbbbbbb666bbbdddeee777777....
        ........222444fffbbbbbb666bbbdddeee777777....
        ........222222222cccdddbbb444eee666..........
        ........222222222cccdddbbb444eee666..........
        ........222222222cccdddbbb444eee666..........
        ..............222444ccc444eee777666..........
        ..............222444ccc444eee777666..........
        ..............222444ccc444eee777666..........
        ..............222222444ccc666777.............
        ..............222222444ccc666777.............
        ..............222222444ccc666777.............
        ....................cccccc...................
        ....................cccccc...................
        ....................cccccc...................
        `, SpriteKind.Boss_II)
    animation.runImageAnimation(
    Big_Sandwich,
    [img`
        .....................cccceee.................
        .....................cccceee.................
        ..................cccbbbbbbbeee3333333.......
        ..................cccbbbbbbbeee3333333.......
        ..................cccbbbbbbbeee3333333.......
        ...............cccbbbbbbbddd444eee3333.......
        ...............cccbbbbbbbddd444eee3333.......
        ...............cccbbbbbbbddd444eee3333.......
        ............cccbbbbbbdddddddddd444eeee.......
        ............cccbbbbbbdddddddddd444eeee.......
        ............cccbbbbbbdddddddddd444eeee.......
        ........ccccbbbbbbdddddddddddddddd4444eee3333
        ........ccccbbbbbbdddddddddddddddd4444eee3333
        ........ccccbbbbbbdddddddddddddddd4444eee3333
        .....cccbbbbbbbddddddddddddddddddddddddddeee3
        .....cccbbbbbbbddddddddddddddddddddddddddeee3
        .....cccbbbbbbbddddddddddddddddddddddddddeee3
        ..cccbbbbbbbdddddd666ccccddd666cccddddddd444e
        ..cccbbbbbbbdddddd666ccccddd666cccddddddd444e
        ..cccbbbbbbbdddddd666ccccddd666cccddddddd444e
        ccbbb2222222222444444777744444477744442222222
        ccbbb2222222222444444777744444477744442222222
        ccbbb2222222222444444777744444477744442222222
        cc222cccddddddddddddd5555dddddd555ddddddd444e
        cc222cccddddddddddddd5555dddddd555ddddddd444e
        cc222cccddddddddddddd5555dddddd555ddddddd444e
        ..222444ddddbbb666ddddddddddddd777bbbbdddeee6
        ..222444ddddbbb666ddddddddddddd777bbbbdddeee6
        ..222444ddddbbb666ddddddddddddd777bbbbdddeee6
        ..2222222222fffbbb6666666666777bbbddddeee7776
        ..2222222222fffbbb6666666666777bbbddddeee7776
        ..2222222222fffbbb6666666666777bbbddddeee7776
        ........2222444fffbbbbbbb666bbbdddeeee777777.
        ........2222444fffbbbbbbb666bbbdddeeee777777.
        ........2222444fffbbbbbbb666bbbdddeeee777777.
        ........2222222222cccddddbbb444eee6666.......
        ........2222222222cccddddbbb444eee6666.......
        ........2222222222cccddddbbb444eee6666.......
        ...............222444cccc444eee7776666.......
        ...............222444cccc444eee7776666.......
        ...............222444cccc444eee7776666.......
        ...............2222224444ccc666777...........
        ...............2222224444ccc666777...........
        ...............2222224444ccc666777...........
        .....................ccccccc.................
        .....................ccccccc.................
        .....................ccccccc.................
        .............................................
        .............................................
        .............................................
        .............................................
        .............................................
        .............................................
        .............................................
        .............................................
        `,img`
        .............................................
        .............................................
        .............................................
        .............................................
        .....................cccceee.................
        .....................cccceee.................
        ..................cccbbbbbbbeee3333333.......
        ..................cccbbbbbbbeee3333333.......
        ..................cccbbbbbbbeee3333333.......
        ...............cccbbbbbbbddd444eee3333.......
        ...............cccbbbbbbbddd444eee3333.......
        ...............cccbbbbbbbddd444eee3333.......
        ............cccbbbbbbdddddddddd444eeee.......
        ............cccbbbbbbdddddddddd444eeee.......
        ............cccbbbbbbdddddddddd444eeee.......
        ........ccccbbbbbbdddddddddddddddd4444eee3333
        ........ccccbbbbbbdddddddddddddddd4444eee3333
        ........ccccbbbbbbdddddddddddddddd4444eee3333
        .....cccbbbbbbbddddddddddddddddddddddddddeee3
        .....cccbbbbbbbddddddddddddddddddddddddddeee3
        .....cccbbbbbbbddddddddddddddddddddddddddeee3
        ..cccbbbbbbbdddddd666ccccddd666cccddddddd444e
        ..cccbbbbbbbdddddd666ccccddd666cccddddddd444e
        ..cccbbbbbbbdddddd666ccccddd666cccddddddd444e
        ccbbb2222222222444444777744444477744442222222
        ccbbb2222222222444444777744444477744442222222
        ccbbb2222222222444444777744444477744442222222
        cc222cccddddddddddddd5555dddddd555ddddddd444e
        cc222cccddddddddddddd5555dddddd555ddddddd444e
        cc222cccddddddddddddd5555dddddd555ddddddd444e
        ..222444ddddbbb666ddddddddddddd777bbbbdddeee6
        ..222444ddddbbb666ddddddddddddd777bbbbdddeee6
        ..222444ddddbbb666ddddddddddddd777bbbbdddeee6
        ..2222222222fffbbb6666666666777bbbddddeee7776
        ..2222222222fffbbb6666666666777bbbddddeee7776
        ..2222222222fffbbb6666666666777bbbddddeee7776
        ........2222444fffbbbbbbb666bbbdddeeee777777.
        ........2222444fffbbbbbbb666bbbdddeeee777777.
        ........2222444fffbbbbbbb666bbbdddeeee777777.
        ........2222222222cccddddbbb444eee6666.......
        ........2222222222cccddddbbb444eee6666.......
        ........2222222222cccddddbbb444eee6666.......
        ...............222444cccc444eee7776666.......
        ...............222444cccc444eee7776666.......
        ...............222444cccc444eee7776666.......
        ...............2222224444ccc666777...........
        ...............2222224444ccc666777...........
        ...............2222224444ccc666777...........
        .....................ccccccc.................
        .....................ccccccc.................
        .....................ccccccc.................
        .............................................
        .............................................
        .............................................
        .............................................
        `,img`
        .............................................
        .............................................
        .............................................
        .............................................
        .....................cccceee.................
        .....................cccceee.................
        ..................cccbbbbbbbeee3333333.......
        ..................cccbbbbbbbeee3333333.......
        ..................cccbbbbbbbeee3333333.......
        ...............cccbbbbbbbddd444eee3333.......
        ...............cccbbbbbbbddd444eee3333.......
        ...............cccbbbbbbbddd444eee3333.......
        ............cccbbbbbbdddddddddd444eeee.......
        ............cccbbbbbbdddddddddd444eeee.......
        ............cccbbbbbbdddddddddd444eeee.......
        ........ccccbbbbbbdddddddddddddddd4444eee3333
        ........ccccbbbbbbdddddddddddddddd4444eee3333
        ........ccccbbbbbbdddddddddddddddd4444eee3333
        .....cccbbbbbbbddddddddddddddddddddddddddeee3
        .....cccbbbbbbbddddddddddddddddddddddddddeee3
        .....cccbbbbbbbddddddddddddddddddddddddddeee3
        ..cccbbbbbbbdddddd666ccccddd666cccddddddd444e
        ..cccbbbbbbbdddddd666ccccddd666cccddddddd444e
        ..cccbbbbbbbdddddd666ccccddd666cccddddddd444e
        ccbbb2222222222444444777744444477744442222222
        ccbbb2222222222444444777744444477744442222222
        ccbbb2222222222444444777744444477744442222222
        cc222cccddddddddddddd5555dddddd555ddddddd444e
        cc222cccddddddddddddd5555dddddd555ddddddd444e
        cc222cccddddddddddddd5555dddddd555ddddddd444e
        ..222444ddddbbb666ddddddddddddd777bbbbdddeee6
        ..222444ddddbbb666ddddddddddddd777bbbbdddeee6
        ..222444ddddbbb666ddddddddddddd777bbbbdddeee6
        ..2222222222fffbbb6666666666777bbbddddeee7776
        ..2222222222fffbbb6666666666777bbbddddeee7776
        ..2222222222fffbbb6666666666777bbbddddeee7776
        ........2222444fffbbbbbbb666bbbdddeeee777777.
        ........2222444fffbbbbbbb666bbbdddeeee777777.
        ........2222444fffbbbbbbb666bbbdddeeee777777.
        ........2222222222cccddddbbb444eee6666.......
        ........2222222222cccddddbbb444eee6666.......
        ........2222222222cccddddbbb444eee6666.......
        ...............222444cccc444eee7776666.......
        ...............222444cccc444eee7776666.......
        ...............222444cccc444eee7776666.......
        ...............2222224444ccc666777...........
        ...............2222224444ccc666777...........
        ...............2222224444ccc666777...........
        .....................ccccccc.................
        .....................ccccccc.................
        .....................ccccccc.................
        .............................................
        .............................................
        .............................................
        .............................................
        `,img`
        .............................................
        .............................................
        .............................................
        .............................................
        .............................................
        .............................................
        .............................................
        .....................cccceee.................
        .....................cccceee.................
        ..................cccbbbbbbbeee3333333.......
        ..................cccbbbbbbbeee3333333.......
        ..................cccbbbbbbbeee3333333.......
        ...............cccbbbbbbbddd444eee3333.......
        ...............cccbbbbbbbddd444eee3333.......
        ...............cccbbbbbbbddd444eee3333.......
        ............cccbbbbbbdddddddddd444eeee.......
        ............cccbbbbbbdddddddddd444eeee.......
        ............cccbbbbbbdddddddddd444eeee.......
        ........ccccbbbbbbdddddddddddddddd4444eee3333
        ........ccccbbbbbbdddddddddddddddd4444eee3333
        ........ccccbbbbbbdddddddddddddddd4444eee3333
        .....cccbbbbbbbddddddddddddddddddddddddddeee3
        .....cccbbbbbbbddddddddddddddddddddddddddeee3
        .....cccbbbbbbbddddddddddddddddddddddddddeee3
        ..cccbbbbbbbdddddd666ccccddd666cccddddddd444e
        ..cccbbbbbbbdddddd666ccccddd666cccddddddd444e
        ..cccbbbbbbbdddddd666ccccddd666cccddddddd444e
        ccbbb2222222222444444777744444477744442222222
        ccbbb2222222222444444777744444477744442222222
        ccbbb2222222222444444777744444477744442222222
        cc222cccddddddddddddd5555dddddd555ddddddd444e
        cc222cccddddddddddddd5555dddddd555ddddddd444e
        cc222cccddddddddddddd5555dddddd555ddddddd444e
        ..222444ddddbbb666ddddddddddddd777bbbbdddeee6
        ..222444ddddbbb666ddddddddddddd777bbbbdddeee6
        ..222444ddddbbb666ddddddddddddd777bbbbdddeee6
        ..2222222222fffbbb6666666666777bbbddddeee7776
        ..2222222222fffbbb6666666666777bbbddddeee7776
        ..2222222222fffbbb6666666666777bbbddddeee7776
        ........2222444fffbbbbbbb666bbbdddeeee777777.
        ........2222444fffbbbbbbb666bbbdddeeee777777.
        ........2222444fffbbbbbbb666bbbdddeeee777777.
        ........2222222222cccddddbbb444eee6666.......
        ........2222222222cccddddbbb444eee6666.......
        ........2222222222cccddddbbb444eee6666.......
        ...............222444cccc444eee7776666.......
        ...............222444cccc444eee7776666.......
        ...............222444cccc444eee7776666.......
        ...............2222224444ccc666777...........
        ...............2222224444ccc666777...........
        ...............2222224444ccc666777...........
        .....................ccccccc.................
        .....................ccccccc.................
        .....................ccccccc.................
        .............................................
        `,img`
        .............................................
        .............................................
        .............................................
        .....................cccceee.................
        .....................cccceee.................
        ..................cccbbbbbbbeee3333333.......
        ..................cccbbbbbbbeee3333333.......
        ..................cccbbbbbbbeee3333333.......
        ...............cccbbbbbbbddd444eee3333.......
        ...............cccbbbbbbbddd444eee3333.......
        ...............cccbbbbbbbddd444eee3333.......
        ............cccbbbbbbdddddddddd444eeee.......
        ............cccbbbbbbdddddddddd444eeee.......
        ............cccbbbbbbdddddddddd444eeee.......
        ........ccccbbbbbbdddddddddddddddd4444eee3333
        ........ccccbbbbbbdddddddddddddddd4444eee3333
        ........ccccbbbbbbdddddddddddddddd4444eee3333
        .....cccbbbbbbbddddddddddddddddddddddddddeee3
        .....cccbbbbbbbddddddddddddddddddddddddddeee3
        .....cccbbbbbbbddddddddddddddddddddddddddeee3
        ..cccbbbbbbbdddddd666ccccddd666cccddddddd444e
        ..cccbbbbbbbdddddd666ccccddd666cccddddddd444e
        ..cccbbbbbbbdddddd666ccccddd666cccddddddd444e
        ccbbb2222222222444444777744444477744442222222
        ccbbb2222222222444444777744444477744442222222
        ccbbb2222222222444444777744444477744442222222
        cc222cccddddddddddddd5555dddddd555ddddddd444e
        cc222cccddddddddddddd5555dddddd555ddddddd444e
        cc222cccddddddddddddd5555dddddd555ddddddd444e
        ..222444ddddbbb666ddddddddddddd777bbbbdddeee6
        ..222444ddddbbb666ddddddddddddd777bbbbdddeee6
        ..222444ddddbbb666ddddddddddddd777bbbbdddeee6
        ..2222222222fffbbb6666666666777bbbddddeee7776
        ..2222222222fffbbb6666666666777bbbddddeee7776
        ..2222222222fffbbb6666666666777bbbddddeee7776
        ........2222444fffbbbbbbb666bbbdddeeee777777.
        ........2222444fffbbbbbbb666bbbdddeeee777777.
        ........2222444fffbbbbbbb666bbbdddeeee777777.
        ........2222222222cccddddbbb444eee6666.......
        ........2222222222cccddddbbb444eee6666.......
        ........2222222222cccddddbbb444eee6666.......
        ...............222444cccc444eee7776666.......
        ...............222444cccc444eee7776666.......
        ...............222444cccc444eee7776666.......
        ...............2222224444ccc666777...........
        ...............2222224444ccc666777...........
        ...............2222224444ccc666777...........
        .....................ccccccc.................
        .....................ccccccc.................
        .....................ccccccc.................
        .............................................
        .............................................
        .............................................
        .............................................
        .............................................
        `,img`
        .....................cccceee.................
        .....................cccceee.................
        ..................cccbbbbbbbeee3333333.......
        ..................cccbbbbbbbeee3333333.......
        ..................cccbbbbbbbeee3333333.......
        ...............cccbbbbbbbddd444eee3333.......
        ...............cccbbbbbbbddd444eee3333.......
        ...............cccbbbbbbbddd444eee3333.......
        ............cccbbbbbbdddddddddd444eeee.......
        ............cccbbbbbbdddddddddd444eeee.......
        ............cccbbbbbbdddddddddd444eeee.......
        ........ccccbbbbbbdddddddddddddddd4444eee3333
        ........ccccbbbbbbdddddddddddddddd4444eee3333
        ........ccccbbbbbbdddddddddddddddd4444eee3333
        .....cccbbbbbbbddddddddddddddddddddddddddeee3
        .....cccbbbbbbbddddddddddddddddddddddddddeee3
        .....cccbbbbbbbddddddddddddddddddddddddddeee3
        ..cccbbbbbbbdddddd666ccccddd666cccddddddd444e
        ..cccbbbbbbbdddddd666ccccddd666cccddddddd444e
        ..cccbbbbbbbdddddd666ccccddd666cccddddddd444e
        ccbbb2222222222444444777744444477744442222222
        ccbbb2222222222444444777744444477744442222222
        ccbbb2222222222444444777744444477744442222222
        cc222cccddddddddddddd5555dddddd555ddddddd444e
        cc222cccddddddddddddd5555dddddd555ddddddd444e
        cc222cccddddddddddddd5555dddddd555ddddddd444e
        ..222444ddddbbb666ddddddddddddd777bbbbdddeee6
        ..222444ddddbbb666ddddddddddddd777bbbbdddeee6
        ..222444ddddbbb666ddddddddddddd777bbbbdddeee6
        ..2222222222fffbbb6666666666777bbbddddeee7776
        ..2222222222fffbbb6666666666777bbbddddeee7776
        ..2222222222fffbbb6666666666777bbbddddeee7776
        ........2222444fffbbbbbbb666bbbdddeeee777777.
        ........2222444fffbbbbbbb666bbbdddeeee777777.
        ........2222444fffbbbbbbb666bbbdddeeee777777.
        ........2222222222cccddddbbb444eee6666.......
        ........2222222222cccddddbbb444eee6666.......
        ........2222222222cccddddbbb444eee6666.......
        ...............222444cccc444eee7776666.......
        ...............222444cccc444eee7776666.......
        ...............222444cccc444eee7776666.......
        ...............2222224444ccc666777...........
        ...............2222224444ccc666777...........
        ...............2222224444ccc666777...........
        .....................ccccccc.................
        .....................ccccccc.................
        .....................ccccccc.................
        .............................................
        .............................................
        .............................................
        .............................................
        .............................................
        .............................................
        .............................................
        .............................................
        `],
    200,
    true
    )
    tiles.placeOnRandomTile(Big_Sandwich, assets.tile`myTile45`)
    Nowhere = sprites.create(img`
        . . . . f f f f f . . . . . . . 
        . . . f e e 4 1 b f . . . . . . 
        . . f d d d d 4 1 b f . . . . . 
        . c d d d d f d e 1 f f . . . . 
        . c d f d d d d 4 1 1 1 f . . . 
        c d e e d d d d e 1 b 1 c . . . 
        c d d d d c d d e 1 b 1 c . . . 
        c c c c c d d 4 1 1 f c . . . . 
        . f 1 1 9 d 4 1 1 f f 5 . . . . 
        . . f f 6 f f a 3 1 1 f 5 . . . 
        . . . . f f 1 1 1 1 1 1 f 4 f f 
        . . . f 1 1 f 1 1 f 1 1 f 4 1 f 
        . . f 1 1 f 1 1 f 1 1 1 f 4 1 f 
        . f b c f c b f b b f 1 f f 1 f 
        . f c c f c c f c c b 1 f f f f 
        . . f f f f f f f f f f f f f . 
        `, SpriteKind.NPC_C)
    tiles.placeOnRandomTile(Nowhere, assets.tile`myTile35`)
    animation.runImageAnimation(
    Nowhere,
    [img`
        . . . . f f f f f . . . . . . . 
        . . . f e e 4 1 b f . . . . . . 
        . . f d d d d 4 1 b f . . . . . 
        . c d d d d f d e 1 f f . . . . 
        . c d f d d d d 4 1 1 1 f . . . 
        c d e e d d d d e 1 b 1 c . . . 
        c d d d d c d d e 1 b 1 c . . . 
        c c c c c d d 4 1 1 f c . . . . 
        . f 1 1 9 d 4 1 1 f f 5 . . . . 
        . . f f 6 f f a 3 1 1 f 5 . . . 
        . . . . f f 1 1 1 1 1 1 f 4 f f 
        . . . f 1 1 f 1 1 f 1 1 f 4 1 f 
        . . f 1 1 f 1 1 f 1 1 1 f 4 1 f 
        . f b c f c b f b b f 1 f f 1 f 
        . f c c f c c f c c b 1 f f f f 
        . . f f f f f f f f f f f f f . 
        `,img`
        . . . . f f f f f . . . . . . . 
        . . . f e e 4 1 b f . . . . . . 
        . . f d d d d 4 1 b f . . . . . 
        . c d d d d f d e 1 f f . . . . 
        . c d f d d d d 4 1 1 1 f . . . 
        c d e e d d d d e 1 b 1 c . . . 
        c d d d d c d d e 1 b 1 c . . . 
        c c c c c d d 4 1 1 f c . . . . 
        . f 1 1 9 d 4 1 1 f f 5 . . . . 
        . . f f 6 f f a 3 1 1 f 5 . . . 
        . . . . f f 1 1 1 1 1 1 f 4 f f 
        . . . f 1 1 f 1 1 f 1 1 f 4 1 f 
        . . f 1 1 f 1 1 f 1 1 1 f 4 1 f 
        . f b c f c b f b b f 1 f f 1 f 
        . f c c f c c f c c b 1 f f f f 
        . . f f f f f f f f f f f f f . 
        `,img`
        . . . . f f f f f . . . . . . . 
        . . . f e e 4 1 b f . . . . . . 
        . . f d d d d 4 1 b f . . . . . 
        . c d d d d f d e 1 f f . . . . 
        . c d f d d d d 4 1 1 1 f . . . 
        c d e e d d d d e 1 b 1 c . . . 
        c d d 7 d c d d e 1 b 1 c . . . 
        c c c c c d d 4 1 1 f c . . . . 
        . f 1 1 9 d 4 1 1 f f 5 . . . . 
        . . f f d f f a 3 1 1 f 5 . . . 
        . . . . f f 1 1 1 1 1 1 f 4 f f 
        . . . f 1 1 f 1 1 f 1 1 f 4 1 f 
        . . f 1 1 f 1 1 f 1 1 1 f 4 1 f 
        . f b c f c b f b b f 1 f f 1 f 
        . f c c f c c f c c b 1 f f f f 
        . . f f f f f f f f f f f f f . 
        `,img`
        . . . . f f f f f . . . . . . . 
        . . . f e e 4 1 b f . . . . . . 
        . . f d d d d 4 1 b f . . . . . 
        . c d d d d f d e 1 f f . . . . 
        . c d f d d d d 4 1 1 1 f . . . 
        c d e e d d d d e 1 b 1 c . . . 
        c d d 7 d c d d e 1 b 1 c . . . 
        c c c c c d d 4 1 1 f c . . . . 
        . f 1 1 9 d 4 1 1 f f 5 . . . . 
        . . f f d f f a 3 1 1 f 5 . . . 
        . . . . f f 1 1 1 1 1 1 f 4 f f 
        . . . f 1 1 f 1 1 f 1 1 f 4 1 f 
        . . f 1 1 f 1 1 f 1 1 1 f 4 1 f 
        . f b c f c b f b b f 1 f f 1 f 
        . f c c f c c f c c b 1 f f f f 
        . . f f f f f f f f f f f f f . 
        `,img`
        . . . . f f f f f . . . . . . . 
        . . . f e e 4 1 b f . . . . . . 
        . . f d d d d 4 1 b f . . . . . 
        . c d d d d f d e 1 f f . . . . 
        . c d f d d d d 4 1 1 1 f . . . 
        c d e e d d d d e 1 b 1 c . . . 
        c d d 7 d c d d e 1 b 1 c . . . 
        c c c 5 c d d 4 1 1 f c . . . . 
        . f 1 1 d d 4 1 1 f f 5 . . . . 
        . . f f d f f a 3 1 1 f 5 . . . 
        . . . . f f 1 1 1 1 1 1 f 4 f f 
        . . . f 1 1 f 1 1 f 1 1 f 4 1 f 
        . . f 1 1 f 1 1 f 1 1 1 f 4 1 f 
        . f b c f c b f b b f 1 f f 1 f 
        . f c c f c c f c c b 1 f f f f 
        . . f f f f f f f f f f f f f . 
        `,img`
        . . . . f f f f f . . . . . . . 
        . . . f e e 4 1 b f . . . . . . 
        . . f d d d d 4 1 b f . . . . . 
        . c d d d d f d e 1 f f . . . . 
        . c d f d d d d 4 1 1 1 f . . . 
        c d e e d d d d e 1 b 1 c . . . 
        c d d 7 d c d d e 1 b 1 c . . . 
        c c c 5 c d d 4 1 1 f c . . . . 
        . f 1 1 d d 4 1 1 f f 5 . . . . 
        . . f f d f f a 3 1 1 f 5 . . . 
        . . . . f f 1 1 1 1 1 1 f 4 f f 
        . . . f 1 1 f 1 1 f 1 1 f 4 1 f 
        . . f 1 1 f 1 1 f 1 1 1 f 4 1 f 
        . f b c f c b f b b f 1 f f 1 f 
        . f c c f c c f c c b 1 f f f f 
        . . f f f f f f f f f f f f f . 
        `,img`
        . . . . f f f f f . . . . . . . 
        . . . f e e 4 1 b f . . . . . . 
        . . f d d d d 4 1 b f . . . . . 
        . c d d d d f d e 1 f f . . . . 
        . c d f d d d d 4 1 1 1 f . . . 
        c d e e d d d d e 1 b 1 c . . . 
        c d d d d c d d e 1 b 1 c . . . 
        c c c c c d d 4 1 1 f c . . . . 
        . f 1 1 d d 4 1 1 f f 5 . . . . 
        . . f f d f f a 3 1 1 f 5 . . . 
        . . . . f f 1 1 1 1 1 1 f 4 f f 
        . . . f 1 1 f 1 1 f 1 1 f 4 1 f 
        . . f 1 1 f 1 1 f 1 1 1 f 4 1 f 
        . f b c f c b f b b f 1 f f 1 f 
        . f c c f c c f c c b 1 f f f f 
        . . f f f f f f f f f f f f f . 
        `],
    300,
    true
    )
    platform.setImage(img`
        ffffffffff
        f86919191f
        f86911911f
        f86919191f
        f86991191f
        f86919911f
        f86991191f
        f86911191f
        f86911191f
        f86991191f
        f86919911f
        f86991191f
        f86919191f
        f86911911f
        f86919191f
        f86991191f
        f86991191f
        f86919191f
        f86911911f
        f86919191f
        f86991191f
        f86919911f
        f86991191f
        f86911191f
        f86911191f
        f86991191f
        f86919911f
        f86991191f
        f86919191f
        f86911911f
        f86919191f
        f86991191f
        f86991191f
        f86919191f
        f86911911f
        f86919191f
        f86991191f
        f86919911f
        f86991191f
        f86911191f
        f86911191f
        f86991191f
        f86919911f
        f86991191f
        f86919191f
        f86911911f
        f86919191f
        ffffffffff
        `)
    platform_2.setImage(img`
        ffffffffffffffffffffffffffffffffffffffffffffffff
        f8888888888888888888888888888888888888888888888f
        f6666666666666666666666666666666666666666666666f
        f9999999999999999999999999999999999999999999999f
        f6169191191961699616919119196169961691911919616f
        f9691911119196911969191111919691196919111191969f
        f1911911119119111191191111911911119119111191191f
        f9199199991991999919919999199199991991999919919f
        f1111111111111111111111111111111111111111111111f
        ffffffffffffffffffffffffffffffffffffffffffffffff
        `)
    tiles.placeOnRandomTile(Player_A1, assets.tile`myTile47`)
    tiles.placeOnRandomTile(platform_2, assets.tile`myTile13`)
    tiles.placeOnRandomTile(platform, assets.tile`myTile4`)
}
function Statusbar_changes_for_normal () {
    LIFE_BARRRRR.setColor(2, 3)
    LIFE_BARRRRR.setBarBorder(1, 10)
    LIFE_BARRRRR.positionDirection(CollisionDirection.Left)
    Level.value = 1
    Level.setColor(9, 15)
    Level.positionDirection(CollisionDirection.Top)
    Level.setBarBorder(1, 8)
    Player_health_in_fight.setBarBorder(1, 0)
    Enemy_Health.setColor(0, 0)
    Player_health_in_fight.setColor(0, 0)
    Enemy_Health.setBarBorder(1, 0)
    Level.value = save_for_Level
    LIFE_BARRRRR.value = Save_for_statusbar_LIFE_BARRRR
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile10`, function (sprite, location) {
    Dead_1()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.plattform2, function (sprite, otherSprite) {
    if (Level.value == 0) {
    	
    } else {
        if (info.life() == 1) {
            Dead_1()
        } else {
            pause(100)
            Player_A1.y += -30
            Player_A1.vx += -30
            info.changeLifeBy(-1)
        }
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile53`, function (sprite, location) {
    Dead_1()
})
function Items_Menu () {
    if (Level.value == 2) {
        MENU()
        Player_POS = Player_A1.tilemapLocation()
        MENU_yes__no = 1
    } else if (Level.value == 3) {
        MENU()
        Player_POS = Player_A1.tilemapLocation()
        MENU_yes__no = 1
    } else if (Level.value == 4) {
        MENU()
        Player_POS = Player_A1.tilemapLocation()
        MENU_yes__no = 1
    } else {
    	
    }
}
controller.combos.attachCombo("AUDAB", function () {
    Statusbar_changes_for_fight()
    Player_health_in_fight.positionDirection(CollisionDirection.Right)
})
function MENU () {
    let Sandwich_ITEM_ITEM = 0
    tiles.setCurrentTilemap(tilemap`level6`)
    scene.setBackgroundImage(img`
        ccccc8888888888888888888888888888888888cc8888cc8888cc8888888ccccc8888888888888888888888888888888888cc88888cccc888cc8ccccc8888888888888888888888888888888888cc888
        888ccccc88888888888888888888888888888ccc8888cccc8888cc888888888ccccc88888888888888888888888888888ccc8888ccccc888cc88888ccccc88888888888888888888888888888ccc8888
        888888ccccccc888888888888888888888cccc88888cccccc8888ccc8888888888ccccccc888888888888888888888cccc88888cccc8888cc888888888ccccccc888888888888888888888cccc88888c
        888888888cccccccccccccc8888888ccccc888888cccc88ccc8888cccc88888888888cccccccccccccc8888888ccccc88888acccc88888cccc88888888888cccccccccccccc8888888ccccc888888ccc
        c888888888888888888888888888cccc8888888cccc88888ccf88888ccccc888888888888888888888888888cccc8aaaaaacccc88888cfc8ccccc888888888888888888888888888cccc8888888cccc8
        cccccccc88888888888888888888888888888ccc8888888ccccfc888888ccccccccc88888888888888aaaaaaaaaaaaa88ccc8888888cfc88888ccccccccc88888888888888888888888888888ccc8888
        8888ccccccccc888888888888888888888cccc8888888cccccccffc888888888ccccccccc88888aaaaaaaaaaa88888cccc888aa88cffccc888a88888ccccccccc888888888888888888888cccc888888
        888aa88888888888888888888888888cccc8888888cccccccc888cfffc888888888888888888888888888888888cccc88aaaa8cfffc88ccccc8aaaaa888888888888888888888888888cccc8888888cc
        88888aaaa8888888888888888888888888888888ccccccccc88888ccfffc88888888888888888888888888888888aaaaaaa8cfffcc88888ccccc88aaaaaaaaaaaaaaaaaaa8888888888888888888cccc
        cccc888aaaaaaaaaaaaaaaa8888888888888cccccc888888888ccccc88ffffcc8888888888aaaaaaaaaaaaaaaaaaaaa8ccffff88ccccc88888cccccc8aaaaaaaaaaaaa888888888888888888cccccccc
        ccccccccccaaaaaaaaaaa8888888888ccccccc8888888888ccccc8888fffffffffffcc888888888888aaaaaaaaa8fffffffffff8888ccccc888888cccccccc888888888888888888888ccccccccccccc
        ccccccccccccccccccccccccccccccccc88cccccccc8888ccc888888ffffffffffffffffffffffffffffffffffffffffffffffff888888ccc8888ccccccccccccccccccccccccccccccccccccccccccc
        ccccccccccc88888888888888cc88888888888888888888888888cffffffffffffffffffffffffffffffffffffffffffffffffffffc88888888888888888888888888cc88888888888888ccccccccccc
        cccccccccc88888888888888888cccc8888888888888888888cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc8888888888888888888cccc88888888888888888cccccccccc
        cccccccccc888888888888888888cccccccc888888888cccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccc888888888cccccccc888888888888888888cccccccccc
        ccccccccc8888888888888888888ccccccccccccccccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcccccccccccccccc8888888888888888888ccccccccc
        ccccccccc8888888888888888888cc8888cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc8888cc8888888888888888888ccccccccc
        cccccccc88e88888888888888888cc8888cccc8cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc8cccc8888cc88888888888888888c88cccccccc
        cccccccc8888888888888888888cc88888cc88ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc88cc88888cc8888888888888888888cccccccc
        cccccccc8e8888888888888888ccc88888cc88cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc88cc88888ccc8888888888888888c8cccccccc
        ccccccc88e8888888888888888cc888888c88ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc88c888888cc8888888888888888c88ccccccc
        ccccccc88e888888888888888cc888888cc88cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc88cc888888cc888888888888888c88ccccccc
        cccccc88c8888888888888888cc888888c88ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc88c888888cc8888888888888888c88cccccc
        cccccc88c888888888888888cc888888cc8cccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcac8cc888888cc888888888888888c88cccccc
        ccccc88cc888888888888888cc88888cc88ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffca88cc88888cc888888888888888cc88ccccc
        ccccc88c888888888888888cc888888cc8cccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcac8cc888888cc888888888888888c88ccccc
        cccc88cc888888888888888c888888cc88ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffca88cc888888c888888888888888cc88cccc
        cccc88cc88e88888888888cc88888cc88ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffaa88cc88888cc88888888888c88cc88cccc
        cccc8cc888888888888888c888888cca8ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcaa8cc888888c888888888888888cc8cccc
        ccc88cc88e88888888888e888888cca8ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffaa88cc888888c88888888888c88cc88ccc
        ccc8cc888e88888888888e88888cc8acccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcaa88cc88888c88888888888c888cc8ccc
        cc88cc88c88888888888e888888cca8ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcaa8cc888888c88888888888c88cc88cc
        cc8ccc8cc8888888888e888888ccaacccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcaa88cc888888c8888888888cc8ccc8cc
        ccccc88cc8888888888e88888ccaacccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcaa88cc88888c8888888888cc88ccccc
        ccccc8cc8888888888888888cccaaccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcaa8ccc8888888888888888cc8ccccc
        cccc88cc8888888888888888ccaacccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcaaa8cc8888888888888888cc88cccc
        cccc8cc8888888888888888ccaacccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcaa88cc8888888888888888cc8cccc
        cccc8cc888888888888888ccaaaccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcaa88cc888888888888888cc8cccc
        ccc8cc8888888888888888ccaacccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccaa8cc8888888888888888cc8ccc
        ccc8cc888888888888888ccaacccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcaaa8cc888888888888888cc8ccc
        cc8cc8888888888888888caacccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcaa88c8a88888888888888cc8cc
        cc8cc8888888888888a8eaaaccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcaa88ca88888888888888cc8cc
        c8cc8888888888888a88eaacccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccaa8c8a88888888888888cc8c
        c8cc888888888888aa8eaacccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcaa88ea88888888888888cc8c
        ccc888888888888aa8eaacccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcaa88ea88888888888888ccc
        ccc888888888888a88aaaccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcaa88a88888888888888ccc
        cc888888888888aa8aaacccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcca88aa88888888888888cc
        cc88888888888aa88aacccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcca88a88888888888888cc
        c88888888888aa88aacccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcaa8aa88888888888888c
        c88888888888aa8aaaccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffca88a88888888888888c
        88888e88888aa88aacccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccc8aa88888888c88888
        88888e8888aa88aacccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccc8a88888888c88888
        888888888aa8888cccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcccaa8888888888888
        8888e8888aa888cccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccca88888888c8888
        8888e888aa8888cccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcccaa8888888c8888
        888c888aa8888cccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccca88888888c888
        888c888a8e88cccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccaa8c88888c888
        888c88888e8cccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcca8c88888c888
        88cc8888c8cccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccaac8888cc88
        88c88888c8cccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccaac88888c88
        88c8888cccccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccccc8888c88
        8cc8888ccccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcccc8888cc8
        8c8888ccccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcccc8888c8
        8c888ccc8cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc8ccc888c8
        8c888ccc8cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc8ccc888c8
        cc88cccc8cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc8cccc88cc
        cc88ccc88cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc88ccc88cc
        cccccc88ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc88cccccc
        ccccc888cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc888ccccc
        8888888ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc8888888
        888888ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc888888
        88888cccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccc88888
        888cccccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccccc888
        cccc8ccccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcccc8cccc
        888c8cc8cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc8cc8c888
        888c8cc8cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc8cc8c888
        888c8cc8cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc8cc8c888
        888c8cc8cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc8cc8c888
        888c8cc88cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc88cc8c888
        888c8cc88cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc88cc8c888
        888c8ccc8cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc8ccc8c888
        888c88cc8ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc8cc88c888
        888c88cc88cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc88cc88c888
        888c88cc88cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc88cc88c888
        888c88cc88cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc88cc88c888
        888c88cc888cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc888cc88c888
        888c88ccc88cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc88ccc88c888
        888c888cc88cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc88cc888c888
        888c888cc88ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc88cc888c888
        888c888cc888cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc888cc888c888
        888c888cc888cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc888cc888c888
        888cc88cc888ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc888cc88cc888
        888cc88cc8888cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc8888cc88cc888
        8888c888c8888ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc8888c888c8888
        8888c888cc8888cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc8888cc888c8888
        8888c888cc8888cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc8888cc888c8888
        8888c888cc8888ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc8888cc888c8888
        8888c8888c88c88cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc88c88c8888c8888
        888888888c88c88ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc88c88c888888888
        888888888c88c888cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc888c88c888888888
        8888888888c88c88ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc88c88c8888888888
        888888c888c88c888cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc888c88c888c888888
        888888c888888c888ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc888c888888c888888
        888888c8888888c888cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc888c8888888c888888
        888888cc888888c888ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc888c888888cc888888
        8888888c888888c8888cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc8888c888888c8888888
        88888c8c8888888c888ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc888c8888888c8c88888
        88888c8c8888888c888ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc888c8888888c8c88888
        88888c8c88888888c88cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc88c88888888c8c88888
        88888c8cc8888888c88cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc88c8888888cc8c88888
        88888c8cc8888888ccccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcccc8888888cc8c88888
        88888c88c8888888cccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccc8888888c88c88888
        88888cc8c8888888ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc8888888c8cc88888
        88888cc8c888888ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc888888c8cc88888
        888888c8cc88888cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc88888cc8c888888
        888888c88c8888ccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcc8888c88c888888
        888888c88c88cccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccc88c88c888888
        888888c8cccccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccccc8c888888
        888888c8cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc8c888888
        888888cccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccc888888
        `)
    Save_for_statusbar_LIFE_BARRRR = LIFE_BARRRRR.value
    save_for_Level = Level.value
    Level.setColor(0, 0)
    LIFE_BARRRRR.setColor(0, 0)
    Level.setBarBorder(1, 0)
    LIFE_BARRRRR.setBarBorder(1, 0)
    if (Item == 1) {
        Text_V1 = textsprite.create("Here are all youre items", 0, 1)
        tiles.placeOnRandomTile(Text_V1, assets.tile`myTile34`)
        scene.cameraFollowSprite(Text_V1)
    } else {
        TEXT_V_II = textsprite.create("You do not have any items", 0, 1)
        tiles.placeOnRandomTile(TEXT_V_II, assets.tile`myTile34`)
        scene.cameraFollowSprite(TEXT_V_II)
    }
    if (METTALL_PIPE_ITEM == 1) {
        Text_V_3 = textsprite.create("Metall pipe", 0, 1)
        Text_V_3.setIcon(img`
            ......................
            ......................
            ......................
            ......................
            ......................
            ......................
            ......................
            ................cccc..
            ...............ccffcc.
            ...............ccccdc.
            ...............ccbbdc.
            .ccccccccccccccccbbdc.
            ccccccccccccccccbbb1c.
            cfcbbbbbbbbbbbbbbbb1c.
            cfcbbbbbbbbbbbbbbbb1c.
            ccdddddddddddddd111c..
            .cccccccccccccccccc...
            ......................
            ......................
            `)
        tiles.placeOnRandomTile(Text_V_3, assets.tile`myTile3`)
    }
    if (timewastermedal_ITEM == 1) {
        Text_v_VI = textsprite.create("Time-waster-medal", 0, 1)
        Text_v_VI.setIcon(img`
            .......111.......
            ....111222111....
            ...12228882221...
            ..12888...88821..
            .128.........821.
            .128.........821.
            .128.........821.
            .128.........821.
            ..128.......821..
            ..128.......821..
            ...1288.4.8821...
            ....12dd54421....
            .....d555554.....
            .....d554554.....
            ....d55545552....
            .....4554452.....
            .....4555552.....
            ......44522......
            ........2........
            `)
        tiles.placeOnRandomTile(Text_v_VI, assets.tile`myTile4`)
    }
    if (Sandwich_ITEM_ITEM == 1) {
        Text_V_5 = textsprite.create("Sandwich Piece", 0, 1)
        Text_V_5.setIcon(img`
            . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . 
            . 2 2 2 7 6 e 2 2 2 7 6 c c . 
            e 2 4 7 7 7 6 2 4 2 7 7 6 c c 
            2 2 2 4 4 4 4 4 4 4 2 2 2 b c 
            e 4 d d d d d d d d d d c 2 c 
            6 e d d d d d d d d d d 4 2 . 
            6 7 e d d d d d d d f 2 2 2 . 
            . 7 7 e d d d d d f 4 2 . . . 
            . . . 6 e 4 d d c 2 2 2 . . . 
            . . . 6 7 e 4 c 4 2 . . . . . 
            . . . . 7 6 c 4 2 2 . . . . . 
            . . . . . . c c . . . . . . . 
            `)
        tiles.placeOnRandomTile(Text_V_5, assets.tile`myTile6`)
    }
    Start_Menu_yesno = 0
    Item_menu_yesno = 1
}
scene.onOverlapTile(SpriteKind.plattform2, assets.tile`myTile14`, function (sprite, location) {
    platform_2.setVelocity(-120, 0)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile51`, function (sprite, location) {
    Dead_1()
})
scene.onOverlapTile(SpriteKind.plattform2, assets.tile`myTile13`, function (sprite, location) {
    platform_2.setVelocity(120, 0)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile48`, function (sprite, location) {
    Dead_1()
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile69`, function (sprite, location) {
    game.showLongText("This Path goes straight to nowhere", DialogLayout.Bottom)
    tiles.setTileAt(location, assets.tile`myTile41`)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile11`, function (sprite, location) {
    Dead_1()
})
function Status_bar_menu_end () {
    LIFE_BARRRRR.setColor(2, 3)
    LIFE_BARRRRR.setBarBorder(1, 10)
    LIFE_BARRRRR.positionDirection(CollisionDirection.Left)
    Level.value = 1
    Level.setColor(9, 15)
    Level.positionDirection(CollisionDirection.Top)
    Level.setBarBorder(1, 8)
    Level.value = save_for_Level
    LIFE_BARRRRR.value = Save_for_statusbar_LIFE_BARRRR
}
let Text_V_5: TextSprite = null
let Text_V_3: TextSprite = null
let Nowhere: Sprite = null
let Big_Sandwich: Sprite = null
let Entrance_sign_lvl_3_W_1: Sprite = null
let Letter: Sprite = null
let Start_Menu_yesno = 0
let MENU_yes__no = 0
let Heal_Value = 0
let Health_item_yesno = 0
let Sandwich_ITEM: Sprite = null
let Item_menu_yesno = 0
let Item_Menu: TextSprite = null
let Nowhere_talkedin_with_us = 0
let Metall_Pipe: Sprite = null
let Platform_3: Sprite = null
let Letter_Item = 0
let fight_count = 0
let Boss_1_dead_yesno = 0
let NPC_1_Mamfred_Monk: Sprite = null
let ZAHL_2 = 0
let Text_V1: TextSprite = null
let TEXT_V_II: TextSprite = null
let Text_v_VI: TextSprite = null
let platform_2: Sprite = null
let platform: Sprite = null
let Player_POS: tiles.Location = null
let Item = 0
let timewastermedal: Sprite = null
let save_for_Level = 0
let LIFE_BARRRRR: StatusBarSprite = null
let Save_for_statusbar_LIFE_BARRRR = 0
let Level: StatusBarSprite = null
let Press_A1: Sprite = null
let Player_health_in_fight: StatusBarSprite = null
let Player_Damage = 0
let radioactive_Sandwich: Sprite = null
let Enemy_Health: StatusBarSprite = null
let Damage = 0
let timewastermedal_ITEM = 0
let METTALL_PIPE_ITEM = 0
let turn_toggle = 0
let Animation_finished = 0
let Fight_Toggle = 0
let Player_A1: Sprite = null
let Zahl = 0
game.splash("STARTING... STARTING... ")
game.splash("Hello")
game.splash("YOU in front of the screen")
game.splash("STARTING... STARTING...")
game.splash("LETS GO!")
THE_REAL_START()
pause(500)
Zahl = 0
forever(function () {
    if (controller.A.isPressed()) {
        if (Level.value + 1 == 2) {
            Start()
        }
    }
})
forever(function () {
    if (controller.B.isPressed()) {
        if (Level.value + 1 == 2) {
            Credits()
        }
    }
})
forever(function () {
    if (controller.B.isPressed() && Item_menu_yesno == 1) {
        Item_menu_page_II()
    }
})
forever(function () {
    if (controller.B.isPressed() && Start_Menu_yesno == 1) {
        sprites.destroy(Text_v_VI)
        sprites.destroy(Item_Menu)
        Items_Menu()
    }
})
forever(function () {
    if (controller.A.isPressed() && MENU_yes__no == 1) {
        sprites.destroy(Text_v_VI)
        sprites.destroy(Text_V1)
        sprites.destroy(TEXT_V_II)
        sprites.destroy(Text_v_VI)
        sprites.destroy(Item_Menu)
        MENU_end()
        MENU_yes__no = 0
    }
})
