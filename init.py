import os
from PIL import Image, ImageDraw, ImageFont

class Board():
    def __init__(self) -> None:
        self.board = Image.open("./images/board.png")
        self.background = Image.new('RGBA', tuple([w+30 for w in self.board.size]), (255, 255, 255, 255))
        self.background_ = Image.new('RGBA', self.board.size, (255, 255, 255, 255))
        self.TILE = round(self.board.width/8)
        
        font = ImageFont.truetype("font.ttf", 8)

        self.background_.paste(self.board)
        background = ImageDraw.Draw(self.background)
        for i in range(8):
            background.text((0, i), f"{i+1}", (0, 0, 0), font)
        
        for i in range(8):
            background.text((0, i), f"{('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')[i]}", (0, 0, 0), font)

    def board(self, player, board_set):
        for i, rank in enumerate(board_set):
            for j, piece_ in enumerate(rank):
                if piece_ != 0:
                    for image in os.listdir("./images/pieces"):
                        if piece_.startswith(image[0]+image[5]):
                            piece = Image.open(f"./images/pieces/{image}")
                            piece = piece.resize((self.TILE, self.TILE))
                            self.board = self.paste(player, piece, (i, j), self.board)
                            break
        
        self.background.paste(self.background_, (0,self.background.height-self.board.height))
        if player:
            self.background = self.background.rotate(180)

        self.background.save("./saved/board.png")

    def paste(self, player, piece, place, board):
        if player:
            piece.rotate(180)
        
        board.paste(piece, (place[1]*self.TILE, place[0]*self.TILE), piece)
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