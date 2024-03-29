from dataclasses import dataclass

from seaborn._marks.base import MappableColor, MappableFloat, MappableString, Mark, document_properties

@document_properties
@dataclass
class Path(Mark):
    color: MappableColor = ...
    alpha: MappableFloat = ...
    linewidth: MappableFloat = ...
    linestyle: MappableString = ...
    marker: MappableString = ...
    pointsize: MappableFloat = ...
    fillcolor: MappableColor = ...
    edgecolor: MappableColor = ...
    edgewidth: MappableFloat = ...

@document_properties
@dataclass
class Line(Path): ...

@document_properties
@dataclass
class Paths(Mark):
    color: MappableColor = ...
    alpha: MappableFloat = ...
    linewidth: MappableFloat = ...
    linestyle: MappableString = ...
    def __post_init__(self) -> None: ...

@document_properties
@dataclass
class Lines(Paths): ...

@document_properties
@dataclass
class Range(Paths): ...

@document_properties
@dataclass
class Dash(Paths):
    width: MappableFloat = ...