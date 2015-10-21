"""
Paver tasks
"""

from paver.tasks import task, needs
from paver.easy import sh


@task
def polynomial():
    # Unit tests
    sh('py.test --cov-report term-missing --cov level2/polynomial.py'
       ' tests/level2/test_polynomial.py')

    # Syntax validation
    sh('pylint level2/polynomial.py tests/level2/test_polynomial.py')


@needs('polynomial')
@task
def default():
    pass
