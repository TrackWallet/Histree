from wikitree.tree import WikiSeed, WikiTree
from wikitree_instance.familytree.petals import *
from wikitree_instance.familytree.stems import *


class FamilySeed(WikiSeed):
    _instance = None

    def __init__(self):
        super().__init__(
            up_stem=ParentStem.instance(),
            down_stem=ChildStem.instance(),
            partner_stem=SpouseStem.instance(),
            petals=[
                GenderPetal.instance(),
                BirthDatePetal.instance(),
                DeathDatePetal.instance(),
                BirthNamePetal.instance()
            ]
        )

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance


class FamilyTree(WikiTree):
    _instance = None

    def __init__(self):
        super.__init__(FamilySeed.instance())

    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
