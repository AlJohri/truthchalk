# TruthChalk

## Pre-Setup
```
brew install pyenv pyenv-virtualenvwrapper node mongodb elasticsearch
# follow the caveats for (brew info mongodb) and (brew info elasticsearch) to start via launchd
```

## Setup
  
```
mkvirtualenv truthchalk
pip install -r requirements.txt
npm install elasticdump -g
```

## Usage
```
workon truthchalk
```