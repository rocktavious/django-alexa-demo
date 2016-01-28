import os
import multiprocessing

addr = os.environ.get("HTTP_ADDR", "0.0.0.0")
port = os.environ.get("HTTP_PORT", "8000")
loglevel = os.environ.get("LOG_LEVEL", "info")

bind = "{0}:{1}".format(addr, port)
workers = multiprocessing.cpu_count() * 5 + 1
worker_class = "gevent"
timeout = 0
