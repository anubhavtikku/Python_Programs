while(True):
    try:
        i=int(input("first no. "))
        j=int(input("second no. "))
        print("division of {} {} = {}".format(i,j,i/j))
    except (ValueError,IOError) as ob:
        print("only int values ")
        print(ob)

    except ZeroDivisionError:
        print("divide by zero ")

    except:
        print("error ..")

    else:
        break;
