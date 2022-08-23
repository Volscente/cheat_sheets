---
title: "Plotly"
tags: ""
---

# Histograms

``` python
# Plot the Histogram of 'vp_region' Distribution with respect to the Year
figure = ex.histogram(vp_users, 
                      x='vp_region', 
                      color='created_at_year',
                      title='Vendor Portal Region Distribution', 
                      labels={'vp_region':'Region',
                              'created_at_year': 'Year'},
                      barmode='group',
                      height=500,
                      histnorm='',
                      category_orders={'created_at_year': [1970, 2019, 2020, 2021, 2022]},
                      template='plotly_dark')

figure.update_layout(yaxis_title='Share', 
                     font=dict(family="PT Sans", 
                               size=14), 
                     title_font=dict(family="PT Sans",
                                     size=30), 
                     title_x=0.7)

# Adjust the x-axis label rotation
figure.update_xaxes(tickangle=45)

figure.show()
```



<br>

# Box Plot

## Single Box Plot
``` python
# Plot boxplot of 'loading'
figure = px.box(train_data, 
                x='loading', 
                title='Loading Distribution',
                color_discrete_sequence=['darkgreen'],
                template='plotly_dark')

figure.update_layout(font=dict(family="PT Sans", 
                               size=14), 
                     title_font=dict(family="PT Sans",
                                     size=30), 
                     title_x=0.5)

# Save figure
figure.write_json("./plots/loading_distribution.json")

# Read & plot figure
read_json('./plots/loading_distribution.json').show()
```

## Multiple Boxplot
``` python
# Plot the 'loading' distribution with respect to the 'product_code'
figure = px.box(train_data, 
                x='product_code', 
                y='loading',
                points='all',
                color='product_code',
                title='Loading Distribution per Product Code',
                color_discrete_sequence=px.colors.qualitative.Set3,
                height=500,
                template='plotly_dark')

figure.update_layout(font=dict(family="PT Sans", 
                               size=14), 
                     title_font=dict(family="PT Sans",
                                     size=30), 
                     title_x=0.5)

# Save figure
figure.write_json("./plots/loading_product_code_distribution.json")

# Read & plot figure
read_json('./plots/loading_product_code_distribution.json').show()
```

<br>

# Pie Chart

``` python
figure = ex.pie(data, 
                names='<pandas_column_name>', 
                title='<title>', 
                template='plotly_dark')

figure.show()
```

<br>

# Bar Chart

``` python
# Plot the models' performance
figure = ex.bar(performance, 
                x=performance.index, 
                y=performance.columns.values, 
                barmode='group', 
                title='Models Comparison', 
                labels={'x':'Model', 'y':'Performance'}, 
                template='plotly_dark')

figure.show()
```

# Line Charts

## Multiple Plots

``` python
# Define subplots
figure = make_subplots(rows=2, 
                       cols=2, 
                       subplot_titles=('Creation Date over Years', 
                                       'Creation Date over Months', 
                                       'Creation Date over Days', 
                                       'Creation Date over Weekdays'))


figure.add_trace(go.Scatter(x=vp_users.groupby(['created_at_year']).size().sort_index().index.to_list(),
                            y=vp_users.groupby(['created_at_year']).size().sort_index().to_list(), 
                            mode='lines', 
                            name='Yearly'),
                 row=1, 
                 col=1)

figure.add_trace(go.Scatter(x=vp_users.groupby(['created_at_month']).size().sort_index().index.to_list(),
                            y=vp_users.groupby(['created_at_month']).size().sort_index().to_list(), 
                            mode='lines', 
                            name='Monthly'), 
                 row=1, 
                 col=2)

figure.add_trace(go.Scatter(x=vp_users.groupby(['created_at_day']).size().sort_index().index.to_list(),
                            y=vp_users.groupby(['created_at_day']).size().sort_index().to_list(), 
                            mode='lines',  
                            name='Daily'), 
                 row=2, 
                 col=1)

figure.add_trace(go.Scatter(x=vp_users.groupby(['created_at_dayofweek']).size().sort_index().index.to_list(),
                            y=vp_users.groupby(['created_at_dayofweek']).size().sort_index().to_list(), 
                            mode='lines', 
                            name='Days of Week'), 
                 row=2, 
                 col=2)

figure.update_layout(yaxis_title='Share', 
                     font=dict(family="PT Sans", 
                               size=14), 
                     title_font=dict(family="PT Sans",
                                     size=30), 
                     title_x=0.7, 
                     height=1000, 
                     template='plotly_dark')

figure.show()
```

# Save & Read Plots

``` python
# Save figure
figure.write_json('./plots/<plot_name>.json')

# Read & plot figure
read_json('./plots/<plot_name>.json').show()
```
