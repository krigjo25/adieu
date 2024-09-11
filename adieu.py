#   Import responsories
import inflect

def main():

    #   Initializing lists
    name = []

    while True:

        try:
            #   Prompt user for name
            x = str(input('name :')).capitalize()
            if len(x) == 0: raise EOFError()

        except EOFError:
            break

        #   Append name
        name.append(x)

    print(f'Adieu, adieu, to {inflect.engine().join(name, final_sep=",")}')

if __name__ == "__main__":
    main()
