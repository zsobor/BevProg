class Developer:
    def __init__(self, name, project, role):
        self._name = name
        self._project = project
        self._role = role
        print("--  Developer létrehozva.  --\n", self._name + " a " + self._project + "-en dolgozik " + self._role + " szerepkörben.")
        #print(self._name + " a " + self._project + "-en dolgozik " + self._role + " szerepkörben.")
    def __eq__(self, other_dev):
        if self._project == other_dev._project:
            print(f"{self._name} és {other_dev._name} dolgoznak egy projekten.")

def CreateDeveloper():
    devs = []
    while True:
        inp = input(">>>")
        if inp == "":
            break
        dev = Developer(inp.split(", ")[0], inp.split(", ")[1], inp.split(", ")[2])
        devs.append(dev)

    for i in range(len(devs)):
        for j in range(i + 1, len(devs)):
            try:
                devs[i] == devs[j]
            finally:
                pass


if __name__ == "__main__":
    print("Input developer information divided by: ,")
    CreateDeveloper()