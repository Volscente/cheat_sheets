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

## XGBoost Callback
```python
from metaflow import step, FlowSpec, current, card, pypi_base, Parameter
from metaflow.cards import VegaChart, Markdown, ProgressBar


@pypi_base(
    packages={"altair": "5.2.0", "scikit-learn": "1.3.2", "xgboost": "2.0.3"},
    python="3.11.7",
)
class MonitorXgboostFlow(FlowSpec):
    num_epochs = Parameter("num_epochs", default=200)

    def fit_xgb(self, num_rounds, update_progress):
        import xgboost as xgb

        class ProgressCallback(xgb.callback.TrainingCallback):
            def after_iteration(self, model, epoch, evals_log):
                data = []
                for label in ("train", "valid"):
                    data.extend(
                        {"logloss": e, "label": label, "epoch": i}
                        for i, e in enumerate(evals_log[label]["mlogloss"])
                    )
                update_progress(epoch, data)

        m_train = xgb.DMatrix(self.train_data, self.train_labels)
        m_valid = xgb.DMatrix(self.valid_data, self.valid_labels)
        return xgb.train(
            {"objective": "multi:softmax", "num_class": self.num_classes},
            m_train,
            evals=[(m_train, "train"), (m_valid, "valid")],
            num_boost_round=num_rounds,
            callbacks=[ProgressCallback()],
        )

    def make_chart(self, data):
        import altair as alt

        source = alt.Data({"values": data})
        nearest = alt.selection_point(
            nearest=True, on="mouseover", fields=["epoch"], empty=False
        )
        line = (
            alt.Chart(source)
            .mark_line()
            .encode(x="epoch:Q", y="logloss:Q", color="label:N")
        )

        # the code below makes an interactive selector bar
        # see https://altair-viz.github.io/gallery/multiline_tooltip.html
        selectors = (
            alt.Chart(source)
            .mark_point()
            .encode(
                x="epoch:Q",
                opacity=alt.value(0),
            )
            .add_params(nearest)
        )
        points = line.mark_point().encode(
            opacity=alt.condition(nearest, alt.value(1), alt.value(0))
        )
        text = line.mark_text(align="left", dx=5, dy=-5).encode(
            text=alt.condition(nearest, "logloss:Q", alt.value(" "))
        )
        rules = (
            alt.Chart(source)
            .mark_rule(color="gray")
            .encode(
                x="epoch:Q",
            )
            .transform_filter(nearest)
        )
        return alt.layer(line, selectors, points, rules, text)

    @card
    @step
    def start(self):
        from sklearn.datasets import make_classification
        from sklearn.model_selection import train_test_split

        print("Generating test data..")
        self.num_classes = 4
        data, labels = make_classification(
            n_samples=100000,
            n_classes=self.num_classes,
            n_features=200,
            n_informative=5,
        )
        (
            self.train_data,
            self.valid_data,
            self.train_labels,
            self.valid_labels,
        ) = train_test_split(data, labels)
        self.next(self.train)

    @card(type="blank", refresh_interval=1)
    @step
    def train(self):
        def update_progress(epoch, data):
            progress.update(epoch + 1)
            chart.update(self.make_chart(data).to_dict())
            current.card.refresh()

        chart = VegaChart.from_altair_chart(self.make_chart([]))
        progress = ProgressBar(max=self.num_epochs, label="epochs")
        current.card.append(Markdown("# XGBoost training"))
        current.card.append(progress)
        current.card.append(chart)
        current.card.refresh()
        self.fit_xgb(self.num_epochs, update_progress)
        self.next(self.end)

    @step
    def end(self):
        pass


if __name__ == "__main__":
    MonitorXgboostFlow()
```

# Altair
## Scatter Plot (Static)
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

## Scatter Plot (Dynamic)
```python
from metaflow import step, FlowSpec, current, card, pypi
from metaflow.cards import VegaChart
import random
import math
import time


class UpdatingAltairFlow(FlowSpec):
    def point(self, i):
        t = math.radians(i)
        return {
            "x": 0.05 * math.exp(0.05 * t) * math.cos(t),
            "y": 0.05 * math.exp(0.05 * t) * math.sin(t),
        }

    @pypi(packages={"altair": "5.2.0", "vega-datasets": "0.9.0"}, python="3.11.7")
    @card(type="blank", refresh_interval=1)
    @step
    def start(self):
        import altair as alt

        data = []
        source = alt.Data({"values": data})
        alt_chart = (
            alt.Chart(source)
            .mark_circle(size=20)
            .encode(x="x:Q", y="y:Q")
            .interactive()
        )
        chart = VegaChart.from_altair_chart(alt_chart)
        current.card.append(chart)
        for i in range(30):
            data.extend(self.point(random.randint(0, 2000)) for i in range(50))
            chart.update(alt_chart.to_dict())
            current.card.refresh()
            time.sleep(0.5)

        self.next(self.end)

    @step
    def end(self):
        pass


if __name__ == "__main__":
    UpdatingAltairFlow()
```

# Data Analysis
## World Map
```python
from metaflow import step, FlowSpec, current, card
from metaflow.cards import VegaChart
from datetime import datetime
import random
import time
import math

# spec from https://altair-viz.github.io/gallery/choropleth.html
vega_spec = {
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "width": 600,
    "height": 400,
    "data": {
        "url": "https://vega.github.io/vega-lite/examples/data/us-10m.json",
        "format": {"type": "topojson", "feature": "counties"},
    },
    "transform": [
        {
            "lookup": "id",
            "from": {
                "data": {
                    "url": "https://vega.github.io/vega-lite/examples/data/unemployment.tsv"
                },
                "key": "id",
                "fields": ["rate"],
            },
        }
    ],
    "projection": {"type": "albersUsa"},
    "mark": {"type": "geoshape", "tooltip": True},
    "encoding": {"color": {"field": "rate", "type": "quantitative"}},
}


class MapChartFlow(FlowSpec):
    @card(type="blank")
    @step
    def start(self):
        chart = VegaChart(vega_spec)
        current.card.append(chart)
        self.next(self.end)

    @step
    def end(self):
        pass


if __name__ == "__main__":
    MapChartFlow()
```

## Add Multiple Contents Dynamically
```python
from metaflow import step, FlowSpec, current, card, pypi, profile
from metaflow.cards import Markdown, ProgressBar, Image

import random
import time


class FractalFlow(FlowSpec):
    def generate_fractal(self, seed):
        import pyfracgen as pf
        from matplotlib import colormaps

        xbound = (2.5, 3.4)
        ybound = (3.4, 4.0)
        res = pf.lyapunov(
            seed, xbound, ybound, width=4, height=3, dpi=250, ninit=2000, niter=500
        )
        img, _ = pf.images.markus_lyapunov_image(
            res, colormaps["GnBu"], colormaps["GnBu_r"], gammas=(8, 1)
        )
        return img

    @pypi(packages={"pyfracgen": "0.1.0"}, python="3.11.7")
    @card(type="blank")
    @step
    def start(self):
        progress = ProgressBar(max=5, label="Fractals generated")
        current.card.append(progress)
        for i in range(6):
            seed = "".join(random.choice("AB") for i in range(8))
            progress.update(i)
            caption = Markdown(f"# Generating {seed}...")
            current.card.append(caption)
            current.card.refresh()
            t = time.time()
            frac = self.generate_fractal(seed)
            n = int(1000 * (time.time() - t))
            caption.update(f"# Fractal {seed} took {n} ms")
            current.card.append(Image.from_matplotlib(frac))
        self.next(self.end)

    @step
    def end(self):
        pass


if __name__ == "__main__":
    FractalFlow()
```