#import pandas to read excel
import pandas as pd
#import matplotlib to plot
import matplotlib.pyplot as plt

def graph():
    #change file path and read excel
    file_path= "C:\\Users\\imman\\Downloads\\FinSample.xlsx"
    data = pd.read_excel(file_path)

    # Preprocess the profit column
    def change_profit(value):
        if isinstance(value, str):
            #convert brackets to negative
            value = value.replace('(', '-').replace(')', '')
            #convert dashes to zero
            value = value.replace('-', '0') if value == '-' else value  # Convert dashes to zero
        return float(value)

    # Apply the preprocessing to the 'Profit' column
    data['Profit'] = data['Profit'].apply(change_profit)

    #get the total profit and units sold by country
    profit_totals = data.groupby('Country')['Profit'].sum()
    units_sold_totals = data.groupby('Country')['Units Sold'].sum()

    def profit_graph():
        country_sums = profit_totals

        # set my x and y values
        x = country_sums.index
        y = country_sums.values

        #setup the graph
        ax.clear()
        ax.bar(x,y,color='green')
        ax.set_xlabel('Country',fontweight='bold')
        ax.set_ylabel('Profit ($)',fontweight='bold')
        ax.set_title('Profit of Countries in 2013/2014')
        ax.grid(True)

        fig.canvas.draw()

    # Function to plot units sold
    def plot_units_sold():
        country_sums = units_sold_totals
        x = country_sums.index
        y = country_sums.values

        ax.clear()
        ax.bar(x, y, color='blue')
        ax.set_xlabel('Country',fontweight='bold')
        ax.set_ylabel('Units Sold',fontweight='bold')
        ax.set_title('Units Sold by Countries in 2013/2014')
        ax.grid(True)

        fig.canvas.draw()

    # Toggle between profit and units sold
    def toggle_view(event):
        nonlocal toggle
        if event.key == 'c':
            toggle = not toggle
            if toggle:
                profit_graph()
            else:
                plot_units_sold()

    # Initial plot
    fig, ax = plt.subplots()
    toggle = True
    profit_graph()

    # Connect the key press event to the toggle function
    fig.canvas.mpl_connect('key_press_event', toggle_view)

    # Print total profit and total units sold for each country
    for country, profit, units_sold in zip(profit_totals.index, profit_totals.values, units_sold_totals.values):
        print(f'Total profit for {country}: ${profit:.2f}')
        print(f'Total units sold for {country}: {units_sold}')

    plt.show()

#plot it
graph()