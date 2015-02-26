# TruthChalk

## Pre-Setup
```bash
brew install pyenv pyenv-virtualenvwrapper node mongodb elasticsearch
```
Follow the caveats for `brew info mongodb` and `brew info elasticsearch` to start via launchd.

## Setup
```bash
mkvirtualenv truthchalk
pip install -r requirements.txt
npm install elasticdump -g
```

## Usage
```bash
workon truthchalk
```