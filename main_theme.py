import altair as alt

def main_theme():
    # Define Typography
    font = "Helvetica"

    # Define Colors
    main_palette = ["#4e79a7","#f28e2c","#e15759","#76b7b2","#59a14f","#edc949","#af7aa1","#ff9da7","#9c755f","#bab0ab"]
    sequential_palette = ["#c7e9b4", "#7fcdbb", "#41b6c4", "#1d91c0", "#225ea8", "#253494"]

    # Axes
    axisColor = "black"
    gridColor = "#DEDDDD"

    return {
        "config": {
            "background": "white",
            "title": {
                #"align": 'center',
                "fontSize": 18,
                "fontWeight": 'bold',
                #"font": font,
                "anchor": "middle",
                "color": "#000000",
                "orient": 'top',
                #"offset": 5,
                "subtitleColor": 'gray',
                #"subtitleFont": font,
                "subtitleFontWeight": 'normal',
                "subtitleFontSize": 16,
                "subtitlePadding": 2,
            },
            "header": {
                "labelFontWeight": "bold",
                "labelFontSize": 14,
                "labelOrient": 'top',
            },
            "axis": {
                "domain": True,
                "domainColor": axisColor,
                "domainWidth": 1,
                
                "grid": False,
                "gridColor": gridColor,
                "gridWidth": 0.5,
                
                "labels": True,
                #"labelFont": font,
                "labelFontSize": 12,
                "labelFlush": False,
                "labelFontWeight": 'light',
                "labelPadding": 2,
                
                "ticks": True,
                "tickCap": 'butt', #butt,round,or square
                "tickColor": axisColor,
                "tickSize": 4,
                "tickCount": 4,
                "tickWidth": 1,
                
                "titleColor": 'black',
                #"titleFont": font,
                "titleAlign": 'center',
                "titleFontWeight": 'bold',
                "titleFontSize": 14,
                "titlePadding": 5,
            },
            "legend": {
                #"labelFont": font,
                "labelFontSize": 14,
                "labelFontWeight": 'light',
                "symbolSize": 100,
                #"titleFont": font,
                "titleFontSize": 14,
                "titleFontWeight": 'bold',
                "padding": 5,
                "titleLimit": 200,
                "gradientLength": 100,
            },
            "range": {
                "category": main_palette,
                "diverging": sequential_palette,
            },
            "view": {
                "stroke": "transparent", # Remove the border around the visualization
            	"strokeWidth": 0,
            },
        	"text": {
            	#"font": 'Courier',
            	#"fontSize": 14,
        	}
        }
    }
