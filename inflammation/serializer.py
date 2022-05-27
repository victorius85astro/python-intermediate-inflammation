import json
from abc import ABC

from inflammation import models


class PatientSerializer:
    model = models.Patient

    @classmethod
    def serialize(cls, instances):
        return [{
            'name': instance.name,
            'observations': instance.observations,
        } for instance in instances]

    @classmethod
    def deserialize(cls, data):
        return [cls.model(**d) for d in data]


class PatientJSONSerializer(PatientSerializer):
    @classmethod
    def save(cls, instances, path):
        with open(path, 'w') as jsonfile:
            json.dump(cls.serialize(instances), jsonfile)

    @classmethod
    def load(cls, path):
        with open(path) as jsonfile:
            data = json.load(jsonfile)

        return cls.deserialize(data)


class Serializer:
    @classmethod
    def serialize(cls, instances):
        raise NotImplementedError

    @classmethod
    def save(cls, instances, path):
        raise NotImplementedError

    @classmethod
    def deserialize(cls, data):
        raise NotImplementedError

    @classmethod
    def load(cls, path):
        raise NotImplementedError


class ObservationSerializer(Serializer, ABC):
    model = models.Observation

    @classmethod
    def serialize(cls, instances):
        return [{
            'day': instance.day,
            'value': instance.value,
        } for instance in instances]

    @classmethod
    def deserialize(cls, data):
        return [cls.model(**d) for d in data]
