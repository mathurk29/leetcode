from protos import new_pb2
import json
from google.protobuf.json_format import MessageToJson


d1 = new_pb2.Flat(attr1=1, attr2=2)

d2 = new_pb2.Flat(attr1=4, attr2=5)


rep_obj = new_pb2.Nested(
    rep=[d1, d2],
    flatAttr=new_pb2.NestedL1(nestedField=6),
)


def get_proto_field(proto_obj, field_path, default=None):
    """
    Args:
    proto_obj: object of class generated from compiling proto.
    field_path: dot separated path to traverse a field in proto file.

    """
    json_obj = json.loads(MessageToJson(proto_obj))
    result = json_obj
    for field_segment in field_path.split("."):
        try:
            if isinstance(result, dict):
                result = result[field_segment]
            elif isinstance(result, list):
                result = result[int(field_segment)]
            else:
                result = getattr(result, field_segment)
        except (KeyError, IndexError):
            print("Incorrect path")
            return default
    return result


assert get_proto_field(rep_obj, "rep.0.attr1") == 1
assert get_proto_field(rep_obj, "rep.1.attr2") == 5
assert get_proto_field(rep_obj, "flatAttr.nestedField") == 6
assert (
    get_proto_field(rep_obj, "rep.2.attr2") == None
)  # index out of bound on rep field
assert (
    get_proto_field(rep_obj, "flatAttr.wrongField") == None
)  # wrong field on nested proto
assert (
    get_proto_field(rep_obj, "rep.2.attr2", "custom_default") == "custom_default"
)  # error with custom default
