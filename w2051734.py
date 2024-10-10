def menu():
    global pass_credit , defer_credit, fail_credit, total_count, exclude_count, progress_count, trailer_count, retriever_count
    progress_count = 0
    trailer_count = 0
    exclude_count = 0
    retriever_count = 0
    total_count = 0
    pass_credit = 0
    defer_credit = 0
    fail_credit = 0
    list_1 = []

    version = int(input("For student version, enter 1 \n For staff version enter 2 \n Enter your choice : "))
    if version == 1:
        try:
            pass_credit = int(input("please enter your credits at pass: "))
            if (not 0 <= pass_credit <= 120) or (pass_credit % 20 != 0):
                print("out of range")
                exit()
            defer_credit = int(input("Please enter your credits at defer: "))
            if (not 0<= defer_credit <= 120) or (defer_credit % 20 != 0):
                print("out of range")
                exit()
            fail_credit = int(input("Please enter your credits at fail: "))
            if (not 0<= fail_credit <= 120) or (fail_credit % 20 != 0):
                print("Out of range")
                exit()
            
            if pass_credit + defer_credit + fail_credit != 120:
                print("Total incorrect")
                
            elif pass_credit == 120:
                print("progression outcome: Progress")
                exit()
            elif pass_credit == 100:
                print("progression outcome: progress(Module Trailer) ")
                exit()
            elif fail_credit >= 80 :
                print("progression outcome: Exclude")
                exit()
            elif pass_credit <= 80 and fail_credit <= 60:
                print("progression outcome: Module Retriever")
                exit()
     
                
        except ValueError:
            print("Integer Required") 

   

    elif version == 2:
        
      
        while True:
            try:
                pass_credit = int(input("please enter your credits at pass: "))
                if (not 0 <= pass_credit <= 120) or (pass_credit % 20 != 0):
                    print("out of range")
                    continue
                defer_credit = int(input("Please enter your credits at defer: "))
                if (not 0<= defer_credit <= 120) or (defer_credit % 20 != 0):
                    print("out of range")
                    continue
                fail_credit = int(input("Please enter your credits at fail: "))
                if (not 0<= fail_credit <= 120) or (fail_credit % 20 != 0):
                    print("Out of range")
                    continue
            
                if pass_credit + defer_credit + fail_credit != 120:
                    print("Total incorrect")
                
                elif pass_credit == 120:
                    print("progression outcome: Progress")
                    progress_count = progress_count + 1
                    total_count = total_count + 1
                    result = "progress"
                elif pass_credit == 100:
                    print("progression outcome: progress(Module Trailer) ")
                    trailer_count = trailer_count + 1
                    total_count = total_count + 1
                    result = "progress(Module Trailer)"
                elif fail_credit >= 80 :
                    print("progression outcome: Exclude")
                    exclude_count = exclude_count + 1
                    total_count = total_count + 1
                    result = "Exclude"
                elif pass_credit <= 80 and fail_credit <= 60:
                    print("progression outcome: Module Retriever")
                    retriever_count = retriever_count + 1
                    total_count = total_count + 1
                    result = "Module Retriever"

                list_1.append([result,pass_credit, defer_credit, fail_credit])

                with open ("outcomes.txt","w") as file:
                    for entry in list_1:
                        file.write(f"{entry[0]}- {entry[1]},{entry[2]},{entry[3]}\n")

         
            
                
            except ValueError:
                print("Integer Required")
                return menu()
            print("Would you like to enter another set of data ?")
            choice = str(input("Enter 'y' for yes or 'q' to quite and view results: "))
            if choice.lower() == 'q':
                with open ("outcomes.txt","r") as file:
                    print(file.read())
          
            
                break
            elif choice.lower() == 'y':
                continue
            else:
                print("Invalid Input")
        

        
menu()

from graphics import GraphWin, Rectangle, Text , Point , Line
def show_histogram():
    win = GraphWin("Progression Outcome", 800,600)
    names = ["progress", "Trailer", "Module Retriever", "Exclude"]
    win.setBackground("white")

    

    
    

    #bar widths
    bar_width = 60
    bar_spacing = 100

    #starting x-cordinate for the first bar
    x = 40

    colors = ["green", "yellow", "red", "blue"]
    total_count = progress_count + trailer_count + exclude_count + retriever_count

    for i in range(len([progress_count, trailer_count, retriever_count, exclude_count])):
        #calculate the height and position
        count = [progress_count, trailer_count, retriever_count, exclude_count][i]
        height = 400 * count /total_count

        
        #create bar Rectangle
        bar = Rectangle(Point(x, 500), Point(x + bar_width, 500 - height))
        bar.setFill(colors[i])
        bar.draw(win)

        #Display height and value at the top of the bar
        text = Text(Point(x + bar_width-20, 500 - height - 10), str(count))
        text.draw(win)

        #Display bar name at the bottom below x axis
        Text(Point(x + bar_width / 2, 525), names[i]).draw(win)

        #Update the x cordinate for the next bar
        x += bar_width + bar_spacing

        #X axis
        Line(Point(40, 500), Point(x - bar_spacing, 500)).draw(win)

        #Display the title
        topic_text = Text(Point(250, 20), "Histogram Results")
        topic_text.setSize(16)
        topic_text.draw(win)

        #Display total below the X axis
        total_count_text = Text(Point(275, 570), f"Total Count: {total_count}" )
        total_count_text.setSize(14)
        total_count_text.draw(win)

        

show_histogram()



