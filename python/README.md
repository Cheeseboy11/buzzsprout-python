A Python BuzzsproutPodcasts class.
=======
## Prerequisites
* Python 3.7
* A Buzzsprout account (and your API token)

## Summary
Provide an API Token and a Profile ID, to create a BuzzsproutPodcasts object containing all episodes for that profile matching the given parameters. 

## Getting started
By default, instatiating the BuzzsproutPodcasts class will populate the **episodes** property with a list of all episode objects for the profile:
```
$ from buzzsprout_tools import BuzzsproutPodcasts
$ buzzsprout = BuzzsproutPodcasts('APITOKEN', 'PROFILEID')
```

You can then print out the list of all podcasts in the profile:
```
$ print(buzzsprout.episodes)
```

## Filtering
You can currently filter by:
- Date
- Tag
- Random

All of these can be used in combination.

To return only episodes newer than 2019-03-01
```
$ recent_episodes = BuzzsproutPodcasts('APITOKEN', 'PROFILEID', datefilter='2019-03-01')
```
To return only episodes that contain the tag "Interviews"
```
$ interview_episodes = BuzzsproutPodcasts('APITOKEN', 'PROFILEID', tagfilter='Interviews')
```
To return one random episode from the results, use the random switch
```
$ random_episode = BuzzsproutPodcasts('APITOKEN', 'PROFILEID', random=True)
```

## Things to note
Weirdly, Buzzsprout's API does not return an episode URL. I have therefore implemented a *slightly* hacky solution which modifies the audio URL.
By default this URL will not use any custom URL's you have set. I have therefore implemented a workaround. If you pass in your custom URL, the **episode_url** property will be updated:
```
$ custom_url_episode = BuzzsproutPodcasts('APITOKEN', 'PROFILEID', random=True, customurl='subdomain.example.com')
```