import logging

from redis import StrictRedis
from rq import get_current_job
from six import StringIO

import eregs


def run_eregs_command(eregs_args, host, port, db):
    """Run `eregs *eregs_args`, capturing all of the logs and storing them in
    Redis"""
    log = StringIO()
    logger = logging.getLogger('regparser')
    log_handler = logging.StreamHandler(log)

    logger.propagate = False
    logger.addHandler(log_handler)

    try:
        eregs.run_or_resolve(lambda: eregs.cli.invoke(
            # Must recreate the context each time so that the arg
            # list can be destroyed again
            eregs.cli.make_context('eregs', args=list(eregs_args))))
    finally:
        log_handler.flush()
        # Recreating the connection due to a bug in rq:
        # https://github.com/nvie/rq/issues/479
        conn = StrictRedis(host=host, port=port, db=db)
        job = get_current_job(conn)
        job.meta['logs'] = log.getvalue()
        job.save()
        logger.removeHandler(log_handler)