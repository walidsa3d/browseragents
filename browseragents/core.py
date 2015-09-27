import useragentdata as data

from random import choice


def random(browser=None, os=None):
    agents = data.agents
    if browser and os:
        agents = [x for x in agents if browser.lower(
        ) in x['browserName'].lower() if os.lower() in x['osName'].lower()]
    elif browser:
        agents = [
            x for x in agents if browser.lower() in x['browserName'].lower()]
    elif os:
        agents = [x for x in agents if os.lower() in x['osName'].lower()]
    return choice(agents)['userAgent']
