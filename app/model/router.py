class Router:
    engineID = None
    deviceFamily = ''
    osVersion = ''
    platform = ''
    status = 'inatice'
    upTime = 0
    lastChecking = None
    throughputAverage = 0
    interfaces = []

    def __init__(self, name):
        self.name = name
