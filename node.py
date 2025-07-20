"""
Entrypoint for the Quantum Ledger node.
Usage: python node.py --mode <consensus|api>
"""
import argparse

from consensus.dag import DAGConsensus
from api.server import start_api
from network.p2p import P2PNode
from storage.storage import Storage


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["consensus", "api"], default="consensus")
    args = parser.parse_args()

    storage = Storage(db_path="./data/state.db")
    p2p = P2PNode()

    if args.mode == "consensus":
        dag = DAGConsensus(storage, p2p)
        dag.run()
    else:
        start_api(storage, p2p)


if __name__ == "__main__":
    main()
