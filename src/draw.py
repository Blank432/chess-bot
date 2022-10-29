import os
from PIL import Image, ImageDraw, ImageFont

from .__init__ import BOARD_IMAGE, PIECE_IMAGES, RANKS, FILES

class Board():
    def __init__(self) -> None:
        self.board = Image.open(BOARD_IMAGE)
        self.background = Image.new('RGBA', tuple([w+35 for w in self.board.size]), (240,240,210,240))
        self.background_ = Image.new('RGBA', self.board.size, (255, 255, 255, 255))
        self.TILE = round(self.board.width/8)

        self.background_.paste(self.board)

    def create(self, player, board_set):
        for i, rank in enumerate(board_set):
            for j, piece_ in enumerate(rank):
                if piece_ != 0:
                    for image in os.listdir(PIECE_IMAGES):
                        if piece_.startswith(image[0]+image[5]):
                            piece = Image.open(PIECE_IMAGES+image)
                            piece = piece.resize((self.TILE, self.TILE))
                            self.background_ = self.paste(player, piece, (i, j), self.background_)
                            break
        if not player:
            self.background_ = self.background_.rotate(180)
        
        font = ImageFont.truetype("font.ttf", 30)
        background = ImageDraw.Draw(self.background)
        for i in range(8):
            background.text((0, i*self.TILE+0.25*self.TILE), f"{RANKS[-i-1 if player else i]}", fill=(0, 0, 0), font=font)
        
        for i in range(8):
            background.text((i*self.TILE+30+0.5*self.TILE, self.background.height-35), f"{FILES[i if player else -i-1]}", (0, 0, 0), font)
        
        self.background.paste(self.background_, (self.background.height-self.board.height,0))
        self.background.save("./edited/board.png")

    def paste(self, player, piece, place, board):
        if not player:
            piece = piece.rotate(180)
        
        board.paste(piece, ((place[1])*self.TILE, place[0]*self.TILE), piece)
        return board


    # def paste(board: Image, piece: Image, c: str, p: str, player: str) -> Image:
    #     if player == 'b':
    #         piece = piece.rotate(180)
        
    #     _c = {'b': 0, 'w': 657}
    #     match p:
    #         case 'r':
    #             board.paste(piece, (0*TILE,_c[c]), piece)
    #             board.paste(piece, (7*TILE,_c[c]), piece)

    #         case 'n':
    #             board.paste(piece, (1*TILE,_c[c]), piece)
    #             board.paste(piece, (6*TILE,_c[c]), piece)

    #         case 'b':
    #             board.paste(piece, (2*TILE,_c[c]), piece)
    #             board.paste(piece, (5*TILE,_c[c]), piece)

    #         case 'q':
    #             board.paste(piece, (3*TILE,_c[c]), piece)

    #         case 'k':
    #             board.paste(piece, (4*TILE,_c[c]), piece)

    #         case 'p':
    #             for i in range(8):
    #                 board.paste(piece, (i*TILE, (TILE if c=='b' else 6*TILE)), piece)
        
    #     return board