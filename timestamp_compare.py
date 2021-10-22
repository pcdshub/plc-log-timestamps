import asyncio
import datetime
import textwrap

import numpy as np

from elasticsearch import AsyncElasticsearch

import matplotlib  # isort: skip

matplotlib.use("Agg")

import matplotlib.pyplot as plt  # isort: skip


es = AsyncElasticsearch("http://ctl-logsrv01.pcdsn:9200")


def to_datetime(ts: str) -> datetime.datetime:
    """Convert elasticsearch timestamp to datetime."""
    dt = datetime.datetime.strptime(ts, "%Y-%m-%dT%H:%M:%S.%fZ")
    return dt.astimezone(datetime.timezone.utc).astimezone()


async def get_plc_to_deltas() -> dict[str, list[datetime.timedelta]]:
    """Get PLC name to timedelta list."""
    resp = await es.search(
        index="twincat-event-0",
        body={
            "query": {
                "match_all": {},
            },
            "sort": [
                {"@timestamp": {"order": "desc", "unmapped_type": "boolean"}},
                {"_doc": {"order": "desc"}},
            ],
            "script_fields": {},
        },
        size=10000,
    )

    def timestamp_delta(source: dict) -> datetime.timedelta:
        return to_datetime(source["@timestamp"]) - to_datetime(
            source["log"]["timestamp"]
        )

    results = [
        (hit["_source"]["log"]["plc"], timestamp_delta(hit["_source"]))
        for hit in resp["hits"]["hits"]
    ]

    by_plc = {}
    for plc_name, delta in results:
        by_plc.setdefault(plc_name, []).append(delta)

    return by_plc


def plot_results(by_plc: dict[str, list[datetime.timedelta]]):
    """Plot the time deltas and print a summary."""
    plt.figure()
    to_plot = []
    labels = []
    for idx, (plc, deltas) in enumerate(sorted(by_plc.items())):
        labels.append(plc)
        deltas = np.asarray([delta.total_seconds() for delta in deltas])
        to_plot.append(deltas)
        print(
            f"{plc:30s}: {len(deltas):8d} messages; "
            f"mean={deltas.mean():8.3f} "
            f"min={deltas.min():8.3f} "
            f"max={deltas.max():8.3f} "
            f"std={deltas.std():8.3f}"
        )

    plt.boxplot(to_plot, notch=True, vert=True)
    plt.xticks(ticks=range(len(labels)), labels=labels)
    plt.tick_params(axis="x", labelrotation=45)
    plt.tight_layout()
    # plt.yscale("log")


if __name__ == "__main__":
    # plt.ion()
    by_plc = asyncio.run(get_plc_to_deltas())
    plot_results(by_plc)
    plt.show()
