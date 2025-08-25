from metaflow import Metaflow, Flow, get_metadata, namespace
import time
print("Current metadata provider: %s" % get_metadata())

# Set namespace to None to search over all namespaces
namespace(None)
for flow in Metaflow():
    run = flow.latest_run
    print("{:<15} Last run: {} Successful: {}".\
          format(flow.id, run.finished_at, run.successful))

# Set namespace to None to search over all namespaces
namespace(None)
flow = Flow('MovieStatsFlow')
runs = list(flow.runs())
print("MovieStatsFlow:")
for run in runs:
    print("Run id: {}, Successful: {}".format(run.id, run.successful))
    print("Tags: {}\n".format(sorted(list(run.tags))))