from wikitree.flower import WikiPetal
from qwikidata.entity import WikidataItem
from wikitree_instance.familytree.property import PROPERTY_MAP


class NamePetal(WikiPetal):
    def __init__(self):
        # Id is not required here as name is not an explicit property
        super().__init__("n/a", "name")

    def parse(self, item: WikidataItem) -> str:
        return item.get_label()


class GenderPetal(WikiPetal):
    gender_map = {
        "Q6581097": "male",
        "Q6581072": "female",
        "Q48270": "non-binary",
        "Q1097630": "intersex",
        "Q2449503": "transgender male",
        "Q1052281": "transgender female",
        "Q505371": "agender"
    }

    def __init__(self):
        label = "sex/gender"
        super().__init__(
            PROPERTY_MAP["petals"][label], label)

    def parse(self, item: WikidataItem) -> str:
        gender_ids = [claim.mainsnak.datavalue.value['id']
                      for claim in item.get_claim_group(self.id)._claims if claim.mainsnak.datavalue]
        if not gender_ids:
            return self.undefined
        return self.gender_map.get(gender_ids[0], self.undefined)


class DatePetal(WikiPetal):
    def __init__(self, id, label):
        super().__init__(id, label)

    def parse(self, item: WikidataItem) -> str:
        dob = [claim.mainsnak.datavalue.value.get(
            "time", self.undefined) for claim in item.get_claim_group(self.id)._claims if claim.mainsnak.datavalue]
        # Note: month and day could be unknown, e.g. 1501-00-00
        if not dob or dob[0] == self.undefined:
            return self.undefined
        return dob[0][1:].split('T')[0]


class BirthDatePetal(DatePetal):
    def __init__(self):
        label = "date of birth"
        super().__init__(
            PROPERTY_MAP["petals"][label], label)


class DeathDatePetal(DatePetal):
    def __init__(self):
        label = "date of death"
        super().__init__(
            PROPERTY_MAP["petals"][label], label)


class BirthNamePetal(WikiPetal):
    def __init__(self):
        label = "birth name"
        super().__init__(
            PROPERTY_MAP["petals"][label], label)

    def parse(self, item: WikidataItem) -> str:
        birth_names = [claim.mainsnak.datavalue.value['text']
                       for claim in item.get_claim_group(self.id)._claims if claim.mainsnak.datavalue]
        if not birth_names:
            return self.undefined
        return birth_names[0]
