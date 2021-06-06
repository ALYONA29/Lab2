# import toml
import serializers.parsers.toml_parser as toml_parser
from serializers.object_serializers.serializer import *


class TomlSerializer(ISerializer):

    def dumps(self, obj: object) -> str:
        return toml_parser.dumps(object_to_dict(obj))

    def loads(self, s: str) -> object:
        return toml_parser.loads(s)


class TomlSerializerCreator(SerializerCreator):

    def create_serializer(self) -> ISerializer:
        serializer = TomlSerializer()
        return serializer
