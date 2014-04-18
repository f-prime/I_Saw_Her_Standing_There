onground = True
walls = []
zombies = []
player = None
her = None
cage = None
moving = False
levels = ["levels/1.map", "levels/2.map", "levels/3.map", "levels/4.map", "levels/5.map", "levels/6.map", "levels/7.map"]
level = 0
infected = False
captured = False
resolution = (1024, 800)
jump = 0
her_moving_right = False
her_moving_left = False
i_died = False
she_died = False
next_ = 0
next_go = False

text = {
        
        0:{
            0:[["I loved her...", (50, 50)]],
            1:[["I loved her... but she was a zombie.", (50, 50)]], # Double array for multiple texts
            2:[["So I put her in a cage where she would be safe.", (50, 50)]],
            3:[["But I died before I could tell her...", (50, 50)]], # I died
            4:[["But I wasn't careful so she got away...", (50, 50)]] # She died
        }, 
        
        1:{

            0:[["I knew she loved me too...", (50, 50)]],
            1:[["I knew she loved me too...", (50, 50)], ["Because she would always try to hug me.", (50, 100)]],
            2:[["But I could never get too close.", (50, 50)]],
            3:[["But I died...", (50, 50)]],
            4:[["I had to let her die...", (50, 50)]],

        },


        2:{
            0:[["She likes to sit just out of reach...", (50, 50)]],
            1:[["But when she sees me she comes running.", (50, 50)]],
            2:[["It saddens me.", (50, 50)]],
            3:[["And I am gone...", (50, 50)]],
            4:[["Now I'm it", (50,50)]]

        },



        3:{

            0:[["Our world is dangerous...", (50, 50)]],
            1:[["Our world is dangerous...", (50, 50)], ["There are plenty of holes.", (50, 110)]],
            2:[["Just don't let her fall.", (50, 50)]],
            3:[["Did you fall?", (50, 50)]],
            4:[["She is gone..."]],

        },


        4:{

            0:[["There were others too...", (50, 50)]],
            1:[["There were others too... they didn't like me.", (50, 50)]],
            2:[["And I didn't like them.", (50, 50)]],
            3:[["So they killed me...", (50, 50)]],
            4:[["So she left me.", (50, 50)]],
        
        },

        5: {

            0:[["They guarded her well..", (50, 50)]],
            1:[["They guarded her well.. But I found ways around it.", (50, 50)]],
            2:[["I conqured them all.", (50, 50)]],
            3:[["I did not fight hard enough.", (50, 50)]],
            4:[["How could I have been so foolish...", (50, 50)]],

        },


        6:{

            0:[["She keeps escaping her cage.", (50, 50)]],
            1:[["She keeps escapign her cage. I don't mind.", (50, 50)]],
            2:[["It is just our little game.", (50, 50)]],
            3:[["I guess it wasn't meant to be.", (50, 50)]],
            4:[["I drove her away...", (50, 50)]]


        },

}
