from formagenerica import FormaGenerica

class Rettangolo(FormaGenerica):

    # inizializzare un oggetto della classe Rettangolo
    def __init__(self):
        super().__init__()

        self.setShape("rettangolo")

    def draw(self) -> None:
        
        print(f"\n{set.getShape()}\n")

        # outer for
        for i in range(5):

            # inner for
            for j in range(5*2):

                #lato a e lato b del rettangolo
                if i == 0 or i == 5-1: 
                    print("*", end = " ")

                # latoc e lato b del rettangolo
                elif j == 0 or j == (5*2) - 1:
                    print("*", end = " ")
                
                # stampare spiazi bianchi
                else:
                    print(" ")
        
        print("\n", end = " ")