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

``` python
figure = ex.box(data_frame=data, 
                y='<pandas_column_name>', 
                template='plotly_dark')

figure.show()
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