---
title: "Plotly"
tags: ""
---

# Histograms

## Base
``` python
# Plot the Histogram of 'country' Distribution with respect to the Year
figure = ex.histogram(train_data, 
                      x='country', 
                      color='date_year',
                      title='Country pe Year Distribution', 
                      labels={'country':'Country',
                              'date_year': 'Year'},
                      barmode='group',
                      height=500,
                      histnorm='',
                      category_orders={'date_year': [2017, 2018, 2019, 2020]},
                      template='plotly_dark')

figure.update_layout(yaxis_title='Sales', 
                     font=dict(family="PT Sans", 
                               size=14), 
                     title_font=dict(family="PT Sans",
                                     size=30), 
                     title_x=0.7)

# Adjust the x-axis label rotation
figure.update_xaxes(tickangle=45)

figure.show()
```

## Top N Elements
``` python
top_n_countries = 10

# Compute the top 'top_n_countries' groups by size
top_countries_list = vp_users.groupby(['country']).size().to_frame().sort_values([0], ascending=False).head(top_n_countries).reset_index()['country'].to_list()
top_countries_count_list = vp_users.groupby(['country']).size().to_frame().sort_values([0], ascending=False).head(top_n_countries).reset_index()[0].to_list()

# Select row from the original DataFrame for having the 'Year' information
top_countries = vp_users[vp_users['country'].isin(top_countries_list)]

# Plot the Histogram of 'country' Distribution per year
figure = px.histogram(top_countries, 
                      x='country', 
                      color='created_at_year',
                      title='Top Country User Distribution per Year', 
                      labels={'country':'Country', 
                              'created_at_year': 'Year'},
                      height=500,
                      barmode='group',
                      category_orders={'created_at_year': [1970, 2019, 2020, 2021, 2022]},
                      color_discrete_sequence=px.colors.qualitative.Set3,
                      histnorm='',
                      template='plotly_dark')

figure.update_layout(yaxis_title='Share', 
                     font=dict(family="PT Sans", 
                               size=14), 
                     title_font=dict(family="PT Sans",
                                     size=30), 
                     title_x=0.7)

# Save figure
figure.write_json('./plots_vp_users/top_counstry_year_distribution.json')

# Read & plot figure
read_json('./plots_vp_users/top_counstry_year_distribution.json').show()
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
