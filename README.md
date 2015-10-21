[![Build Status](https://travis-ci.org/lancelote/hh_school.svg)](https://travis-ci.org/lancelote/hh_school)
[![Requirements Status](https://requires.io/github/lancelote/hh_school/requirements.svg?branch=master)](https://requires.io/github/lancelote/hh_school/requirements/?branch=master)

# hh_school

HH.ru school 2015 application

# Requirements

Installation:
```bash
pip install -r requirements.txt
```

Or with `pip-tools`:
```bash
pip-sync
```

To update requirements:

1. Install `pip-tools`: `pip install pip-tools`
2. Update `requirements.in` file: `vim requirements.in`
3. Compile `requirements.txt`: `pip-compile`

# Testing

```bash
paver polynomial
```
