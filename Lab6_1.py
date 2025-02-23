from ConnectFour import ConnectFour 

x=int(input("Enter how many rows for this game: "))

game= ConnectFour(x)

game.print_game()


def gaming():

    while True:

        for i in ["X" , "O"]:

            move= int(input("player" + i + "Enter a number: "))

            while game.is_column_full(move)== True or game.does_column_exist(move)== False:

                move= int(input("player" + i +"Enter a number: "))


            game.make_move(move)

            game.print_game()

            if game.get_winner()!= " ":

                print(game.get_winner() + " is the winner")

                return

gaming()
