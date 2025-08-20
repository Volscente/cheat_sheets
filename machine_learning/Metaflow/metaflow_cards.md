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

## Read from Event Generator
```python
from metaflow import step, FlowSpec, current, card, pypi
from metaflow.cards import VegaChart, Markdown, Artifact

import time
import json
from collections import Counter, defaultdict
from datetime import datetime


class WikiEventsFlow(FlowSpec):
    def event_stream(self):
        import requests
        import sseclient

        # retrieve real-time page edit events from Wikipedia
        URL = "https://stream.wikimedia.org/v2/stream/recentchange"
        resp = requests.get(URL, stream=True)
        client = sseclient.SSEClient(resp)
        counts = Counter()
        log = defaultdict(list)
        last_update = 0
        for event in client.events():
            try:
                body = json.loads(event.data)
                if (
                    body["meta"]["domain"] == "en.wikipedia.org"
                    and ":" not in body["title"]
                ):
                    # bucket events in 5-second bins
                    key = (body["timestamp"] // 5) * 5
                    counts[key] += 1
                    log[key].append(body["title"][:20])
                    if time.time() - last_update > 5:
                        # update the chart every 5 seconds
                        yield counts, log
                        last_update = time.time()
            except:
                continue

    @pypi(packages={"altair": "5.2.0", "sseclient-py": "1.8.0"}, python="3.11.7")
    @card(type="blank")
    @step
    def start(self):
        import altair as alt

        FOLLOW_SECONDS = 45
        data = []
        source = alt.Data({"values": data})
        chart = alt_chart = None
        begin = time.time()
        current.card.append(Markdown("# Listening to Wikipedia events.."))
        countbox = Markdown("0 events observed")
        current.card.append(countbox)
        current.card.refresh()
        for counts, log in self.event_stream():
            # format data
            data.clear()
            data.extend(
                {
                    "time": datetime.fromtimestamp(t).isoformat(),
                    "event_count": c,
                    "log": ", ".join(log[t]),
                }
                for t, c in sorted(counts.items())
            )
            if chart is None:
                # format data
                first_event = min(counts)
                min_t = datetime.fromtimestamp(first_event - 10).isoformat()
                max_t = datetime.fromtimestamp(
                    first_event + FOLLOW_SECONDS + 10
                ).isoformat()
                alt_chart = (
                    alt.Chart(source)
                    .mark_bar(width={"band": 10.0})
                    .encode(
                        x=alt.X("time:T", scale=alt.Scale(domain=(min_t, max_t))),
                        y="event_count:Q",
                        tooltip=["log:N"],
                    )
                )
                chart = VegaChart.from_altair_chart(alt_chart)
                current.card.append(chart)
                current.card.append(Markdown("Point at a bar to see pages edited"))
            else:
                chart.update(alt_chart.to_dict())
            countbox.update(f"{sum(counts.values())} events observed")
            current.card.refresh()
            if time.time() - begin > 45:
                break
        self.next(self.end)

    @step
    def end(self):
        pass


if __name__ == "__main__":
    WikiEventsFlow()
```

## Custom Dynamic Progress Bar
```python
import time
import copy
import random

from metaflow import FlowSpec, step, card, current
from metaflow.cards import Markdown, Table, VegaChart


class SparklinesFlow(FlowSpec):
    @card(type="blank", refresh_interval=1)
    @step
    def start(self):
        sparks = []
        rows = []
        for i in range(1, 7):
            spark = RandomSpark(index=i)
            sparks.append(spark)
            rows.append([spark.label, spark.chart])
        current.card.append(Table(rows))
        current.card.refresh()

        for i in range(MAX):
            time.sleep(1)
            for spark in sparks:
                spark.advance()
            current.card.refresh()
        self.next(self.end)

    @step
    def end(self):
        print("done")


# Sparkline as a Vega Lite spec
MAX = 30
SPARKSPEC = {
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "data": {"values": []},
    "height": 20,
    "width": 400,
    "mark": {"type": "area"},
    "encoding": {
        "x": {
            "field": "x",
            "type": "quantitative",
            "scale": {"domain": [0, MAX - 1]},
            "axis": {
                "title": None,
                "orient": "top",
                "domain": False,
                "ticks": False,
                "labels": False,
                "grid": False,
            },
        },
        "y": {
            "field": "y",
            "aggregate": "sum",
            "type": "quantitative",
            "axis": {
                "title": None,
                "domain": False,
                "labels": False,
                "ticks": False,
                "grid": False,
            },
        },
    },
}


class RandomSpark:
    def __init__(self, max_len=MAX, index=0):
        self.max_len = max_len
        self.spec = copy.deepcopy(SPARKSPEC)
        self.speed = random.randint(3, MAX // 6)
        self.data = [{"x": 0, "y": 0}]
        self.index = index
        self.label = Markdown(f"### Updating {self.index}")
        self.spec["data"]["values"] = self.data
        self.chart = VegaChart(self.spec)

    def advance(self):
        import random

        for i in range(self.speed):
            if len(self.data) < self.max_len:
                new_val = max(0, self.data[-1]["y"] + random.randint(-1, 3))
                self.data.append({"x": len(self.data), "y": new_val})
        if len(self.data) == self.max_len:
            self.spec["mark"]["color"] = "green"
            self.label.update(f"### Done updating {self.index}")
        self.chart.update(self.spec)


if __name__ == "__main__":
    SparklinesFlow()
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

# Thread & Processes
## Monitor a Thread
```python
from metaflow import step, FlowSpec, current, card, pypi, profile
from metaflow.cards import VegaChart, Markdown, Table

import time
from tempfile import NamedTemporaryFile
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

URL = (
    "https://metaflow-demo-public.s3.us-west-2.amazonaws.com"
    "/taxi/sandbox/train_sample.parquet"
)


class DuckDBFlow(FlowSpec):
    def exec_duckdb(self, stats):
        # this function runs in a separate thread
        import duckdb
        import requests

        with NamedTemporaryFile(suffix=".parquet") as tmp:
            with profile("download", stats_dict=stats):
                tmp.write(requests.get(URL).content)
            tmp.flush()
            with profile("create_table", stats_dict=stats):
                duckdb.sql("CREATE TABLE taxi AS SELECT * FROM '%s'" % tmp.name)
                for i in range(20):
                    duckdb.sql("INSERT INTO taxi SELECT * FROM '%s'" % tmp.name)

        time.sleep(5)
        with profile("query", stats_dict=stats):
            return duckdb.sql(
                "select date_trunc('day', key), sum(fare_amount) from taxi group by 1"
            ).fetchall()

    def update_charts(self, proc, components, db_profile, mem_stats, cpu_stats):
        t = datetime.now().isoformat()
        cpu_stats.append({"time": t, "cpu": proc.cpu_percent()})
        mem_stats.append({"time": t, "memory": proc.memory_info().rss / 1024**2})
        for k, v in db_profile.items():
            if v:
                components[k].update(str(v))
        components["cpu_chart"].update(self.make_chart("cpu", cpu_stats).to_dict())
        components["mem_chart"].update(self.make_chart("memory", mem_stats).to_dict())
        current.card.refresh()

    def make_chart(self, label, data):
        import altair as alt

        source = alt.Data({"values": data})
        return (
            alt.Chart(source).mark_line().encode(x="time:T", y="%s:Q" % label)
        ).properties(title=label.capitalize(), width=300, height=200)

    @pypi(
        packages={"altair": "5.2.0", "duckdb": "0.9.2", "psutil": "5.9.7"},
        python="3.11.7",
    )
    @card(type="blank", refresh_interval=1)
    @step
    def start(self):
        import psutil

        proc = psutil.Process()
        db_profile = {"download": 0, "create_table": 0, "query": 0}
        mem_stats = []
        cpu_stats = []
        components = {}
        rows = []
        for label in db_profile:
            m = components[label] = Markdown("")
            rows.append([Markdown(label), m])

        [components["cpu_chart"], components["mem_chart"]] = chart_row = [
            VegaChart.from_altair_chart(self.make_chart("cpu", [])),
            VegaChart.from_altair_chart(self.make_chart("memory", [])),
        ]

        current.card.append(Markdown("# Execute a DuckDB query"))
        current.card.append(Table([chart_row]))
        current.card.append(Table(rows, headers=["Stage", "Milliseconds"]))
        current.card.refresh()

        with ThreadPoolExecutor(max_workers=1) as exe:
            res = exe.submit(self.exec_duckdb, db_profile)
            while True:
                try:
                    q = res.result(1)
                    break
                except TimeoutError:
                    self.update_charts(
                        proc, components, db_profile, mem_stats, cpu_stats
                    )

        # cool down in the end to record final stats
        for i in range(10):
            self.update_charts(proc, components, db_profile, mem_stats, cpu_stats)
            time.sleep(1)
        self.next(self.end)

    @step
    def end(self):
        pass


if __name__ == "__main__":
    DuckDBFlow()
```

## Monitor the Subprocess
```python
import sys
import re
from multiprocessing import Pool, TimeoutError
from tempfile import NamedTemporaryFile

from metaflow import step, FlowSpec, current, card, pypi_base
from metaflow.cards import VegaChart, Markdown, Artifact

VEGA_SPEC = {
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "data": {"values": []},
    "mark": "line",
    "title": "Training loss",
    "encoding": {
        "x": {"field": "epoch", "type": "quantitative"},
        "y": {"field": "loss", "type": "quantitative", "scale": {"type": "log"}},
    },
}


@pypi_base(
    packages={"scikit-learn": "1.3.2"},
    python="3.11.7",
)
class MonitorSklearnFlow(FlowSpec):
    @card
    @step
    def start(self):
        from sklearn.datasets import make_classification

        print("Generating test data..")
        self.num_classes = 2
        self.train_data, self.train_labels = make_classification(
            n_samples=100000,
            n_classes=self.num_classes,
            n_features=400,
            n_informative=50,
        )
        self.next(self.train)

    @card(type="blank", refresh_interval=1)
    @step
    def train(self):
        data = []
        VEGA_SPEC["data"]["values"] = data
        chart = VegaChart(VEGA_SPEC)

        def update_charts(logfile):
            with open(logfile) as f:
                # parse model training logs
                vals = re.findall("Avg. loss: (.+)", f.read(), re.MULTILINE)
                data.clear()
                data.extend({"epoch": i, "loss": v} for i, v in enumerate(vals))
                chart.update(VEGA_SPEC)
                current.card.refresh()

        current.card.append(Markdown("# Training an SGDClassifier model"))
        current.card.append(chart)
        current.card.refresh()

        with NamedTemporaryFile() as tmp:
            with Pool(1) as pool:
                # start training in a subprocess
                proc = pool.apply_async(
                    train_process, (self.train_data, self.train_labels, tmp.name)
                )
                # wait until training is done
                while True:
                    try:
                        # wait for a second
                        self.model = proc.get(1)
                    except TimeoutError:
                        # update charts if we are not done
                        update_charts(tmp.name)
                    else:
                        # otherwise output the model and stop
                        current.card.append(Markdown("Training done!"))
                        current.card.append(Artifact(self.model))
                        break
            update_charts(tmp.name)
        self.next(self.end)

    @step
    def end(self):
        pass


def train_process(train_data, train_labels, output_file):
    # this function is run in a subprocess
    from sklearn.linear_model import SGDClassifier

    # redirect verbose output to a file
    # NOTE remember set buffering=1 or otherwise charts will update slowly
    sys.stdout = open(output_file, "w", buffering=1)
    model = SGDClassifier(verbose=1, max_iter=1000)
    model.fit(train_data, train_labels)
    return model


if __name__ == "__main__":
    MonitorSklearnFlow()
```

# Custom Cards
## VegaChart Example
```python
from metaflow import step, FlowSpec, current, card, pypi, Parameter
from metaflow.cards import VegaChart
from datetime import datetime
import random
import time
import math

COLORS = ["#004f5f", "#f18a07", "#4dbd05", "#127cb1", "#9b45a3"]


class ScatterFlow(FlowSpec):
    num_points = Parameter("num_points", default=2000)
    num_classes = Parameter("num_classes", default=3)
    num_epochs = Parameter("num_epochs", default=20)

    @pypi(
        packages={"scikit-learn": "1.3.2"},
        python="3.11.7",
    )
    @card(type="scatter3d")
    @step
    def start(self):
        from sklearn.datasets import make_classification

        np_data, np_labels = make_classification(
            n_samples=self.num_points,
            n_classes=self.num_classes,
            n_features=3,
            n_informative=3,
            n_redundant=0,
            n_repeated=0,
            n_clusters_per_class=1,
        )
        self.points = [list(arr) for arr in np_data]
        self.classes = list(map(int, np_labels))
        self.labels = [f"class-{i}" for i in range(self.num_classes)]
        self.colors = COLORS[: self.num_classes] #pylint: disable=invalid-slice-index

        batch = self.num_points // self.num_epochs
        for i in range(1, self.num_epochs + 1):
            current.card.refresh(
                {
                    "title": f"Epoch {i}/{self.num_epochs}",
                    "points": self.points[: i * batch],
                    "classes": self.classes[: i * batch],
                    "labels": self.labels,
                    "colors": self.colors,
                }
            )
            time.sleep(1)
        self.next(self.end)

    @step
    def end(self):
        pass


if __name__ == "__main__":
    ScatterFlow()
```