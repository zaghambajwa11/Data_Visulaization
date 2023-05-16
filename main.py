def select_chart():
    print("Start your data visualization journey!")
    data_type = input("Is your data categorical or numerical? Enter 'c' for categorical or 'n' for numerical: ")
    
    if data_type.lower() == 'c':
        print("Is your data nominal or ordinal?")
        data_subtype = input("Enter 'n' for nominal or 'o' for ordinal: ")
        
        if data_subtype.lower() == 'n':
            print("Do you want to show the frequency or distribution of categories?")
            frequency_or_distribution = input("Enter 'f' for frequency or 'd' for distribution: ")
            
            if frequency_or_distribution.lower() == 'f':
                return "Bar chart"
            elif frequency_or_distribution.lower() == 'd':
                print("Which chart style do you prefer?")
                chart_style = input("Enter 'p' for pie chart, 'd' for donut chart, or 's' for stacked bar chart: ")
                if chart_style.lower() == 'p':
                    return "Pie chart"
                elif chart_style.lower() == 'd':
                    return "Donut chart"
                elif chart_style.lower() == 's':
                    return "Stacked bar chart"
        
        elif data_subtype.lower() == 'o':
            print("Do you want to show the order or rank of categories?")
            order_or_rank = input("Enter 'o' for order or 'r' for rank: ")
            
            if order_or_rank.lower() == 'o':
                return "Ordered bar chart"
            elif order_or_rank.lower() == 'r':
                print("Which chart style do you prefer?")
                chart_style = input("Enter 'd' for dot plot, 'r' for ranked bar chart, or 'l' for ladder chart: ")
                if chart_style.lower() == 'd':
                    return "Dot plot"
                elif chart_style.lower() == 'r':
                    return "Ranked bar chart"
                elif chart_style.lower() == 'l':
                    return "Ladder chart"
    
    elif data_type.lower() == 'n':
        print("What is the nature of your numerical data?")
        nature_of_data = input("Enter 'o' for one variable, 't' for two variables, or 'm' for more than two variables: ")
        
        if nature_of_data.lower() == 'o':
            print("Do you want to show the distribution or comparison of values?")
            distribution_or_comparison = input("Enter 'd' for distribution or 'c' for comparison: ")
            
            if distribution_or_comparison.lower() == 'd':
                print("Which chart style do you prefer?")
                chart_style = input("Enter 'h' for histogram, 'b' for box plot, or 'dp' for density plot: ")
                if chart_style.lower() == 'h':
                    return "Histogram"
                elif chart_style.lower() == 'b':
                    return "Box plot"
                elif chart_style.lower() == 'dp':
                    return "Density plot"
                
            elif distribution_or_comparison.lower() == 'c':
                print("Which chart style do you prefer?")
                chart_style = input("Enter 'b' for bar chart, 'l' for line chart, or 'a' for area chart: ")
                if chart_style.lower() == 'b':
                    return "Bar chart"
                elif chart_style.lower() == 'l':
                    return "Line chart"
                elif chart_style.lower() == 'a':
                    return "Area chart"
        
        elif nature_of_data.lower() == 't':
            print("Do you want to show the relationship or comparison between variables?")
            relationship_or_comparison = input("Enter 'r' for relationship or 'c' for comparison: ")
        
        if relationship_or_comparison.lower() == 'r':
            print("Which chart style do you prefer?")
            chart_style = input("Enter 's' for scatter plot, 'b' for bubble chart, or 'h' for heatmap: ")
            if chart_style.lower() == 's':
                return "Scatter plot"
            elif chart_style.lower() == 'b':
                return "Bubble chart"
            elif chart_style.lower() == 'h':
                return "Heatmap"
            
        elif relationship_or_comparison.lower() == 'c':
            print("Which chart style do you prefer?")
            chart_style = input("Enter 'g' for grouped bar chart, 'l' for line chart, or 'a' for area chart: ")
            if chart_style.lower() == 'g':
                return "Grouped bar chart"
            elif chart_style.lower() == 'l':
                return "Line chart"
            elif chart_style.lower() == 'a':
                return "Area chart"
    
    elif nature_of_data.lower() == 'm':
        print("Do you want to show patterns or trends in multivariate data?")
        patterns_or_trends = input("Enter 'p' for patterns or 't' for trends: ")
        
        if patterns_or_trends.lower() == 'p':
            print("Which chart style do you prefer?")
            chart_style = input("Enter 'h' for heatmap, 'c' for clustered bar chart, or 'pc' for parallel coordinates: ")
            if chart_style.lower() == 'h':
                return "Heatmap"
            elif chart_style.lower() == 'c':
                return "Clustered bar chart"
            elif chart_style.lower() == 'pc':
                return "Parallel coordinates"
            
        elif patterns_or_trends.lower() == 't':
            print("Which chart style do you prefer?")
            chart_style = input("Enter 'l' for line chart, 'a' for area chart, or 'sg' for streamgraph: ")
            if chart_style.lower() == 'l':
                return "Line chart"
            elif chart_style.lower() == 'a':
                return "Area chart"
            elif chart_style.lower() == 'sg':
                return "Streamgraph"
            
    else:
        print("Invalid input!")

print("Invalid input!")



selected_chart = select_chart()
print("Selected chart:", selected_chart)
    
