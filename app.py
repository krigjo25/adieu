#   Import responsories

from inflect import engine

def main():

    #  Declaring variable
    x = type(None)

    while True:

        #  Prompting user for input
        x = str(input('Name(s) :')).capitalize()

        if len(x) > 0: break 

    print(f"Adieu, adieu to {engine().join([i.strip().title() for i in x.split(',')], final_sep=',')}")

if __name__ == "__main__":
    main()
