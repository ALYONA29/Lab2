
#import yaml
import serializers.parsers.toml_parser as yaml_parser
from serializers.object_serializers.serializer import *


class YamlSerializer(ISerializer):
    
    def dumps(self, obj: object) -> str:
        return yaml_parser.dump(object_to_dict(obj), sort_keys=False)
    
    def loads(self, s: str) -> object:
        return yaml_parser.full_load(s)


class YamlSerializerCreator(SerializerCreator):
    
    def create_serializer(self) -> ISerializer:
        serializer = YamlSerializer()
        return serializer