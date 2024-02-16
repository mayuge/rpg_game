import tkinter as tk
import rpg_map

class PanelSetting:
    def __init__(self):
       
        #横17マス、縦が13マス
        self.width_tile = 17
        self.height_tile = 13

        # イメージ作成
        self.ground_img = tk.PhotoImage(file="ground.png")
        self.wall_img = tk.PhotoImage(file="wall.png")
        self.player_img = tk.PhotoImage(file="player.png")

class PlayerSetting:
    def __init__(self):
        #人間が動く場合はTrue、背景が動く場合はFalse
        self.move_mode = False

        #フィールド描画開始位置
        self.field_x = 0
        self.field_y = 0

         #画面中央のプレイヤー座標
        self.center_x = 8
        self.center_y = 6

        # プレイヤーの位置を設定
        self.player_x = 8
        self.player_y = 6

   
def collision(x, y,mypanel,mymap):
    if(mymap.map_1[y][x] == 1):
        return True
    else:
        return False

def handle_key(event, mypanel, mymap, player, canvas):
    place_x = 0
    place_y = 0

    if event.keysym == 'w':
        place_y -= 1
    elif event.keysym == 'a':
        place_x -= 1
    elif event.keysym == 's':
        place_y += 1     
    elif event.keysym == 'd':
        place_x += 1

    #falseで当たり判定検出なし、trueで障害物発見
    #can_move = collision(place_x+ player.field_x+player.center_x, place_y+player.field_y+player.center_y, mypanel, mymap)
    #print(player.field_x+place_x+player.center_x,player.field_y+player.center_y)
    
    #人物が動かない場合
    if player.move_mode == False:
    #falseで当たり判定検出なし、trueで障害物発見
        can_move = collision(place_x+ player.field_x+player.center_x, place_y+player.field_y+player.center_y, mypanel, mymap)
        if can_move == False:
            player.field_x += place_x 
            player.field_y += place_y
    #人物が動く場合
    else:
        can_move = collision(place_x+ player.player_x, place_y+player.player_y, mypanel, mymap)
        if can_move == False:
            player.player_x += place_x 
            player.player_y += place_y
    #print(player.field_x)a

    
        
    #プレイヤー位置が変更されたので再描画
    canvas.delete("all")
    displayMap(mypanel, mymap, player, canvas)

def main():
     #画面作成
    root = tk.Tk()
    root.title("rpg")
    root.geometry("544x416")

    #キャンバス作成
    canvas = tk.Canvas(root, bg="#000000", height=416, width=544)
    canvas.pack()

    #クラスの呼び出し
    mymap = rpg_map.RpgMap()
    mypanel = PanelSetting()
    player = PlayerSetting()
    
    #print(mymap.map_1)

    displayMap(mypanel, mymap, player, canvas)

    # キーボードイベントをウィンドウにバインド
    root.bind('<KeyPress>', lambda event: handle_key(event, mypanel, mymap, player, canvas))

    root.mainloop()


def displayMap(mypanel, mymap, player, canvas):
    ground_img = mypanel.ground_img
    wall_img = mypanel.wall_img
    player_img = mypanel.player_img
    
    # キャンバスにイメージを表示
    #写真の中央が設置座標だということに注意

    for i in range(len(mymap.map_1)):
        for j in range(len(mymap.map_1[i])):
            if player.move_mode == True:
                if mymap.map_1[i][j] == 0:
                    canvas.create_image(32*j+16, 32*i+16, image=ground_img)
                elif mymap.map_1[i][j] == 1:
                    canvas.create_image(32*j+16, 32*i+16, image=wall_img)
            else:
                if mymap.map_1[i][j] == 0:
                    canvas.create_image(32*j-(32*player.field_x)+16, 32*i-(32*player.field_y)+16, image=ground_img)
                elif mymap.map_1[i][j] == 1:
                    canvas.create_image(32*j-(32*player.field_x)+16, 32*i-(32*player.field_y)+16, image=wall_img)
    
    # プレイヤーを表示
    canvas.create_image(32*player.player_x+16, 32*player.player_y+16, image=player_img)


if __name__ == "__main__":
    main()