import altair as alt

def offset_theme():
    # Define Colors
    main_palette = ["#4e79a7","#f28e2c","#e15759","#76b7b2","#59a14f","#edc949","#af7aa1","#ff9da7","#9c755f","#bab0ab"]
    sequential_palette = ["#c7e9b4", "#7fcdbb", "#41b6c4", "#1d91c0", "#225ea8", "#253494"]

    # Axes
    axisColor = "#000000"
    gridColor = "#DEDDDD"

    return {
        "config": { #https://altair-viz.github.io/user_guide/generated/core/altair.Config.html#altair.Config
            "autosize": "fit",
            "font": "Helvetica",
            "title": {
                "fontSize": 18,
                "fontWeight": "bold",
                "anchor": "middle",
                "color": "#000000",
                "orient": "top",
                "subtitleColor": gridColor,
                "subtitleFontWeight": "normal",
                "subtitleFontSize": 16,
                "subtitlePadding": 2,
            },
            "header": {
                "labelFontWeight": "bold",
                "labelFontSize": 14,
                "labelOrient": "top",
            },
            "axis": {
                "domain": True,
                "domainCap": "square",
                "domainColor": axisColor,
                "domainWidth": 1,
                "grid": False,
                "gridCap": "square",
                "gridColor": gridColor,
                "gridOpacity": 1,
                "gridWidth": 0.5,
                "labels": True,
                "labelFontSize": 12,
                "labelFlush": False,
                "labelFontWeight": "normal",
                "labelPadding": 2,
                "ticks": True,
                "tickCap": "butt",
                "tickColor": axisColor,
                "tickSize": 4,
                "tickCount": 4,
                "tickWidth": 1,
                "titleColor": axisColor,
                "titleAlign": "center",
                "titleFontWeight": "bold",
                "titleFontSize": 14,
                "titlePadding": 2,
            },
            "legend": {
                "labelFontSize": 14,
                "labelFontWeight": "lighter",
                "symbolSize": 100,
                "titleFontSize": 14,
                "titleFontWeight": "bold",
                "padding": 5,
                "titleLimit": 200,
                "gradientLength": 100,
            },
            "range": {
                "category": main_palette,
                "diverging": sequential_palette,
            },
            "view": { #https://altair-viz.github.io/user_guide/generated/core/altair.ViewConfig.html#altair.ViewConfig
                "strokeWidth": 0, # Remove the border around the visualization
                "continuousWidth": 300,
                "continuousHeight": 300,
            },
        }
    }
