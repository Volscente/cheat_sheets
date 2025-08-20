# Training Dynamic Effects
## Progression Bar
```python
from metaflow import step, FlowSpec, current, card
from metaflow.cards import Markdown, ProgressBar


class ClockFlow(FlowSpec):
    @card(type="blank", refresh_interval=1)
    @step
    def start(self):
        from datetime import datetime
        import time

        m = Markdown("# Clock is starting 🕒")
        p = ProgressBar(max=30, label="Seconds passed")
        current.card.append(m)
        current.card.append(p)
        current.card.refresh()
        for i in range(31):
            t = datetime.now().strftime("%H:%M:%S")
            m.update(f"# Time is {t}")
            p.update(i)
            current.card.refresh()
            print(t)
            time.sleep(1)
        m.update("# ⏰ ring ring!")
        self.next(self.end)

    @step
    def end(self):
        pass


if __name__ == "__main__":
    ClockFlow()
```

## Bar Line
```python
from metaflow import step, FlowSpec, current, card
from metaflow.cards import VegaChart
from datetime import datetime
import random
import time
import math

vega_spec = {
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "data": {"values": []},
    "mark": "line",
    "encoding": {
        "x": {"field": "time", "type": "temporal"},
        "y": {"field": "value", "type": "quantitative"},
    },
}


class SimpleChartFlow(FlowSpec):
    @card(type="blank", refresh_interval=1)
    @step
    def start(self):
        data = vega_spec["data"]["values"]
        chart = VegaChart(vega_spec)
        current.card.append(chart)
        for i in range(30):
            val = math.sin(i * 0.1) + random.random() * 0.1 - 0.05
            data.append({"time": datetime.now().isoformat(), "value": val})
            chart.update(vega_spec)
            current.card.refresh()
            time.sleep(1)
        self.next(self.end)

    @step
    def end(self):
        pass


if __name__ == "__main__":
    SimpleChartFlow()
```

# Altair
## Scatter Plot
```python
from metaflow import step, FlowSpec, current, card, pypi
from metaflow.cards import VegaChart

# An interactive Altair example from
# https://altair-viz.github.io/gallery/selection_histogram.html
class AltairFlow(FlowSpec):
    @pypi(packages={"altair": "5.2.0", "vega-datasets": "0.9.0"}, python="3.11.7")
    @card(type="blank")
    @step
    def start(self):
        import altair as alt
        from vega_datasets import data

        source = data.cars()
        brush = alt.selection_interval()
        points = (
            alt.Chart(source, width=500, height=400)
            .mark_point()
            .encode(
                x="Horsepower:Q",
                y="Miles_per_Gallon:Q",
                color=alt.condition(brush, "Origin:N", alt.value("lightgray")),
            )
            .add_params(brush)
        )

        bars = (
            alt.Chart(source)
            .mark_bar()
            .encode(y="Origin:N", color="Origin:N", x="count(Origin):Q")
            .transform_filter(brush)
        )

        chart = VegaChart.from_altair_chart(points & bars)
        current.card.append(chart)
        self.next(self.end)

    @step
    def end(self):
        pass


if __name__ == "__main__":
    AltairFlow()
```