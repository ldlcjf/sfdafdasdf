#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Tkinter
import time
import threading
from PIL import Image, ImageTk
import random
import copy
import ttk
import tkMessageBox as msg


class prize :
    hit_prize_number = 3
    hit_prize_persion = []

    one_prize_all_number = 1
    one_prize_now_number = 0

    two_prize_all_number = 2
    two_prize_now_number = 0

    three_prize_all_number = 3
    three_prize_now_number = 0

    Vip_prize_all_number = 100
    Vip_prize_now_number = 0

    menu = ["一等奖", "二等奖", "三等奖"]


class person :
    photo = [['t1', 'test_photo\unkown.png'],
             ['t2', 'test_photo\unkown.png'],
             ['t3', 'test_photo\unkown.png'],
             ['t4', 'test_photo\\robot.png']]

    photo_f = []

    unkown_photo = ['???', 'test_photo\unkown.png']

    prize_menu = prize.menu

    def __init__ ( self ) :
        self.photo_f = copy.deepcopy ( self.photo )

    def reset ( self ) :
        self.photo_f = copy.deepcopy ( self.photo )


class APP_UI :
    backim_size = None

    start_place = [0.8, 0.8]
    reset_place = [0.82, 0.95]
    all_show_place = [0.7, 0.2]
    prize_menu_place = [0.5, 0.05]
    # prize_show_place

    show_start = [0.05, 0.2]
    show_zone = 0.95
    persion_size = [182, 176]

    isloop = False
    newloop = False

    meubar = None

    hit_show = []

    def __init__ ( self ) :
        self.isloop = False
        self.newloop = False
        self.person = person ()
        self.app = Tkinter.Tk ()
        self.app.title ( '新年抽奖' )
        # back_photo = Tkinter.PhotoImage(file='bakimage.png')
        self.back_photo, self.backim_size = self.photo_resize ( 'bakimage.png', 1 )
        self.back_lable = Tkinter.Label ( self.app, image=self.back_photo, width=self.backim_size[0],
                                          height=self.backim_size[1] ).pack ()
        # size = "%dx%d" % (self.backim_size[0],self.backim_size[1])
        # self.app.geometry(size)
        # self.app.resizable(0,0)
        self.init_windows ()
        self.app.config ( menu=self.meubar )
        self.app.mainloop ()

    def init_windows ( self ) :
        self.init_button ()
        self.init_prize_menu ()
        self.init_text ()
        self.init_show_photo ()

    def init_hit_list ( self, number ) :
        self.prize_hit_list = []
        for i in range ( number ) :
            self.prize_hit_list.append ( self.person.unkown_photo )

    def init_text ( self ) :
        # self.prize_text = Tkinter.StringVar()
        self.prize_text = Tkinter.Text ( self.app, width=5, height=1, bg="red" )
        p_size = self.getplace ( self.prize_menu_place )
        self.prize_text.place ( x=p_size[0], y=p_size[1] )
        self.prize_text.insert ( Tkinter.INSERT, '三等奖' )
        self.prize_num = 3
        self.init_hit_list ( self.prize_num )

    def init_show_photo ( self ) :
        hit_list = self.prize_hit_list
        place_all = self.clac_show_place ( hit_list )
        self.clear_hit_show ()
        self.hit_show = []
        self.now_show_photo = []
        self.str_text = []
        if len ( place_all ) < len ( hit_list ) : return
        print
        "now: place_all ", place_all
        for i in range ( len ( hit_list ) ) :
            now_photo, _ = self.photo_size_set ( hit_list[i][1], self.persion_size )
            self.now_show_photo.append ( now_photo )
            self.str_text.append ( hit_list[i][0] )
            self.hit_show.append (
                Tkinter.Label ( self.app, text=self.str_text[-1], compound='center', image=self.now_show_photo[-1] ) )
            p_size = self.getplace ( place_all[i] )
            self.hit_show[-1].place ( x=p_size[0], y=p_size[1] )

    def clac_show_place ( self, hit_list ) :
        place_all = []
        number = min ( len ( hit_list ), self.prize_num )
        # print number
        zone_sigle = self.show_zone / number
        new_start = self.show_start[0]
        new_place = 0.0
        photo_new = (self.persion_size[0] * 1.0) / (self.backim_size[0] * 2 * 1.0)
        for i in range ( number ) :
            new_place = [(new_start + zone_sigle / 2 - photo_new), self.show_start[1]]
            place_all.append ( new_place )
            new_start += zone_sigle
        return place_all

    def init_prize_menu_by_box ( self ) :
        self.comvalue = Tkinter.StringVar ()
        self.comboxlist = ttk.Combobox ( self.app, textvariable=self.comvalue )
        self.comboxlist["values"] = self.person.prize_menu
        self.comboxlist.current ( 2 )
        self.comboxlist.bind ( "<<ComboboxSelected>>", self.prize_chose )
        p_size = self.getplace ( self.prize_menu_place )
        self.comboxlist.place ( x=p_size[0], y=p_size[1] )

    def init_prize_menu ( self ) :
        self.meubar = Tkinter.Menu ( self.app )
        self.prize_bar = Tkinter.Menu ( self.meubar, tearoff=0 )
        self.prize_bar.add_command ( label="一等奖", command=self.prize_menu_chose_one )
        self.prize_bar.add_command ( label="二等奖", command=self.prize_menu_chose_two )
        self.prize_bar.add_command ( label="三等奖", command=self.prize_menu_chose_three )
        self.meubar.add_cascade ( label='奖项设置', menu=self.prize_bar )

    def prize_menu_chose_one ( self ) :
        print
        "enter config...  prize_menu_chose_one"
        self.prize_menu_chose ( 1 )

    def prize_menu_chose_two ( self ) :
        print
        "enter config...  prize_menu_chose_two"
        self.prize_menu_chose ( 2 )

    def prize_menu_chose_three ( self ) :
        print
        "enter config...  prize_menu_chose_two"
        self.prize_menu_chose ( 3 )

    def prize_menu_chose ( self, number ) :
        if number < 1 : print
        "error"
        self.prize_text.delete ( '1.0', Tkinter.END )
        self.prize_text.insert ( Tkinter.INSERT, self.person.prize_menu[number - 1] )
        self.clear_hit_show ()
        self.prize_num = number
        self.init_hit_list ( self.prize_num )
        self.add_hit_prize ( self.prize_hit_list )
        self.app.update ()

    def prize_chose ( self, *args ) :
        print ( self.comboxlist.get () )

    def init_button ( self ) :
        # start_photo = Tkinter.PhotoImage(file="start.gif")
        self.start_btn = Tkinter.Button ( self.app, text="开始", command=self.newtask, bg='gold' )
        p_size = self.getplace ( self.start_place )
        self.start_btn.place ( x=p_size[0], y=p_size[1], width=70, height=50 )

        self.restart_btn = Tkinter.Button ( self.app, text="重置", command=self.init_windows, font=("Arial", 5),
                                            bg='SeaGreen' )
        p_size = self.getplace ( self.reset_place )
        self.restart_btn.place ( x=p_size[0], y=p_size[1] )

    def test ( self ) :
        print
        "just test---"
        if self.isloop == True : return
        # number = 0
        # all_number = len(self.person.photo_f)
        if len ( self.person.photo_f ) == 0 :
            self.clear_hit_show ()
            msg.showwarning ( 'showwarning', '已经抽奖完了所有人' )
            return
        while True :
            if self.newloop == True :
                print
                "start chose hit..."
                self.newloop = False
                self.clear_hit_show ()
                self.chose_prize_hit ( self.person.photo_f )
                print
                self.prize_hit_list
                self.add_hit_prize ( self.prize_hit_list )
                time.sleep ( 0.1 )
                self.app.update ()
                time.sleep ( 0.1 )
                self.clear_hit_show ()
                print
                "end chose hit..."
                return
            # if all_number == (number+1):
            #    random.shuffle(self.person.photo_f)
            #    number = 0
            # number+=1
            self.srcoll_show ( self.person.photo_f )

    def test2 ( self ) :
        # self.srcoll_show(self.person.photo_f)
        # self.now_show_photo = []
        # self.str_text = []
        print
        'here 1'
        hit_list = self.person.photo_f
        random.shuffle ( hit_list )
        place_all = self.clac_show_place ( hit_list )
        for i in range ( self.prize_num ) :
            self.str_text[i] = hit_list[i][0]
            temp, _ = self.photo_size_set ( hit_list[i][1], self.persion_size )
            self.now_show_photo[i] = temp
            print
            'here 2'
            self.app.update ()
            time.sleep ( 2 )
            print
            'here 3'
            time.sleep ( 2 )
            print
            'here 4'

    def chose_prize_hit ( self, person_list ) :
        random.shuffle ( person_list )
        for i in range ( self.prize_num ) :
            if len ( person_list ) == 0 : break
            new = person_list[0]
            self.prize_hit_list.append ( new )
            person_list.remove ( new )

    def add_hit_prize ( self, hit_list ) :
        place_all = self.clac_show_place ( hit_list )
        self.clear_hit_show ()
        self.hit_show = []
        self.now_show_photo = []
        if len ( place_all ) < len ( hit_list ) : return
        print
        "now: place_all ", place_all
        for i in range ( len ( hit_list ) ) :
            now_photo, _ = self.photo_size_set ( hit_list[i][1], self.persion_size )
            self.now_show_photo.append ( now_photo )
            self.hit_show.append (
                Tkinter.Label ( self.app, text=hit_list[i][0], compound='center', image=self.now_show_photo[-1] ) )
            p_size = self.getplace ( place_all[i] )
            self.hit_show[-1].place ( x=p_size[0], y=p_size[1] )

    def clear_hit_show ( self ) :
        print
        self.hit_show
        for show in self.hit_show :
            # show.place_forget()
            show.destroy ()
            time.sleep ( 0.1 )
        self.now_show_photo = []
        self.prize_hit_list = []
        self.hit_show = []

    def srcoll_show ( self, person_list ) :

        random.shuffle ( person_list )
        time.sleep ( 0.05 )
        show_list = []
        for i in range ( self.prize_num ) :
            if len ( person_list ) <= i : break
            show_list.append ( person_list[i] )
        self.clear_hit_show ()
        self.add_hit_prize ( show_list )
        time.sleep ( 0.05 )
        self.app.update ()
        time.sleep ( 0.05 )

    def photo_resize ( self, photo_file, para ) :
        im = Image.open ( photo_file )
        print
        photo_file, " : ", im.size
        width = (float) ( im.size[0] ) * para
        height = (float) ( im.size[1] ) * para
        im = im.resize ( ((int) ( width ), (int) ( height )), Image.ANTIALIAS )
        return ImageTk.PhotoImage ( im ), im.size

    def photo_size_set ( self, photo_file, size ) :
        im = Image.open ( photo_file )
        print
        photo_file, " : ", im.size
        im = im.resize ( ((int) ( size[0] ), (int) ( size[1] )), Image.ANTIALIAS )
        return ImageTk.PhotoImage ( im ), im.size

    def getplace ( self, place ) :
        p_x = (float) ( self.backim_size[0] ) * place[0]
        p_y = (float) ( self.backim_size[1] ) * place[1]
        return [p_x, p_y]

    def newtask ( self ) :
        if self.isloop == False :
            # self.clear_hit_show()
            # 建立线程
            print
            "new..."
            t = threading.Thread ( target=self.test )
            # 开启线程运行
            t.start ()
            # 设置循环开始标志
            time.sleep ( 0.1 )
            self.isloop = True
        elif self.isloop == True :
            print
            "stop..."
            self.isloop = False
            self.newloop = True

    def start_new_thread ( self ) :
        t = threading.Thread ( target=self.thread_show )
        # 开启线程运行
        t.start ()
        # 设置循环开始标志
        time.sleep ( 0.1 )
        self.isloop = True

    # def


def main () :
    app_ui = APP_UI ()


if __name__ == '__main__' :
    main ()