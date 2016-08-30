---
name: Argos
desc: An application for helping you keep up with the news.
resources:
    - "The project's source code is [available on GitHub](https://github.com/publicscience/argos)."
    - "Some posts about the project: [Introduction](http://spaceandtim.es/projects/argos) and [Clustering](http://spaceandtim.es/projects/argos_clustering)"
---

![Overview](/assets/argos/overview.jpg)

Argos was a prototype for an intelligent news reader, one which kept up with stories on your behalf. My relationship was news was such that I would only sporadically be able to check in, but the news churns out new articles relentlessly, without regard to your schedule. So Argos would see what stories you were following, and whenever you return, it would give you a summary of what's happened since you last checked.

Argos makes the distinction between _articles_, _events_, and _stories_. An _article_ is a single piece published by a news outlet. Multiple articles may be covered the same _event_, and then multiple events in sequence form a _story_. By applying text clustering algorithms, Argos would automatically identify articles that were discussing the same event, and automatically group events into coherent stories.

Once this structure was applied to a news stream, Argos then would apply text summarization algorithms to extract bullet point summaries for each event. That way, when you return a story you need only to skim a few bullet points to be caught up. Bullet points are associated with their sources so can dig in deeper if you want.

The development of Argos was supported by a Knight Prototype Grant.

## Web client

[![](/assets/argos/web_01.jpg)](/assets/argos/web_01.jpg)
[![](/assets/argos/web_02.jpg)](/assets/argos/web_02.jpg)
[![](/assets/argos/web_03.jpg)](/assets/argos/web_03.jpg)
[![](/assets/argos/web_04.jpg)](/assets/argos/web_04.jpg)
[![](/assets/argos/web_05.jpg)](/assets/argos/web_05.jpg)

## Mobile client

[![](/assets/argos/mobile_01.jpg)](/assets/argos/mobile_01.jpg)
[![](/assets/argos/mobile_02.jpg)](/assets/argos/mobile_02.jpg)
[![](/assets/argos/mobile_elements.png)](/assets/argos/mobile_elements.png)
[![](/assets/argos/mobile_streams.png)](/assets/argos/mobile_streams.png)
[![](/assets/argos/mobile_event.png)](/assets/argos/mobile_event.png)
[![](/assets/argos/mobile_concept.png)](/assets/argos/mobile_concept.png)
