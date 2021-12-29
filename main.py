import pygame as pg

import elements as elem
import parameter as para


class main_game:
    cheif = None
    window = None
    gameover = False
    game_map = None
    def __init__(self) -> None:
        pg.display.init()
        main_game.window = pg.display.set_mode([para.width, para.height])
        self.init_map()
        self.init_cheif()

    def init_map(self):
        main_game.game_map = elem.main_map(para.width, para.height)

    def init_cheif(self):
        cheif = elem.character(para.width/2, para.height/2)
        main_game.cheif = cheif

    def deal_event(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.endgame()
            elif e.type == pg.KEYDOWN:
                if e.key == pg.K_w :
                    main_game.cheif.rect.y -= 3
                elif e.key == pg.K_a :
                    main_game.cheif.rect.x -= 3
                elif e.key == pg.K_s :
                    main_game.cheif.rect.y += 3
                elif e.key == pg.K_d :
                    main_game.cheif.rect.x += 3

    def start(self):
        pg.key.set_repeat(200, 50)
        while not main_game.gameover :
            self.deal_event()
            main_game.window.fill((255, 255, 255))
            # main_game.game_map.display_map(main_game.window)
            main_game.cheif.display(main_game.window)
            pg.display.update()

    def endgame(self):
        print("game over!\nthank you for your time!")
        pg.time.wait(400)
        pg.quit()

if __name__ == "__main__" :
    game = main_game()
    game.start()
