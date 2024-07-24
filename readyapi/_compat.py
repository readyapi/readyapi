from collections import deque
from copy import copy
from dataclasses import dataclass, is_dataclass
from enum import Enum
from typing import (
    Any,
    Callable,
    Deque,
    Dict,
    FrozenSet,
    List,
    Mapping,
    Sequence,
    Set,
    Tuple,
    Type,
    Union,
)

from pydantic import BaseModel, create_model
from pydantic.version import VERSION as P_VERSION
from readyapi.exceptions import RequestErrorModel
from readyapi.types import IncEx, ModelNameMap, UnionType
from starlette.datastructures import UploadFile
from typing_extensions import Annotated, Literal, get_args, get_origin

# Reassign variable to make it reexported for mypy
PYDANTIC_VERSION = P_VERSION
PYDANTIC_V2 = PYDANTIC_VERSION.startswith("2.")


sequence_annotation_to_type = {
    Sequence: list,
    List: list,
    list: list,
    Tuple: tuple,
    tuple: tuple,
    Set: set,
    set: set,
    FrozenSet: frozenset,
    frozenset: frozenset,
    Deque: deque,
    deque: deque,
}

sequence_types = tuple(sequence_annotation_to_type.keys())

if PYDANTIC_V2:
    from pydantic import PydanticSchemaGenerationError as PydanticSchemaGenerationError
    from pydantic import TypeAdapter
    from pydantic import ValidationError as ValidationError
    from pydantic._internal._schema_generation_shared import (  # type: ignore[attr-defined]
        GetJsonSchemaHandler as GetJsonSchemaHandler,
    )
    from pydantic._internal._typing_extra import eval_type_lenient
    from pydantic._internal._utils import lenient_issubclass as lenient_issubclass
    from pydantic.fields import FieldInfo
    from pydantic.json_schema import GenerateJsonSchema as GenerateJsonSchema
    from pydantic.json_schema import JsonSchemaValue as JsonSchemaValue
    from pydantic_core import CoreSchema as CoreSchema
    from pydantic_core import PydanticUndefined, PydanticUndefinedType
    from pydantic_core import Url as Url

    try:
        from pydantic_core.core_schema import (
            with_info_plain_validator_function as with_info_plain_validator_function,
        )
    except ImportError:  # pragma: no cover
        from pydantic_core.core_schema import (
            general_plain_validator_function as with_info_plain_validator_function,  # noqa: F401
        )

    Required = PydanticUndefined
    Undefined = PydanticUndefined
    UndefinedType = PydanticUndefinedType
    evaluate_forwardref = eval_type_lenient
    Validator = Any

    class BaseConfig:
        pass

    class ErrorWrapper(Exception):
        pass

    @dataclass
    class ModelField:
        field_info: FieldInfo
        name: str
        mode: Literal["validation", "serialization"] = "validation"

        @property
        def alias(self) -> str:
            a = self.field_info.alias
            return a if a is not None else self.name

        @property
        def required(self) -> bool:
            return self.field_info.is_required()

        @property
        def default(self) -> Any:
            return self.get_default()

        @property
        def type_(self) -> Any:
            return self.field_info.annotation

        def __post_init__(self) -> None:
            self._type_adapter: TypeAdapter[Any] = TypeAdapter(
                Annotated[self.field_info.annotation, self.field_info]
            )

        def get_default(self) -> Any:
            if self.field_info.is_required():
                return Undefined
            return self.field_info.get_default(call_default_factory=True)

        def validate(
            self,
            value: Any,
            values: Dict[str, Any] = {},  # noqa: B006
            *,
            loc: Tuple[Union[int, str], ...] = (),
        ) -> Tuple[Any, Union[List[Dict[str, Any]], None]]:
            try:
                return (
                    self._type_adapter.validate_python(value, from_attributes=True),
                    None,
                )
            except ValidationError as exc:
                return None, _regenerate_error_with_loc(
                    errors=exc.errors(include_url=False), loc_prefix=loc
                )

        def serialize(
            self,
            value: Any,
            *,
            mode: Literal["json", "python"] = "json",
            include: Union[IncEx, None] = None,
            exclude: Union[IncEx, None] = None,
            by_alias: bool = True,
            exclude_unset: bool = False,
            exclude_defaults: bool = False,
            exclude_none: bool = False,
        ) -> Any:
            # What calls this code passes a value that already called
            # self._type_adapter.validate_python(value)
            return self._type_adapter.dump_python(
                value,
                mode=mode,
                include=include,
                exclude=exclude,
                by_alias=by_alias,
                exclude_unset=exclude_unset,
                exclude_defaults=exclude_defaults,
                exclude_none=exclude_none,
            )

        def __hash__(self) -> int:
            # Each ModelField is unique for our purposes, to allow making a dict from
            # ModelField to its JSON Schema.
            return id(self)

    def get_annotation_from_field_info(
        annotation: Any, field_info: FieldInfo, field_name: str
    ) -> Any:
        return annotation

    def _normalize_errors(errors: Sequence[Any]) -> List[Dict[str, Any]]:
        return errors  # type: ignore[return-value]

    def _model_rebuild(model: Type[BaseModel]) -> None:
        model.model_rebuild()

    def _model_dump(
        model: BaseModel, mode: Literal["json", "python"] = "json", **kwargs: Any
    ) -> Any:
        return model.model_dump(mode=mode, **kwargs)

    def _get_model_config(model: BaseModel) -> Any:
        return model.model_config

    def get_schema_from_model_field(
        *,
        field: ModelField,
        schema_generator: GenerateJsonSchema,
        model_name_map: ModelNameMap,
        field_mapping: Dict[
            Tuple[ModelField, Literal["validation", "serialization"]], JsonSchemaValue
        ],
        separate_input_output_schemas: bool = True,
    ) -> Dict[str, Any]:
        override_mode: Union[Literal["validation"], None] = (
            None if separate_input_output_schemas else "validation"
        )
        # This expects that GenerateJsonSchema was already used to generate the definitions
        json_schema = field_mapping[(field, override_mode or field.mode)]
        if "$ref" not in json_schema:
            # TODO remove when deprecating Pydantic v1
            # Ref: https://github.com/pydantic/pydantic/blob/d61792cc42c80b13b23e3ffa74bc37ec7c77f7d1/pydantic/schema.py#L207
            json_schema["title"] = (
                field.field_info.title or field.alias.title().replace("_", " ")
            )
        return json_schema

    def get_compat_model_name_map(fields: List[ModelField]) -> ModelNameMap:
        return {}

    def get_definitions(
        *,
        fields: List[ModelField],
        schema_generator: GenerateJsonSchema,
        model_name_map: ModelNameMap,
        separate_input_output_schemas: bool = True,
    ) -> Tuple[
        Dict[
            Tuple[ModelField, Literal["validation", "serialization"]], JsonSchemaValue
        ],
        Dict[str, Dict[str, Any]],
    ]:
        override_mode: Union[Literal["validation"], None] = (
            None if separate_input_output_schemas else "validation"
        )
        inputs = [
            (field, override_mode or field.mode, field._type_adapter.core_schema)
            for field in fields
        ]
        field_mapping, definitions = schema_generator.generate_definitions(
            inputs=inputs
        )
        return field_mapping, definitions  # type: ignore[return-value]

    def is_scalar_field(field: ModelField) -> bool:
        from readyapi import params

        return field_annotation_is_scalar(
            field.field_info.annotation
        ) and not isinstance(field.field_info, params.Body)

    def is_sequence_field(field: ModelField) -> bool:
        return field_annotation_is_sequence(field.field_info.annotation)

    def is_scalar_sequence_field(field: ModelField) -> bool:
        return field_annotation_is_scalar_sequence(field.field_info.annotation)

    def is_bytes_field(field: ModelField) -> bool:
        return is_bytes_or_nonable_bytes_annotation(field.type_)

    def is_bytes_sequence_field(field: ModelField) -> bool:
        return is_bytes_sequence_annotation(field.type_)

    def copy_field_info(*, field_info: FieldInfo, annotation: Any) -> FieldInfo:
        cls = type(field_info)
        merged_field_info = cls.from_annotation(annotation)
        new_field_info = copy(field_info)
        new_field_info.metadata = merged_field_info.metadata
        new_field_info.annotation = merged_field_info.annotation
        return new_field_info

    def serialize_sequence_value(*, field: ModelField, value: Any) -> Sequence[Any]:
        origin_type = (
            get_origin(field.field_info.annotation) or field.field_info.annotation
        )

        if not issubclass(origin_type, sequence_types):
            raise TypeError(f"Expected a sequence type, but got {origin_type}")

        inner_type = get_args(field.field_info.annotation)[0]
        inner_type_adapter: TypeAdapter[Any] = TypeAdapter(inner_type)
        return [
            inner_type_adapter.dump_python(
                v,
                mode="json",
                include=None,
                exclude=None,
                by_alias=True,
                exclude_unset=False,
                exclude_defaults=False,
                exclude_none=False,
            )
            for v in value
        ]


else:
    from pydantic import SchemaExtraCallable as SchemaExtraCallable
    from pydantic import ValidationError as ValidationError
    from pydantic.class_validators import Validator
    from pydantic.error_wrappers import ErrorWrapper as ErrorWrapper
    from pydantic.fields import Field as Field
    from pydantic.fields import FieldInfo as FieldInfo
    from pydantic.fields import ModelField as ModelField
    from pydantic.schema import (
        get_annotation_from_field_info as get_annotation_from_field_info,
    )
    from pydantic.schema import get_definitions as get_definitions
    from pydantic.schema import get_schema as get_schema
    from pydantic.schema import get_schema_from_model_field as get_schema_from_model_field
    from pydantic.schema import get_compat_model_name_map as get_compat_model_name_map
    from pydantic.schema import (
        is_bytes_field as is_bytes_field,
        is_bytes_sequence_field as is_bytes_sequence_field,
        is_scalar_field as is_scalar_field,
        is_scalar_sequence_field as is_scalar_sequence_field,
        is_sequence_field as is_sequence_field,
        serialize_sequence_value as serialize_sequence_value,
    )
    from pydantic.schema import field_annotation_is_scalar as field_annotation_is_scalar
    from pydantic.schema import (
        field_annotation_is_scalar_sequence as field_annotation_is_scalar_sequence,
    )
    from pydantic.schema import (
        field_annotation_is_sequence as field_annotation_is_sequence,
    )
    from pydantic.schema import is_bytes_or_nonable_bytes_annotation as is_bytes_or_nonable_bytes_annotation
    from pydantic.schema import (
        field_annotation_is_sequence,
        is_bytes_field,
        is_bytes_sequence_annotation,
        serialize_sequence_value,
    )

    from pydantic.utils import lenient_issubclass as lenient_issubclass
    from pydantic.utils import deep_update as deep_update
    from pydantic.utils import smart_deepcopy as smart_deepcopy

    from pydantic import BaseConfig as BaseConfig

    def _normalize_errors(errors: Sequence[Any]) -> List[Dict[str, Any]]:
        return [
            {
                "loc": error.loc_tuple(),
                "msg": error.msg,
                "type": error.type_,
            }
            for error in errors
        ]

    def _model_rebuild(model: Type[BaseModel]) -> None:
        pass

    def _model_dump(
        model: BaseModel, mode: Literal["json", "python"] = "json", **kwargs: Any
    ) -> Any:
        return model.dict(**kwargs) if mode == "python" else model.json(**kwargs)

    def _get_model_config(model: BaseModel) -> Any:
        return model.__config__
