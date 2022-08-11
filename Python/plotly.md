---
title: "Plotly"
tags: ""
---

# Histograms

``` python
figure = ex.histogram(data, 
                      x='<pandas_column_name>', 
                      title='<title>', 
                      labels={'x': '<feature_name>', 'y': 'Count'}, 
                      template='plotly_dark', 
                      height=500)

# Adjus the x-axis label rotation
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