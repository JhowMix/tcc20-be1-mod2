class Interface:
    name = ''
    phyAddress = '00-00-00-00-00-00'
    throughput = None
    state = 2
    lastChange = 0
    address = None

    def __init__(self, name):
        self.name = name
