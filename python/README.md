Some Python modules for interacting with Buzzsprout.
=======
## Prerequisites
* Python 3.7
* A Buzzsprout account (and your API token)

## Usage
### Random episode generator
Provide an API token and a profile ID, return a random episode from the profile.
```
$ from buzzsprout_tools import random_episode
$ random_episode('APITOKEN', 'PROFILEID')
```

